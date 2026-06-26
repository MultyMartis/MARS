# FP-0002 Services V2 Program DOM Reconciliation v1

## Old DOM order

```html
<article class="services-program-v2__item">
  <div class="services-program-v2__item-media">...</div>
  <div class="services-program-v2__item-body">
    <p class="services-program-v2__item-text">...</p>
  </div>
</article>
```

## New DOM order

```html
<article class="services-program-v2__item">
  <div class="services-program-v2__item-body">
    <h3 class="services-program-v2__item-title">...</h3>
    <p class="services-program-v2__item-desc">...</p>
  </div>
  <div class="services-program-v2__item-media">
    <img class="services-program-v2__item-image" ...>
  </div>
</article>
```

## Card style (Home direction pattern)

- Item padding: `var(--pad-gap)`
- Media inset: `padding: 0 var(--pad-gap-line) var(--pad-gap-line)`
- Image: `border-radius: var(--radius-main)`, `height: 220px`, `object-fit: cover`

## Probe

- `programDomOrderOk`: true (all 4 items)

## Verdict

`BODY_BEFORE_MEDIA` + `HOME_DIRECTION_STYLE_REUSED`
