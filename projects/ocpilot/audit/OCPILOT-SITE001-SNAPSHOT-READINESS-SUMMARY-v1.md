# OCPilot SITE-001 Snapshot Readiness Summary v1

**Status:** **documented** — snapshot acquisition readiness summary (audit only).  
**Program:** OCPilot + EAR  
**Audit date:** 2026-06-07  
**Parent:** [OCPILOT-SITE001-SNAPSHOT-READINESS-AUDIT-v1.md](OCPILOT-SITE001-SNAPSHOT-READINESS-AUDIT-v1.md) · [OCPILOT-SITE001-SNAPSHOT-READINESS-REGISTER-v1.md](OCPILOT-SITE001-SNAPSHOT-READINESS-REGISTER-v1.md)  
**Is not:** acquisition, Run 5 execution, git commit.

---

## Final verdict

```text
READY FOR ACQUISITION REQUEST — NOT READY FOR RUN 5 EXECUTION
```

SITE-001 charter **authorized**; Run 5 execution **paused** until первый **EAR Snapshot Package Quality Level 1** опубликован. Минимальный пакет для возобновления Run 5 (Phases 2–3) требует **version proof** + **file-manifest** + **acquisition-log** с подтверждением канала. Режим **Mode 1 (Guided Evidence)** — рекомендованный; **Mode 2 недоступен** (PILOT-001 не авторизован).

---

## 1. Minimum Snapshot Package (exact checklist)

**Target:** `package_quality_level: 1` · `ear_mode: 1` · `snapshot_contract: ear-opencart-snapshot-v1`

### Hard gate (Run 5 Phases 2–3)

| ✓ | Section / export | Source |
|---|------------------|--------|
| ☐ | Package **identity** + **metadata/** (platform ocStore, baseline `ocstore-3038-rs2`, consumer `ocpilot`) | EAR assembly |
| ☐ | **environment/** = TEST | Passport / brief |
| ☐ | **acquisition-log/** + **EXP-P3-C** channel confirmation | Operator |
| ☐ | **EXP-P1-A** — version proof (`index.php`, `admin/index.php`) | Operator |
| ☐ | **EXP-P1-B** — root folder layout | Operator |
| ☐ | **EXP-P1-C** — file manifest (`admin/`, `catalog/`, `system/`) | Operator |
| ☐ | **safe-unknown/** — honest list of deferred P2/P3 items | Operator + EAR |

### May defer at `p1` (phases blocked until `p2` or section filled)

| ✓ | Section / export | Blocks phase |
|---|------------------|--------------|
| ☐ | **theme-info/** ← EXP-P2-A | Phase 4 |
| ☐ | **extension-inventory/** + **ocmod-inventory/** ← EXP-P2-B | Phase 5 |
| ☐ | **seo-structure/** ← EXP-P3-A | Phase 6 |
| ☐ | **database-metadata/** ← EXP-P3-B | Phase 7 |

**Validate rule:** без version proof в manifest → Level 1 **fail** → Run 5 не возобновляется.

---

## 2. Required acquisition mode

| Mode | Verdict |
|------|---------|
| **Mode 0** — Manual Evidence | **Allowed** (fallback) |
| **Mode 1** — Guided Evidence | **REQUIRED RECOMMENDATION** |
| **Mode 2** — Connected Read Only | **NOT AVAILABLE** — PILOT-001 execution NOT STARTED; dry run does not authorize live SFTP |
| **Mode 3** — Read Write | **Forbidden** |

**Recommended path:** Mode 1 + Path **L1-D** (Beget panel → ZIP) or **L1-A** (ZIP drop) or **L1-B** (manual SFTP).

---

## 3. Required operator actions (summary)

| Priority | Action |
|----------|--------|
| **P0** | Choose Mode 1; target Level 1; select acquisition path |
| **P0** | Re-verify TEST URL; confirm external credentials location |
| **P0** | Deliver P1 exports + P3-C channel note to external bulk |
| **P0** | Define exclusions + config redaction; name Validate/Publish approver |
| **P0** | **Do not** start PILOT-001 or Mode 2 without HG-4 authorization |
| **P1** | Document safe-unknown plan for deferred P2/P3 |
| **P2** | Optional doc sync (access-brief, README, passport pause notes) |

---

## 4. Required files and exports

| ID | File | External location |
|----|------|-------------------|
| EXP-P1-A | Version excerpts | `...\site-001\materials\run5\` |
| EXP-P1-B | Root layout listing | `...\site-001\materials\run5\` |
| EXP-P1-C | `run5-file-manifest.txt` | `...\site-001\materials\run5\` |
| EXP-P3-C | `acquisition-channel-note.md` | `...\site-001\materials\run5\` |
| EXP-P2-C | Optional compact ZIP | `...\site-001\snapshots\files\` |

**Forbidden in all artifacts:** passwords, live `config.php`, API keys, session cookies, customer PII, full DB dumps.

---

## 5. Expected deliverables

### After acquisition cycle (EAR)

1. Candidate Snapshot Package assembled from exports  
2. Validate PASS at Level 1 (human HITL)  
3. Published `snapshot_id` (e.g. `snap-YYYYMMDD-site-001-run5-p1`)  
4. Repo index note — external paths only  

### After OCPilot consumes snapshot (Run 5 resume)

| Phase | Output |
|-------|--------|
| 2 | `opencart-analysis/version-verification-v1.md` |
| 3 | `opencart-analysis/file-diff-summary-v1.md` |
| 4–7 | Theme / extension / SEO / DB reports (as sections available) |
| 8 | `reports/RUN-5-AUDIT-REPORT.md` |
| — | Registry → **AUDIT IN PROGRESS** (human approval) |

Optional **`p2` snapshot** for extension/SEO/DB gaps per partial re-entry model.

---

## 6. Readiness score

| Check | Result |
|-------|--------|
| Charter | **PASS** |
| Baseline | **PASS** |
| EAR docs | **PASS** |
| EAR readiness checklist (20 items) | **4 pass** — **FAIL** (Acquire gate) |
| Operator P1 exports | **FAIL** |
| Published snapshot | **FAIL** |
| Run 5 execution | **BLOCKED** (correct) |

---

## 7. Related documents

| Doc | Role |
|-----|------|
| [OCPILOT-SITE001-SNAPSHOT-READINESS-AUDIT-v1.md](OCPILOT-SITE001-SNAPSHOT-READINESS-AUDIT-v1.md) | Full audit |
| [OCPILOT-SITE001-SNAPSHOT-READINESS-REGISTER-v1.md](OCPILOT-SITE001-SNAPSHOT-READINESS-REGISTER-v1.md) | Registers |
| [RUN-5-DATA-REQUEST.md](../sites/site-001/tasks/RUN-5-DATA-REQUEST.md) | Guided artifact list |
| [AUDIT-BLOCKERS-v1.md](../freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md) | Blocker authority |

---

*OCPilot SITE-001 Snapshot Readiness Summary v1 — documentation only.*

---

OPERATOR ACTIONS REQUIRED

1. **Зафиксировать решение по режиму:** выбрать **Mode 1 (Guided Evidence)**; записать `ear_mode: 1`, target **Quality Level 1**, sequence `p1` — в acquisition request (вне git или в supervised session note).
2. **Выбрать путь сбора:** приоритет **L1-D** (Beget panel → ZIP); запасные **L1-A** (ZIP drop) или **L1-B** (ручной SFTP). **Не** выбирать Mode 2 / PILOT-001 без HG-4 authorization.
3. **Перепроверить TEST URL:** подтвердить, что `https://sibcar.new-site.space/` доступен; зафиксировать в **EXP-P3-C**.
4. **Подтвердить канал доступа (P3-C):** записать в `materials/run5/acquisition-channel-note.md` — какой канал разрешён (panel / SFTP / ZIP-only / evidence-only); admin URL pattern без credentials.
5. **Проверить credentials:** убедиться, что секреты лежат только в `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\secrets\` — не в репозитории.
6. **Подписать read-only discipline:** явное подтверждение — без записи файлов, SQL mutation, admin changes, cache reset.
7. **Определить policy исключений manifest:** cache, logs, sessions, `image/catalog/` — исключить из P1-C per RUN-5-DATA-REQUEST.
8. **Определить plan редактирования config.php:** ZIP/архивы без тел `config.php` / `admin/config.php`; redacted stub или omit.
9. **Назначить Validate и Publish approver (HITL):** два distinct ref per EAR dual-HITL model.
10. **Собрать EXP-P1-A:** sanitized version excerpts из `index.php` и `admin/index.php` → `materials/run5/`.
11. **Собрать EXP-P1-B:** listing корня сайта (top-level folders, наличие `install/`) → `materials/run5/`.
12. **Собрать EXP-P1-C:** file manifest `admin/`, `catalog/`, `system/` → `materials/run5/run5-file-manifest.txt` (или manifest из ZIP после L1-D).
13. **(Опционально) EXP-P2-C:** compact ZIP без secrets/media bulk → `snapshots/files/` — если P1-C проще сделать offline.
14. **Задокументировать safe-unknown для p1:** перечислить отложенные EXP-P2-A/B, P3-A/B — theme, extensions, SEO, DB metadata.
15. **Уведомить OCPilot:** сообщить external paths + one-line description каждого файла — **без секретов в чате**.
16. **Передать пакет в EAR цикл:** Request → Acquire (assembly) → Validate L1 → Publish → получить `snapshot_id`.
17. **После publish — запросить возобновление Run 5:** human charter для Phases 2–8; обновить registry → **AUDIT IN PROGRESS** при старте Phase 2.
18. **Не выполнять:** live SFTP через PILOT-001, Mode 2, Run 5 execution, Phase 1 writes — до появления published snapshot и отдельного resume charter.
