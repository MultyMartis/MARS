#!/usr/bin/env python3
"""Build EQ-ALT-A harness from EXP-A01b with binary-safe CRLF edits."""
from pathlib import Path

src = Path(
    r"X:\AI MARS\projects\mars-server-ops\tools\experiments\EXP-A01b\Invoke-EXP-A01b.ps1"
)
dst = Path(
    r"X:\AI MARS\projects\mars-server-ops\tools\experiments\EQ-ALT-A-REALITY-VISION\Invoke-EQ-ALT-A-REALITY-VISION.ps1"
)

raw = src.read_bytes()
bom = b""
if raw.startswith(b"\xef\xbb\xbf"):
    bom = raw[:3]
    raw = raw[3:]
text = raw.decode("utf-8")
# Preserve original newlines exactly
nl = "\r\n" if "\r\n" in text else "\n"

text = text.replace(
    "$script:HarnessVersion = 'EXP-A01b-1.0.0'",
    "$script:HarnessVersion = 'EQ-ALT-A-REALITY-VISION-1.0.0'",
)
text = text.replace(
    "X:\\AI MARS\\projects\\mars-server-ops\\evidence\\EXP-A01b",
    "X:\\AI MARS\\projects\\mars-server-ops\\evidence\\EQVPS-TRANSPORT-ALTERNATIVES-WAVE-01",
)

banner = nl.join(
    [
        "",
        "# --- EQ-ALT-A overlay (profile selection) ---",
        "$script:AltAProfileName = 'MCA-ONE-EQ-ALT-A-REALITY-VISION'",
        r"$script:AltAImportUri = 'X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\eqvps-alt-a-reality-vision-2026-08-29\vless-share.uri.local'",
        "$script:AltAPort = 9443",
        "$script:AltAExpectedEgress = '95.216.126.173'",
        "function Show-AltAProfileBanner {",
        "    Write-Host ''",
        "    Write-Host ('#' * 72) -ForegroundColor Magenta",
        "    Write-Host 'EQ-ALT-A-REALITY-VISION / offline acceptance' -ForegroundColor Magenta",
        "    Write-Host (\"Profil v2rayN: {0}\" -f $script:AltAProfileName) -ForegroundColor Magenta",
        "    Write-Host (\"Server port: {0} REALITY+Vision. Do NOT use/modify EQVPS :8443.\" -f $script:AltAPort) -ForegroundColor Magenta",
        "    Write-Host (\"Expected egress: {0}\" -f $script:AltAExpectedEgress) -ForegroundColor Magenta",
        "    Write-Host (\"Import if missing: {0}\" -f $script:AltAImportUri) -ForegroundColor Magenta",
        "    Write-Host 'Harness does not switch VPN. Admin PowerShell NOT required.' -ForegroundColor Magenta",
        "    Write-Host ('#' * 72) -ForegroundColor Magenta",
        "    Write-Host ''",
        "}",
        "",
    ]
)

# Insert banner function after harness version line (before ProxyUrl)
ver_line = "$script:HarnessVersion = 'EQ-ALT-A-REALITY-VISION-1.0.0'" + nl
if ver_line not in text:
    raise SystemExit("version line missing")
text = text.replace(ver_line, ver_line + banner, 1)

# Call banner at start of main try, before PHASE 0 header
phase0 = "Write-StageHeader 'PHASE 0"
pos = text.find(phase0)
if pos < 0:
    raise SystemExit("PHASE 0 header missing")
# back up to start of line
line_start = text.rfind(nl, 0, pos)
if line_start < 0:
    line_start = 0
else:
    line_start += len(nl)
indent = "    "
insert = indent + "Show-AltAProfileBanner" + nl + indent
text = text[:line_start] + insert + text[line_start:]

text = text.replace(
    "В v2rayN ВРУЧНУЮ выберите профиль:",
    "ВНИМАНИЕ EQ-ALT-A: профиль MCA-ONE-EQ-ALT-A-REALITY-VISION (не EQVPS :8443). "
    "Импорт при необходимости: vless-share.uri.local. "
    "В v2rayN ВРУЧНУЮ выберите профиль:",
    1,
)
text = text.replace(
    "VEESP RAW :8443  →  EQVPS RAW :8443",
    "VEESP RAW :8443  →  MCA-ONE-EQ-ALT-A-REALITY-VISION (:9443 REALITY+Vision)",
)
text = text.replace(
    "EQVPS RAW :8443  →  VEESP RAW :8443",
    "MCA-ONE-EQ-ALT-A-REALITY-VISION (:9443)  →  VEESP RAW :8443",
)
text = text.replace(
    "ПЕРЕКЛЮЧИТЕ VPN НА EQVPS RAW :8443",
    "ПЕРЕКЛЮЧИТЕ VPN НА MCA-ONE-EQ-ALT-A-REALITY-VISION (:9443)",
)

out = bom + text.encode("utf-8")
# Ensure CRLF if source was CRLF (decode may have kept them; if LF-only source had CRLF in bytes)
if nl == "\r\n" and b"\r\n" not in out:
    out = bom + text.replace("\n", "\r\n").encode("utf-8")
dst.write_bytes(out)
print("OK", dst, "bytes", len(out), "nl", repr(nl), "crlf", out.count(b"\r\n"))
