# Server B SSH Access Model v1

**Status:** **ACTIVE** — 2026-08-25 (Phase 3C)  
**Locus:** `SERVER-B-PLANNING`  
**Not:** credential store, automated fleet connector, or VPN access model

---

## 1. Intended remote access path

```text
Operator workstation / MARS Cursor
  → Ed25519 private key (local-only)
  → SSH tcp/22
  → user: marsops
  → optional sudo (password-confirmed)
  → Server B (metacode-cloud.com / <SERVER_B_IP>)
```

| Surface | Policy |
|---------|--------|
| Remote SSH user | `marsops` only (practical) |
| Root remote SSH | **DISABLED** |
| Password SSH | **DISABLED** |
| Public-key SSH | **ENABLED** |
| Port | `22` (unchanged Phase 3C) |
| AllowUsers restriction | **NOT** applied |

---

## 2. Authentication / elevation

| Layer | Method | Secret location |
|-------|--------|-----------------|
| SSH login | Ed25519 key | `X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\ssh\marsops_ed25519` |
| Public key on host | `/home/marsops/.ssh/authorized_keys` | fingerprint in Git docs only |
| Sudo | password | `secrets.local.md` → Operator sudo |
| NOPASSWD | **NOT** used | — |

Fingerprint (public): `SHA256:LKHbvYWrslvA0Ip+WHGmZ4AbaULLCuXr22sxGBNAXsA`

---

## 3. Emergency / recovery surfaces

| Path | Role | Phase 3C state |
|------|------|----------------|
| Provider emergency console | Last-resort interactive | **UNCHANGED**; live availability **SAFE UNKNOWN** |
| Local root password | Console / recovery secret | **PRESERVED** local-only; not for remote SSH |
| Prior root+password SSH | Temporary bootstrap | **RETIRED** for remote use |

---

## 4. Explicit non-goals (this model)

- VPN / 3X-UI / Xray client access  
- SSH port change / obfuscation  
- Shared personal keys / Server A key reuse  

**Note (Phase 3D):** UFW + fail2ban are now active host controls — see [SERVER-B-FIREWALL-BASELINE-v1.md](SERVER-B-FIREWALL-BASELINE-v1.md) and [SERVER-B-FAIL2BAN-BASELINE-v1.md](SERVER-B-FAIL2BAN-BASELINE-v1.md). They do not replace key-only SSH auth.

---

## 5. secret_ref

```text
secret_ref: local/infrastructure/SERVER-B-PLANNING/secrets.local.md
  → Initial SSH (historical bootstrap)
  → Operator SSH
  → Operator sudo
  → SSH policy state: KEY-ONLY REMOTE ACCESS
```

---

*SSH access model · key-only remote · password sudo · no secrets in Git.*
