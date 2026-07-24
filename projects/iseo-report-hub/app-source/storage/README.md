# storage/ — local runtime artefacts

Holds logs, uploads, and cache for future phases.

Phase 0:

- directories exist with `.keep` placeholders;
- no uploads, no log writers, no cache writers;
- ignored by git except `.keep` (see `.gitignore`).

Do not store secrets or real private client metrics here in shared copies.
