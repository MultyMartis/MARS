# WPilot

**Classification:** Program / Operational System.
**Chat type:** External Systems.
**Status:** **ACTIVE** — registry band; documented program pack in active reference use.
**Lifecycle:** [WPILOT-LIFECYCLE-STATE.md](WPILOT-LIFECYCLE-STATE.md) · **Reference Implementation** — first proven CMS Pilot runtime reference in MARS; **v0.3.0-RC5** proven on DEV; RC5 development focus **closed** (2026-06-19).
**Model reference:** [System Entity Model](../../governance/system-entity-model.md).

WPilot is a human-supervised AI-assisted WordPress administration system for testing whether a Cursor/operator workflow can safely inspect and make tightly scoped changes on a Beget-hosted test WordPress site.

Strategic direction: WPilot's preferred long-term target is **Factory-native WordPress** created through MARS Website Factory contracts. Legacy/external WordPress support remains a secondary compatibility bridge for existing sites with unknown builders, themes, plugins, and content shape.

## Current Runtime Status

| Field | Value |
|-------|-------|
| **Status** | **ACTIVE** |
| **Lifecycle state** | **Reference Implementation** |
| **Final state (RC5)** | [WPILOT-FINAL-STATE-RC5.md](WPILOT-FINAL-STATE-RC5.md) |
| **Authority** | `WPILOT-RC5-PROVEN-CONNECTION-RUNTIME-2026-06-19` |
| **Plugin version** | `0.3.0` (schema `0.2.0`) |
| **Release candidate** | `v0.3.0-RC5` — live on DEV |
| **Runtime maturity** | Proven content writes + authenticated REST bridge |
| **Environment** | DEV only — `https://dev.gktriumph.ru` |
| **Proven REST path** | inspect → backup → scoped-replace → validate → rollback |
| **Connection proof** | Authenticated REST, connection tracking, admin Last Successful Connection / Last Endpoint |
| **Maintenance policy** | [WPILOT-MAINTENANCE-POLICY-v1.md](WPILOT-MAINTENANCE-POLICY-v1.md) |
| **Sprint 3** | **HOLD** — explicit charter only |
| **RC5 spec** | [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md](WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md) |
| **Milestones** | [MILESTONE-001](milestones/WPILOT-MILESTONE-001-FIRST-PROVEN-WRITE-PATH.md) · [MILESTONE-002 RC5 Finalization](milestones/WPILOT-MILESTONE-002-RC5-FINALIZATION.md) |

Plugin source: `plugin/metacode-wpilot/`. Use as **reference runtime**, **architectural template**, and **validation source** for future CMS Pilots — not as active MVP development target. Not production. Not autonomous.

## MARS Token Standard

Operator token storage for WPilot REST auth is local-only under the MARS workspace:

| Field | Value |
|-------|-------|
| **Storage root** | `C:\MARS Phenix\AI MARS\local\tokens\` |
| **DEV token file** | `C:\MARS Phenix\AI MARS\local\tokens\wpilot-dev-gktriumph.token` |
| **Auth header** | `X-WPilot-Token` |
| **DEV site** | `https://dev.gktriumph.ru` |

Canonical policy: [local-storage-policy.md](local-storage-policy.md). Token values must never appear in git, reports, or chat transcripts intended for the repository.

## Mission Charter

Official positioning for WPilot: a **Personal WordPress Operations Platform** for the owner (Andrey / MetaCODE), human-supervised, backup-first, and integrated with MARS — not a public SaaS or autonomous WordPress administrator by default. Commercialization and public distribution are optional and not required for mission fulfillment.

Canonical document: [WPILOT-MISSION-v1.md](WPILOT-MISSION-v1.md)

## Core Model

Документированный policy stack WPilot v1 (сверху вниз по зависимости):

Mission → Operations Manifest → Risk Classes → ChangeSet → Rollback → Target Registry

Каждый слой отвечает на свой вопрос: зачем (Mission), что делать (Operations), насколько опасно (Risk), как выполняется run (ChangeSet), как откатывать (Rollback), на какие сущности можно воздействовать (Target Registry). Логическая модель; не доказательство runtime.

## Operations Manifest

Первый формальный слой операций WPilot: типизированные `operation_id`, категории (Inspection / Draft / Apply / Recovery), жизненный цикл, scope rules и список forbidden operations. Логическая модель; не доказательство реализации в плагине или runtime.

Canonical document: [WPILOT-OPERATIONS-MANIFEST-v1.md](WPILOT-OPERATIONS-MANIFEST-v1.md)

## Risk Classes

Формальный policy-слой риска для операций WPilot: шкала R0–R5 (Read Only → Forbidden), ожидания по approval, backup, validation и rollback. Дополняет Operations Manifest ответом на вопрос «насколько опасна операция»; не описывает реализацию в плагине или runtime.

Canonical document: [WPILOT-RISK-CLASSES-v1.md](WPILOT-RISK-CLASSES-v1.md)

## ChangeSets

Основная единица изменения в WPilot: контейнер, через который выполняются операции (не напрямую). ChangeSet фиксирует цель, риск, approval, backup, apply, validation, rollback и evidence trail. Логическая модель; не доказательство БД, API или runtime.

Canonical document: [WPILOT-CHANGESET-v1.md](WPILOT-CHANGESET-v1.md)

## Rollback

Policy-слой отката WPilot: что считается rollback, когда он обязателен, допустимые источники восстановления, validation after rollback, evidence и связь с ChangeSet и Risk Classes. Логическая модель; не доказательство runtime или plugin implementation.

Canonical document: [WPILOT-ROLLBACK-v1.md](WPILOT-ROLLBACK-v1.md)

## Target Registry

Канонический реестр целей WPilot: на какие сущности (page, post, shortcode, menu, header, footer и др.) могут воздействовать операции. Определяет `target_type` / `target_id` для ChangeSets, scope rules Manifest, rollback scope и будущих bindings. Policy/documentation layer; не доказательство plugin API или runtime.

Canonical document: [WPILOT-TARGET-REGISTRY-v1.md](WPILOT-TARGET-REGISTRY-v1.md)

## Operation Bindings

Официальный policy-слой связей между `operation_id`, допустимыми targets, `risk_class` и требованиями approval / backup / validation / rollback. Связывает Operations Manifest, Target Registry, Risk Classes, ChangeSet и Rollback expectations. Policy layer only; не endpoint map, не API contract, не plugin implementation.

Canonical document: [WPILOT-OPERATION-BINDINGS-v1.md](WPILOT-OPERATION-BINDINGS-v1.md)

## Proven Capabilities

Evidence-слой: только **подтверждённые** возможности WPilot по completed DEV work, reports, validation и recovery artifacts. Не roadmap, не policy, не forecast.

Canonical document: [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md)

## Site Snapshot Model

Каноническая модель состояния WordPress-сайта: структурированное описание site identity, structure, content, configuration и environment для inspection, validation, ChangeSet planning и rollback planning. Snapshot ≠ backup; логический state layer, не runtime и не API.

Canonical document: [WPILOT-SITE-SNAPSHOT-MODEL-v1.md](WPILOT-SITE-SNAPSHOT-MODEL-v1.md)

## Diff Model

Каноническая модель сравнения и описания различий между состояниями сайта: delta-записи (added, removed, modified, moved, unknown), уровни diff, severity, источники сравнения (snapshot, live, backup, operator verified). Diff ≠ backup, Diff ≠ snapshot; логический change layer между state capture и ChangeSet / validation / rollback planning. Не runtime и не execution engine.

Canonical document: [WPILOT-DIFF-MODEL-v1.md](WPILOT-DIFF-MODEL-v1.md)

## Core Architecture Review

Аудит Core Model v1 (2026-06-19): полнота архитектуры, матрица ответственности слоёв, циклические зависимости, терминология, canonical sources, избыточность, alignment Proven Capabilities, runtime readiness, стабильность модели и рекомендация **A — Stop Core Modeling, move to Runtime Contracts**. Документация only; без изменений кода, roadmap или runtime.

Canonical document: [WPILOT-CORE-ARCHITECTURE-REVIEW-v1.md](WPILOT-CORE-ARCHITECTURE-REVIEW-v1.md)

## Runtime Contracts

Мост Core Model v1 → реализация плагина: runtime boundary, ChangeSet/Snapshot/Diff в исполнении, операции, backup, минимальная DB, REST surface, mapping Proven Capabilities, конфликты и рекомендация следующего этапа (**Runtime Prototype**). Не Core Layer; не меняет Mission/Charter.

Canonical document: [runtime-contracts/WPILOT-RUNTIME-CONTRACTS-v1.md](runtime-contracts/WPILOT-RUNTIME-CONTRACTS-v1.md)

## State Freeze, Lifecycle & Milestones

- [WPILOT-FINAL-STATE-RC5.md](WPILOT-FINAL-STATE-RC5.md) — **RC5 final state** (Reference Implementation).
- [WPILOT-LIFECYCLE-STATE.md](WPILOT-LIFECYCLE-STATE.md) — lifecycle state definitions.
- [WPILOT-MAINTENANCE-POLICY-v1.md](WPILOT-MAINTENANCE-POLICY-v1.md) — post-RC5 maintenance policy.
- [WPILOT-AUTHORITY-STATE-RC5.md](WPILOT-AUTHORITY-STATE-RC5.md) — authority registration.
- [reports/wpilot-state-freeze-2026-06-19.md](reports/wpilot-state-freeze-2026-06-19.md) — RC5 release freeze.
- [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md](WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md) — live RC5 specification on DEV.
- [WPILOT-STATE-FREEZE-2026-06-19-v1.md](WPILOT-STATE-FREEZE-2026-06-19-v1.md) — Core Model + runtime sprint freeze.
- [milestones/WPILOT-MILESTONE-001-FIRST-PROVEN-WRITE-PATH.md](milestones/WPILOT-MILESTONE-001-FIRST-PROVEN-WRITE-PATH.md) — first proven plugin REST write path.
- [milestones/WPILOT-MILESTONE-002-RC5-FINALIZATION.md](milestones/WPILOT-MILESTONE-002-RC5-FINALIZATION.md) — RC5 finalization (**COMPLETE**).
- [ecosystem-sync/WPILOT-ECOSYSTEM-SYNC-RC5-2026-06-19.md](ecosystem-sync/WPILOT-ECOSYSTEM-SYNC-RC5-2026-06-19.md) — RC5 ecosystem sync.
- [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) — WPilot navigation index.

## What WPilot Is

- A documentation-first operational system under `projects/`.
- The **first proven CMS Pilot runtime reference implementation** in MARS (RC5 on DEV).
- A human-supervised workflow pack for inspection, backup confirmation, rollback planning, low-risk file-level tests, WP admin copy/create tests, WPBakery/The7 structure inspection, child theme CSS patch tests, QA, and reporting.
- A future bridge candidate for Website Factory-approved WordPress drafts, templates, structured content payloads, and human-approved publishing workflows.
- An External Systems lane because WordPress, Beget, hosting panels, databases, plugins, themes, and admin dashboards remain outside MARS ownership.

## What WPilot Is Not

- Not an autonomous WordPress admin.
- Not a MARS runtime component.
- Not a deploy bot.
- Not a universal autonomous WordPress AI runtime.
- Not credential storage.
- Not a plugin/theme updater.
- Not proof that MARS owns or controls any WordPress site.

## Strategic Modes

- **Mode A - Factory-native controlled sites:** primary target. Known stack, approved plugins/themes, approved templates, structured Website Factory content contracts, predictable layouts, known mutation zones, and human-approved publishing gates.
- **Mode B - legacy/external compatibility:** secondary target. WPBakery, The7, Elementor, unknown plugins/themes, historical HTML/content chaos, refusal-first inspection, dry-run-heavy validation, and conservative mutation policy.

WPBakery/The7 handling belongs to Mode B compatibility. It is valuable for the current DEV/testing baseline and existing site support, but it is not the ideal long-term WPilot target.

## Ecosystem Relationships (canonical visibility)

| System | Relationship |
|--------|--------------|
| **MARS Website Factory** | Upstream for Factory-native WordPress via **Forge WordPress** — [handoff contract](../mars-website-factory/subsystems/forge-wordpress/contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md) (documentation; not runtime claim). WPilot operates packages; does **not** design theme/content architecture. |
| **OCPilot** | **Sibling** in CMS/Ecommerce Pilots family; shared safety/access patterns only, no parent-child ownership. |
| **EAR Runtime** | Future provider candidate for published acquisition snapshots; relationship is planned and bounded by separate charters. |
| **ORCA** | Strategy/semantic upstream context when WordPress implementation is part of broader marketing workflow; no ORCA runtime ownership of WPilot. |

## Phase 1 Document Map

- [phase-1-mvp.md](phase-1-mvp.md) - MVP scope and workflow sequence.
- [boundaries.md](boundaries.md) - ownership, external-system, and forbidden-claim boundaries.
- [beget-test-plan.md](beget-test-plan.md) - Beget-hosted test-site run plan.
- [backup-rollback-rules.md](backup-rollback-rules.md) - backup confirmation and rollback discipline.
- [access-safety.md](access-safety.md) - credential and access handling rules.
- [local-storage-policy.md](local-storage-policy.md) - local-only `C:\MARS Phenix\AI MARS\backups\` and `C:\MARS Phenix\AI MARS\local\` policy, token handoff workflow, rollback snapshot storage, and no-secret-in-git rules.
- [qa-checklist.md](qa-checklist.md) - Phase 1 QA gates.
- [reports/test-report-template.md](reports/test-report-template.md) - operator report template.
- [templates/site-passport-template.md](templates/site-passport-template.md) - sanitized site facts template.
- [templates/change-request-template.md](templates/change-request-template.md) - scoped change request template.
- [templates/rollback-plan-template.md](templates/rollback-plan-template.md) - rollback plan template.

## Plugin MVP Planning Pack

- [plugin-mvp/reconciliation-map-v0.md](plugin-mvp/reconciliation-map-v0.md) - CORE reconciliation map; start here before changing plugin planning docs.
- [metacode-wpilot-plugin-concept.md](metacode-wpilot-plugin-concept.md) - PLANNED canonical plugin concept, MVP boundaries, REST surface, auth, audit, rollback, scoped replacement, and WPBakery strategy.
- [metacode-wpilot-plugin-mvp-roadmap.md](metacode-wpilot-plugin-mvp-roadmap.md) - PLANNED DEV-only plugin MVP sequence, strategic modes, Factory-native integration direction, and exclusions.

The plugin MVP planning pack is documentation only. It does not prove a WordPress plugin, runtime bridge, autonomous admin layer, production integration, or deployed code exists.

## Security Baseline

- No secrets in repo.
- No credentials, passwords, tokens, cookies, SSH keys, API keys, or hosting panel secrets.
- No `wp-config.php` copies or database dumps.
- No committed `C:\MARS Phenix\AI MARS\local\` or `C:\MARS Phenix\AI MARS\backups\` contents; those folders are local-only operational support if created on an operator machine.
- No destructive SQL.
- No live production changes in MVP.
- No plugin or theme updates in MVP.
- No autonomous editing claims.

## Future Agent Candidates

Future WPilot roles may later belong in `agents/` only if the operator chooses to define bounded agent cards. Candidate roles include `wp-audit-agent`, `css-patch-agent`, `backup-rollback-agent`, `wp-admin-copy-agent`, and `qa-report-agent`.

Until then, they are candidate roles only, not running agents.

## SAFE UNKNOWN

- Exact Beget panel permissions, WordPress admin roles, FTP/SFTP access, and database visibility are unknown until the operator provides verified external evidence.
- The target site theme, child theme state, WPBakery usage, plugin list, and backup tooling on **new** sites are unknown until REST inspection — DEV baseline (`dev.gktriumph.ru`) is proven for RC5.
- Production safety is unknown unless the operator confirms the environment is a test site.
