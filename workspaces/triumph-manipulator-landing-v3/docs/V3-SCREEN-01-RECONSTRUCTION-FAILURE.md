# Triumph Manipulator Landing V3 — Screen 01 Reconstruction Failure

## Status

The current Screen 01 pass is a reconstruction failure.

It repeated the first failed visual approach by using a CSS/semantic approximation for the central hero media instead of reconstructing from the actual V1 visual source.

## Failure Summary

- The right-side hero media in `projects/triumph-manipulator-landing/design/v1/01.png` is a key source visual, not decorative filler.
- The current V3 pass approximated that area with CSS gradients, constructed vehicle shapes, generic callouts, and semantic media scaffolding.
- This creates fake fidelity: the implementation visually suggests a source-faithful hero while the required truck/background asset is not actually present.
- That is not acceptable for V3 reconstruction.

## Asset Authority Result

`projects/triumph-manipulator-landing/design/shared-assets/` contains approved logo and social assets for Screen 01:

- `brand/logo--white.svg`
- `social/WhatsApp-ico.svg`
- `social/Telegram-ico.svg`

It does not contain the required standalone hero truck, construction background, or complete hero media source shown in V1 Screen 01.

## Required Rule

If a key visual asset is required by the V1 source screen and no approved standalone asset exists, V3 must not replace it with a CSS mockup or semantic placeholder.

Allowed outcomes are:

- Use an extracted temporary raster crop from the source PNG.
- Mark the section `BLOCKED BY ASSET`.
- Ask for HITL asset approval.

For the current Screen 01 recovery, use temporary source crops from `projects/triumph-manipulator-landing/design/v1/01.png`.

## Forbidden

- Fake fidelity.
- CSS-drawn trucks, backgrounds, icons, or callouts presented as reconstruction-equivalent media.
- Semantic placeholder media when the missing source visual is central to the section.
- Final production-readiness claims based on temporary reconstruction crops.

Temporary crops are reconstruction aids only. Final production asset replacement remains a separate future decision.
