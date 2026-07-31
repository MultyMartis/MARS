# FIELD-EXTRACTION-TRACE-v1

**Phase:** 3D.1  
**Sample:** latest operator audit-form test before parser repair (sanitized)

## Boundary table

| Field | Source Present | Parsed (pre-fix) | Normalized | Final Card |
|-------|----------------|-------------------|------------|------------|
| client_name | Yes (`От кого:`) | No | No | — |
| contact_method | Yes (`Способ связи: Телефон`) | No | No | (empty contacts) |
| phone | Yes (`Контакт:`) | No | No | — |
| email | No | No | No | — |
| messenger | No | No | No | — |
| site | Yes (`Адрес сайта:`) | No | No | — |
| service | Yes (audit title) | N/A | Audit (from raw text) | Аудит |
| comment/request | Yes (`Комментарий:`) | Only as full blob | summary=full blob | Кратко: full labeled blob |
| source_page | No | No | No | — |

## Node path

Gmail Fetch Leads → Intake Gate (`lead`) → **Parse Lead (fail extract)** → Append RAW → Read/Normalize CONFIG → Deterministic Lead Processor (`quality=bad`) → AI OFF → Dedupe → CLEAN → Format Telegram → Send Telegram → PROCESSED + remove incoming.

## Downstream erasure check

No downstream node erased successfully extracted fields: Parse Lead never extracted them. Deterministic processor and Telegram formatter correctly reflected empty `parsed_*` inputs.

## Local harness replay (post-fix)

Same sanitized collapsed template under `sm-parser-v3.1`:

| Field | Extracted |
|-------|-----------|
| client_name | yes |
| phone | yes (normalized display retained) |
| site | yes (including `.example` test host) |
| contact_method | phone |
| form_name | Заявка на бесплатный аудит |
| request_text | comment (+ audit preface) |
