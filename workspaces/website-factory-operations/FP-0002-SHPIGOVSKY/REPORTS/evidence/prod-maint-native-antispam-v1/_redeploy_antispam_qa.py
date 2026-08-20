# -*- coding: utf-8 -*-
"""Redeploy AntiSpam.php then resume QA."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _deploy_and_qa import (  # noqa: E402
    DEPLOY_MAP,
    RuntimeContext,
    remote_for,
    sha256_bytes,
    write_json,
)
import _qa_resume as resume  # noqa: E402


def main() -> int:
    ctx = RuntimeContext()
    ctx.connect()
    try:
        rel = "src/Forms/AntiSpam.php"
        local = DEPLOY_MAP[rel]
        remote = remote_for(rel)
        data = local.read_bytes()
        ctx.sftp_put_bytes(remote, data)
        after = ctx.sftp_get(remote)
        write_json(
            "02f-antispam-redeploy.json",
            {
                "match": after == data,
                "local_sha256": sha256_bytes(data),
                "prod_sha256": sha256_bytes(after) if after else None,
            },
        )
        print("redeploy match", after == data)
    finally:
        ctx.close()
    return resume.main()


if __name__ == "__main__":
    raise SystemExit(main())
