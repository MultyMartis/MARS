# Current Exporter Inventory (D2)

| Component | Path | Current capability | D2 action |
|-----------|------|--------------------|-----------|
| CLI | `src/.../cli.py` | validate-only, build-envelope | Extended producer commands; push-webhook blocked |
| Pipeline | `pipeline.py` | load→normalize→envelope→security | Reused |
| Envelope builder | `envelope_builder.py` | mars.client_ops.report v1 | Unchanged |
| Event identity | `event_identity.py` | UUID v5 deterministic | Unchanged |
| Normalizer | `normalizer.py` | OK/ATTENTION/FAILED/BLOCKED | Unchanged |
| Security validator | `security_validator.py` | path/token/stack gates | Unchanged |
| Producer modules | `producer_*.py` | — | Added offline producer layer |
