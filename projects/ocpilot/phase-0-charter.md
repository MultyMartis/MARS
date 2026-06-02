# OCPilot — Phase 0 Charter

**Status:** **CURRENT** (единственная активная фаза на момент создания скелета).  
**Goal:** структура репозитория + operational documentation baseline.  
**Not in scope:** runtime, плагины OpenCart, live FTP/PMA, catalog import execution.

## Delivered in Phase 0

- Дерево `projects/ocpilot/` по OPERATIONAL-INDEX skeleton.
- Core docs: README, boundaries, architecture, workflows, access rules.
- Templates для паспортов, change request, rollback, inspection, DB snapshot metadata.
- Placeholder zones: `baselines/`, `sites/_template-site/`, `freeze/battle-pilots/`.

## Explicit exclusions (Phase 0)

- Нет изменений production OpenCart.
- Нет коммита credentials, дампов, `config.php` с секретами.
- Нет правок `mars-runtime/`, `workspaces/`, WPilot, ORCA, Website Factory.
- Нет claims: autonomous hosting, auto catalog import, deployed bridge.

## Exit criteria (human-reviewed)

| Criterion | Evidence |
|-----------|----------|
| Structure exists | Tree under `projects/ocpilot/` |
| Docs readable | README + OPERATIONAL-INDEX + boundaries |
| Sibling model correct | architecture.md — standalone, WPilot = sibling |
| Next run identified | Run 2: Clean OpenCart Baseline Setup |

## Next run after Phase 0

**Run 2 — Clean OpenCart Baseline Setup:** зафиксировать версию OpenCart, sanitized file tree + DB schema snapshot metadata в `baselines/clean-opencart/` (без секретов в git). См. [clean-opencart-baseline.md](clean-opencart-baseline.md).
