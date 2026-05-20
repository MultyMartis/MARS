# Campaign Architecture Methodology v1

## Purpose

Defines how ORCA converts clean PPC intelligence into draft search campaign architecture for human review.

## Architecture Inputs

- Project input.
- SERP snapshots.
- Competitor and offer intelligence.
- Semantic clusters.
- Landing analysis.
- QA findings.

## Structure Rules

- Separate campaigns when geography, offer, audience, budget logic, or operational ownership differs.
- Separate ad groups when intent, landing page, or ad message differs.
- Keep urgent, local, competitor, branded, and informational intents distinct unless human strategy says otherwise.
- Avoid hiding weak semantics inside large generic ad groups.
- Use naming that can survive Direct Commander review.

## Yandex.Direct Focus

- Prepare for tabular review and manual import.
- Keep campaign and ad group names explicit.
- Preserve negative keyword logic.
- Treat bids and budgets as human-only fields.
- Check local service and aggregator pressure before launch structure approval.

## Output

- Draft campaign list.
- Ad group map.
- Landing map.
- Negative placement notes.
- Human decision list.
- SAFE UNKNOWN list.

## Boundary

The methodology produces reviewable architecture, not live campaigns. It does not publish, activate, optimize, bid, or orchestrate advertising systems.
