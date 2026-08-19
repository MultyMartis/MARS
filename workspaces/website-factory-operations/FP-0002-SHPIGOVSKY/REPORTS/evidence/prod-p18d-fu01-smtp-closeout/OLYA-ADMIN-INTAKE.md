# OLYA / ADMIN INTAKE — P18D-FU01

## Rule used

Normal WordPress Admin edits by Olya/Admin are treated as **current production truth** for content and editor-owned settings.

They are:

- not code drift;
- not QA residue;
- not candidates for rollback from older DB snapshots.

## Fresh intake summary

Source: `02-activity-and-qa-leads.json`

### Preserved editorial/Admin changes

- `admin` updated legal pages on 2026-08-18:
  - `#3` Политика конфиденциальности
  - `#22` Пользовательское соглашение
  - `#23` Согласие на обработку персональных данных
  - `#24` Политика Cookie-файлов
- `admin` updated homepage, services, and specialists on 2026-08-16:
  - homepage `#4`
  - services `#73`, `#74`, `#1889`, `#1894`
  - specialists including `#1031`, `#1032`, `#1097`, `#1949`, `#1957`, `#1963`, `#1967`, `#1988`

Classification: **business/editorial/Admin truth**  
Action: **preserve / no rollback**

### Technical/Admin state changes

- SMTP settings saves and recipient changes on 2026-08-19 by `mars`, `metacode`, and `admin`
- SMTP test failures recorded before FU01 correction
- `indexing_opened` recorded on 2026-08-19 by `admin`

Classification: **technical / launch-state / operator-controlled**  
Action:

- SMTP settings preserved and corrected in place for verified activation
- indexing re-closed in FU01 per current gate and operator charter

### Unknowns not force-mutated

- Activity Log rows with `System` actor from prior indexing QA/history were not treated as proof of current operator intent
- No broad DB rollback
- No broad option overwrite from historical exports

## FU01 conclusion

**OLYA ADMIN CHANGES PRESERVED AS CURRENT PRODUCTION TRUTH**

Editorial/Admin object edits remain live.  
Technical closeout mutated only SMTP/indexing runtime state and exact QA/MU artifacts needed for safe mail closeout.
