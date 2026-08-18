# WP Forge — New-site starter checklist v1

**Use with:** [BLUEPRINT](../standards/FORGE-WORDPRESS-PRODUCTION-WEBSITE-BLUEPRINT-v1.md)  
**Goal:** do not rediscover FP-0002 decisions.

---

## Before coding

- [ ] **P1b CMS pack** started: entity map, ownership map, relationships, Site Settings map, page editability ([CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md))  
- [ ] Design-to-CMS worksheet for primary templates ([worksheet](FORGE-WORDPRESS-DESIGN-TO-CMS-MAPPING-WORKSHEET-v1.md))  
- [ ] Page vs CPT vs options vs repeater decided (matrix completed — [REPEATER-VS-ENTITY](../standards/FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md))  
- [ ] URL map (hubs vs singles; `has_archive`)  
- [ ] Settings SoT (one contacts/social owner)  
- [ ] Internal CTAs = object relationship, not pasted staging URLs  
- [ ] Component empty-state contracts named  
- [ ] Admin IA (menu, tabs, list tables) sketched  
- [ ] SEO owner (one)  
- [ ] Form owner (one) + pre-SMTP policy  
- [ ] Locale + i18n from first module  
- [ ] Sitemap = native extension  
- [ ] Search module yes/no  
- [ ] Native slug UX (no custom permalink UI)  
- [ ] Typography owner (render-time)  
- [ ] Dashboard widget planned (runtime status; no global notices; update in the same production wave)  
- [ ] Indexing closed until explicit human approval; Admin control if pre-launch  
- [ ] Default SMTP technical sender `noreply@<domain>` (no credentials in Git)  
- [ ] Site Settings → Почта и формы as the only SMTP/recipient owner  
- [ ] Lead table persist-before-mail; Заявки Admin  
- [ ] Metrika counter in SEO; form stores goal only; fire after backend success  

## Before production connection

- [ ] Exact access matrix (real docroot)  
- [ ] Source/runtime authority understood  
- [ ] Backup plan (exact-file vs full)  
- [ ] WPilot READ; write disabled  
- [ ] Environment classification plan  
- [ ] Secrets not in Git  

## Before cutover

Complete [PRE-CUTOVER-READINESS-MATRIX](FORGE-WORDPRESS-PRE-CUTOVER-READINESS-MATRIX-v1.md) (P17-style):

- [ ] Freeze + fresh full backup  
- [ ] Webroot hygiene  
- [ ] Users clean  
- [ ] Redirects  
- [ ] DNS zone inventory (mail preserved)  
- [ ] SSL plan  
- [ ] SMTP after domain (`noreply@<domain>` mailbox naming)  
- [ ] Indexing still closed until gate; Dashboard control ready; no auto-open  

## Anti-patterns to refuse

AP-001…018 in [ANTI-PATTERN-REGISTRY](../standards/FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md)  
AP-CMS-001…015 in [CMS-ANTI-PATTERNS](../standards/FORGE-WORDPRESS-CMS-ANTI-PATTERNS-v1.md)

---

*Starter checklist v1.1 — includes P1b CMS / editable architecture.*
