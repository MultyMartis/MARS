# -*- coding: utf-8 -*-
"""Resume QA after successful deploy (parity already proven)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _deploy_and_qa import (  # noqa: E402
    DEPLOY_MAP,
    DOCROOT,
    EV,
    INTAKE_PHP,
    QA_PHP,
    RATE_PHP,
    RuntimeContext,
    fill_php,
    http_form_probe,
    remote_for,
    sha256_bytes,
    utcnow,
    write_json,
)


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    ctx = RuntimeContext()
    ctx.connect()
    try:
        # Lint + smoke
        lint = {}
        for rel, local in DEPLOY_MAP.items():
            remote = remote_for(rel)
            out, err, code = ctx.run_ssh(f"php8.2 -l {remote} || /usr/local/bin/php8.2 -l {remote} || php -l {remote}")
            lint[rel] = {"code": code, "out": (out or err or "")[:400]}
        write_json("02b-php-lint.json", lint)

        smoke = ctx.run_php_remote(
            "<?php echo json_encode(array('php'=>PHP_VERSION,'ok'=>true));",
            "smoke",
        )
        write_json("02c-php-smoke.json", smoke)

        post = ctx.run_php_remote(fill_php(INTAKE_PHP), "intake_post")
        write_json("03-post-intake.json", post)

        qa = ctx.run_php_remote(fill_php(QA_PHP), "qa_matrix")
        write_json("04-qa-matrix.json", qa)

        rate = ctx.run_php_remote(fill_php(RATE_PHP), "rate")
        write_json("05-rate-limit-qa.json", rate)

        probes = http_form_probe()
        write_json("06-public-form-probe.json", probes)

        # Re-check parity without re-upload
        parity = []
        for rel, local in DEPLOY_MAP.items():
            remote = remote_for(rel)
            remote_bytes = ctx.sftp_get(remote)
            local_bytes = local.read_bytes()
            parity.append(
                {
                    "rel": rel,
                    "match": remote_bytes == local_bytes,
                    "local_sha256": sha256_bytes(local_bytes),
                    "prod_sha256": sha256_bytes(remote_bytes) if remote_bytes else None,
                }
            )
        write_json("07-parity-recheck.json", parity)

        parity_ok = all(x["match"] for x in parity)
        qa_data = qa.get("data") if isinstance(qa.get("data"), dict) else {}
        indexing = qa_data.get("indexing") or {}
        if not indexing and isinstance(post.get("data"), dict):
            indexing = (post.get("data") or {}).get("indexing") or {}
            if int((post.get("data") or {}).get("blog_public") or 0) == 1:
                indexing_open = True
            else:
                indexing_open = (indexing.get("effective") == "OPEN")
        else:
            indexing_open = (int(indexing.get("blog_public") or 0) == 1) or (
                indexing.get("effective") == "OPEN"
            )
        valid_ok = bool((qa_data.get("valid_human") or {}).get("ok"))
        honey_ok = bool((qa_data.get("honeypot") or {}).get("rejected")) and not bool(
            (qa_data.get("honeypot") or {}).get("accepted")
        )
        fast_ok = bool((qa_data.get("too_fast") or {}).get("rejected"))
        tamp_ok = bool((qa_data.get("tampered_token") or {}).get("rejected"))
        exp_ok = bool((qa_data.get("expired_token") or {}).get("rejected"))
        replay_ok = bool((qa_data.get("replay") or {}).get("first_accepted")) and bool(
            (qa_data.get("replay") or {}).get("second_rejected")
        )
        direct_ok = bool((qa_data.get("direct_missing_token") or {}).get("rejected"))
        heur = qa_data.get("heuristics") or {}
        heur_ok = (
            bool((heur.get("A_normal_ru") or {}).get("ok"))
            and bool((heur.get("B_multiline") or {}).get("ok"))
            and bool((heur.get("C_one_url") or {}).get("ok"))
            and bool((heur.get("G_cyrillic") or {}).get("ok"))
            and bool((heur.get("H_intl_phone_ok") or {}).get("ok"))
            and not bool((heur.get("D_spam_urls") or {}).get("ok"))
            and not bool((heur.get("E_giant") or {}).get("ok"))
            and not bool((heur.get("F_script") or {}).get("ok"))
        )
        rate_ok = bool((rate.get("data") or {}).get("saw_rate_limit")) if rate.get("ok") else False
        no_captcha = all(
            (not isinstance(v, dict))
            or (
                not v.get("has_g_recaptcha_field")
                and not v.get("has_google_recaptcha_script")
                and not v.get("has_form_started_at")
            )
            for v in probes.values()
        )
        core = (post.get("data") or {}).get("core") if post.get("ok") else qa_data.get("core")
        summary = {
            "captured_at": utcnow(),
            "parity_ok": parity_ok,
            "core": core,
            "indexing_open_ok": indexing_open,
            "valid_human_ok": valid_ok,
            "honeypot_ok": honey_ok,
            "too_fast_ok": fast_ok,
            "tampered_ok": tamp_ok,
            "expired_ok": exp_ok,
            "replay_ok": replay_ok,
            "direct_ok": direct_ok,
            "heuristics_ok": heur_ok,
            "rate_limit_ok": rate_ok,
            "no_external_captcha_ok": no_captcha,
            "cleanup_deleted": (qa_data.get("cleanup") or {}).get("deleted"),
            "qa_ok_flag": qa.get("ok"),
            "post_ok_flag": post.get("ok"),
        }
        write_json("00-summary.json", summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        ok = all(
            [
                parity_ok,
                indexing_open,
                valid_ok,
                honey_ok,
                fast_ok,
                tamp_ok,
                exp_ok,
                replay_ok,
                direct_ok,
                heur_ok,
                rate_ok,
                no_captcha,
                core == "0.3.24-antispam",
            ]
        )
        return 0 if ok else 2
    finally:
        ctx.close()


if __name__ == "__main__":
    raise SystemExit(main())
