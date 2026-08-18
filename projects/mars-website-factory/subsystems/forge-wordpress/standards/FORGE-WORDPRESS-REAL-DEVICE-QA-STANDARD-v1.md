# Forge WordPress — Real-Device QA Standard v1

**ID:** FW-S-17  
**Status:** ACTIVE — CANONICAL ACCEPTANCE GATE for device-specific behavior  
**Date:** 2026-08-18  
**Class:** H  
**Evidence:** FP-0002 lifebuoy P12 false PASS → P13 FIX02 physical iPhone

---

## 1. Rules

1. **Chromium mobile emulation is not iOS Safari proof.**
2. Treat **WebKit** scroll/compositor as a separate engine (Safari iOS, often Safari macOS).
3. Avoid fragile stacks of `transform` + `position: fixed` + `contain` + viewport units + **parent transforms**. Prefer **one transform owner**.
4. If cross-browser abstraction fails twice, a **bounded** browser-specific fallback is acceptable (FP-0002 iOS `top`/`left` + `visualViewport` vs transform on other engines).
5. Physical-device evidence **overrules** emulation. Do not close a device bug on emulator PASS.
6. MacBook **trackpad** is a first-class input for horizontal sliders — not “nice to have”.

---

## 2. Required device matrix (when the feature is device-sensitive)

| Device / engine | When mandatory |
|-----------------|----------------|
| Physical iPhone Safari | Fixed/parallax/transform/scroll-linked UI; touch sliders; viewport units |
| Android Chrome (physical) | Touch sliders; mobile chrome |
| Windows Chromium | Baseline + mouse drag |
| Windows Firefox | At least smoke if CSS is non-trivial |
| MacBook trackpad | Horizontal Swiper/mousewheel |

If the page is static text-only, physical iOS may be a **sample** smoke, not a motion lab. If you animate a fixed layer, iPhone is **blocking**.

---

## 3. Lifebuoy / parallax history (reusable, anonymized)

| Attempt | Result |
|---------|--------|
| Windows/Android implementation | PASS |
| “WebKit-safe” transform | Insufficient on Apple |
| Compositor/contain/fixed repair | Emulation PASS; **physical iPhone FAIL** |
| Bounded iOS fallback | Required |

Do not copy the decorative asset. Copy the **QA and compositor rules**.

---

## 4. Sign-off

Reports must state: **physical device** model + OS + browser, or **NOT PERFORMED** (then the related feature is not production-proven).

---

*FW-S-17 v1.*
