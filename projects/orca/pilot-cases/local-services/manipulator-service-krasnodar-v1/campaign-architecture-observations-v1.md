# Campaign Architecture Observations v1

## Boundary

These are research observations only. They do not authorize campaign creation, upload, activation, bidding, automation, or live optimization.

## Recommended Separation

- Separate urgent intent from planned transport.
- Separate city-local queries from krai / intercity / nearby settlement queries.
- Separate `манипулятор` service from broad грузоперевозки.
- Separate B2B construction/equipment jobs from private moving-like queries where possible.
- Keep price-intent groups distinct for ad and landing-message testing.

## Mobile-First Ad Structure

- Prioritize call-ready messages.
- Use short value claims: `манипулятор в Краснодаре`, `расчет по фото`, `подача по городу`, `оплата наличными/безналом`.
- Avoid unsupported guarantees such as exact arrival time unless operationally true.

## Call-First Campaigns

Urgent groups should support phone-first conversion. Human review must confirm call handling hours, dispatcher availability, and whether the business can handle after-hours demand.

## WhatsApp-Oriented Extensions

WhatsApp may be useful for quote requests requiring photos, dimensions, and addresses. It should be positioned as `send cargo details` rather than generic chat if the service workflow supports it.

## High-Trust Messaging

- Real vehicle parameters.
- Local coverage.
- Same-day availability when true.
- Reviews or completed-job proof.
- Cashless payment for companies.
- Careful cargo handling and experienced operator.

## Aggregator-Defense Strategy

- Match marketplace convenience with fast direct quote.
- Make equipment details clearer than directory listings.
- Show proof that the provider is local and reachable.
- Use ad copy that reduces comparison anxiety: price framework, availability, and direct dispatcher.

## Manual Review Questions

- Which services are actually offered: crane-truck only, movers, loaders, equipment evacuation, intercity routes?
- Is 24/7 operationally true?
- What truck capacities and boom lengths are available?
- Which districts and settlements are profitable?
- Which CTAs are actually staffed?

## SAFE UNKNOWN

No campaign structure should be implemented from this file without live keyword data, current SERP validation, landing review, and business constraints.
