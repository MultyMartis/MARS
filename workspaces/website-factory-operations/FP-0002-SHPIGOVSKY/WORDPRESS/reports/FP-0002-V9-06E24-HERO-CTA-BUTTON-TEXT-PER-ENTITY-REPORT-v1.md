# REPORT — FP-0002 V9-06E24 HERO CTA BUTTON TEXT PER ENTITY

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: cad17f71b21bc5af98c89524f92cbbeda10dbc96
- Local short HEAD: cad17f71
- Remote HEAD: cad17f71b21bc5af98c89524f92cbbeda10dbc96
- Remote short HEAD: cad17f71
- Ahead: 0
- Behind: 0
- Foreign WIP: extensive outside FP-0002 WORDPRESS E24 scope — preserved unstaged
- Pre-existing staged files: none
- E22 ancestor check: PASS (`cad17f71` is HEAD)
- Result: **PASS**

## 2. Authorization and scope

- Operator authorization: V9-06E24 Hero CTA Button Text Per Entity — GRANTED
- Task mode: LOCAL HERO CTA FIELD + SEED + FRONTEND (no global hero)
- DB checkpoint: YES
- Fresh DB dump: YES
- DB writes: 10 (hero_cta_label postmeta seeds + ACF group sync metadata)
- Source/theme changes: 6 files
- Project plugin changes: 1 file
- Third-party plugin changes: 0
- ACF JSON changes: 4 files
- Runtime delivery: YES
- Page delete/trash/draft changes: 0
- Service clone implementation: NO
- Blog/other pages porting: NO
- Obsolete page cleanup: NO
- Batch 3 implementation: NO
- Global hero settings: NO (absent)
- `Настройки сайта → Герои`: NO (absent)
- Local hero fields preserved: YES
- Reviews alias restore: NO
- Reviews data writes: 0
- Legal text writes: 0
- WP nav menu DB writes: 0
- Privacy setting writes: 0
- Rewrite/permalink changes: NO
- Plugin install/update/delete: 0
- OCPilot writes: 0
- Documentation/evidence writes: YES
- Result: **PASS**

## 3. DB checkpoint

| Item | Result | Path/notes |
|---|---|---|
| Fresh mysqldump | PASS | `v9-06e24-hero-cta-button-text-per-entity-pre-20260707-212945/mars_wp_fp0002.sql` |
| SHA256 | PASS | 81F44938880CCB9188388FC0154F6C306A75C67E478967D35BBE21325D1399BA |
| Snapshots | PASS | local-hero-cta-meta, reviews preservation, global-hero absence |
| Restore instructions | PASS | `validation/v9-06e24-hero-cta-button-text-per-entity/db-checkpoint.json` |
| Committed dump | NO | per charter |

## 4. Baseline local hero CTA audit

| Context | Entity/type | Current hero settings | Current CTA source | E24 field needed | Notes |
|---|---|---|---|:---:|---|
| Home | page | `hero_media`, slides | Site option default | yes | No local CTA field before |
| Services hub | page | `hero_media`, intro | Global default helper | yes | No local CTA field before |
| Dependencies subdivision | service | layout + hero fields | Global default | yes | `hero_cta_label` existed, empty |
| Alcohol leaf | service | layout + hero fields | Route hardcoded | yes | V9 static CTA |
| Demo leaves | service | layout + hero fields | Global default | yes | E14 demo services |
| Psych subdivision | service | layout + hero fields | Global default | yes | |
| Eating subdivision | service | layout + hero fields | Global default | yes | |
| O-centre | page | institutional hero | Global default | yes | Field existed, relabelled |
| Contacts | page | no hero group | NO_CURRENT_HERO_CTA | no | |
| Legal | page | legal group only | NO_CURRENT_HERO_CTA | no | |

## 5. Implementation plan

| Component | Planned implementation | Safety |
|---|---|---|
| ACF home/hub | Add `hero_cta_label` with Russian label | PASS — local only |
| ACF service/institutional | Relabel existing `hero_cta_label` | PASS |
| Helper | `shpigovsky_get_local_hero_cta_label()` | PASS — no global reads |
| Seed | Empty local values only | PASS |
| Frontend | 4 renderers updated | PASS — fallback preserved |

## 6. Local hero CTA field implementation

| Field group/context | Field added | Location preserved | Result | Notes |
|---|---|---:|---|---|
| `group_fp02_page_home` | yes | yes | PASS | `field_fp02_hero_cta_label_home` |
| `group_fp02_page_services_hub` | yes | yes | PASS | `field_fp02_hero_cta_label_hub` |
| `group_fp02_service_layout_hero` | relabel | yes | PASS | existing field |
| `group_fp02_page_institutional` | relabel | yes | PASS | existing field |

## 7. Local hero CTA seed

| Entity/route | Before | After | Seed source | Result |
|---|---|---|---|---|
| Home `/` | empty | Заказать звонок | CURRENT_HARDCODED | PASS |
| Services hub `/uslugi/` | empty | Заказать звонок | CURRENT_HARDCODED | PASS |
| Subdivision `/uslugi/zavisimosti/` | empty | Заказать звонок | CURRENT_HARDCODED | PASS |
| Alcohol leaf | empty | Записаться на консультацию | V9_STATIC | PASS |
| Other hero services | empty | Заказать звонок | CURRENT_HARDCODED | PASS |
| O-centre | empty | Заказать звонок | CURRENT_HARDCODED | PASS |

## 8. Frontend renderer migration

| Renderer/context | Before | After | Fallback | Result |
|---|---|---|---|---|
| Home hero | `default_button_label` option | local `hero_cta_label` | route → site default → static | PASS |
| Services hub hero | global default helper | local `hero_cta_label` | site default → static | PASS |
| Service inner hero | direct field read | `shpigovsky_get_local_hero_cta_label()` | alcohol route → default | PASS |
| Institutional hero | direct field + default | `shpigovsky_get_local_hero_cta_label()` | site default → static | PASS |

## 9. ACF local hero field group sync

| Field group | Before | After | Sync | Result |
|---|---|---|---|---|
| `group_fp02_page_home` | no CTA field | `hero_cta_label` | PHP import | PASS |
| `group_fp02_page_services_hub` | no CTA field | `hero_cta_label` | PHP import | PASS |
| `group_fp02_service_layout_hero` | CTA label EN | RU label | PHP import | PASS |
| `group_fp02_page_institutional` | CTA label EN | RU label | PHP import | PASS |

## 10. Runtime delivery

| File | Delivered | Result | Notes |
|---|:---:|---|---|
| `FieldGroups.php` | yes | PASS | |
| `hero-helpers.php` | yes | PASS | |
| `institutional-helpers.php` | yes | PASS | |
| `home/hero.php` | yes | PASS | |
| `services-hub/hero.php` | yes | PASS | |
| `service/inner-hero.php` | yes | PASS | |
| 4× ACF JSON | yes | PASS | local hero groups |

## 11. Post-implementation admin validation

| Admin context | Field visible | Result | Notes |
|---|:---:|---|---|
| No `Герои` under Site Settings | n/a | PASS | E22 preserved |
| Home local hero CTA | yes | PASS | ACF location probe |
| Services hub local hero CTA | yes | PASS | |
| Subdivision local hero CTA | yes | PASS | post ID 73 |
| Alcohol leaf local hero CTA | yes | PASS | post ID 74 |
| E21 Шапка/Подвал/Комфорт | yes | PASS | |
| Batch 1 preserved | yes | PASS | |
| Top-level Отзывы | yes | PASS | |

## 12. Post-implementation frontend validation

| Route/check | Result | Notes |
|---|---|---|
| `/` | PASS | HTTP 200, CTA present |
| `/uslugi/` | PASS | |
| `/uslugi/zavisimosti/` | PASS | |
| Alcohol + demo leaves | PASS | |
| Psych / eating subdivisions | PASS | |
| `/kontakty/` | PASS | no unwanted hero CTA |
| `/o-centre/` | PASS | |
| `/otzyvy/`, `/privacy-policy/` | PASS | no hero regression |

## 13. Screenshots / evidence

| Evidence | Captured | Result | Notes |
|---|:---:|---|---|
| Admin screenshots | no | PARTIAL | CLI — no WP admin session |
| HTTP marker validation | yes | PASS | 13 routes |
| ACF/DB probes | yes | PASS | |

## 14. Final E24 local hero CTA contract

| Item | Final state | Notes |
|---|---|---|
| Canonical field | `hero_cta_label` | alias `hero_button_text` documented |
| Local groups | 4 updated | no global hero group |
| Global `Герои` | absent | E22 preserved |
| Fallback chain | local → route → site default → V9 | |
| Seed | 10 entities | no overwrite of non-empty |

## 15. No-scope-drift

- DB writes: 10 (hero CTA only)
- Global hero option writes: 0
- Local hero image/title/subtitle value writes: 0
- Page/service content writes: 0
- Source/theme changes: 6
- Project plugin changes: 1
- Third-party plugin changes: 0
- ACF JSON changes: 4
- Runtime delivery: bounded YES
- Page delete/trash/draft changes: 0
- Service clone implementation: NO
- Blog/other pages porting: NO
- Obsolete page cleanup: NO
- Batch 3 implementation: NO
- Reviews alias restore: NO
- Reviews data writes: 0
- Legal text writes: 0
- WP nav menu DB writes: 0
- Privacy setting writes: 0
- Rewrite flush: NO
- Plugin install/update/delete: 0
- OCPilot writes: 0
- Production migration: NO
- V9 src/dist changes: 0
- DB dumps staged: NO
- Backup payload staged: NO
- Runtime snapshots staged: NO
- Helpers/temp staged: NO
- Secrets/API keys: 0
- Result: **PASS**

## 16. Documentation changes

| File | Action | Reason |
|---|---|---|
| `architecture/FP-0002-V9-06E24-*.md` | created | E24 contract pack |
| `validation/v9-06e24-hero-cta-button-text-per-entity/*.json` | created | evidence |
| `reports/FP-0002-V9-06E24-HERO-CTA-BUTTON-TEXT-PER-ENTITY-REPORT-v1.md` | created | wave report |
| `WORDPRESS/README.md` | updated | status |
| `SOURCE-AUTHORITY.md` | updated | E24 entry |
| `PROJECT-STATUS.md` | updated | E24 PASS |

## 17. Git checkpoint

- Exact staged files: E24 plugin/theme/ACF JSON/docs/validation only
- Staged list inspected: pending commit
- Theme source files staged: 5
- Project plugin files staged: 1
- Third-party plugin files staged: 0
- ACF JSON staged: 4
- Runtime files staged: 0
- OCPilot files staged: 0
- DB dumps staged: 0
- Backup payload staged: 0
- Runtime snapshots staged: 0
- Uploaded media files staged: 0
- Helper/temp files staged: 0
- Secrets staged: 0
- Commit: pending operator request
- Push: not performed
- Result: **PENDING COMMIT**

## 18. Final verdict

**PASS**

V9-06E24 Hero CTA Button Text Per Entity: **COMPLETE**

DB checkpoint: **PASS**  
Fresh DB dump: **PASS**  
Local hero CTA field: **PASS**  
Local hero CTA seed: **PASS**  
Frontend hero CTA rendering: **PASS**  
Global hero settings absent: **PASS**  
`Настройки сайта → Герои` absent: **PASS**  
Local hero architecture preserved: **PASS**  
Hero frontend regression: **PASS**  
E21 Header/Footer/Comfort preserved: **PASS**  
Batch 1 preserved: **PASS**  
Reviews alias remains removed: **PASS**  
Top-level Reviews preserved: **PASS**  
No-scope-drift: **PASS**

Recommended next phase: **CREATE_V9_06E25_OPERATOR_HERO_CTA_QA_TASK**

## 19. Recommended next action

**CREATE_V9_06E25_OPERATOR_HERO_CTA_QA_TASK**

## 20. Final safety statement

Target folder: X:\AI MARS

V9-06E24 Hero CTA Button Text Per Entity performed: **YES**

DB checkpoint: **YES**  
Fresh DB dump: **YES**  
DB writes: **10**  
Global hero option writes: **0**  
Local hero image/title/subtitle value writes: **0**  
Page/service content writes: **0**  
Source/theme changes: **6**  
Project plugin changes: **1**  
Third-party plugin changes: **0**  
ACF JSON changes: **4**  
Runtime delivery: **YES**  
Page delete/trash/draft changes: **0**  
Service clone implementation: **NO**  
Blog/other pages porting: **NO**  
Obsolete page cleanup: **NO**  
Batch 3 implementation: **NO**  
Reviews alias restore: **NO**  
Reviews data writes: **0**  
Legal text writes: **0**  
WP nav menu DB writes: **0**  
Privacy setting writes: **0**  
Rewrite flush performed: **NO**  
OCPilot writes: **0**  
Production migration performed: **NO**  
V9 source changed: **NO**  
V9 dist changed: **NO**  
DB dump committed: **NO**  
Backup payload committed: **NO**  
Runtime snapshot committed: **NO**  
Helper/temp committed: **NO**  
Secrets committed: **0**
