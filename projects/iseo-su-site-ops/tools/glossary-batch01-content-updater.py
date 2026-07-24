#!/usr/bin/env python3
"""Batch-01 glossary draft updater via authenticated in-page WP REST + admin ACF/Yoast.

Safety:
- CPT glossary only; exact matched draft IDs; dry-run default; no publish; no create.
Does not print credentials.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(r"X:\AI MARS\projects\iseo-su-site-ops")
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
BATCH = ROOT / "_glossary-scratch" / "batch-01-content.json"
CORPUS = ROOT / "_glossary-scratch" / "final-corpus-v1.csv"
CORPUS_JSON = ROOT / "_glossary-scratch" / "final-corpus-v1.json"
SCRATCH = ROOT / "_glossary-scratch" / "batch01-wp"
CSV_OUT = ROOT / "data" / "glossary-editorial" / "ISEO-SU-GLOSSARY-BATCH-01-CONTENT-v1.csv"
BASE = "https://i-seo.su"


def parse_secrets(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r"^([A-Za-z0-9_/-]+):\s*(.*)$", line.strip())
        if m:
            data[m.group(1)] = m.group(2).strip()
    return data


def normalize_title(title: str) -> str:
    title = html.unescape(title or "")
    title = re.sub(r"<[^>]+>", "", title)
    title = re.sub(r"\s+", " ", title).strip().lower()
    return title


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(s or "")).strip()


def login(page, secrets: dict) -> bool:
    login_url = secrets.get("wordpress_login_url") or f"{BASE}/wp-login.php"
    page.goto(login_url, wait_until="domcontentloaded", timeout=90000)
    page.fill("#user_login", secrets["wordpress_username"])
    page.fill("#user_pass", secrets["wordpress_password"])
    page.click("#wp-submit")
    page.wait_for_load_state("domcontentloaded")
    return "wp-admin" in page.url and "wp-login" not in page.url


def ensure_api(page) -> None:
    page.goto(f"{BASE}/wp-admin/post.php?post=2612&action=edit", wait_until="domcontentloaded", timeout=90000)
    page.wait_for_function("() => !!(window.wpApiSettings && wpApiSettings.nonce)", timeout=30000)


def rest_get_all_drafts(page) -> list[dict]:
    return page.evaluate(
        """async () => {
          const root = wpApiSettings.root;
          const nonce = wpApiSettings.nonce;
          const all = [];
          for (let pageN = 1; pageN <= 20; pageN++) {
            const url = root + 'wp/v2/glossary?status=draft&per_page=100&page=' + pageN + '&context=edit';
            const resp = await fetch(url, {credentials:'same-origin', headers:{'X-WP-Nonce': nonce}});
            if (!resp.ok) {
              const t = await resp.text();
              throw new Error('list_failed ' + resp.status + ' ' + t.slice(0,200));
            }
            const chunk = await resp.json();
            if (!Array.isArray(chunk) || chunk.length === 0) break;
            for (const x of chunk) {
              all.push({
                id: x.id,
                status: x.status,
                slug: x.slug,
                type: x.type,
                title_raw: (x.title && (x.title.raw || x.title.rendered)) || '',
                content_raw: (x.content && (x.content.raw || '')) || '',
                excerpt_raw: (x.excerpt && (x.excerpt.raw || '')) || '',
                link: x.link || ''
              });
            }
            if (chunk.length < 100) break;
          }
          return all;
        }"""
    )


def rest_update(page, post_id: int, payload: dict) -> dict:
    return page.evaluate(
        """async ({postId, payload}) => {
          const root = wpApiSettings.root;
          const nonce = wpApiSettings.nonce;
          const resp = await fetch(root + 'wp/v2/glossary/' + postId, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
              'X-WP-Nonce': nonce,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
          });
          const text = await resp.text();
          let json = null;
          try { json = JSON.parse(text); } catch (e) {}
          return {status: resp.status, body: json, text_head: text.slice(0,300)};
        }""",
        {"postId": post_id, "payload": payload},
    )


def snapshot_acf_yoast(page, post_id: int) -> dict:
    page.goto(f"{BASE}/wp-admin/post.php?post={post_id}&action=edit", wait_until="domcontentloaded", timeout=90000)
    return page.evaluate(
        """() => {
          const pick = (sels) => {
            for (const sel of sels) {
              const el = document.querySelector(sel);
              if (el) return el.value || '';
            }
            return '';
          };
          return {
            glossary_synonyms: pick(['#acf-field_iseo_glossary_synonyms','[data-name="glossary_synonyms"] textarea']),
            glossary_keywords: pick(['#acf-field_iseo_glossary_keywords','[data-name="glossary_keywords"] textarea']),
            glossary_lsi_phrases: pick(['#acf-field_iseo_glossary_lsi','[data-name="glossary_lsi_phrases"] textarea']),
            glossary_source_notes: pick(['#acf-field_iseo_glossary_source_notes','[data-name="glossary_source_notes"] textarea']),
            yoast_title: pick(['#yoast_wpseo_title','input[name="yoast_wpseo_title"]']),
            yoast_metadesc: pick(['#yoast_wpseo_metadesc','textarea[name="yoast_wpseo_metadesc"]']),
            post_status_display: (document.querySelector('#post-status-display')||{}).textContent || '',
            hidden_post_status: (document.querySelector('#hidden_post_status')||{}).value || '',
          };
        }"""
    )


def update_acf_yoast(page, post_id: int, fields: dict) -> dict:
    page.goto(f"{BASE}/wp-admin/post.php?post={post_id}&action=edit", wait_until="domcontentloaded", timeout=90000)
    filled = page.evaluate(
        """(fields) => {
          const setVal = (sels, val) => {
            for (const sel of sels) {
              const el = document.querySelector(sel);
              if (el) {
                el.focus();
                el.value = val;
                el.dispatchEvent(new Event('input', {bubbles:true}));
                el.dispatchEvent(new Event('change', {bubbles:true}));
                return true;
              }
            }
            return false;
          };
          return {
            synonyms: setVal(['#acf-field_iseo_glossary_synonyms','[data-name="glossary_synonyms"] textarea'], fields.synonyms || ''),
            notes: setVal(['#acf-field_iseo_glossary_source_notes','[data-name="glossary_source_notes"] textarea'], fields.notes || ''),
            keywords: setVal(['#acf-field_iseo_glossary_keywords','[data-name="glossary_keywords"] textarea'], fields.keywords || ''),
            lsi: setVal(['#acf-field_iseo_glossary_lsi','[data-name="glossary_lsi_phrases"] textarea'], fields.lsi || ''),
            yoast_title: setVal(['#yoast_wpseo_title','input[name="yoast_wpseo_title"]'], fields.seo_title || ''),
            yoast_metadesc: setVal(['#yoast_wpseo_metadesc','textarea[name="yoast_wpseo_metadesc"]'], fields.meta_description || ''),
          };
        }""",
        fields,
    )
    # Prefer Save Draft
    if page.locator("#save-post").count():
        page.click("#save-post")
    else:
        btn = page.locator("#publish")
        label = (btn.inner_text() or "").lower() if btn.count() else ""
        if "опублик" in label and "обнов" not in label:
            return {"saved": False, "error": "publish_button", "filled": filled}
        page.click("#publish")
    page.wait_for_load_state("domcontentloaded")
    status = page.evaluate(
        """() => ({
          display: (document.querySelector('#post-status-display')||{}).textContent || '',
          hidden: (document.querySelector('#hidden_post_status')||{}).value || ''
        })"""
    )
    return {"saved": True, "filled": filled, "status": status}


def patch_csv_apply_status(mapping: dict[str, dict]) -> None:
    if not CSV_OUT.exists():
        return
    import csv

    rows = list(csv.DictReader(CSV_OUT.open(encoding="utf-8")))
    fields = list(rows[0].keys()) if rows else []
    for row in rows:
        src = row.get("source_term")
        if src in mapping:
            row["post_id"] = str(mapping[src].get("post_id") or "")
            row["slug"] = mapping[src].get("slug") or row.get("slug") or ""
            row["wordpress_apply_status"] = mapping[src].get("apply_status") or row.get("wordpress_apply_status")
    with CSV_OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--skip-acf", action="store_true", help="Skip ACF/Yoast admin updates")
    args = ap.parse_args()
    dry = not args.apply
    SCRATCH.mkdir(parents=True, exist_ok=True)

    secrets = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    batch = json.loads(BATCH.read_text(encoding="utf-8"))
    corpus = {c["source_term"]: c for c in json.loads(CORPUS_JSON.read_text(encoding="utf-8"))}
    if not (28 <= len(batch) <= 32):
        raise SystemExit(f"batch size {len(batch)}")

    receipt: dict = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "mode": "dry-run" if dry else "apply",
        "target_count": len(batch),
        "matched": [],
        "skipped": [],
        "collisions": [],
        "updates": [],
        "ok": False,
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        if not login(page, secrets):
            receipt["error"] = "login_failed"
            (SCRATCH / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
            print(json.dumps({"ok": False, "error": "login_failed"}))
            browser.close()
            return 1
        ensure_api(page)
        drafts = rest_get_all_drafts(page)
        receipt["draft_count_seen"] = len(drafts)

        by_norm: dict[str, list[dict]] = {}
        for d in drafts:
            if d.get("type") and d.get("type") != "glossary":
                receipt["collisions"].append({"reason": "non_glossary", "id": d.get("id")})
                continue
            if d.get("status") != "draft":
                receipt["collisions"].append({"reason": "not_draft", "id": d.get("id"), "status": d.get("status")})
                continue
            by_norm.setdefault(normalize_title(d.get("title_raw") or ""), []).append(d)

        snapshot = []
        plan = []
        for b in batch:
            src = b["source_term"]
            can = b["canonical_term"]
            corp = corpus.get(src, {})
            matches = by_norm.get(normalize_title(src), []) or by_norm.get(normalize_title(can), [])
            if len(matches) != 1:
                receipt["skipped"].append({"source_term": src, "match_count": len(matches), "ids": [m.get("id") for m in matches]})
                continue
            post = matches[0]
            post_id = int(post["id"])
            content_empty = not strip_tags(post.get("content_raw") or "")
            excerpt_empty = not strip_tags(post.get("excerpt_raw") or "")
            snap = {
                "post_id": post_id,
                "title": post.get("title_raw") or "",
                "slug": post.get("slug") or "",
                "status": post.get("status"),
                "content_empty": content_empty,
                "excerpt_empty": excerpt_empty,
                "content_raw": post.get("content_raw") or "",
                "excerpt_raw": post.get("excerpt_raw") or "",
                "link": post.get("link") or "",
            }
            snapshot.append(snap)

            desired_slug = (b.get("slug") or corp.get("canonical_slug") or snap["slug"]).strip()
            if desired_slug and desired_slug != snap["slug"]:
                for other in drafts:
                    if int(other.get("id") or 0) != post_id and (other.get("slug") or "") == desired_slug:
                        receipt["collisions"].append(
                            {"reason": "slug_collision", "desired_slug": desired_slug, "post_id": post_id, "other_id": other.get("id")}
                        )
                        desired_slug = snap["slug"]
                        break

            payload = {
                "title": can,
                "content": b.get("body_html") or "",
                "excerpt": b.get("short_definition") or "",
                "status": "draft",
            }
            if desired_slug and desired_slug != snap["slug"]:
                payload["slug"] = desired_slug

            plan.append(
                {
                    "source_term": src,
                    "canonical_term": can,
                    "post_id": post_id,
                    "rename": normalize_title(snap["title"]) != normalize_title(can),
                    "old_title": snap["title"],
                    "new_title": can,
                    "old_slug": snap["slug"],
                    "new_slug": payload.get("slug", snap["slug"]),
                    "payload": payload,
                    "synonyms": b.get("synonyms") or "",
                    "seo_title": b.get("seo_title") or "",
                    "meta_description": b.get("meta_description") or "",
                    "keywords": corp.get("source_keywords") or "",
                    "lsi": corp.get("source_lsi") or "",
                    "notes": f"Batch 01 content load 2026-07-25; source={src}",
                }
            )
            receipt["matched"].append({"source_term": src, "post_id": post_id, "rename": normalize_title(snap["title"]) != normalize_title(can)})

        # ACF snapshot sample
        ensure_api(page)
        for s in snapshot[:5]:
            try:
                s["acf_yoast"] = snapshot_acf_yoast(page, s["post_id"])
                ensure_api(page)
            except Exception as e:
                s["acf_yoast"] = {"error": type(e).__name__}

        (SCRATCH / "prewrite-snapshot.json").write_text(
            json.dumps({"utc": receipt["utc"], "items": snapshot}, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        (SCRATCH / "dry-run-plan.json").write_text(
            json.dumps(
                {
                    "target_count": len(batch),
                    "matched_count": len(plan),
                    "renames": sum(1 for x in plan if x["rename"]),
                    "content_updates": len(plan),
                    "excerpt_updates": len(plan),
                    "acf_updates": 0 if args.skip_acf else len(plan),
                    "yoast_updates": 0 if args.skip_acf else len(plan),
                    "skipped": receipt["skipped"],
                    "collisions": receipt["collisions"],
                    "plan": [{k: v for k, v in x.items() if k != "payload"} for x in plan],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

        gates = {
            "target_in_range": 28 <= len(batch) <= 32,
            "matched_equals_target": len(plan) == len(batch),
            "no_non_glossary": not any(c.get("reason") == "non_glossary" for c in receipt["collisions"]),
            "no_published_target": True,
            "no_unresolved_slug_collision": not any(c.get("reason") == "slug_collision" for c in receipt["collisions"]),
        }
        receipt["gates"] = gates
        receipt["matched_count"] = len(plan)

        if dry:
            receipt["ok"] = all(gates.values())
            (SCRATCH / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
            print(json.dumps({"ok": receipt["ok"], "mode": "dry-run", "target": len(batch), "matched": len(plan), "skipped": len(receipt["skipped"]), "collisions": len(receipt["collisions"]), "gates": gates}, ensure_ascii=False))
            browser.close()
            return 0 if receipt["ok"] else 2

        if not all(gates.values()):
            receipt["error"] = "gates_failed"
            (SCRATCH / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
            print(json.dumps({"ok": False, "error": "gates_failed", "gates": gates}, ensure_ascii=False))
            browser.close()
            return 3

        # Full ACF snapshot before write
        ensure_api(page)
        for s in snapshot:
            try:
                s["acf_yoast_before"] = snapshot_acf_yoast(page, s["post_id"])
                ensure_api(page)
            except Exception as e:
                s["acf_yoast_before"] = {"error": type(e).__name__}
        (SCRATCH / "prewrite-snapshot.json").write_text(
            json.dumps({"utc": receipt["utc"], "items": snapshot}, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        mapping: dict[str, dict] = {}
        ensure_api(page)
        for item in plan:
            pid = item["post_id"]
            res = rest_update(page, pid, item["payload"])
            body = res.get("body") if isinstance(res.get("body"), dict) else {}
            ok = res.get("status") in (200, 201) and body.get("status") == "draft"
            acf_res = None
            if ok and not args.skip_acf:
                acf_res = update_acf_yoast(
                    page,
                    pid,
                    {
                        "synonyms": item["synonyms"],
                        "notes": item["notes"],
                        "keywords": item["keywords"],
                        "lsi": item["lsi"],
                        "seo_title": item["seo_title"],
                        "meta_description": item["meta_description"],
                    },
                )
                ensure_api(page)
            receipt["updates"].append(
                {
                    "post_id": pid,
                    "source_term": item["source_term"],
                    "canonical_term": item["canonical_term"],
                    "rest": {"status": res.get("status"), "slug": body.get("slug"), "post_status": body.get("status")},
                    "acf": acf_res,
                    "ok": ok,
                }
            )
            mapping[item["source_term"]] = {
                "post_id": pid,
                "slug": body.get("slug") or item["new_slug"],
                "apply_status": "applied" if ok else "failed",
            }
            time.sleep(0.25)

        receipt["ok"] = all(u.get("ok") for u in receipt["updates"]) and len(receipt["updates"]) == len(plan)
        patch_csv_apply_status(mapping)
        (SCRATCH / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"ok": receipt["ok"], "mode": "apply", "updated": sum(1 for u in receipt["updates"] if u.get("ok")), "failed": sum(1 for u in receipt["updates"] if not u.get("ok"))}, ensure_ascii=False))
        browser.close()
        return 0 if receipt["ok"] else 4


if __name__ == "__main__":
    raise SystemExit(main())
