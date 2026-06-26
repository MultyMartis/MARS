# FP-0002 Static Demo — Next Passes v1

## PASS 2 — Generator + page instances

| Field | Value |
| ----- | ----- |
| Input | This page registry draft, four canonical templates |
| Scope | Generator, all page instances, placeholders, nested dist output |
| Backup | ZIP from baseline tag before generator commit |
| Commit boundary | `feat(fp-0002): static demo generator and page instances` |
| Acceptance | Build exit 0; ~56 pages; templates unmodified; unique title/H1/URL |
| Result | Browsable static demo (links may still be partial) |

## PASS 3 — Navigation wiring

| Field | Value |
| ----- | ----- |
| Input | PASS 2 output + navigation registry |
| Scope | Header, footer, hub cards, subdivision cards, breadcrumbs hrefs |
| Backup | Pre-PASS-3 source ZIP |
| Commit boundary | `feat(fp-0002): wire static demo navigation graph` |
| Acceptance | Zero internal 404; unresolved only external/social |
| Result | Full internal link graph |

## PASS 4 — QA + deploy package

| Field | Value |
| ----- | ----- |
| Input | PASS 3 build |
| Scope | Link crawl, template spot-check, client deploy package |
| Backup | Pre-deploy tag |
| Commit boundary | `chore(fp-0002): static demo QA and deploy pack` |
| Acceptance | Operator sign-off checklist |
| Result | Deployable static package |
