# SITE-002-M9-PDP-CONSOLIDATION-CHECKPOINT-01

**Verdict:** `SITE-002 M9 PDP CONSOLIDATION CHECKPOINT COMPLETE — ACCEPTED STATE RECORDED`

**Date (UTC):** 2026-09-07  
**Site:** SITE-002 / ЗПМ Production (`https://bzpm.ru/`)  
**Mode:** no-mutation consolidation checkpoint  
**Branch:** `mars/canonical-post-recovery`  
**HEAD:** `17e717ed33ba945b13a2fad9a64efafd851876ad`

Storage evidence root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-M9-PDP-CONSOLIDATION-CHECKPOINT-01\`

---

## 1. Scope

Record the accepted production state after M9 filter and PDP hero-spec waves. Inventory live files, rollback/evidence folders, uncommitted repo/report state, public HTTP GET smoke, and a safe continuation map.

This is **not** a development, deploy, import, cache, or rollback task.

---

## 2. No-mutation boundary

Confirmed this pass:

- DB writes: none
- FTP writes / STOR: none (FTP GET / RETR only)
- Deploy / cache clear / import / baseline refresh: none
- M9 profile / PDP resolver / `global_hidden.php` / template edits: none
- Cleanup / delete / rollback / git prune / gc / force push / `git add .` / `git add -A` / `git commit -a`: none
- Screenshot recapture: none (`screenshot_capture_allowed: false`)
- n8n / Data Table / Telegram: none

`manifests/operation.json` flags are all false. Environment: `NO_MUTATION_CONSOLIDATION_CHECKPOINT`.

---

## 3. Inputs read

All seven required reports exist under `projects/ocpilot/sites/site-002/reports/`. Storage copies exist under each wave’s deployment folder.

| Operation | Repo report git |
|-----------|-----------------|
| SITE-002-PROD-M9-STELLAZHI-PROFILE-86-01 | untracked `??` |
| SITE-002-PROD-PDP-HERO-SPECS-STELLAZHI-86-01 | untracked `??` |
| SITE-002-PROD-M9-STOLY-PROFILE-301-REFRESH-01 | tracked; local `3bfd717c` **unpushed** |
| SITE-002-PROD-M9-POLKI-PROFILE-331-01 | untracked `??` |
| SITE-002-PROD-M9-HLEBOPEKARNOE-PROFILE-186-01 | untracked `??` |
| SITE-002-M9-FILTERS-AND-PDP-VISUAL-QA-PASS-01 | untracked `??` |
| SITE-002-PROD-PDP-HERO-SPECS-HLEBOPEKARNOE-186-01 | untracked `??` |

Report files often still say `OPERATOR VISUAL CHECK REQUIRED`. Operator later accepted those waves (charter + combined visual QA). This checkpoint records the **accepted** state, not the original report heading.

Repo mirrors read under `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/patch/system/library/zpm/`:

- `filter_profiles/86_stellazhi.php`
- `filter_profiles/301_stoly.php`
- `filter_profiles/331_polki.php`
- `filter_profiles/186_hlebopekarnoe.php`
- `filter_profile_resolver.php`

`product_hero_specs_resolver.php` is **not** in the repo. Authority: live production + Storage payload under `SITE-002-PROD-PDP-HERO-SPECS-HLEBOPEKARNOE-186-01\deploy\payload\`.

---

## 4. Accepted production state

### Filters (M9)

- **`[86] Стеллажи`** — profile live; resolver additive 86; `Стандарт` hidden; visual PASS
- **`[301] Столы`** — profile refreshed; `Тип опоры` PRIMARY → SECONDARY; attrs 47/51 unchanged; visual PASS
- **`[331] Полки`** — new profile; resolver additive 331; `global_hidden.php` unchanged; visual PASS
- **`[186] Хлебопекарное`** — new root profile; inherited by `[188] Миксеры` and `[189] Тестомесы`; hub has no listing/sidebar expected; later visual accepted via combined pass

### PDP hero specs

- **`[86] Стеллажи`** — family fields after L/W/H/mass when present; lower `Характеристики` table preserved
- **`[186] Хлебопекарное`** — Mixer V30 and Тестомес ТТ-D25D show family fields as in the 186 PDP report; `[86]` shelving PDP regression unchanged on this smoke

Live SHA256s of the six inventoried files match last-wave expected hashes. No dangerous live vs expected mismatch.

---

## 5. Recent wave inventory

| Operation | Verdict (accepted) | Prod files | Rollback | Screenshots |
|-----------|--------------------|------------|----------|-------------|
| STELLAZHI M9 86 | PASS | `86_stellazhi.php` + resolver additive | yes | combined QA |
| STELLAZHI PDP 86 | PASS | `product_hero_specs_resolver.php` NEW + `product.php` PATCH | yes | combined QA (07 clip sparse) |
| STOLY 301 refresh | PASS | `301_stoly.php` only | yes (`27b89d42…`) | combined QA |
| POLKI 331 | PASS | `331_polki.php` NEW + resolver additive | yes | combined QA |
| HLEBOPEKARNOE M9 186 | PASS (visual later) | `186_hlebopekarnoe.php` NEW + resolver additive | yes (resolver `8e28a86a…` + delete 186) | combined QA |
| Combined visual QA | PASS (no prod change) | none | n/a | 14 PNG in Storage |
| HLEBOPEKARNOE PDP 186 | PASS | `product_hero_specs_resolver.php` only | yes | operator visual; combined QA used B5/SH-20 earlier |

Combined QA mixer/testomes PDPs used **B5 / SH-20**; the 186 PDP wave used **V30 / TT-D25D**. Both recorded; not a contradiction.

CSV: Storage `storage-evidence-inventory/wave-evidence-inventory.csv`.

---

## 6. Live file inventory

FTP GET / RETR only. `ftp_ok: true`. Fetched copies under Storage `live-file-inventory/fetched/`.

| Remote path | Exists | Bytes | SHA256 | MDTM | Last owning wave |
|-------------|--------|-------|--------|------|------------------|
| `.../filter_profiles/86_stellazhi.php` | yes | 1596 | `69ed7773295933ae6cc42281b418aa8aa2935d61c7d9e40f4c804dea9c747f16` | 20260906182421 | STELLAZHI M9 86 |
| `.../filter_profiles/301_stoly.php` | yes | 1423 | `df7233eaaa770b4d8d01ca4aaf25ecdd28c825c2f80de9dcd8a4ab70dee84715` | 20260906202028 | STOLY 301 |
| `.../filter_profiles/331_polki.php` | yes | 1812 | `ab301a5cc61baf69b20a223091e617dd5c8a4f7748f8982acf74bee4d64a8b04` | 20260906205401 | POLKI 331 |
| `.../filter_profiles/186_hlebopekarnoe.php` | yes | 1975 | `e4863b92dfb80ca90e8c964c009afe9619bc034a34ac94ca82667618a8249958` | 20260906213515 | HLEBOPEKARNOE M9 186 |
| `.../filter_profile_resolver.php` | yes | 6321 | `0d9941918e0092e3489b0567936e8b81fd805bdc4bc062b54158672d7d6d8fd9` | 20260906213517 | last additive 186 |
| `.../product_hero_specs_resolver.php` | yes | 4309 | `19c9bc82368ff5d50b27540b59d3abfd995943995eb70714656ffd6ba68f534e` | 20260907082953 | HLEBOPEKARNOE PDP 186 |

Repo profile mirrors for 86 / 301 / 331 / 186 are **byte-identical** to live. Repo `filter_profile_resolver.php` is **not** (5984 / `4c23c39a…` vs live 6321 / `0d994191…`) — expected CRLF/additive live vs mixed working copy.

---

## 7. Rollback map

Record only. Do **not** execute without a separate charter.

Filter resolver SHA chain: 86 `e2110576…` (6245) → 331 `8e28a86a…` (6277) → 186 live `0d994191…` (6321).

PDP hero resolver: 86 `452ebf1e…` (3002) → 186 live `19c9bc82…` (4309).

`product.php` patched only in STELLAZHI PDP 86 (`6074f749…`, 50109). 186 PDP did not re-upload it.

STOLY restore: `rollback-ready/301_stoly.php` SHA `27b89d42…`.

HLEBOPEKARNOE M9 undo: restore resolver `8e28a86a…` **and delete** `186_hlebopekarnoe.php`.

Combined QA: no rollback (no production change).

---

## 8. Repo / Git state

- Workspace: `X:\AI MARS`; volume label **AI WS**
- Branch: `mars/canonical-post-recovery`
- HEAD ≠ `origin/mars/canonical-post-recovery` (`131882bd…`)
- Staged: empty
- Unpushed: **280** commits, including `3bfd717c — ocpilot: refresh M9 tables filter profile`
- `git status --short` line count: **1395** (foreign WIP — not staged, restored, cleaned, or listed here)
- STOP tokens for commit/push: `UNPUSHED COMMITS PRESENT`, `REMOTE/HEAD MISMATCH`

Relevant M9/PDP paths:

- `M` `filter_profile_resolver.php` — do not commit until reviewed vs live
- `??` reports for 86 / PDP 86 / 331 / 186 / combined QA / 186 PDP / this checkpoint
- tracked 301 report + `301_stoly.php` already in unpushed `3bfd717c`

**Commit this pass:** skipped. Reason: dirty tree + 280 unpushed commits; charter allows commit only if exceptionally clean and **only** this report is staged. That bar is not met. **No push.**

Later allowlist (operator isolation required): untracked wave reports + byte-identical `86`/`331`/`186` profile mirrors + this checkpoint report. Never `git add .`.

---

## 9. Public smoke

HTTP GET only. 14 URLs. `smoke_hard_fail: false`. No PHP warnings. No public `БЗПМ`.

All listed PLP/PDP/root pages **200** except `/zapchasti` **404** (expected). Sidebar present on listing PLPs. Hub `/hlebopekarnoe-oborudovanie` has no listing/sidebar expected. PDP hero phrases present on shelving / V30 / TT-D25D. `/upakovochnoe-oborudovanie` 200 with **DZ-260**. `/posuda-i-inventar` 200.

No click tests this pass.

---

## 10. Known SAFE UNKNOWN

- PRIMARY attr click/reset on some PLPs: combined QA clicked `in_stock=1`; not retested here
- `[207] Зонты` 404 noted in the 86 report; not in this smoke list
- Whether origin will ever receive the 280 local commits (including `3bfd717c`)
- Exact byte-level cause of repo vs live resolver mismatch (CRLF vs additive vs mixed WC) until a review charter
- Combined QA screenshot glob in Cursor vs PowerShell (14 files exist on disk)

---

## 11. Known intentionally unchanged

- `/zapchasti` 404
- `/upakovochnoe-oborudovanie` 200 with DZ-260 placeholder image
- `/posuda-i-inventar` generic/basic filter, not M9-prioritized
- L/W/H sliders as a separate UX layer
- `global_hidden.php` not edited in these waves
- No DB / product / SEO writes in the listed waves
- `product.php` not changed in the 186 PDP wave

---

## 12. Next work map

Do not start automatically. Operator picks.

- **A** Git/report consolidation after isolation charter (recommended if hygiene is next; resolver needs review; PDP resolver not in repo)
- **B** PDP hero specs for `[331] Полки` only if useful after visual review
- **C** Real photo for Upakovochnoe DZ-260
- **D** L/W/H slider charter
- **E** More M9 categories — operator-selected only

Must not touch without a separate charter: live M9/PDP files, `product.php`, `global_hidden.php`, DB/FTP write, cache, import, SEO, `/zapchasti` 404, foreign WIP, force push.

Recommended: **wait for operator pick.** Candidate A only after isolation.

---

## 13. Storage artifacts

Root: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-M9-PDP-CONSOLIDATION-CHECKPOINT-01\`

Includes: `preflight/`, `reports-read/`, `live-file-inventory/` (+ `fetched/`), `repo-inventory/`, `storage-evidence-inventory/`, `public-smoke/` (+ `bodies/`), `rollback-map/`, `git/`, `decision-map/`, `next-work/`, `reports/`, `logs/`, `manifests/operation.json`.

---

## 14. Final verdict

**`SITE-002 M9 PDP CONSOLIDATION CHECKPOINT COMPLETE — ACCEPTED STATE RECORDED`**

No production mutation. Live files match last-wave hashes. Public smoke matches expected 200/404 pattern. Waves reconciled. Rollback map recorded. Next-work map recorded. Git commit skipped because of foreign WIP and 280 unpushed commits.
