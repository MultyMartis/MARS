# Search Term Clustering Rules v1

## Purpose

Support lightweight grouping of reviewed search terms for human PPC decisions.

This is not full semantic clustering automation.

## Useful Clusters

- keep as commercial demand;
- negative keyword candidates;
- informational leakage;
- geo mismatch;
- urgent-intent terms;
- competitor terms;
- equipment ambiguity;
- low-confidence terms;
- terms needing landing review.

## Clustering Rules

- group by user intent before wording similarity;
- keep urgent intent separate when CTA differs;
- keep wrong-geo terms visible;
- separate informational leakage from weak commercial terms;
- do not overbuild clusters for tiny volumes;
- keep uncertain terms in `SAFE_UNKNOWN`.

## Review Output

For each cluster, record:

- cluster name;
- reason;
- sample terms;
- proposed action;
- overblocking risk;
- reviewer.

## Boundary

ORCA does not perform autonomous clustering or apply account changes. Human review is mandatory.
