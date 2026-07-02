# REPORT — FP-0002 V9 Phase 03E Rollback / Preloader Removal / Modal Rework

**Verdict:** COMPLETE — pending operator narrow visual review  
**Phase:** V9-03E  
**Branch:** `mars/canonical-post-recovery` @ `5e7c86db73398df6a01074a60af3afa796de41b3`  
**V9 status:** Restored from V9-03C authority; preloader removed; modal scroll rework applied  
**Git checkpoint:** NONE (by operator policy)

## Restore
- Authority ZIP SHA-256: `da06dd7dfcbc485a4810d091ae200a39e92916d9e29ae7ed80e6b8d4ccf95e71` ✓
- Failed V9-03D backup SHA-256: `81431152733F58008149040582A60F782ACEF7B30AA8949ACA50332D568AD164`
- Scoped restore: `src/`, `dist/`, `tools/`, `foundation/`, package files; removed V9-03D-only files
- G6 absence: PASS

## Preloader removal
- Deleted: `preloader.html`, `initPreloader`, session key, head/body-start preloader hooks, preloader SCSS, page-load fade states
- Active source occurrences: **0**

## Modal
- Overlay: `rgba(17, 24, 39, 0.56)` semitransparent, fixed viewport
- Lock: shell-scoped fixed + body overflow (no global body-fixed)
- Focus: `preventScroll: true`
- Rejected V9-03D body-fixed pattern: absent from JS

## Build / validation
- `npm run build`: PASS — 31 routes
- `npm run validate`: PASS
- CSS SHA256: `A5E5091D334A5CC674F6612C0E11BA1866C1243E593C4A42485B6571C2DE3EC9`
- JS SHA256: `0F42116923482B064787FA86F490B73A9C7C02AC927B3A193D0078B610167D92`

## Preview
**http://127.0.0.1:8791/**

### Operator narrow review
1. Private window — no preloader / no white screen / immediate page
2. Modal overlay semitransparent; page visible underneath
3. Home footer `Записаться` — no jump open/close
4. Home middle CTA — no jump
5. O-Centre footer trigger — no jump; G6 absent
6. Mobile ~380px — scroll low, open modal, focus field, close, same position
7. Regression: color-only button hover, gallery fade, section reveal

Evidence root: `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-03e-preloader-removal-modal-rework\`
