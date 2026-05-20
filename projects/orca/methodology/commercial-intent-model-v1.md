# Commercial Intent Model v1

## Purpose

Defines how ORCA evaluates commercial strength in PPC queries and SERPs.

## Strong Commercial Signals

- buy, order, book, call, calculate, request, quote.
- price, cost, tariff, estimate.
- urgent, emergency, today, 24/7.
- near me, city, district, metro, with visit.
- service + commercial modifier.
- visible ad density and local pack activity.

## Weak Or Cold Signals

- how to, what is, examples, guide, DIY.
- reviews only without provider selection.
- generic category research.
- job, training, template, forum, free.
- marketplace browsing when direct lead generation is not relevant.

## Interpretation Rules

- Use SERP evidence to validate wording.
- Treat commercial modifiers as intent clues, not final proof.
- Separate comparison intent when users need trust or price evaluation.
- Mark mixed intent when ads and informational results coexist strongly.
- Human review decides whether cold research terms belong in paid campaigns.

## Output Labels

- `commercial_ready`.
- `commercial_with_review`.
- `research_only`.
- `mixed_requires_split`.
- `exclude_or_negative_candidate`.

## Boundary

Commercial intent scoring is a planning aid. It does not make automatic budget, bid, keyword activation, or optimization decisions.
