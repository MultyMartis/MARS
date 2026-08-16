# PROD-P07-FU01-CONT2 — Beget IP-unblock recovery

**Date:** 2026-08-14  
**Wave:** PROD-P07-FU01-CONT2

```text
PRIOR TRANSPORT FAILURE ROOT CAUSE = BEGET IP BLOCK — OPERATOR IP UNBLOCKED BY BEGET SUPPORT
```

Operator confirmed Beget support unblocked the operator IP. This continuation did **not**:

* investigate fail2ban;
* investigate credentials;
* create FTP/SSH users;
* rotate passwords;
* change hosting security configuration.

Previous blocker `STOP — BEGET SSH/FTP PROTOCOL BANNER TIMEOUT` is closed by a single SSH/SFTP session after the unblock.

Proof: `cont2-transport-check.json`  
Verdict: `BEGET FILE TRANSPORT RESTORED`
