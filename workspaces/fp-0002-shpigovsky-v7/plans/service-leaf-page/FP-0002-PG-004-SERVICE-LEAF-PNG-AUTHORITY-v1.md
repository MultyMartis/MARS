# FP-0002-PG-004 — PNG Authority v1

| Authority | Path | Dimensions | SHA-256 | Verdict |
| --------- | ---- | ---------: | ------- | ------- |
| Desktop | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026/Услуга - десктоп.png` | 1437×13313 | `A7AB847F2BBF9CA9FF63F11C44EF9FD1472072F04A6274B9550FE6D6C3790D7E` | VALID |
| Mobile | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026/Услуга - мобильная.png` | 380×18136 | `6B252C5F43F3E61A090787D8031880F635BD4F58291268A5484870A826BBFC84` | VALID |

## Identity checks

- **Desktop page identity:** SERVICE_LEAF — hero «Центр лечения алкогольной зависимости», breadcrumbs trail ending «Лечение алкогольной зависимости», leaf-specific upper copy «Алкогольная зависимость — это не персональный выбор», «Признаки алкогольной зависимости», alcohol-themed FAQ (6 questions). Not Service Subdivision hub listing.
- **Mobile page identity:** Same service leaf; stacked mobile layout; anchor pills; leaf editorial blocks; shared lower blocks (program, specialists, comfort, FAQ, form).
- **Runtime screenshot mistakenly used:** NO — dimensions and full-page design chrome match approved design PNG pair; not a `dist/` runtime capture.
- **Confusion guard:** `Услуга подраздел - десктоп/мобильная` rejected (different page; larger subdivision listing anatomy).

## Result

**DESKTOP_AND_MOBILE_REGISTERED**
