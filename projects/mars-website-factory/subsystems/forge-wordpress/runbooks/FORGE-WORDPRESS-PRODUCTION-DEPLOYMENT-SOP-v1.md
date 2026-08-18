# Forge WordPress — Production Deployment SOP v1

**ID:** FW-RB-02  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**Class:** C  
**Evidence:** FP-0002 P07–P17 exact-file SFTP waves

---

## Method: exact-file, never blind directories

For **every** touched product file:

1. Production-before snapshot + SHA256  
2. Local canonical change (after drift intake)  
3. Syntax / static QA (php -l, obvious grep)  
4. Exact upload  
5. Production-after SHA  
6. Source/prod parity table in the report  

WPilot `write_enabled=false` unless a **separate write charter** exists.

---

## Manifest (minimum)

```text
path | sha_before | sha_after | source_sha | match | rollback_copy
```

Store snapshots under the project backup root on `X:\AI MARS STORAGE` (not Git).

---

## Forbidden

Directory sync of `wp-content`; deploying `uploads`; deploying `wp-config.php`; deploying MU suppress by accident; deploying from dirty unrelated WIP.

---

*FW-RB-02 v1.*
