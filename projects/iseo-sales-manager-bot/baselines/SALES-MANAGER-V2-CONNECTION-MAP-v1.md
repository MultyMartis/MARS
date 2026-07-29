# SALES MANAGER V2 CONNECTION MAP v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A.1  
**Source SHA256:** `AD90715FD14B6F8EF568BCBD69CC0F123D41FF024296AD3E54D3B9FD11AB821C`  
**Edges:** 18 · **Broken targets:** 0

## 1. Main graph

```
Schedule Trigger
  → Get many messages
  → Lead-Mail-Parser
       ├→ Запись лида (RAW)          [no further edges]
       └→ Prepare-OpenRouter-Request
            → HTTP Request (AI #1)
            → Normalize-AI-Result
            → Prepare-AI-Normalizer-Request
            → AI-Normalizer (AI #2)
            → Normalize-Clean-Lead
            → Find Duplicate Lead
            → Mark-Duplicate-Status
            → IF - Bad Quality
                 ├ true  → Add label ERROR → Remove label LEADS_ISEO2
                 └ false → Осмысленные лиды (CLEAN) → message v2 → Add label PROCESSED → Remove label LEADS_ISEO
```

## 2. Edge list

| From | Channel | To |
|------|---------|----|
| `Schedule Trigger` | `main` | `Get many messages` |
| `Get many messages` | `main` | `Lead-Mail-Parser` |
| `Add label PROCESSED` | `main` | `Remove label LEADS_ISEO` |
| `Lead-Mail-Parser` | `main` | `Запись лида (RAW)` |
| `Lead-Mail-Parser` | `main` | `Prepare-OpenRouter-Request` |
| `Prepare-OpenRouter-Request` | `main` | `HTTP Request (AI #1)` |
| `Normalize-AI-Result` | `main` | `Prepare-AI-Normalizer-Request` |
| `Normalize-Clean-Lead` | `main` | `Find Duplicate Lead` |
| `Prepare-AI-Normalizer-Request` | `main` | `AI-Normalizer (AI #2)` |
| `HTTP Request (AI #1)` | `main` | `Normalize-AI-Result` |
| `AI-Normalizer (AI #2)` | `main` | `Normalize-Clean-Lead` |
| `Осмысленные лиды (CLEAN)` | `main` | `message v2` |
| `message v2` | `main` | `Add label PROCESSED` |
| `IF - Bad Quality` | `main` | `Add label ERROR` |
| `IF - Bad Quality` | `main` | `Осмысленные лиды (CLEAN)` |
| `Add label ERROR` | `main` | `Remove label LEADS_ISEO2` |
| `Find Duplicate Lead` | `main` | `Mark-Duplicate-Status` |
| `Mark-Duplicate-Status` | `main` | `IF - Bad Quality` |

## 3. Side-effect gates

| Gate | v2 behavior | Operational.dev target |
|------|-------------|------------------------|
| RAW write | Parallel after parse | Post-parse; no AI columns |
| AI #1+#2 | Always on | Max one gated call |
| CLEAN | Only if not Bad Quality | Upsert with enums |
| Telegram | After CLEAN; success assumed | IF success before labels |
| PROCESSED | After Telegram node | Only on TG success |
| ERROR | Bad quality; removes incoming | ERROR label; preserve incoming on TG/process fail |

*Connection graph identical in sanitized v1.*
