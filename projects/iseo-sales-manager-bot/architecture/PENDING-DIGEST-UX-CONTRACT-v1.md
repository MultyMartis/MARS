# PENDING DIGEST UX CONTRACT v1

**Contract id:** `iseo-pending-digest-renderer-v1.0`  
**Phase:** 3H.10  
**Status:** deployed (Admin.dev Reminder Build Claims)

## Purpose

One primary Telegram reminder per active recipient: an **actionable pending-queue digest**, not a bundle of full lead cards.

## Inputs

- Authoritative unique current pending leads (current-state selector)
- Window label (e.g. `10:00 МСК`)
- Category mapping (presentation-only)
- Opaque lead action tokens

## Outputs

- One message body (HTML/plain text safe)
- Inline keyboard of lead actions
- Counters: total · today · older_than_24h · oldest_age
- Overflow flag + `📋 Все необработанные` when capped

## Rules

- Human categories: Аудит · SEO · Реклама · Разработка сайта · Другое · Требует уточнения
- Category order: Аудит → SEO → Реклама → Разработка сайта → Другое → Требует уточнения
- Within category: oldest first
- Age labels: сегодня / N день|дня|дней; markers ⚠️ (3–4d) · 🔴 (5+d)
- Label: client name → site → `Лид без имени`
- No phone / email / raw lead id in digest body
- Body budget ≈ 3500 chars; button cap **25**
- Zero pending → no reminder (`SKIPPED_ZERO_PENDING`)
- One primary message per recipient per window

## Non-goals

- Does not mutate lead status
- Does not replace `/pending_leads` full listing
- Does not restore revoked ACCESS profiles
