# Informational Leakage Rules v1

## Purpose

Detect search terms that look informational rather than commercially useful.

## Leakage Signals

- how to;
- what is;
- instructions;
- guide;
- DIY;
- photos;
- examples;
- specifications;
- reviews without provider intent;
- free;
- job or training intent.

## Local-Service Leakage

Watch for terms that pull traffic away from service requests:

- equipment specs instead of equipment service;
- repair instructions instead of repair order;
- moving tips instead of moving service;
- pricing research without local provider intent;
- legal or document research when the service cannot answer it.

## Handling

- exclude clear non-commercial terms;
- monitor ambiguous terms;
- split terms that indicate a separate useful intent;
- mark weak evidence as `SAFE_UNKNOWN`;
- avoid blocking useful local phrases too early.

## Boundary

ORCA does not automatically add exclusions. Human review must confirm leakage and overblocking risk.
