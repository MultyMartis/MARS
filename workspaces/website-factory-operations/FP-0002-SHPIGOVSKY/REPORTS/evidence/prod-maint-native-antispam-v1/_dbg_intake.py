# -*- coding: utf-8 -*-
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _deploy_and_qa import DOCROOT, INTAKE_PHP, QA_PHP, RuntimeContext, fill_php, write_json  # noqa: E402


def main() -> int:
    ctx = RuntimeContext()
    ctx.connect()
    try:
        for label, tpl in (("intake", INTAKE_PHP), ("qahead", QA_PHP[:800] + "\necho json_encode(array('partial'=>true));\n")):
            php = fill_php(tpl)
            remote = f"{DOCROOT}/_fp02_as_{label}_dbg.php"
            ctx.sftp_put_bytes(remote, php.encode("utf-8"))
            lint_out, lint_err, lint_code = ctx.run_ssh(f"php8.2 -l {remote}")
            run_out, run_err, run_code = ctx.run_ssh(
                f"cd {DOCROOT} && php8.2 {remote}; echo EXIT:$?",
                timeout=180,
            )
            write_json(
                f"02e-{label}-dbg.json",
                {
                    "lint_code": lint_code,
                    "lint": (lint_out or lint_err)[:1000],
                    "run_code": run_code,
                    "out": (run_out or "")[-6000:],
                    "err": (run_err or "")[-3000:],
                    "php_head": php[:400],
                },
            )
            print("====", label)
            print("LINT", lint_code, (lint_out or lint_err)[:300])
            print("OUT", (run_out or "")[-2000:])
            print("ERR", (run_err or "")[-1000:])
            ctx.run_ssh(f"rm -f {remote}")
        return 0
    finally:
        ctx.close()


if __name__ == "__main__":
    raise SystemExit(main())
