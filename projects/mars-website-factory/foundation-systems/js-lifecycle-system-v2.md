# JS lifecycle foundation system v2

**Status:** documented vanilla + jQuery-compatible discipline. **Not** React/Vue, **not** MARS runtime.

**Goal:** section replacement and hot-swap without duplicate listeners, ghost state, or memory leaks.

---

## 1. Core API

```text
initCore()     — once per page load (modals registry, global resize debounce)
initPage()     — scan [data-section] or main landmark
initSection(el) — bind modules inside section root
destroySection(el) — unbind all modules in section
reinitSection(el) — destroySection → initSection
```

**Page load:**

```javascript
document.addEventListener('DOMContentLoaded', () => {
  initCore();
  initPage();
});
```

---

## 2. Module convention (`data-module`)

| Attribute | Meaning |
|-----------|---------|
| `data-module="modal"` | Modal controller |
| `data-module="form"` | Form AJAX + validation |
| `data-module="accordion"` | Disclosure |
| `data-module="tabs"` | Tab panels |
| `data-module="slider"` | Carousel / scroll snap |
| `data-module="sticky-cta"` | Show/hide sticky bar |

**Registry pattern:**

```javascript
const MODULES = {
  form: { init: initForm, destroy: destroyForm },
  modal: { init: initModal, destroy: destroyModal },
  // ...
};

function initSection(root) {
  if (root.__wfSectionInit) return;
  root.__wfSectionInit = true;
  root.querySelectorAll('[data-module]').forEach((el) => {
    const name = el.dataset.module;
    const mod = MODULES[name];
    if (mod) mod.init(el);
  });
}

function destroySection(root) {
  root.querySelectorAll('[data-module]').forEach((el) => {
    const name = el.dataset.module;
    const mod = MODULES[name];
    if (mod) mod.destroy(el);
  });
  delete root.__wfSectionInit;
}
```

---

## 3. Idempotency

- Every `init*` checks `__wf*Bound` flag or WeakMap before attaching listeners.
- `initSection` on same node twice is a no-op.
- Global `initCore` guarded by `window.__wfCoreInit` or module closure flag.

---

## 4. Event namespace discipline

Use namespaced events for jQuery projects:

```javascript
// vanilla
el.addEventListener('click', onClick);
// jQuery equivalent: $(el).off('.wf').on('click.wf', onClick);

function destroyForm(root) {
  $(root).off('.wf');
  delete root.__wfFormBound;
}
```

**Delegated listeners:** attach to `root`, filter by selector; remove one listener on destroy.

---

## 5. Resize handling

- Single debounced `resize` on `window` (150ms) registered in `initCore`.
- Modules subscribe via callback registry — do not each bind raw `resize`.
- `destroyCore` only on full page unload (SPA not in scope).

---

## 6. Observer cleanup

If `IntersectionObserver` / `MutationObserver` used:

- Create in `init*`, disconnect in `destroy*`.
- Never observe `document.body` without narrow `subtree` + `attributes` filter.

---

## 7. State ownership

| State | Owner |
|-------|--------|
| DOM classes (`.is-active`) | Module that toggles them |
| `aria-*` | Same module |
| Form submit lock | `form` module |
| Open modal id | `modal` core (stack array) |
| Global analytics | Optional bridge — fire once per action |

**Forbidden:** cross-module direct DOM edits outside owned subtree.

---

## 8. DOM mutation survivability

**Section replacement flow:**

```text
destroySection(oldRoot)
→ swap HTML partial (Gulp include)
→ initSection(newRoot)
```

If only inner HTML of a module changes without section root replace → `reinitSection` on nearest `[data-section]`.

---

## 9. Module-specific notes

| Module | Init | Destroy must |
|--------|------|----------------|
| **tabs** | aria roles, keyboard arrows optional | remove keydown, reset aria-selected |
| **accordion** | one open or multi per handoff | close listeners |
| **modal** | ESC handler per open modal | close + unlock body |
| **slider** | touch listeners | cancel rAF, destroy swiper instance if used |
| **form** | submit, blur validation | abort fetch if `AbortController` |
| **sticky-cta** | intersection hide | unobserve |

---

## 10. jQuery compatibility

- Projects may use jQuery 3.x — wrap DOM queries in `$(root).find(...)` inside module boundary.
- Do not rely on `$.fn.plugin` without destroy support.
- Prefer vanilla where project has no jQuery — API stays identical via thin adapter.

---

## 11. Anti-patterns

- `$(document).on('click')` without namespace/off in destroy.
- Inline `<script>` in partials.
- `setInterval` without `clearInterval` in destroy.
- Reading state from `window.wf*` blobs mutated by multiple sections.

*Wave 2 — JS lifecycle foundation.*
