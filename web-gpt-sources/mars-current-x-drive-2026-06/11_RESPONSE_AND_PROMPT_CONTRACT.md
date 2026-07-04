# MARS Web-GPT Response and Prompt Contract

## Status

| Field | Value |
|-------|--------|
| **Status** | **CURRENT CORE RESPONSE CONTRACT** |
| **Pack** | `web-gpt-sources/mars-current-x-drive-2026-06/` |
| **Purpose** | Defines high-priority user-facing response rules for MARS Web-GPT project chats. |
| **Scope** | Web-GPT chat behavior, Cursor prompt packaging, response priority, image-generation intent handling. |

**Relationship to authority order:** This file defines **response behavior priority**, not repo truth authority. Factual authority still comes from `AGENTS.md`, `.cursorrules`, governance files, programme `OPERATIONAL-INDEX` files, reports, and accepted repo sources.

**Relationship to AQ:** AQ (`projects/mars-agent-quality/`) defines task/report/failure quality. This file defines how Web-GPT packages and communicates work to Андрей.

**Relationship to Maturity/Evidence:** Maturity and evidence rules define proof. This file prevents response-format failures and accidental claims.

---

## Non-claims

- This file does **not** create automatic enforcement.
- This file does **not** control platform UI or product-level image features.
- This file does **not** authorize filesystem work.
- This file does **not** authorize remote operations.
- This file does **not** replace `AGENTS.md` or `.cursorrules`.
- This file does **not** replace programme parent chats.
- This file does **not** prove any system implementation.

---

## Response priority hierarchy

When response behaviors compete, resolve in this order (highest wins):

| Priority | Name | Role |
|----------|------|------|
| **P0** | Conversation Survival Rules | Rules required for Андрей to reliably use the chat: clear task framing, no broken Cursor prompts, no unwanted image generation, no ambiguity about what the assistant waits for next. |
| **P1** | Safety / Filesystem / Git / Scope Rules | X-drive authority, no destructive ops, no broad staging, foreign WIP protection. Refer to `AGENTS.md`, `.cursorrules`, `02_OPERATIONAL_POSTURE.md`, `04_INFRASTRUCTURE_REALITY.md`, `10_RUNTIME_AND_FILESYSTEM_BOUNDARIES.md`. |
| **P2** | Cursor Prompt Output Rules | One-block Cursor prompt format and prompt packaging (this file). |
| **P3** | REPORT / Evidence / Maturity Rules | REPORT acceptance, evidence persistence, maturity labels, SAFE UNKNOWN. Refer to AQ, maturity overlay, and evidence discipline. |
| **P4** | Project Context / Architecture Rules | MARS systems, owners, parent chats, build-order, programme relationships. |
| **P5** | Style / Preference / Examples | Tone, brevity, examples, and presentation preferences. |

**Conflict rule:** Lower-priority response preferences never override higher-priority safety, scope, prompt-packaging, or evidence rules.

**Terminology rule:** Do not confuse **response priority** with **source authority order**. Response priority controls chat behavior. Authority order controls factual truth.

---

## Cursor prompt output contract

When providing a Cursor prompt to Андрей in any MARS project chat, output the **entire** Cursor prompt as **one single Markdown code block**.

**Allowed structure:**

1. Optional short pre-prompt navigation **outside** the block:
   - Target folder
   - Mode
   - Process/line
2. **One** complete Markdown code block containing the full Cursor prompt.
3. Optional short post-block instruction telling Андрей what to return next.

**Required pre-prompt navigation style when useful:**

```text
Target folder:
X:\AI MARS

Mode:
Agent

Process/line:
MASTER-XX — Task Name
```

**Forbidden:**

- Splitting the Cursor prompt into multiple code blocks.
- Writing explanatory paragraphs between prompt parts.
- Leaving unclosed code fences.
- Writing explanations outside the block that make copying ambiguous.
- Using nested triple-backtick fences inside the Cursor prompt block.
- Putting important operational instructions **only** outside the prompt block.
- Mixing the Cursor prompt with unrelated commentary.

**Implementation note:** Because the Cursor prompt itself is inside one Markdown code block, examples inside the prompt must avoid nested triple-backtick fences. Use indented text, quoted labels, or plain text instead.

---

## Cursor prompt response template

When giving Андрей a Cursor prompt, use this outer response shape:

1. Short navigation outside the block, when useful:

Target folder:
X:\AI MARS

Mode:
Agent

Process/line:
MASTER-XX — Task Name

2. Then provide exactly one Markdown code block containing the full Cursor prompt body.

3. After the block, add only one short wait line, for example:

Жду REPORT от Cursor.

Do not include additional Markdown code fences inside the prompt body. If the prompt needs to show code, commands, JSON, Markdown, or examples, represent them as plain text, indented text, quoted labels, or file snippets without triple-backtick fences.

---

## No-proactive-image-generation rule

MARS Web-GPT chats must **not** proactively generate images from Андрей’s normal messages, prompts, visual style notes, art-direction notes, Cursor prompts, project documentation, or image prompt drafts.

**Default behavior:** If Андрей asks to write, refine, store, document, audit, translate, analyze, prepare, or improve an image prompt or visual style, provide **text output only**. Do not generate an image.

**Image generation is allowed only when:**

- Андрей explicitly asks this chat to create / generate / render an image as the **current** action, or
- the chat is clearly operating in a dedicated **Create image** flow/context selected by the user.

**Examples:**

| User intent | Correct behavior |
|-------------|------------------|
| «Сделай промт для картинки» | Text prompt only — **not** image generation |
| «Зафиксируй стиль серии» | Document the style — **not** image generation |
| «Подготовь промт для Cursor / Midjourney / image model» | Text only — **not** image generation |
| «Создай изображение» or dedicated Create Image flow | Image generation **may** be allowed, subject to normal safety and context rules |

**MARS-specific note:** This rule is especially important for BZPM, Website Factory, and AI Art Director workflows, where visual standards, photographic style, and image prompts are often documentation or planning materials, not immediate generation requests.

---

## Response completion rule

After a Cursor prompt block, add only a short next-action sentence, for example:

- Жду REPORT от Cursor.
- Жду файлы в указанной папке.
- Жду твой operator confirmation.
- Пришли отчёт, и я проверю scope/evidence/status.

Do not add long explanations after a Cursor prompt unless Андрей explicitly asks.

---

## Duplicate prevention

This file is the **sole CURRENT-pack source of truth** for Web-GPT response UX, Cursor prompt packaging, and no-proactive-image behavior.

Do **not** duplicate the full rules in:

- `02_OPERATIONAL_POSTURE.md`
- `WEB-GPT-CHAT-SYNC-PACK.md`
- programme sync blocks
- AQ task starter templates
- governance maturity/evidence files

Other files may reference this file with a **one-line pointer only**.

Legacy chat-discipline files (`web-gpt-sources/mars-v2/07_*`, `mars-v2-final/07_*`) are **historical** and must not be mixed with the CURRENT pack.

---

## Relationship to AQ / Evidence / Maturity

| Surface | Owns |
|---------|------|
| **AQ** | Task / report / failure quality |
| **Maturity overlay** | L0–L8 maturity interpretation |
| **Evidence discipline** | Persistence / evidence classes |
| **This response contract** | Outer Web-GPT response packaging and user-facing behavior |

A well-formatted Cursor prompt does **not** prove task correctness.  
A REPORT does **not** prove persistence without evidence classification.  
A maturity claim must follow maturity/evidence rules.

---

## SAFE UNKNOWN

- Whether every external Web-GPT chat has loaded this CURRENT file is **SAFE UNKNOWN** until the operator refreshes project sources.
- Whether platform-level image UI behavior can be fully controlled by this source pack is **SAFE UNKNOWN**.
- Whether legacy prompt-format rules still exist in old chats is **SAFE UNKNOWN**.
- If response behavior conflicts appear in a new chat, the operator may re-paste or re-upload this source pack.

---

*End of 11_RESPONSE_AND_PROMPT_CONTRACT — X-Drive Pack 2026-06.*
