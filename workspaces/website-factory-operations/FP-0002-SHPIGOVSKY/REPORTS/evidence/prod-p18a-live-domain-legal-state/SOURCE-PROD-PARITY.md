# SOURCE / PRODUCTION PARITY — P18A

Exact-file deploy. `php8.2 -l` PASS each file. Production SHA256 = source SHA256.

| File | MATCH |
|------|--------|
| theme `inc/legal-helpers.php` | MATCH |
| theme `functions.php` | MATCH |
| theme `template-parts/legal/document-page.php` | MATCH |
| plugin `shpigovsky-core.php` | MATCH |
| plugin `src/Admin/SystemDashboard.php` | MATCH |
| plugin `src/Fields/FieldGroups.php` | MATCH |
| plugin `src/Admin/EditorRestrictions.php` | MATCH |

**7/7 MATCH**

ACF JSON `group_fp02_page_legal.json` is Git schema; not present as a file under production `acf-json/` (PHP `FieldGroups` is runtime registration). Labels ship via plugin PHP.

Machine: `DEPLOY-QA.json`, `SOURCE-PROD-FOCUS-BEFORE.json` (pre-change MATCH on previous bytes).
