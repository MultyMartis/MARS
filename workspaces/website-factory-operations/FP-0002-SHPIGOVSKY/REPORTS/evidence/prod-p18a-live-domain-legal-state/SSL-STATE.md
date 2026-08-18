# SSL STATE — P18A

| Host | Result | Class |
|------|--------|-------|
| shpigovsky.ru:443 | Let's Encrypt YE2; SAN apex+www; notBefore 2026-06-27; **verify OK** | Valid on **legacy** public origin |
| www.shpigovsky.ru:443 | Let's Encrypt YR2; SAN includes archive + apex + www; notBefore **2026-08-18 13:16 GMT**; verify OK | Valid; issued today; **not** proven as WP origin |
| shpigovsky.beget.tech:443 | handshake/read timeout | WordPress HTTPS **not ready** |

HTTP `http://shpigovsky.ru/` → 301 → `https://shpigovsky.ru/` (nginx on the public/legacy origin).

**Wave classification for WordPress:** SSL **IN PROGRESS** / issued-but-not-fully-routed-to-WP. Do not force additional HTTP→HTTPS on the WP vhost until that origin is the public one (loop risk: beget `/` already 301s to apex legacy).

Next check: after Beget attaches `shpigovsky.ru` to the WP docroot, re-verify cert SAN + WordPress HTML (`generator: WordPress`).

Machine: `SSL-STATE.json`.
