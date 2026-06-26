# FP-0002 Services V2 Gallery Equal Height Map v1

**Target:** `.services-category-section-v2__gallery-item` (Category 1 addictions, Category 2 mental health)

## Previous behavior

- `min-height` / `max-height` on images caused unequal row heights from source aspect ratios

## New approach

```scss
.page-uslugi-v2 .services-category-section-v2__gallery-image {
  aspect-ratio: 4 / 3;
  width: 100%;
  object-fit: cover;
}
```

- Caption (`.services-category-section-v2__caption`) remains below image; not included in image box
- No `__gallery-media` wrapper added (gallery HTML embedded in page JSON strings)

## Probe @ 1398 — addictions gallery

- Heights: `[285, 285, 285]`
- `galleryHeightsEqual`: true

## Verdict

`NORMALIZED`
