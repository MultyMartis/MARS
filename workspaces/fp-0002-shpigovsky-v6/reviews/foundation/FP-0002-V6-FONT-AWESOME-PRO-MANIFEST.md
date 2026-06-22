# FP-0002 V6 — Font Awesome Pro 5.15.4 Build Manifest

**Source:** `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`  
**Integration:** `src/scss/vendors/_fontawesome.scss` (`meta.load-css('fa-all')`)  
**Build bridge:** `src/scss/vendors/fa-all.css` (generated, gitignored)  
**Compiled bundle:** `dist/assets/css/style.css`  
**Webfonts destination:** `dist/assets/webfonts/`

| Style | Prefix | Font file (primary) | Build destination | Status |
| ----- | ------ | ------------------- | ----------------- | ------ |
| Solid | `fas` | `fa-solid-900.woff2` (+ subset `pro-fa-solid-900-*.woff2`) | `dist/assets/webfonts/` | CONNECTED |
| Regular | `far` | `fa-regular-400.woff2` (+ subset `pro-fa-regular-400-*.woff2`) | `dist/assets/webfonts/` | CONNECTED |
| Light | `fal` | `pro-fa-light-300-5.15.4.woff2` (+ subsets) | `dist/assets/webfonts/` | CONNECTED |
| Duotone | `fad` | `pro-fa-duotone-900-5.15.4.woff2` (+ subsets) | `dist/assets/webfonts/` | CONNECTED |
| Brands | `fab` | `fa-brands-400.woff2` (+ subset `pro-fa-brands-400-*.woff2`) | `dist/assets/webfonts/` | CONNECTED |

**CSS verification:** compiled `style.css` contains selectors `.fas`, `.far`, `.fal`, `.fad`, `.fab` and `all.min.css` font-family declarations.  
**Path resolution:** CSS `url(../webfonts/...)` resolves from `dist/assets/css/style.css`.  
**Vendor policy:** licensed package not committed to workspace; copied to `dist/` at build time only.
