#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Glossary draft content updater (Batch 01 refine + Batch 02/03 load).

Safety:
- CPT glossary only; exact matched draft IDs; dry-run default; force status=draft;
- no create; no publish; allowlist by source/canonical match only.
Does not print credentials.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(r"X:\AI MARS\projects\iseo-su-site-ops")
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
STORAGE_BACKUP_ROOT = Path(r"X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups")
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
                modified: x.modified || '',
                modified_gmt: x.modified_gmt || '',
                link: x.link || ''
              });
            }
            if (chunk.length < 100) break;
          }
          return all;
        }"""
    )


def rest_get_one(page, post_id: int) -> dict:
    return page.evaluate(
        """async (postId) => {
          const root = wpApiSettings.root;
          const nonce = wpApiSettings.nonce;
          const resp = await fetch(root + 'wp/v2/glossary/' + postId + '?context=edit', {
            credentials:'same-origin', headers:{'X-WP-Nonce': nonce}
          });
          const text = await resp.text();
          let json = null;
          try { json = JSON.parse(text); } catch (e) {}
          return {status: resp.status, body: json, text_head: text.slice(0,200)};
        }""",
        post_id,
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


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_batch_items(batch: str) -> list[dict]:
    if batch == "01":
        return json.loads((ROOT / "_glossary-scratch/batch-01-content.json").read_text(encoding="utf-8"))
    if batch == "02":
        return json.loads((ROOT / "_glossary-scratch/batch-02-content.json").read_text(encoding="utf-8"))
    if batch == "03":
        return json.loads((ROOT / "_glossary-scratch/batch-03-content.json").read_text(encoding="utf-8"))
    raise SystemExit("batch must be 01, 02, or 03")


def load_corpus_map() -> dict[str, dict]:
    path = ROOT / "data/glossary-editorial/ISEO-SU-GLOSSARY-FINAL-CORPUS-v1.csv"
    with path.open(encoding="utf-8-sig", newline="") as f:
        return {r["source_term"]: r for r in csv.DictReader(f)}


def patch_csv(batch: str, mapping: dict[str, dict]) -> None:
    names = {
        "01": "ISEO-SU-GLOSSARY-BATCH-01-CONTENT-v1.csv",
        "02": "ISEO-SU-GLOSSARY-BATCH-02-CONTENT-v1.csv",
        "03": "ISEO-SU-GLOSSARY-BATCH-03-CONTENT-v1.csv",
    }
    csv_path = ROOT / "data/glossary-editorial" / names[batch]
    if not csv_path.exists():
        return
    rows = list(csv.DictReader(csv_path.open(encoding="utf-8-sig")))
    fields = list(rows[0].keys()) if rows else []
    for row in rows:
        src = row.get("source_term")
        if src in mapping:
            row["post_id"] = str(mapping[src].get("post_id") or "")
            row["slug"] = mapping[src].get("slug") or row.get("slug") or ""
            row["wordpress_apply_status"] = mapping[src].get("apply_status") or row.get("wordpress_apply_status")
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", choices=["01", "02", "03", "both"], required=True)
    ap.add_argument("--mode", choices=["snapshot", "dry-run", "apply"], default="dry-run")
    ap.add_argument("--only-source", action="append", default=[], help="Limit to exact source_term values")
    ap.add_argument("--skip-acf", action="store_true")
    ap.add_argument("--backup-dir", default="")
    args = ap.parse_args()

    batches = ["01", "02"] if args.batch == "both" else [args.batch]
    corpus = load_corpus_map()
    items_by_batch: dict[str, list[dict]] = {}
    for b in batches:
        items = load_batch_items(b)
        if args.only_source:
            items = [x for x in items if x["source_term"] in set(args.only_source)]
        items_by_batch[b] = items

    scratch_name = "batch03-wp" if args.batch == "03" else "batch02-wp"
    scratch = ROOT / "_glossary-scratch" / scratch_name
    scratch.mkdir(parents=True, exist_ok=True)
    utc = datetime.now(timezone.utc).isoformat()
    receipt: dict = {"utc": utc, "mode": args.mode, "batches": {}, "ok": False}

    secrets = parse_secrets(SECRETS.read_text(encoding="utf-8"))

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        if not login(page, secrets):
            receipt["error"] = "login_failed"
            (scratch / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
            print(json.dumps({"ok": False, "error": "login_failed"}, ensure_ascii=False))
            browser.close()
            return 1
        ensure_api(page)
        drafts = rest_get_all_drafts(page)
        by_norm: dict[str, list[dict]] = {}
        for d in drafts:
            by_norm.setdefault(normalize_title(d.get("title_raw") or ""), []).append(d)

        # Also index by known Batch 01 IDs for refine matching after rename
        by_id = {int(d["id"]): d for d in drafts if d.get("id")}

        all_snapshot_items = []
        plans: dict[str, list[dict]] = {}

        for b, items in items_by_batch.items():
            plan = []
            skipped = []
            collisions = []
            for it in items:
                src = it["source_term"]
                can = it["canonical_term"]
                matches = by_norm.get(normalize_title(src), [])
                if not matches:
                    matches = by_norm.get(normalize_title(can), [])
                # Batch 01 may already be renamed to canonical
                if len(matches) != 1:
                    skipped.append({"batch": b, "source_term": src, "match_count": len(matches), "ids": [m.get("id") for m in matches]})
                    continue
                post = matches[0]
                if post.get("type") and post.get("type") != "glossary":
                    collisions.append({"reason": "non_glossary", "id": post.get("id")})
                    continue
                if post.get("status") != "draft":
                    collisions.append({"reason": "not_draft", "id": post.get("id"), "status": post.get("status")})
                    continue
                post_id = int(post["id"])
                snap = {
                    "batch": b,
                    "source_term": src,
                    "canonical_term": can,
                    "post_id": post_id,
                    "title": post.get("title_raw") or "",
                    "slug": post.get("slug") or "",
                    "status": post.get("status"),
                    "modified": post.get("modified") or "",
                    "modified_gmt": post.get("modified_gmt") or "",
                    "content_raw": post.get("content_raw") or "",
                    "excerpt_raw": post.get("excerpt_raw") or "",
                    "link": post.get("link") or "",
                }
                all_snapshot_items.append(snap)
                desired_slug = (it.get("slug") or corpus.get(src, {}).get("canonical_slug") or snap["slug"]).strip()
                if desired_slug and desired_slug != snap["slug"]:
                    for other in drafts:
                        if int(other.get("id") or 0) != post_id and (other.get("slug") or "") == desired_slug:
                            collisions.append(
                                {
                                    "reason": "slug_collision",
                                    "desired_slug": desired_slug,
                                    "post_id": post_id,
                                    "other_id": other.get("id"),
                                }
                            )
                            desired_slug = snap["slug"]
                            break
                payload = {
                    "title": can,
                    "content": it.get("body_html") or "",
                    "excerpt": it.get("short_definition") or "",
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
                        "synonyms": it.get("synonyms") or "",
                        "seo_title": it.get("seo_title") or "",
                        "meta_description": it.get("meta_description") or "",
                        "keywords": corpus.get(src, {}).get("source_keywords") or "",
                        "lsi": corpus.get(src, {}).get("source_lsi") or "",
                        "notes": f"Batch {b} content apply {utc[:10]}; source={src}",
                    }
                )
            plans[b] = plan
            receipt["batches"][b] = {
                "target_count": len(items),
                "matched_count": len(plan),
                "renames": sum(1 for x in plan if x["rename"]),
                "skipped": skipped,
                "collisions": collisions,
            }

        # Snapshot ACF/Yoast for all matched IDs (backup / dry-run evidence)
        ensure_api(page)
        for s in all_snapshot_items:
            try:
                s["acf_yoast"] = snapshot_acf_yoast(page, s["post_id"])
                ensure_api(page)
            except Exception as e:
                s["acf_yoast"] = {"error": type(e).__name__}

        backup_dir = Path(args.backup_dir) if args.backup_dir else None
        if args.mode == "snapshot" or args.mode == "apply":
            if backup_dir is None:
                ts = datetime.now().strftime("%Y%m%d-%H%M%S")
                if args.batch == "03":
                    backup_dir = STORAGE_BACKUP_ROOT / f"glossary-batch03-{ts}"
                else:
                    backup_dir = STORAGE_BACKUP_ROOT / f"glossary-batch01-refine-batch02-{ts}"
            backup_dir.mkdir(parents=True, exist_ok=True)
            snap_path = backup_dir / "scoped-glossary-prewrite-snapshot.json"
            meta = {
                "utc": utc,
                "method": "authenticated_wp_rest_plus_admin_acf_yoast_fields",
                "contains_secrets": False,
                "git_status": "NOT COMMITTED — store outside Git / Storage only for raw snapshot",
                "target_count": len(all_snapshot_items),
                "batch01_count": sum(1 for x in all_snapshot_items if x["batch"] == "01"),
                "batch02_count": sum(1 for x in all_snapshot_items if x["batch"] == "02"),
                "batch03_count": sum(1 for x in all_snapshot_items if x["batch"] == "03"),
                "items": all_snapshot_items,
            }
            snap_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
            digest = sha256_file(snap_path)
            (backup_dir / "SHA256.txt").write_text(f"{digest}  {snap_path.name}\n", encoding="utf-8")
            receipt["backup"] = {
                "path": str(backup_dir),
                "snapshot_file": str(snap_path),
                "sha256": digest,
                "bytes": snap_path.stat().st_size,
                "target_count": len(all_snapshot_items),
            }
            pointer = {
                "utc": utc,
                "storage_path": str(backup_dir),
                "snapshot_file": snap_path.name,
                "sha256": digest,
                "bytes": snap_path.stat().st_size,
                "target_count": len(all_snapshot_items),
                "post_ids": [x["post_id"] for x in all_snapshot_items],
            }
            pointer_name = (
                "ISEO-SU-GLOSSARY-BATCH-03-PREWRITE-SNAPSHOT-POINTER-v1.json"
                if args.batch == "03"
                else "ISEO-SU-GLOSSARY-BATCH-02-PREWRITE-SNAPSHOT-POINTER-v1.json"
            )
            (ROOT / "data/glossary-editorial" / pointer_name).write_text(
                json.dumps(pointer, ensure_ascii=False, indent=2), encoding="utf-8"
            )

        # Dry-run plan artifact
        plan_public = {}
        for b, plan in plans.items():
            plan_public[b] = {
                "target_count": receipt["batches"][b]["target_count"],
                "matched_count": len(plan),
                "renames": sum(1 for x in plan if x["rename"]),
                "content_updates": len(plan),
                "excerpt_updates": len(plan),
                "acf_updates": 0 if args.skip_acf else len(plan),
                "yoast_updates": 0 if args.skip_acf else len(plan),
                "skipped": receipt["batches"][b]["skipped"],
                "collisions": receipt["batches"][b]["collisions"],
                "plan": [{k: v for k, v in x.items() if k != "payload"} for x in plan],
            }
        (scratch / "dry-run-plan.json").write_text(json.dumps(plan_public, ensure_ascii=False, indent=2), encoding="utf-8")

        # Gates
        gates = {}
        for b, plan in plans.items():
            coll = receipt["batches"][b]["collisions"]
            target = receipt["batches"][b]["target_count"]
            base = {
                "matched_equals_target": len(plan) == target,
                "no_non_glossary": not any(c.get("reason") == "non_glossary" for c in coll),
                "no_published_target": not any(c.get("reason") == "not_draft" for c in coll),
                "no_unresolved_slug_collision": not any(c.get("reason") == "slug_collision" for c in coll),
                "no_skipped": len(receipt["batches"][b]["skipped"]) == 0,
            }
            if b == "02":
                base["target_in_range"] = 42 <= target <= 48
            elif b == "03":
                base["target_in_range"] = 50 <= target <= 60
                # refuse duplicate target IDs within plan
                ids = [x["post_id"] for x in plan]
                base["no_duplicate_target_ids"] = len(ids) == len(set(ids))
            gates[b] = base
        receipt["gates"] = gates
        all_gates_ok = all(all(v.values()) for v in gates.values())

        if args.mode in ("snapshot", "dry-run"):
            receipt["ok"] = all_gates_ok if args.mode == "dry-run" else bool(receipt.get("backup"))
            (scratch / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
            print(
                json.dumps(
                    {
                        "ok": receipt["ok"],
                        "mode": args.mode,
                        "gates": gates,
                        "backup": receipt.get("backup"),
                        "batches": {b: {"target": receipt["batches"][b]["target_count"], "matched": receipt["batches"][b]["matched_count"], "skipped": len(receipt["batches"][b]["skipped"]), "collisions": len(receipt["batches"][b]["collisions"])} for b in receipt["batches"]},
                    },
                    ensure_ascii=False,
                )
            )
            browser.close()
            return 0 if receipt["ok"] else 2

        # apply
        if not all_gates_ok:
            receipt["error"] = "gates_failed"
            (scratch / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
            print(json.dumps({"ok": False, "error": "gates_failed", "gates": gates}, ensure_ascii=False))
            browser.close()
            return 3

        ensure_api(page)
        for b, plan in plans.items():
            mapping: dict[str, dict] = {}
            updates = []
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
                updates.append(
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
                time.sleep(0.2)
            patch_csv(b, mapping)
            receipt["batches"][b]["updates"] = updates
            receipt["batches"][b]["updated_ok"] = sum(1 for u in updates if u.get("ok"))
            receipt["batches"][b]["failed"] = sum(1 for u in updates if not u.get("ok"))

        receipt["ok"] = all(
            receipt["batches"][b].get("failed", 1) == 0
            and receipt["batches"][b].get("updated_ok", 0) == receipt["batches"][b]["matched_count"]
            for b in plans
        )
        (scratch / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
        print(
            json.dumps(
                {
                    "ok": receipt["ok"],
                    "mode": "apply",
                    "batches": {
                        b: {
                            "updated": receipt["batches"][b].get("updated_ok"),
                            "failed": receipt["batches"][b].get("failed"),
                        }
                        for b in plans
                    },
                    "backup": receipt.get("backup"),
                },
                ensure_ascii=False,
            )
        )
        browser.close()
        return 0 if receipt["ok"] else 4


if __name__ == "__main__":
    raise SystemExit(main())
