# OCPilot Boundaries

**Status:** documented boundary rules.  
**Entity:** Program / Operational System — standalone OpenCart bridge (см. [architecture.md](architecture.md)).

## Ownership

| Owner | Responsibility |
|-------|----------------|
| Human operator | Final approval, credentials, target confirmation, backup confirmation |
| OpenCart site / hosting | Live execution truth, files, DB, modules, theme |
| MARS repo (`projects/ocpilot/`) | Sanitized guides, templates, reports — **not** proof of access |

## External systems (не принадлежат MARS)

OpenCart installation, hosting panel, FTP/SFTP, phpMyAdmin, CDN, payment/shipping extensions, ocMod/vQmod vendors, image storage.

## Operational prohibitions

| Rule | Meaning |
|------|---------|
| No production edits without approval | Любая запись на live — только после explicit human charter + REPORT |
| No destructive SQL without approval | DROP/TRUNCATE/mass DELETE — запрещены без HITL |
| No credentials in repo | Пароли, tokens, `config.php` secrets, DB dumps — вне git |
| No FTP/PMA/browser without human-confirmed target | URL/host/path/DB name подтверждает оператор до действия |
| No database overwrite without backup | Restore/import — только после documented backup |
| No controller/module/theme change without rollback path | [templates/rollback-plan-template.md](templates/rollback-plan-template.md) обязателен до write-phase |
| No autonomous actions | Агент не «сам» правит сайт, хостинг или БД |

## Forbidden claims

- OCPilot autonomously administers OpenCart.
- OCPilot is part of WPilot or «WPilot for OpenCart».
- MARS owns hosting, OpenCart license, or client production data in repo.
- Registry/README presence proves runtime bridge or plugin exists.

## Forbidden paths (OCPilot work must not land in)

- `mars-runtime/**`
- `workspaces/**`
- `projects/wpilot/**` (sibling — read patterns only)
- `projects/orca/**` (reference only)
- `projects/mars-website-factory/**`
- Client production trees committed with secrets

## Production rule

Default: **read-only / planning**. Production write requires new charter, backup evidence, rollback plan, risk class review (см. mars-survivability patterns — advisory, not auto-enforced).

## SECURITY RISK

Accidental secret in repo or chat → stop, notify operator, no further copy. Rotate credentials per operator instruction.
