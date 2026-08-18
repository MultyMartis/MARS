# Forge WordPress — Regression pack v1

**ID:** FW-S-42  
**Status:** ACTIVE — QA STANDARD  
**Date:** 2026-08-18  
**Use with:** [QA-MATRIX](../templates/FORGE-WORDPRESS-QA-MATRIX-v1.md) · [REAL-DEVICE-QA](FORGE-WORDPRESS-REAL-DEVICE-QA-STANDARD-v1.md) · [FRONTEND-ACCEPTANCE](FORGE-WORDPRESS-FRONTEND-ACCEPTANCE-STANDARD-v1.md)

A frontend change is **not done** on screenshot parity alone.

---

## 1. Representative routes (typical WP Forge site)

| Route | Must exist in the pack |
|-------|------------------------|
| Home | front page |
| Standard Page | legal / about-style |
| CPT hub | archive-or-hub page |
| CPT single | one published object |
| Article | one post |
| Contacts / legal | forms + footer globals |

Project adds routes that are commercially critical.

---

## 2. Functions

Navigation · mobile menu · search (if enabled) · forms · CTA/modal · sitemap GET · REST/AJAX used on those routes · WP Admin (editor smoke).

---

## 3. Redirects

- one known legacy path  
- host redirect **after** launch (not before the final host works)

---

## 4. Risk-based device matrix

| Change type | Windows Chromium | Firefox | Physical iPhone Safari | Android Chrome | MacBook trackpad |
|-------------|------------------|---------|------------------------|----------------|------------------|
| Backend-only (PHP Admin, no FE CSS/JS) | smoke optional | — | — | — | — |
| Copy / CMS field | affected route | — | — | — | — |
| Layout / CSS | yes | smoke if non-trivial | if layout uses viewport/fixed | if touch layout | — |
| Menu / modal / accordion | yes | smoke | yes if mobile nav | yes | — |
| Slider | yes | smoke | touch | touch | **yes** |
| Transform / parallax / fixed / vh | yes | smoke | **blocking** | yes | — |
| Forms | yes | — | mobile keyboard | mobile keyboard | — |

Do not require all devices for a backend-only change.

---

## 5. QA fixtures

Maintain a small set of **canonical test objects**:

- draft QA posts/pages marked in title (`[QA]`)  
- reversible IDs recorded in the project QA note  
- cleanup lifecycle (delete or keep draft)  
- **do not** mutate unknown production objects to “see what happens”  
- **do not** use unknown production PHP in webroot as test tools ([FW-S-20](FORGE-WORDPRESS-PUBLIC-WEBROOT-HYGIENE-GATE-v1.md))

---

## 6. After a frontend change (minimum)

Routes in §1 that the change can touch + keyboard on interactive controls + one relevant breakpoint + device row from §4.

---

*FW-S-42 v1.*
