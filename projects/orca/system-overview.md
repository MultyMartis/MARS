# ORCA System Overview

## Purpose

ORCA provides a practical operating model for AI-assisted PPC research and campaign architecture. It helps a human operator move from business input to reviewable campaign materials without claiming autonomous campaign management.

## Operational Target

The target is a repeatable preparation workflow for search campaigns in systems such as Yandex.Direct and Google Ads:

- understand the business and offer;
- research search demand and SERP context;
- collect and cluster semantics;
- design campaign, ad group, and keyword structures;
- draft ads and extensions;
- prepare export-ready tables;
- verify outputs before any platform upload.

## Main Layers

1. Intake layer - captures business goals, geography, offer, constraints, and platform intent.
2. Research layer - collects SERP observations, competitor patterns, query intent, and risk notes.
3. Semantic layer - collects keywords, negatives, clusters, and intent labels.
4. Architecture layer - converts clusters into campaigns, ad groups, naming, and targeting logic.
5. Creative layer - drafts ad text for human review.
6. Export layer - prepares structured files for manual import workflows.
7. QA layer - checks completeness, policy risk, duplicates, naming, and review readiness.

## Input / Output Model

Inputs are structured project briefs, research notes, keyword sources, known exclusions, platform constraints, and human decisions.

Outputs are reviewable documents and tables: SERP notes, semantic clusters, campaign structures, ad drafts, export packages, QA reports, and SAFE UNKNOWN lists.

ORCA outputs are recommendations and draft artifacts. They are not live campaign changes.

## Human Supervision Model

The human remains the strategic authority for:

- market positioning;
- budget and bidding decisions;
- account structure approval;
- keyword and negative keyword acceptance;
- compliance and policy judgment;
- final platform upload and activation.

Every ORCA output requires human review before use in Yandex.Direct, Google Ads, or any advertising account.

## Risks And Boundaries

ORCA must not claim or imply automatic optimization, autonomous bidding, live account management, or production runtime behavior.

Main risks:

- weak source data causing poor keyword or cluster quality;
- unreviewed ad copy causing policy or brand risk;
- export format mismatch with platform tools;
- overconfident assumptions about competitor strategy;
- hidden duplication across campaigns or ad groups.

When evidence is missing, ORCA records SAFE UNKNOWN instead of inventing facts.
