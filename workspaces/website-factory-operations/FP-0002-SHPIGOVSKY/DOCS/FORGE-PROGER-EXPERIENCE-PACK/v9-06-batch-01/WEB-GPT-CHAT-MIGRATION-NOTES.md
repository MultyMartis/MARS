# Web-GPT Chat Migration Notes — FP-0002 after V9-06E53

**Purpose:** bootstrap a fresh Web-GPT chat without redoing accepted work.  
**Experience pack:** `DOCS/FORGE-PROGER-EXPERIENCE-PACK/v9-06-batch-01/` (docs only; not brains).

---

## Current project status

| Field | Value |
|-------|-------|
| Factory project | FP-0002 Shpigovsky.ru |
| Last accepted phase | **V9-06E53** Admin UX section styling (operator: «Ну вот теперь гуд.») |
| Prior accepted | E52 generic pages ACF SoT + placeholder |
| Frozen surfaces | Home E42; Services hub E44; Услуга model E47; sections E50; placeholder mode E51; full service rollout E49-after-FIX01; **E53 admin UX** |
| Recommended next | Migrate chat; then charter next page-type / content / polish tasks separately |

---

## Where to continue

Start from:

1. `PROJECT-STATUS.md` (top status block)
2. `WORDPRESS/SOURCE-AUTHORITY.md` (E52/E53/closeout entries)
3. Freeze markers under `REPORTS/FREEZE-FP-0002-V9-06E*.md`
4. This experience pack for process memory

Do **not** restart Home/hub/section/service generic SoT unless an explicit change charter exists.

---

## Runtime / source paths

| Role | Path |
|------|------|
| Git source theme | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/shpigovsky/` |
| Git source plugin | `.../WORDPRESS/plugins/shpigovsky-core/` |
| Git ACF JSON | `.../WORDPRESS/acf-json/` |
| Runtime | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` (`http://shpigovsky.test`) |
| DB | `mars_wp_fp0002` |
| Backups | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\` |

---

## What not to redo

- Home admin parity / freeze (E38–E42)
- Services hub freeze (E43–E44)
- Layout governance Option B (E45) unless charter
- Услуга field model (E47) / full rollout content (E48–E49) unless charter
- Section ACF SoT (E50)
- Placeholder contract (E51) — especially do not reintroduce bare `name` override
- Generic pages ACF SoT (E52) unless new page inventory
- Admin section styling (E53) — accepted frozen

---

## Key accepted models (short)

- Editor roles: Раздел / Услуга / Заглушка (+ nested Услуга/Заглушка)
- Technical service layout for Услуга: `service_general` (legacy alias `alcohol_special`)
- Placeholder = render-only stub
- Generic: `generic_page_lead` / `generic_page_body`; `page_layout_mode` full|placeholder
- Empty optional → hide
- Operator runtime CSS drift `v9-style.css` `11A45ABE…` — **preserve**

---

## Git state (at closeout writing)

- Branch: `mars/canonical-post-recovery`
- Prior pushed FP-0002 persistence: `dba97a38…`, `d3f3fdf2…` (via divergence-resolve remote tip historically `03ff6777…`)
- E52–E53 closeout commit: see closeout report / push evidence
- Dirty main typically contains **foreign WIP** — ignore unless charter includes it

---

## Remaining local / uncommitted tails (typical)

Even after closeout commit, often still untracked/uncommitted outside allowlist:

- `INCOMING/` design binaries
- `_chrome-profile-*` validation caches
- `__pycache__`
- `temp.zip` / large fig
- Other projects’ WIP

Do not stage these.

---

## Next likely page types / tasks

Examples (operator must charter):

- Remaining institutional pages deeper admin parity (o-centre, contacts polish)
- Specialists / blog deeper ACF SoT if not fully covered
- Content replacement from client (non-DEMO)
- Preview/hosting packaging (out of scope until asked)
- Second Forge Proger experience batch → then brain upgrade charter

---

## Warnings

1. **Do not confuse WPilot with OCPilot** — different projects/plugins.
2. **Do not mention MetaBOT as FP-0002 scope** — adjacent monorepo noise only.
3. **Respect MARS monorepo Git model** — exact paths; no force; clean worktree for divergence.
4. **Preserve operator CSS / runtime CSS drift** — never overwrite runtime `v9-style.css` from source casually.
5. Experience pack is **not** authorized brain injection.
