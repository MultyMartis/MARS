# EAR Runtime — Persistence (Store only)

**Phase:** R1.8 Persistence Model  
**Scope:** Mock snapshot packages → EAR Store under configured `output_root` only.

## Allowed

- `persist_mock_snapshot()` — writes `metadata.json`, `safe-unknown.json`, `acquisition-log.json`
- Layout under `{output_root}/{acquisition_id}/snapshots/{snapshot_id}/`
- `pathlib` directory creation under validated `output_root`

## Forbidden (this package)

- Publish / OCPilot / consumer intake
- Live SFTP, SSH, FTP, paramiko, socket
- SITE-001 / PILOT-001 live execution
- Writes outside configured `output_root`
- Overwrite of existing `snapshot_id` directory
- ZIP archives, evidence bulk writes (R1.8 minimal scope)

## Entry point

`snapshot_store.persist_mock_snapshot(snapshot_package, config)`
