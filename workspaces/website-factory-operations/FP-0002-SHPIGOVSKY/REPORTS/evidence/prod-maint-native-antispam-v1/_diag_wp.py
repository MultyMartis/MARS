# -*- coding: utf-8 -*-
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _deploy_and_qa import DOCROOT, RuntimeContext, WP_LOAD, write_json  # noqa: E402


def main() -> int:
    ctx = RuntimeContext()
    ctx.connect()
    try:
        php = f"""<?php
error_reporting(E_ALL);
ini_set('display_errors','1');
chdir('{DOCROOT}');
echo "cwd=".getcwd()."\\n";
echo "wpload_exists=".(file_exists('{WP_LOAD}')?'1':'0')."\\n";
try {{
  require '{WP_LOAD}';
  echo "AFTER_LOAD\\n";
  echo "CORE=".(defined('SHPIGOVSKY_CORE_VERSION')?SHPIGOVSKY_CORE_VERSION:'no')."\\n";
  echo "ANTISPAM=".(class_exists('\\\\Shpigovsky\\\\Core\\\\Forms\\\\AntiSpam')?'1':'0')."\\n";
  echo wp_json_encode(array('ok'=>true,'core'=>defined('SHPIGOVSKY_CORE_VERSION')?SHPIGOVSKY_CORE_VERSION:null), JSON_UNESCAPED_UNICODE);
}} catch (Throwable $e) {{
  echo "EX=".$e->getMessage()."\\n".$e->getFile().":".$e->getLine()."\\n";
}}
"""
        remote = f"{DOCROOT}/_fp02_as_diag.php"
        ctx.sftp_put_bytes(remote, php.encode("utf-8"))
        out, err, code = ctx.run_ssh(
            f"cd {DOCROOT} && (php8.2 {remote} || /usr/local/bin/php8.2 {remote} || php {remote}); echo EXIT:$?",
            timeout=120,
        )
        write_json("02d-wp-diag.json", {"code": code, "out": out[-8000:], "err": err[-4000:]})
        print(out)
        print("ERR", err)
        print("CODE", code)
        ctx.run_ssh(f"rm -f {remote}")
        return 0
    finally:
        ctx.close()


if __name__ == "__main__":
    raise SystemExit(main())
