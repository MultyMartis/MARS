# V2 — Asset rules (implementation pack v0)

**Purpose:** How **`design/shared-assets/`** may be used relative to **`design/v2/`**. **Critical:** shared assets **≠** semantics.

## Source discipline

| Path | Role |
|------|------|
| `design/v2/*.png` | What appears on **this** landing in **this** order — composition + crops + context. |
| `design/shared-assets/` | **Reusable** SVG/PNG (logos, social icons, hero bg, review logos, etc.). |
| `design/v1/` | **Archive** — not an automatic media source for V2. |

---

## Allowed uses of `shared-assets/`

- **Brand:** logos, favicon — paths under `shared-assets/brand/` or equivalent.
- **Social / review badges:** icons as in repo when mock expects same networks.
- **Hero / background art:** when same raster is **intentionally** shared across versions **and** V2 mock shows it.

**Rule:** If V2 mock shows a **different** crop, subject, or background — follow **`design/v2/`**, not “nearest file in shared-assets.”

---

## Forbidden inferences

- **Do not** infer **section titles**, **order**, or **value props** from asset filenames.
- **Do not** pull **V1-only** imagery from **`design/v1/`** for V2 without operator approval.

---

## Technical hygiene

- Prefer **SVG** for logos/icons; raster: respect intrinsic dimensions; no squashing (`object-fit` as mock implies).
- **Alt text:** FLEXIBLE per `content-authority.md` — accurate, non-deceptive.

---

## Fonts / icon packs

- Font files and licensed libraries (e.g. Font Awesome Pro in repo) follow **project icon policy** — not covered by `shared-assets/` naming alone.
- For Font Awesome selection discipline, use [`../../../notes/icon-source-policy.md`](../../../notes/icon-source-policy.md) plus the reusable Website Factory layer [`../../../../mars-website-factory/font-awesome-governance-layer.md`](../../../../mars-website-factory/font-awesome-governance-layer.md): semantic fidelity first, section-local family consistency, optical rhythm, documented exceptions.
