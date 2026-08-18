# REDIRECT MANIFEST — FP-0002 P17 CONT1

**Runtime now:** `http://shpigovsky.beget.tech/`  
**Future canonical:** `https://shpigovsky.ru/`  
**Rule style:** path-relative Apache `mod_rewrite` (no hardcoded `https://shpigovsky.ru/...`)

Canonical fragment (source of the custom block):  
`DOCS/PRODUCTION/fp-0002-legacy-redirects.htaccess.fragment`  
Runtime owner: production `public_html/.htaccess` (see ownership doc).

---

### Already implemented legacy redirects

Status: **IMPLEMENTED PRE-CUTOVER** — do **not** reimplement at domain cutover.

| Source | Destination | Live | Destination HTTP | Hops |
|--------|-------------|------|------------------|------|
| `/yoga` `/yoga/` | `/o-centre/programma-lecheniya/kinezioterapiya/` | 301 | 200 | 1 |
| `/about` `/about/` | `/o-centre/` | 301 | 200 | 1 |
| `/psy` `/psy/` | `/o-centre/programma-lecheniya/psihokorrektsiya/` | 301 | 200 | 1 |
| `/home` `/home/` | `/o-centre/programma-lecheniya/` | 301 | 200 | 1 |
| `/policy` `/policy/` | `/privacy-policy/` | 301 | 200 | 1 |
| `/neuro` `/neuro/` | `/o-centre/programma-lecheniya/prostranstvo-vosstanovleniya/` | 301 | 200 | 1 |
| `/reviews` `/reviews/` | `/otzyvy/` | 301 | 200 | 1 |

Query string: `/about?utm_source=test` → `/o-centre/?utm_source=test` (preserved).  
Prefix overreach checks `/yoga-example/` `/about-us/` `/reviews-old/` did **not** follow these rules.

Tokens: `7/7 LEGACY REDIRECTS LIVE` · `7/7 FINAL TARGETS = 200` · `NO REDIRECT LOOPS`

---

### Cutover redirects not yet active

| Class | Action | When |
|-------|--------|------|
| B. temporary host → final domain | `shpigovsky.beget.tech/<path>` → 301 → `https://shpigovsky.ru/<path>` | After final-domain + SSL + siteurl smoke. **Not now.** |
| C. HTTP → HTTPS | 301 to HTTPS | After valid certificate |
| D. www ↔ apex | `https://www.shpigovsky.ru/` → 301 → `https://shpigovsky.ru/` (planned; apex is documented canonical) | After SSL; confirm policy once more at cutover |

---

### Any discovered old host redirects

None proven as additional required mappings this wave. Old public site remains on `92.255.111.71` via current `shpigovsky.ru` DNS until NS cutover. No extra legacy paths beyond the seven operator-approved rules.

---

Evidence: `REDIRECT-LIVE-QA.json`, `REDIRECT-TARGETS.json`, `HTACCESS-DEPLOY.json`
