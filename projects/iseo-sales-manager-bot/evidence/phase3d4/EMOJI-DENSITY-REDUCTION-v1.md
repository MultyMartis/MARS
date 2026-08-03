# EMOJI DENSITY REDUCTION v1

**Phase:** 3D.4  
**Version bump:** `sm-msg-v2` → **`sm-msg-v2.1`**

---

## 1. Problem (v2.0)

Phase 3D.3 `sm-msg-v2` introduced emoji indicators for lead type, lifecycle, and system sections. Operator review found **stacked emoji noise** on some cards — multiple indicators on adjacent lines reduced scannability without adding information.

---

## 2. v2.1 policy

| Rule | v2.0 | v2.1 |
|------|------|------|
| Title lead-type emoji | one per card | **unchanged** — one per card |
| Lifecycle emoji | on lifecycle line | **unchanged** |
| Section labels (Качество, Следующий шаг, …) | occasional ⚠️/ℹ️ prefix | **removed** — plain Russian labels |
| System footer (archive, corrupt contact) | ℹ️ prefix allowed | **single** ℹ️ max per card footer |
| Quality line | emoji + text | **text only** |
| «Не хватает» line | optional ⚠️ | **text only** |
| Max emoji per card (non-archive) | up to 3–4 | **max 2** (title + lifecycle) |

---

## 3. Preserved indicators

These remain — they carry distinct meaning:

| Emoji | Location | Meaning |
|-------|----------|---------|
| 🟢🟡🟠🔵 | Title | Lead type |
| 🕓✅🚫 | Lifecycle line | pending / processed / spam |
| ℹ️ | Archive footer only | «Архивная копия…» (when applicable) |

Admin command replies (stats, config, health) retain their existing system emoji vocabulary — this change applies to **manager lead cards** only.

---

## 4. CONFIG alignment

| Key | Value |
|-----|-------|
| `message_format_version` | **`sm-msg-v2.1`** |

Operational.dev formatter node stamps v2.1 on new cards. Archive `/leads` cards use the same formatter path.

---

## 5. Acceptance

| Check | Result |
|-------|--------|
| Harness F-MU01–F-MU04 title emoji | PASS |
| No section-prefix emoji on Качество/Следующий шаг | PASS |
| Lifecycle line emoji preserved | PASS |
| Archive footer single ℹ️ | PASS |
| Regression: copy `<code>` / `<pre>` blocks | PASS |
| Regression: inline keyboard attachment | PASS |

---

## 6. Non-goals

- No change to block order or Russian label text.
- No reintroduction of Markdown formatting.
- No emoji added to client reply `<pre>` block.

---

*Related: TELEGRAM-UX-CONTRACT-v1 §8 · TELEGRAM-FORMATTER-SPEC-v1 §6.*
