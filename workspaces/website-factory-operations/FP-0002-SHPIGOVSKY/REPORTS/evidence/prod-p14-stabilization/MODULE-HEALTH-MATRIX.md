# MODULE-HEALTH-MATRIX — PROD-P14

| Module | Loaded | Owner | Version/schema | Errors | Status |
|--------|--------|-------|----------------|--------|--------|
| Services CPT | yes | shpigovsky-core `ContentTypes\Service` | rewrite live | none observed | PASS |
| Specialists CPT | yes | shpigovsky-core `ContentTypes\Specialist` | rewrite `specyalisty` | none | PASS |
| Reviews / settings | yes | ACF Site Settings / theme helpers | options | none in smoke | PASS |
| Smart Search | yes | theme REST + CSS/JS | endpoint OK HTTP | none | PASS |
| SEO / Integrations | yes | `Fields\SeoIntegrationsOptions` + theme | Admin owner | none | PASS |
| Sitemap | yes | WP core `/wp-sitemap.xml` | HTTP 200 | none | PASS |
| Social / Messenger | yes | `Fields\SocialPlatformsOptions` | FE wired | none | PASS |
| Activity Log | yes | `Admin\ActivityLog` | DB v1 / retention 8000 | none | PASS |
| DOCX Publisher | yes | `Admin\DocxImporter` | template asset present | none | PASS |
| MetaCODE Dashboard | yes | `Admin\SystemDashboard` | P14 baseline widget | none | PASS |
| Native slug UX | yes | `PermalinkSlugUX` + `ServicePermalinks` | FU01 model | none | PASS |
| Article TOC | yes | theme blog helpers / CSS/JS | P13 | none | PASS |
| Nav second level | yes | `nav-walker` + templates | P13 | none | PASS |
| Lifebuoy FE | yes | `fp02-lifebuoy-parallax.*` | P12/P13 FIX02 | device QA optional | PASS (code) |
| Admin menu hygiene | yes | `AdminMenuHygiene` | ACFE Options hidden | none | PASS |
| MU mars-local-runtime | present | migration residue | notices removed P13 | leftover for P06 | PASS w/ P06 tail |
| WPilot | yes | metacode-wpilot | 0.3.2 / writes off | none | PASS |

Frontend smoke (HTTP): home, /uslugi/, service, specialists, specialist, blog, contacts, sitemap, robots, search — all **200**, no PHP fatals.

Admin smoke (`mars`): dashboard widget present with baseline; services/specialists/posts/pages/users/activity log — **200** no fatals; no LOCAL MARS global notice; slug screens retain single native permalink row.
