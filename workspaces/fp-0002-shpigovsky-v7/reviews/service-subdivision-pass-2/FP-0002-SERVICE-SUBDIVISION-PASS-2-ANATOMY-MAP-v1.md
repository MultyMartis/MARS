# FP-0002 Service Subdivision Pass 2 — Anatomy Map v1

| Order | Block | Desktop node | Mobile node | Existing pattern | Decision |
|------:|-------|--------------|-------------|------------------|----------|
| 1–6 | Pass 1 blocks | — | — | Pass 1 partials | unchanged |
| 7 | Природа зависимости | `1:3657` / `1:3672` in `1:3654` | `1:7195`–`1:7220` in `1:7181` | editorial + red lead | `REUSE_WITH_SCOPED_VARIANT` → `service-subdivision-nature-v1` |
| 8 | Info cards ×2 | `1:3675`–`1:3687` | `1:7199`–`1:7213` | `home-recovery-intro__card` | `REUSE_WITH_SCOPED_VARIANT` |
| 9 | First CTA | `1:3688` | `1:7221` | `services-program-cta-band-v2` | `REUSE_WITH_CONTENT` → `service-subdivision-first-cta-v1` |
| 10 | Program 4 directions | `1:3701` | `1:7233` | `services-program-v2` | `REUSE_WITH_CONTENT` |

**Verdict:** `PASS_2_ANATOMY_IMPLEMENTED`
