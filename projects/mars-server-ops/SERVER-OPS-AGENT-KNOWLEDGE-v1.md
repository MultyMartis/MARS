# MARS Server Ops — Agent knowledge pack v1

**Programme:** MARS Server Ops & VPS Forge  
**Status:** **human-readable knowledge** for Cursor/Codex operators — **not** an autonomous agent product  
**Not claimed:** runtime orchestration, standing SSH fleet, CMDB engine, unattended remediation  

---

## 1. How to use this pack

Before VPN / VPS / provider / acceptance claims:

1. Read [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)  
2. Read [SERVER-INVENTORY-v1.md](SERVER-INVENTORY-v1.md)  
3. Consult [SUPERSEDED-CONCLUSIONS-REGISTER-v1.md](SUPERSEDED-CONCLUSIONS-REGISTER-v1.md)  
4. Apply [REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md](REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md)  
5. Apply [CONTROL-EVIDENCE-METHODOLOGY-v1.md](CONTROL-EVIDENCE-METHODOLOGY-v1.md)  
6. Keep secrets out of Git per [SECRET-HANDLING-MODEL-v1.md](SECRET-HANDLING-MODEL-v1.md)

FriendHosting canonical home: [assets/FRIENDHOSTING-DE/](assets/FRIENDHOSTING-DE/README.md)

---

## 2. Reusable operational lifecycle (beyond VPN)

```text
REQUIREMENTS
  → PREFLIGHT
  → PROVIDER / CAPACITY
  → BACKUP / ROLLBACK PLAN
  → DEPLOY
  → TECHNICAL VALIDATION
  → REAL-WORKLOAD ACCEPTANCE
  → HARDEN
  → BACKUP (verified)
  → DOCUMENT
  → MONITOR
  → RECOVER
```

Do not skip **real-workload acceptance** after a transport PASS.  
Do not call **PRODUCTION_ACCEPTED** without soak + operational gates.

Generalizes to: Linux VPS · Docker · PostgreSQL · n8n · reverse proxy · TLS · migration · incident response.

---

## 3. Acceptance ladder (never collapse)

```text
PING PASS
  ≠ TCP PASS
  ≠ TLS PASS
  ≠ TRANSPORT PASS
  ≠ APPLICATION PASS
  ≠ REAL-WORKLOAD PASS
  ≠ OPERATIONALLY ACCEPTED (scoped workload)
  ≠ LONG-TERM OPERATIONAL STABILITY
  ≠ PRODUCTION_ACCEPTED
```

**Negative case:** EQVPS — transport PASS / real workloads FAIL.  
**Independent positive case:** FriendHosting — same general client/Xray/RAW class; real workloads PASS.  
**Known-good control:** VEESP — real workloads PASS.

---

## 4. Anti-config-churn

When transport is healthy but applications fail:

**Do not** immediately cycle Reality / WS / gRPC / XHTTP / random MTU / BBR / sysctl / DNS / core downgrade.

**Prefer:** failure classification → controls → single-variable A/B → provider/network control → real-workload evidence.

---

## 5. Provider qualification

```text
looking-glass PASS  ≠  assigned IP / subnet PASS
```

Direct ISP preflight on the **assigned** IP is required where possible.  
Canonical lesson: AdminVPS Finland (Server B).  
FriendHosting lesson: independent ASN + known-listener TCP gate + real-workload acceptance.

---

## 6. Backup honesty

```text
BACKUP VERIFIED  ≠  FULL DISASTER RESTORE TESTED
```

---

## 7. Secret boundary (VPN / panels)

Never write into Git/REPORT:

- VLESS UUIDs / URIs / QR  
- root passwords / SSH private keys  
- panel credentials / secret panel path  
- TLS private keys  

State **where** secrets live and **how** to restore them.

---

## 8. FriendHosting operator defaults

- Prefer 3X-UI native QR/copy-link for device provisioning  
- One VLESS identity per device  
- Do not open `:2096` for convenience  
- P4 `:24443` remains deferred until chartered  
- Do not mutate live servers from documentation waves  

---

## 9. Related maturity

[SERVER-OPS-CAPABILITY-MATURITY-v1.md](SERVER-OPS-CAPABILITY-MATURITY-v1.md)  
[SERVER-OPS-WIDER-ROADMAP-v1.md](SERVER-OPS-WIDER-ROADMAP-v1.md)

---

*Agent knowledge pack v1 · documentation only · 2026-08-30.*
