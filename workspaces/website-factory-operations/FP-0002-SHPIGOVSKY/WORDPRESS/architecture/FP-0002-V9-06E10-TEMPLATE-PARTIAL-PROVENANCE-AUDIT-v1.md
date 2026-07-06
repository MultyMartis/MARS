# FP-0002 V9-06E10 Template Partial Provenance Audit v1

**Evidence JSON:** `validation/v9-06e10-full-backup-wp-port-root-cause-audit/template-partial-provenance-audit.json`

## Provenance summary

| Category | Count | Risk profile |
|----------|------:|--------------|
| DIRECT_V9_PORT | 8 | Low |
| V9_ADAPTED_PARTIAL | 35 | Low–medium |
| SEMANTIC_RECONSTRUCTION | 12 | **High on V9 routes** |
| ACF_DYNAMIC_REBUILD | 18 | Medium |
| DEMO_FALLBACK | 7 | **High** |
| OLD_PRE_V9_PARTIAL | 6 | **High** |

## Highest-risk partials (service leaf focus)

| Partial | Used by | Provenance | Risk | Notes |
|---------|---------|------------|------|-------|
| `service/leaf-stack.php` | Generic leaf CPT | SEMANTIC_RECONSTRUCTION | **high** | 10 sections vs 17 static |
| `service/alcohol-stack.php` | Alcohol leaf | SEMANTIC_RECONSTRUCTION | medium | Correct order; home partial reuse |
| `home/specialists.php` | Home + service routes | V9_ADAPTED_PARTIAL | medium | Service-leaf ids passed via args |
| `home/reviews.php` | Home + service routes | V9_ADAPTED_PARTIAL | medium | Wraps shared slider |
| `home/clinic-landscape.php` | Home + service routes | V9_ADAPTED_PARTIAL | medium | Modifier class only |
| `service/program.php` | All service variants | DEMO_FALLBACK | high | V9 fixture lorem |
| `inc/v9-static-content.php` | Hub + alcohol | DEMO_FALLBACK | high | PHP re-encoding not HTML include |

## Mixing finding

**V8/V9/old/demo components are mixed** at stack level: D7-D service stacks call D9-D home partials and D8-C ACF-driven section bodies. No single provenance chain per page.
