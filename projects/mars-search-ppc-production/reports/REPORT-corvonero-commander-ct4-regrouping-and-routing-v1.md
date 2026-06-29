# REPORT — Corvonero Commander CT-4 Regrouping and Routing v1

Generated: 2026-06-29T18:42:23.597Z

## Source authority SHA-256 (pre-modification)

- **phrase_allocation**: `727c996b17f1905d51c9a89977d2b4780dfd9d19139a7cd5d1b0345a5850b948` — `X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-AD-WAVE-1-FINAL-PHRASE-ALLOCATION-v1.json`
- **group_register**: `bd20bfa3e0e97265e1008839512fc7b62b6200b524c2a9dbe849c7c30a040acc` — `X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.json`
- **primary_ads**: `dc7558dda060b096725f2bc0ca70f0a33a671bddc87c3974dcf53b27010a2758` — `X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-AD-WAVE-1-P1-FINAL-PRIMARY-ADS-v1.json`
- **campaign_negatives**: `a44be409268ed7d6aba6ba2d85cd1de8a39d4f42d5f17fd2159689d5913b1ae9` — `X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXT-W1-NEGATIVE-DEPLOYMENT-v1.json`
- **callouts**: `c3a957f7db7de183625e2e991f1f0156b68762c73f9df3343dc8977aced8846a` — `X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXT-W1-CALLOUTS-v2.json`
- **utm_map**: `ab005d99af9c40bd9fd3e6d411eef41a9441c46d8c424924167aec924ef78d2e` — `X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXT-W1-UTM-POLICY-v2.json`
- **campaign_settings**: `44cdb0a29a060994495fc08d1d9a07cf655699b401e6d4b750decd78a87f1c9f` — `X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXT-W1-CAMPAIGN-SETTINGS-v2.json`
- **cross_campaign**: `9cf899a57d79052ff07c9c70e3b4dfc399ff64a13395d49e29c5ce24b34e77c2` — `X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXT-W1-CROSS-NEGATIVES-v2.json`
- **bids**: `cc0063bab8110fce8cb483a9da54405fae5fe69a67ce616aeff68db463a333ba` — `X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-COMMANDER-INITIAL-BIDS-v1.json`
- **display_paths**: `5f74caea0123d0f7ff5f6c0361edd5ba8c18f318764bc0876356f1f368a8c697` — `X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXT-W1-DISPLAY-PATHS-v1.json`

## Verdict

```
CORVONERO COMMANDER CT-4:
PARTIAL — REGROUPING COMPLETE, OPERATOR AD APPROVAL REQUIRED
```

## Counts

| Metric | Value |
|--------|-------|
| Original total phrases | 895 |
| Reviewed oversized-group phrases | 585 |
| Kept | 454 |
| Moved within campaign | 379 |
| Moved to other campaign | 6 |
| Rejected | 56 |
| Abstain | 0 |
| Final deployable phrases | 839 |
| Original groups | 15 |
| Final groups | 21 |
| Groups over 200 | 0 |
| Unapproved derived ads | 7 |

## Migration map

{
  "ca-01-specialist-search": [
    "ca-01-specialist-search",
    "ca-01-specialist-extended",
    "ca-01-find-hire-specialist",
    "ca-01-remote-freelance-specialist",
    "ca-01-specialist-by-product"
  ],
  "ca-05-direct-service-order": [
    "ca-05-marking-setup",
    "ca-05-chestny-znak-service",
    "ca-05-marking-codes"
  ]
}

## CT-4 authority files

Manifest: `X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CT4-AUTHORITY-MANIFEST-v1.json`

## Transport validation (validate-only)

Command:

```text
cd projects/mars-search-ppc-production/tools/commander-transport
node src/cli.mjs validate --manifest "<CT-4 manifest path>"
```

| Gate | Result |
|------|--------|
| groups_over_200 | PASS (max 144) |
| Region | PASS — Новосибирская область |
| Organization | PASS — BLANK |
| Campaign negatives | PASS |
| Group negatives | PASS |
| Ads per group | BLOCKED_BY_OPERATOR_REVIEW — 7 derived ads |

**Transport validation:** BLOCKED ONLY BY UNAPPROVED DERIVED ADS

**CT-5 generation:** NOT YET AUTHORIZED

## CA-01 regrouping summary

| group_id | phrases | ad status |
|----------|---------|-----------|
| ca-01-specialist-search | 144 | UNCHANGED_OPERATOR_APPROVED |
| ca-01-specialist-extended | 133 | DERIVED_REQUIRES_OPERATOR_REVIEW |
| ca-01-find-hire-specialist | 16 | DERIVED_REQUIRES_OPERATOR_REVIEW |
| ca-01-remote-freelance-specialist | 13 | DERIVED_REQUIRES_OPERATOR_REVIEW |
| ca-01-specialist-by-product | 11 | DERIVED_REQUIRES_OPERATOR_REVIEW |
| ca-01-price-intent | 23 | UNCHANGED_OPERATOR_APPROVED |
| ca-01-direct-service-order | 4 | UNCHANGED_OPERATOR_APPROVED |

## CA-05 regrouping summary

| group_id | phrases | ad status |
|----------|---------|-----------|
| ca-05-marking-setup | 90 | DERIVED_REQUIRES_OPERATOR_REVIEW |
| ca-05-chestny-znak-service | 104 | DERIVED_REQUIRES_OPERATOR_REVIEW |
| ca-05-marking-codes | 5 | DERIVED_REQUIRES_OPERATOR_REVIEW |
| ca-05-integration | 14 | UNCHANGED_OPERATOR_APPROVED |
| ca-05-ts-piot | 4 | UNCHANGED_OPERATOR_APPROVED |
| ca-05-support-and-maintenance | 2 | UNCHANGED_OPERATOR_APPROVED |

`ca-05-direct-service-order` retired — phrases migrated to marking-setup / chestny-znak-service / marking-codes.
