# Triumph phone mask reference

- Authority path: X:\AI MARS\workspaces\triumph-manipulator-landing-v6\src\js\form.js
- Function: bindPhoneMask (custom vanilla; no Inputmask; no jQuery)
- Format: +7 (XXX) XXX-XX-XX
- Selectors: input[type=tel], input[name=phone], [data-phone-mask]
- Paste: via input event digit normalize (8→7, prepend 7, max 11)
- Submit: formatted display string
- Validation: digits.length >= 10
- Modal: one-time bind; no teardown required
