# WPilot Phase 1 QA Checklist

**Status:** documented checklist.

Use this checklist before closing any WPilot Phase 1 Beget test.

## Scope And Environment

- [ ] Target confirmed as test site, not production.
- [ ] Human authorization confirmed.
- [ ] WPilot classified as Program / Operational System, not agent/runtime/deploy bot.
- [ ] External systems named without MARS ownership claims.

## Access Safety

- [ ] No secrets written to repo.
- [ ] No credentials, tokens, cookies, SSH keys, API keys, or passwords recorded.
- [ ] No `wp-config.php` copied.
- [ ] No database dumps copied.
- [ ] Access class recorded without secret values.

## Backup And Rollback

- [ ] File backup confirmed.
- [ ] Database backup confirmed.
- [ ] Rollback plan completed before change.
- [ ] Stop conditions defined.
- [ ] Restore owner or escalation owner known.

## Read-Only Inspection

- [ ] Public site inspection recorded.
- [ ] WordPress/theme/builder signals recorded with evidence or SAFE UNKNOWN.
- [ ] WPBakery/The7 ownership assumptions avoided.
- [ ] Database treated as read-only.

## Safe Test Actions

- [ ] File-level test avoided core, parent theme, plugin files, and `wp-config.php`.
- [ ] CSS patch limited to child theme or approved custom CSS location.
- [ ] WP admin page copy/create test used test page only.
- [ ] No plugin/theme/core updates performed.
- [ ] No destructive SQL performed.
- [ ] No production page changed.

## QA Evidence

- [ ] Before/after observations recorded.
- [ ] Visual/site availability check completed.
- [ ] Rollback verified or rollback readiness documented.
- [ ] SAFE UNKNOWN section filled.
- [ ] SECURITY RISK section filled.
- [ ] Final report contains touched files/pages and human approvals.

## Closeout

- [ ] Temporary access revocation or session closeout considered by operator.
- [ ] No autonomous editing claim made.
- [ ] No deployment claim made.
