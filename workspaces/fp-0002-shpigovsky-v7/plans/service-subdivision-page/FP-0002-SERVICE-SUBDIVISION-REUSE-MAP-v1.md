# FP-0002 Service Subdivision — Reuse Map v1

| Order | Design block | Existing partial/pattern | Decision | Required change |
|------:|--------------|--------------------------|----------|-----------------|
| 1 | Header | `partials/layout/header.html` | REUSE_EXACT | active nav params |
| 2 | Service Hero | `services-inner-hero-v2` | REUSE_WITH_CONTENT | page title, lead, hero image |
| 3 | Breadcrumbs / subnav | `breadcrumbs`, `services-page-subnav` | REUSE_WITH_CONTENT | crumb trail |
| 4 | Page intro | `services-category-section-v2` heading/lead pattern | REUSE_WITH_SCOPED_VARIANT | no category services grid |
| 5 | Service list + nature | `services-category-section-v2` service rows | REUSE_WITH_SCOPED_VARIANT | subdivision copy |
| 6 | Info cards (2-col) | `home-feature-grid` / card patterns in `style.scss` | REUSE_WITH_SCOPED_VARIANT | verify geometry vs mockup |
| 7 | Rehab stages numbered | `home-rehabilitation-requirements__steps` | REUSE_WITH_SCOPED_VARIANT | different copy/count |
| 8 | CTA band 1 | `services-program-cta-band-v2` | REUSE_WITH_CONTENT | source id |
| 9 | Program 4 directions | `services-program-v2` / `home-rehabilitation-program` | REUSE_WITH_CONTENT | reuse program assets |
| 10 | Center / team + stats | `home-staff-photo`, `home-recovery-life` intro | REUSE_WITH_SCOPED_VARIANT | stats cards TBD deep-read |
| 11 | Interior image | `home-rehabilitation-requirements__photo` pattern | REUSE_WITH_CONTENT | asset path |
| 12 | Exterior / building | `home-clinic-landscape` | REUSE_WITH_CONTENT | asset path |
| 13 | Specialists | `home-specialists` | REUSE_WITH_CONTENT | swiper init |
| 14 | Founder quote | `home-founder-quote` | REUSE_WITH_CONTENT | variant-b |
| 15 | Comfort | `home-comfort` | REUSE_WITH_CONTENT | gallery captions |
| 16 | Reviews | `home-reviews` | REUSE_WITH_CONTENT | program-specific reviews |
| 17 | FAQ | `home-faq` | REUSE_WITH_CONTENT | page FAQ copy |
| 18 | Final form | `home-final-form` | REUSE_WITH_CONTENT | lead source |
| 19 | Footer | `partials/layout/footer.html` | REUSE_EXACT | — |
| 20 | Modal | `modal-consultation` | REUSE_EXACT | source ids |

## Summary

- **Exact Home reuse:** founder, comfort, faq, final-form, specialists, reviews patterns
- **Exact Services reuse:** inner-hero-v2, subnav, program-v2, cta-band-v2, category heading/lead
- **Scoped variants:** intro block, service rows, info cards, rehab stages, center/team composite
- **New components:** only if deep Figma read proves no partial match (stats card row — pending Pass 1 frame read)
- **Unsupported assumptions:** desktop/mobile share identical section order — **rejected**
