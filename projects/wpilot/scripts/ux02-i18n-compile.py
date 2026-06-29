import os
import re
from pathlib import Path

import polib

MARS_ROOT = Path(os.environ.get("MARS_ROOT", r"X:\AI MARS"))
plugin = MARS_ROOT / "projects" / "wpilot" / "plugin" / "metacode-wpilot"
admin_files = list((plugin / "admin").glob("*.php"))

pattern = re.compile(r"__\(\s*'((?:\\'|[^'])*)'\s*,\s*'metacode-wpilot'\s*\)")
esc_pattern = re.compile(r"esc_(?:html|attr)__\(\s*'((?:\\'|[^'])*)'\s*,\s*'metacode-wpilot'\s*\)")

entries = {}
for f in admin_files:
    text = f.read_text(encoding="utf-8")
    rel = str(f.relative_to(plugin)).replace("\\", "/")
    for m in pattern.finditer(text):
        msgid = m.group(1).replace("\\'", "'")
        entries.setdefault(msgid, rel)
    for m in esc_pattern.finditer(text):
        msgid = m.group(1).replace("\\'", "'")
        entries.setdefault(msgid, rel)

ru_map = {
    "Overview": "Обзор",
    "Runtime": "Runtime",
    "Connection": "Подключение",
    "Endpoints": "Endpoints",
    "Safety": "Безопасность",
    "Diagnostics": "Диагностика",
    "WPilot sections": "Разделы WPilot",
    "Schema": "Схема",
    "Last MARS Connection": "Последнее подключение MARS",
    "Last Success": "Последний успех",
    "Last Failure": "Последний сбой",
    "Write Readiness": "Готовность к записи",
    "DEV Confirmation": "Подтверждение DEV",
    "Proven Operations Count": "Количество проверенных операций",
    "Endpoints Count": "Количество endpoints",
    "Last Milestone": "Последний milestone",
    "success": "успех",
    "failed": "сбой",
    "never": "никогда",
    "Last Failure Reason": "Причина последнего сбоя",
    "Last token use (UTC)": "Последнее использование токена (UTC)",
    "MARS Connection Diagnostics": "Диагностика подключения MARS",
    "Connection diagnostics store safe metadata only. Tokens, headers, payloads, and secrets are never persisted.": (
        "Диагностика подключения хранит только безопасные метаданные. "
        "Токены, заголовки, payload и секреты никогда не сохраняются."
    ),
    "Auth header for MARS operators:": "Заголовок auth для операторов MARS:",
    "Current Safety State": "Текущее состояние безопасности",
    "Schema valid option": "Опция schema valid",
    "yes": "да",
    "Token created at UTC": "Токен создан (UTC)",
    "Token revoked at UTC": "Токен отозван (UTC)",
    "Bridge": "Мост",
    "Summary": "Сводка",
}

pot_path = plugin / "languages" / "metacode-wpilot.pot"
po_path = plugin / "languages" / "metacode-wpilot-ru_RU.po"
mo_path = plugin / "languages" / "metacode-wpilot-ru_RU.mo"

pot = polib.pofile(str(pot_path))
existing_pot = {e.msgid for e in pot}
for msgid, ref in sorted(entries.items(), key=lambda x: x[0].lower()):
    if msgid not in existing_pot:
        pot.append(polib.POEntry(msgid=msgid, occurrences=[(ref, "")]))

pot.metadata["POT-Creation-Date"] = "2026-06-19 18:00+0000"
pot.save(str(pot_path))

po = polib.pofile(str(po_path))
existing_po = {e.msgid for e in po}
for msgid, ref in sorted(entries.items(), key=lambda x: x[0].lower()):
    if msgid not in existing_po:
        po.append(
            polib.POEntry(
                msgid=msgid,
                msgstr=ru_map.get(msgid, msgid),
                occurrences=[(ref, "")],
            )
        )

for e in po:
    if e.msgid in ru_map and (not e.msgstr or e.msgstr == e.msgid):
        e.msgstr = ru_map[e.msgid]

po.save(str(po_path))
po.save_as_mofile(str(mo_path))

print(f"POT entries: {len(pot)}")
print(f"PO entries: {len(po)}")
print(f"MO written: {mo_path}")
