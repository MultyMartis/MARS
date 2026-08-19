# REPORT — FP-0002 PROD-P18D-FU01 SMTP Closeout + Olya Intake

**Date:** 2026-08-19  
**Evidence:** `REPORTS/evidence/prod-p18d-fu01-smtp-closeout/`

## 1. Status

**PASS**

Fresh production intake showed that runtime was still effectively at `P18C-FU02`, not the assumed P18D end-state: SMTP was complete-but-failing (`smtp_encryption=none`, `verified=0`, `delivery_active=0`), the suppression MU still existed, and indexing was open. FU01 corrected runtime to the intended production truth without rolling back Olya/Admin editorial work.

## 2. Olya/Admin Intake

**OLYA ADMIN CHANGES PRESERVED AS CURRENT PRODUCTION TRUTH**

- Recent `admin` edits to homepage, legal pages, services, and specialists were detected in Activity Log and preserved.
- These changes were treated as current editorial/Admin truth in the Beget database.
- No old DB snapshot or historical manifest was applied over current editor-owned content.

See: `OLYA-ADMIN-INTAKE.md`, `ACTIVITY-LOG-CLASSIFICATION.md`

## 3. Code Reality

**P18D-FU01 CURRENT PRODUCTION CODE REALITY VERIFIED**

Fresh file intake confirmed:

- `MailOps.php` — MATCH
- `SmtpTransport.php` — MATCH
- `ConsultationHandler.php` — MATCH
- `ActivityLog.php` — MATCH
- `LeadRegistry.php` — MATCH
- `SystemDashboard.php` and `shpigovsky-core.php` were stale before FU01 source/runtime sync
- MU file `fp02-pre-cutover-mail-suppression.php` existed physically before FU01

## 4. SMTP

**SMTP VERIFIED / ACTIVE STILL TRUE BEFORE CLOSEOUT**

Actual fresh intake found runtime not yet there:

- host `smtp.beget.com`
- port `465`
- encryption `none`
- state `ERROR`
- verified `0`
- delivery_active `0`

FU01 corrected `none -> ssl`, ran a bounded SMTP test, recorded `verified_ready`, then activated delivery to `verified_active`.

## 5. Suppression Retirement

**PRE-CUTOVER MAIL SUPPRESSION MU PHYSICALLY REMOVED**

- file existed at `wp-content/mu-plugins/fp02-pre-cutover-mail-suppression.php`
- SHA-256 before removal: `d725dcd63c2cf60131f7c4c72852c43312c7e8a797f48dcbc8d3ff6280d52834`
- readiness proven first (`verified_active`, `should_suppress=false`)
- exact file snapshot stored in evidence
- exact file removed
- `pre_wp_mail` callbacks after removal: none

## 6. Post-Removal Delivery

**SMTP / FORM DELIVERY STILL PASS AFTER MU REMOVAL**

- post-removal runtime state: `verified_active`
- bounded QA form/mail proof: PASS
- QA lead `#7` reached `MAIL_ACCEPTED`
- recipient count at send time: `2`
- no fatal; dashboard/runtime still healthy

## 7. QA Cleanup

**P18D QA LEADS CLEANED WITHOUT TOUCHING REAL LEADS**

- exact QA lead created: `#7`
- markers: `is_qa=1`, `form_context=p18d-fu01-qa`, `utm_source=p18d-fu01-qa`
- exact deletion after evidence capture: PASS
- no other QA rows remained

## 8. Validation Tools

**P18D VALIDATION TOOL LIFECYCLE RESOLVED**

- P18D validation helpers remain canonical in `WORDPRESS/validation/`
- they are source-only controlled execution tools
- they must not remain public webroot artifacts
- FU01 normalized source syntax so the scripts are valid for controlled execution

## 9. Admin Settings

- SMTP status: **VERIFIED / ACTIVE**
- host / port / encryption: `smtp.beget.com` / `465` / `ssl`
- username: `noreply@shpigovsky.ru`
- password: configured, hidden
- recipients: `2`
- Metrika goal: empty but preserved
- retention: `0`, preserved

## 10. Dashboard

**METACODE DASHBOARD REFLECTS POST-SMTP-CLOSEOUT REALITY**

FU01 updates target:

- live domain `https://shpigovsky.ru`
- Production / Beget
- SMTP VERIFIED / ACTIVE
- sender `noreply@shpigovsky.ru`
- recipients `2`
- temporary suppression REMOVED
- registry ACTIVE
- indexing CLOSED
- latest wave `P18D-FU01 SMTP Closeout + Olya Intake`

## 11. Public Domain

- `https://shpigovsky.ru/` now returns WordPress
- `http://shpigovsky.beget.tech/` resolves through to the live WordPress domain
- old “Craftum currently visible” dashboard note is stale and replaced by FU01 truth

## 12. Indexing

**INDEXING REMAINS CLOSED**

Fresh intake found `blog_public=1` and a live open robots policy despite prior assumptions. FU01 re-closed indexing via `IndexingControl`, restoring:

- `blog_public=0`
- `robots.txt` with `Disallow: /`
- dashboard/indexing state back to closed

## 13. Editorial vs Code Authority

**EDITORIAL PRODUCTION TRUTH IS PRESERVED ACROSS TECHNICAL WAVES**

- Production DB edits through normal Admin are editorial/Admin truth.
- Source-controlled theme/plugin/ACF code remains Git authority after drift intake.
- Old full backups are rollback artifacts, not the source of current editorial truth.

## 14. Parity

**CODE PARITY PASS / EDITORIAL DB TRUTH PRESERVED**

Source-owned SMTP/form/leads files were verified against production before mutation.  
FU01 then aligned runtime state without overwriting editorial DB content.

## 15. Git Replay

**P18D KNOWLEDGE + PRODUCTION SOURCE PRESENT ON CANONICAL REMOTE**

Approved local P18D commits to replay:

- `83f9eaf2` → `FP-0002: verify and activate production SMTP`
- `89cd35ed` → `WP Forge: standardize SMTP verification and activation lifecycle`

FU01 adds closeout/source-status/dashboard/editorial-truth updates on top.

## 16. Secret Scan

**PASS**

- SMTP password not printed
- no credentials stored in evidence
- recipient addresses not dumped broadly outside bounded runtime state

## 17. Dirty Main

- dirty shared branch remained untouched for foreign WIP
- canonical replay must occur from a clean worktree based on current `origin/mars/canonical-post-recovery`

## 18. Remaining Work

1. Public-domain finalization only if operator later observes a routing regression.
2. Olya indexing approval.
3. Sitemap submissions.
4. Final crawl.

Open business decision:

- form lead retention period

## 19. Acceptance

**FP-0002 P18D-FU01 COMPLETE — OLYA'S CURRENT ADMIN/EDITORIAL CHANGES PRESERVED AS PRODUCTION TRUTH — SMTP REMAINS VERIFIED / ACTIVE — PRE-CUTOVER MAIL SUPPRESSION MU PHYSICALLY RETIRED — POST-REMOVAL MAIL/FORM DELIVERY VERIFIED — QA LEADS CLEANED EXACTLY — VALIDATION TOOL LIFECYCLE RESOLVED — DASHBOARD UPDATED — P18D REPLAY READY FOR SAFE CANONICAL CHERRY-PICK — EDITORIAL DB TRUTH AND CODE DRIFT ARE EXPLICITLY SEPARATED — INDEXING REMAINS CLOSED**
