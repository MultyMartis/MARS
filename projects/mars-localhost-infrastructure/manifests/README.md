# MLI Runtime Manifests

**Location:** `C:\MARS Phenix\AI MARS\projects\mars-localhost-infrastructure\manifests\`
**Contract:** [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](../MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md)

---

## Purpose

Brain-side canonical pointers to runtimes on `E:\MARS-Localhost`. Runtime files stay on D:; manifests stay in Git (values only — no secrets).

---

## Rules

- One manifest per sustained runtime (`synthetic`, `projects`, `sandboxes`)
- Filename: `{runtime-id}.json` or `{platform}-{class}-{slug}.json`
- Update manifest when local path, URL, or database id changes
- `current_status: planned` until MLI-01+ provisioning

---

## MLI-00 state

No runtime manifests created yet — no Laragon sites provisioned.

---

*Manifests directory — MLI-00.*
