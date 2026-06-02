# Browser / Admin Panel Access Pattern

**Scope:** shared pattern for CMS/ecommerce admin and browser-supervised inspection.  
**Applies to:** WPilot, OCPilot, future MODxPilot, CustomSitePilot.

## Purpose

Human-supervised workflow for inspecting or operating through a web admin panel (WordPress admin, OpenCart admin, MODx manager, custom admin UI).

## Pre-access gates

| Gate | Operator confirms |
|------|-------------------|
| Target | Exact admin URL, correct site/account |
| Environment | test / staging / production |
| Backup | File and/or DB backup status for write-class work |
| Scope | read-only inspect vs scoped write |
| Credentials | Operator holds session; not stored in repo |

## Workflow

1. Operator opens admin in browser; AI/Cursor does **not** blind-click production.
2. Operator confirms target URL and environment **before** any navigation beyond public pages.
3. For read-only audit: operator provides screenshots, exported HTML snippets, or sanitized settings summaries — no secrets in exports.
4. For write-class work: explicit human charter; backup confirmed; rollback path documented.
5. End session: operator confirms logout / session close; record outcome in REPORT only.

## Allowed evidence in repo

| Allowed | Forbidden |
|---------|-----------|
| Sanitized screenshots (no cookies, no passwords) | Session tokens, cookies |
| Settings *labels* and version strings | Full admin export with secrets |
| Module/extension *names* | API keys, payment credentials |
| Operator-written facts | Blind automated admin actions |

## OpenCart-specific notes (OCPilot)

- Paths differ from WordPress: `admin/`, Extensions, Modifications, ocMod — not `wp-admin/`.
- Do not assume WP theme/plugin semantics apply.

## WordPress-specific notes (WPilot)

- Paths: `wp-admin/`, plugins, themes — not OpenCart `catalog/`.
- Do not assume OpenCart extension semantics apply.

## Stop conditions

- Wrong site or environment detected → halt; SAFE UNKNOWN until operator re-confirms.
- Secret visible in screenshot → redact before commit; halt if already committed.
- Destructive action requested without backup → refuse until backup confirmed.

## REPORT requirement

Every browser/admin access session must produce: `# REPORT — <pilot> <operation> — <site>` with scope, findings, SAFE UNKNOWN, and security closeout.
