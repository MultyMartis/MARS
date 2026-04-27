# Secrets Management v0

**Status:** documented — conceptual handling model for sensitive credentials in MARS. Documentation-only; no secret manager implementation.

## 1. Purpose

- Define what MARS treats as secret material in runtime and integration planning.
- Establish strict repository hygiene and access rules for sensitive values.
- Align secrets posture with security and risk governance artefacts.

## 2. What counts as a secret

- API keys for external services.
- Access tokens, session tokens, and signing tokens.
- Database credentials and direct DB access material.
- Any credential-like value that grants access to protected systems or data.

## 3. Normative rules (v0)

1. Secrets must never be stored in this repository, including markdown examples that expose live values.
2. Secrets access is assumed to occur through a secure access layer in future implementation.
3. Secret handling behavior remains **planned-implementation** unless runtime evidence exists in-repo.
4. Any secret-related uncertainty is **SAFE UNKNOWN** until documented by a dedicated implementation contract.

## 4. Access posture (conceptual)

- Runtime components should consume secret material indirectly via controlled interfaces.
- Security controls, approval flow, and auditability requirements apply to secret access paths.
- Secret lifecycle (rotation, revocation, incident handling) is out of implementation scope in v0 and remains conceptual.

## 5. Relation to other artefacts

- [../security/threat-model-v0.md](../security/threat-model-v0.md) — threat classes involving exfiltration, abuse, and boundary failures.
- [../governance/risk-register.md](../governance/risk-register.md) — explicit tracking of secret-leak and integration security risks.

## 6. Explicit non-goals

- No secret storage backend selection.
- No key vault product binding.
- No credential bootstrap workflow.
- No environment variable templates containing sensitive placeholders.

**Explicit statement:** **NO secret storage implementation** is defined in this file.
