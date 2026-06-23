# Product/Service Disambiguation Policy v1

**Policy ID:** `product-service-disambiguation-policy-v1`

## Mandatory rule

```text
PRODUCT OBJECT + PURCHASE/SUPPLY MODIFIER
does not imply provider-hire intent
```

## PRODUCT-ONLY — REJECT

User seeks: buy product, boxed delivery, license, edition, version, product price, download, official distributive, self-install, product update as goods, license supply without explicit service scope.

## SERVICE — ACCEPT

User seeks provider for: implementation, configuration, integration, customization, support, migration, recovery, commercial training, specialist installation, delivery with explicit service scope.

## AMBIGUOUS — ABSTAIN

Phrase allows both product purchase and service hire without decisive next-action signal.

## Constraints

- «Поставка» is not automatically service — analyze object and bundled service scope.
- Product name alone does not force REJECT.
- Phrase-specific exceptions forbidden.

Machine-readable: `product-service-disambiguation-policy-v1.json`
