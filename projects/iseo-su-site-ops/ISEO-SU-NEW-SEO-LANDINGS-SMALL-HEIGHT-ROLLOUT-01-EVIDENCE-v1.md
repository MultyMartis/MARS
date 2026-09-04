# ISEO-SU NEW SEO LANDINGS SMALL-HEIGHT ROLLOUT 01 EVIDENCE v1

**Task ID:** ISEO-SU-SITE-OPS-NEW-SEO-LANDINGS-SMALL-HEIGHT-OVERLAP-ROLLOUT-01  
**Date (UTC stamp):** 20260904T051415Z  
**Final status:** COMPLETE — NEW SEO LANDINGS LOW-HEIGHT OVERLAP ROLLOUT / 14 PAGES SAFE / PILOT GENERALIZED

---

## 1. Scope

Layout-only generalization of the approved Novosibirsk small-height first-screen fix across the **14 new SEO landings** (5 city + 7 niche + 2 USA/UAE). Legacy/control pages unchanged. SEO/content/forms/canonical/sitemap unchanged.

## 2. Operator Pilot Approval

Operator visually approved:

https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html

Approved pilot behavior: height: auto + min-height: 100vh on .page_scene_inner eliminates overlap at normal and low desktop heights.

## 3. Pilot Root Cause

Shared main.css rule:

.page_scene_inner { height: 100vh }

Longer first-screen intros overflow the fixed viewport box. #SecondScreen remains in normal document flow and starts at the end of the fixed-height first section → visual overlap on short desktop heights.

## 4. 14-Page Inventory

### CITY (5)
1. /services/seo/prodvizhenie-v-sankt-peterburge.html
2. /services/seo/prodvizhenie-v-kazani.html
3. /services/seo/prodvizhenie-v-ekaterinburge.html
4. /services/seo/prodvizhenie-v-novosibirske.html
5. /services/seo/prodvizhenie-v-krasnoyarske.html

### NICHE (7)
6. /services/seo/prodvizhenie-sajta-pitomnika.html
7. /services/seo/prodvizhenie-sajta-smi.html
8. /services/seo/prodvizhenie-sajta-restorana.html
9. /services/seo/prodvizhenie-internet-magazina-zapchastej.html
10. /services/seo/prodvizhenie-sajta-internet-provajdera.html
11. /services/seo/prodvizhenie-internet-magazina-kosmetiki.html
12. /services/seo/prodvizhenie-internet-magazina-czvetov.html

### INTERNATIONAL (2)
13. /services/seo/prodvizhenie-v-ssha.html
14. /services/seo/prodvizhenie-v-oae.html

Canonical source root: production-source/static-html/services/seo/

## 5. Page-Family Architecture

All 14 pages use .page_scene_inner + #SecondScreen. City/niche/USA-UAE were cloned from different originals, but all inherit the shared fragile height:100vh first-screen mechanism from main.css. Control originals (-regionakh.html, prodvizhenie-avtomobilnogo-sajta.html, zarubezhnye.html, services/seo.html) retain fixed 100vh and were **not** mutated.

## 6. Pre-Rollout Viewport Matrix

Pilot evidence already showed Novosibirsk overlapping before pilot CSS. Pre-rollout audit: all 14 exposed to the same fragile mechanism. Visible overlap risk highest on longer-intro pages at 1366×650 / 1440×600. Sibling city/niche/intl pages lacked the Novosibirsk pilot class until this rollout.

## 7. Final Fix Design

**MODEL A — ALL 14 USE SAME SAFE CLASS**

Reason: every page in the contour uses .page_scene_inner with the shared fixed 100vh rule; one maintainable override is appropriate and harmless for the contour.

`css
body.new-seo-landing-flex-first-screen .page_scene_inner {
	height: auto;
	min-height: 100vh;
	position: relative;
}
`

Shared CSS: production-source/css/new-seo-landing-flex-first-screen.css  
Body class on all 14: 
ew-seo-landing-flex-first-screen  
CSS link after media.css: ../../css/new-seo-landing-flex-first-screen.css

No per-city CSS, no JS height measurement, no magic px heights, no overflow:hidden workaround.

## 8. Pilot Cleanup

Removed:
- body class city-seo-novosibirsk-height-pilot
- stylesheet city-seo-novosibirsk-height-pilot.css (source + production)
- all pilot CSS <link> references

Novosibirsk now uses the shared class/CSS only. Live pilot CSS → HTTP 404.

## 9. Source Changes

- Added production-source/css/new-seo-landing-flex-first-screen.css
- Updated 14 HTML landings (body class + shared CSS link; pilot markers removed)
- Deleted production-source/css/city-seo-novosibirsk-height-pilot.css
- Layout-only; title/description/H1/intro/canonical/forms untouched

## 10. Production Backup

Backup root:

X:\AI MARS\local\sites\iseo-su-production\_new-seo-landings-small-height-rollout-01\20260904T051415Z

Backed up: 14 HTML .before files + pilot CSS .before (shared CSS was MISSING before deploy — new file). SHA-256 before recorded in 	ools/_new-seo-landings-small-height-rollout-01-validate.json.

## 11. Deployment

Scoped upload of 14 HTML + shared CSS; removal of obsolete pilot CSS. Production/source SHA alignment: **YES**. Tool: 	ools/_new-seo-landings-small-height-rollout-01-deploy-validate.py.

## 12. Post-Rollout Viewport Matrix

All 14 pages × required viewports: **PASS / OVERLAP 0**

| Viewport | Result |
|----------|--------|
| 1440×900 | PASS (14/14) |
| 1366×768 | PASS (14/14) |
| 1280×720 | PASS (14/14) |
| 1366×650 | PASS (14/14) |
| 1440×600 | PASS (14/14) |
| 390×844 | PASS (14/14) |
| 360×800 | PASS (14/14) |

Also exercised 1920×1080 on representative long pages. **TOTAL POST-ROLLOUT OVERLAPS: 0**

## 13. Novosibirsk Pilot Preservation

Live Novosibirsk: HTTP 200; has shared class/CSS; no pilot class/CSS; viewport matrix PASS including low heights. Behavior matches approved pilot (grow beyond 100vh when needed; no SecondScreen overlap).

## 14. City Validation

5/5 HTTP 200; shared class present; overlap 0 across matrix; cross-city nav unchanged.

## 15. Niche Validation

7/7 HTTP 200; shared class present; overlap 0; hub links from services/seo.html unchanged.

## 16. USA/UAE Validation

2/2 HTTP 200; shared class present; overlap 0; still not in menu; still not in sitemap.

## 17. SEO Regression

TITLE / DESCRIPTION / H1 / CANONICAL: **unchanged** (14/14). Sitemap changed: **NO**. Static sitemap URL count: **139**.

## 18. Form Regression

Representative smoke (home, tariff-calc, city NSK, niche pitomnik, USA, hub): consent + privacy present; HTTP 200. Layout-only — no mail test required. FORM REGRESSION: **NONE**.

## 19. Control-Page Regression

Controls SHA unchanged / no production mutation: -regionakh.html, prodvizhenie-avtomobilnogo-sajta.html, zarubezhnye.html, services/seo.html. CONTROL PAGE REGRESSION: **NONE**.

## 20. Visual Evidence

Screenshots (144 PNG across 14 page folders):

X:\AI MARS\projects\iseo-su-site-ops\evidence\new-seo-landings-small-height-rollout-01\screenshots\20260904T051415Z

Includes Novosibirsk low-height boundary shots, other city, niche, USA/UAE, normal desktop, mobile.

## 21. Production / Source Alignment

PRODUCTION/SOURCE ALIGNED: **YES**. No pilot-only production tail; obsolete pilot include/CSS removed.

## 22. Rollback

Restore HTML/CSS from X:\AI MARS\local\sites\iseo-su-production\_new-seo-landings-small-height-rollout-01\20260904T051415Z (.before files). Re-upload shared CSS removal / restore pilot CSS only if emergency revert to pilot isolation is required (not recommended — prefer shared fix).

## 23. Final Decision

**COMPLETE — NEW SEO LANDINGS LOW-HEIGHT OVERLAP ROLLOUT / 14 PAGES SAFE / PILOT GENERALIZED**

Pilot evidence retained as **SUPERSEDED** historical proof; this evidence is the accepted rollout authority.
