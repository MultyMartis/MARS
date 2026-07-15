# Placeholder Mode Guidelines — from FP-0002

**Status:** experience documentation only

---

## Contract

1. **Placeholder is render-only** — switching to Заглушка must **not** delete ACF content.
2. **Final page state decisions must be explicit** — after testing, set pages back to intended role/layout (e.g. `#78` ended as Услуга).
3. **Services vs generic pages**
   - Services: editor role includes Заглушка; maps to `placeholder` stack.
   - Generic Content pages: optional `page_layout_mode` full|placeholder; default full; not mass-enabled.
4. **Do not globalize to dedicated templates** (specialists, blog singles, etc.) without a separate task.
5. **Real admin switch validation required** — Update in wp-admin with proper `acf[field_…]` names.
6. **Role/layout metadata sync** — editor choice must persist both human role and technical variant/stack consistently.

---

## Frontend stub expectations

Typical stub:

- Site header / navigation
- Page H1
- Footer
- No full service/section marketing stacks

Implementation example: `placeholder-stack.php` (project-specific).

---

## Validation minimum

| Check | Required |
|-------|----------|
| Switch to placeholder via real admin | FE becomes stub |
| Switch back to Услуга/full | FE restores; content fingerprint preserved |
| Unrelated frozen pages | Untouched |
| Operator confirm | Quoted in freeze marker |

---

## E51 lesson (mandatory memory)

If `prepare_field` rewrites ACF input `name` away from `acf[field_…]`, WordPress Update will not persist through ACF — simulations may still lie. Fix the prepare hook; prove with real form POST.
