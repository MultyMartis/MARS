# FP-0002 — Services V2 Content Build Validation v1

**Date:** 2026-06-26

| Check | Result |
| ----- | ------ |
| Node | `C:\MARS Phenix\AI MARS\.tools\node-portable\node.exe` v22.16.0 |
| Build command | `node node_modules/gulp/bin/gulp.js build` |
| Exit code | 0 |
| EBUSY | none |
| Preview | `http://127.0.0.1:4174/uslugi-v2.html` → HTTP 200 |
| Server PID | dynamic (http-server on 4174) |

**Regression hashes (unchanged):**

| File | SHA-256 |
| ---- | ------- |
| index.html | `B1D5D53F3467746EEF40212D365305816F54F2D9CEA90DECBB610E48D13B7075` |
| uslugi.html | `C2937DC67CF9AACEF90C041F4C909C36FB860F4B0E1D9AC2505877C5BD4A9619` |
| services-inner-hero-v2.html | `5808021C66E8A9555CABDFC254E92F446D93CEA35F05905F40B83C52243A51F1` |
| breadcrumbs.html | `2800FCEBA9F5E167E20D37F9F65F08250B3409B82733229CAA4991089EFBBBA3` |
| services-page-subnav.html | `BF1E2473E353B36833932D4A370431627F3EEC4A41855398C21E316853A4CB67` |
| main.js | `1693BAB784B024A460738C94E778C157DACD55A957C24B87BBC760FD6958DB67` |

**Verdict:** CLEAN BUILD PASS
