# Environment Model v0

**Status:** documented — conceptual environment separation for MARS runtime planning. This file is documentation-only and does not define executable deployment assets.

## 1. Purpose

- Define `local`, `staging`, and `production` as distinct runtime environments in the target architecture.
- Prevent cross-environment confusion in data handling, permissions, and external integrations.
- Provide a governance baseline for approval-sensitive actions in high-impact environments.

## 2. Environment set (v0)

| Environment | Purpose | Typical usage posture |
|-------------|---------|------------------------|
| `local` | Developer-safe environment for documentation-driven iteration and future implementation testing. | Fast feedback, isolated scope, low blast radius assumptions. |
| `staging` | Pre-production validation environment for integration rehearsal and acceptance gates. | Controlled pre-release checks with representative workflows. |
| `production` | Business-impact environment for real operations once runtime implementation exists. | Highest control, strict approvals, and audit expectations. |

## 3. Why separation is required

- **Safety:** limits accidental high-impact actions by keeping risky operations out of lower-trust flows.
- **Integrity:** avoids mixing test/experimental records with business-critical data.
- **Governance:** enables different approval and permission postures by environment risk profile.

## 4. What differs between environments

### 4.1 Data

- Data scope, retention profile, and acceptable test fixtures differ across environments.
- Production-grade datasets must not be assumed present outside `production`.
- Test or synthetic data practices are expected in `local` and often in `staging`.

### 4.2 Permissions

- Agent/tool/model permissions can be environment-scoped by risk level.
- Sensitive operations require stronger controls as environment criticality increases.
- Effective rights in `production` are the most restrictive and approval-aware.

### 4.3 Integrations

- Integration endpoints, connectivity posture, and operational expectations may vary by environment.
- External side-effecting integrations require additional gate discipline in `staging` and `production`.
- Environment-specific integration behavior must remain explicit in future integration contracts.

## 5. Normative rules (v0)

1. `production` actions with meaningful side effects must not be executed directly without explicit approval.
2. Environment intent must be explicit in runtime-facing contracts and future execution context metadata.
3. Cross-environment assumptions are **SAFE UNKNOWN** until declared in an environment-aware contract.
4. This model does not authorize implementation claims for runtime isolation, provisioning, or enforcement.

## 6. Relations to other artefacts

- [../security/permissions-v0.md](../security/permissions-v0.md) — permission vocabulary and constraints to be environment-aware in future implementation.
- [../security/approval-gates.md](../security/approval-gates.md) — approval classes and HITL boundaries for high-risk actions.

## 7. Explicit non-goals

- No real deployment or hosting configuration.
- No environment provisioning scripts.
- No container/orchestrator manifests.
- No executable policy engine behavior.

**Explicit statement:** **NO real deployment configs** are defined or implied by this file.
