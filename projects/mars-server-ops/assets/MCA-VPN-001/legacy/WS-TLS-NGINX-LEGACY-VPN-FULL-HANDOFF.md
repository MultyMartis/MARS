---
MARS Server Ops — Legacy Source Archive
Source: Legacy Web-GPT chat ""WS + TLS + nginx""
Imported from: X:\AI MARS STORAGE\incoming\MARS-SERVER-OPS-LEGACY-VPN-FULL-HANDOFF.md
Import date: 2026-08-25
Source classification: SANITIZED HISTORICAL HANDOFF (LEGACY WEB-GPT KNOWLEDGE)
Live-state authority: NO — current facts require read-only reconciliation against Server A
Secrets: Sanitized — no secret values should be present; verify defensively before Git commit
Do not convert SAFE UNKNOWN into facts; do not promote historical state to current production truth
---
REPORT — WS + TLS + NGINX LEGACY VPN FULL KNOWLEDGE HANDOFF
1. Executive Verdict

Overall status: HANDOFF COMPLETE WITH GAPS.

Этот чат содержит достаточно подтверждённой информации, чтобы:

передать текущий VPN Server A в MARS Server Ops & VPS Forge;
не потерять историю аварии 3X-UI;
зафиксировать known-good состояние панели;
сохранить сведения о существующих backup;
сформировать безопасную стратегию Server B;
не повторить ошибочные диагностические действия;
продолжить проект уже через MARS с live read-only intake.

Ключевой вывод: текущий VPS — отдельный VPN-сервер. n8n и прочие приложения находятся на другом VEESP VPS. nginx/WS/TLS masking-контур на отдельном сервере обсуждался как будущее решение и не должен ошибочно считаться уже развёрнутым на Server A.

Также важная коррекция старых сообщений этого чата: архив, который назывался mca-gate-full-..., не является подтверждённым full-server backup Ubuntu. Команда, которой он создавался, архивировала выбранные VPN/3X-UI/Xray/certificate paths. Полный bare/server filesystem backup в доступной истории не доказан как созданный.

2. Source / Confidence Boundary

Используются только сведения из доступной истории этого разговора и связанного текущего контекста. Web research не выполнялся, к VPS/VEESP/DNS/3X-UI подключения не выполнялись.

Классификация:

Статус	Значение
CONFIRMED CURRENT	Последнее подтверждённое рабочее состояние
CONFIRMED HISTORICAL	Реально наблюдалось, но позднее могло измениться
PLANNED / NOT IMPLEMENTED	Обсуждалось, но применение не доказано
SUPERSEDED	Заменено более поздним решением
FAILED / ABANDONED	Не сработало или от решения отказались
SAFE UNKNOWN	Надёжных данных нет

Confidence:

HIGH — непосредственно подтверждено действиями/скриншотами/результатом.
MEDIUM — хорошо следует из истории, но live state не проверялся сейчас.
LOW — фрагментарное свидетельство.

Особенно важно: часть предыдущих ответов ассистента содержала слишком уверенные выводы. В этом handoff они не принимаются за факт без подтверждения действиями пользователя.

3. Current VPN Server Passport
Identity
Параметр	Значение	Статус	Confidence
Logical ID	MCA-VPN-001	Принято как рабочее обозначение	HIGH
Provider	VEESP	CONFIRMED CURRENT	HIGH
Purpose	Отдельный VPN VPS	CONFIRMED CURRENT	HIGH
Hostname	wsp-cloud	CONFIRMED HISTORICAL/CURRENT	HIGH
Domain	wsp-cloud.com	CONFIRMED CURRENT	HIGH
IPv4	<SERVER_IP>	CONFIRMED CURRENT, значение redacted	HIGH
OS	Ubuntu 22.04.5 LTS	CONFIRMED CURRENT по inventory	HIGH
Virtualization	KVM	CONFIRMED CURRENT	HIGH
CPU	1 vCPU, host CPU family Xeon Gold 6248	CONFIRMED CURRENT	HIGH
RAM	~1 GB	CONFIRMED CURRENT	HIGH
Disk	~20 GB	CONFIRMED CURRENT	HIGH
SSH	TCP/22 использовался для WinSCP/SFTP plan	CONFIRMED HISTORICAL	MEDIUM
Root administration	использовался root	CONFIRMED CURRENT	HIGH
Separation from other infrastructure

CONFIRMED CURRENT — HIGH

Server A предназначен именно для VPN.

Отдельный второй VEESP VPS уже существует для:

n8n;
связанных Telegram/automation компонентов;
других приложений.

Его нельзя смешивать с MCA-VPN-001.

PLANNED / NOT IMPLEMENTED — HIGH

Для будущей конструкции:

WS + TLS + nginx

оператор решил заказать ещё один отдельный VPS, не трогая:

текущий VPN VPS;
существующий n8n VPS.
Current VPN software

Последнее известное:

3X-UI;
Xray;
SQLite database 3X-UI;
TLS certificates;
Reality;
systemd service x-ui.

3X-UI version была идентифицирована как 3.4.1 после обновления/аварии.

Status: CONFIRMED HISTORICAL, confidence MEDIUM-HIGH.

Xray в логах запускался как:

Xray 26.6.22 started

Status: CONFIRMED HISTORICAL, confidence HIGH.

3X-UI panel

Known-good после ремонта:

Protocol: HTTPS
Port: 5928
Base path: <3XUI_PANEL_PATH>
URL: https://wsp-cloud.com:5928/<3XUI_PANEL_PATH>/

Полный URL намеренно не выводится: base path фактически является частью защиты панели.

Status: CONFIRMED CURRENT, confidence HIGH.

Other observed listeners during incident

До восстановления старых настроек в логах наблюдалось:

Web server running HTTPS on [::]:443
Sub server running HTTPS on [::]:2096

Это историческое аварийное/переходное состояние, а не доказанная current topology.

Status: CONFIRMED HISTORICAL.

Docker

Для MCA-VPN-001 использование Docker как части VPN runtime не подтверждено.

Существовал файл:

/root/docker_list.txt

но это само по себе не доказывает, что текущий VPN работает через Docker.

Status: SAFE UNKNOWN.

MTProto

В /root наблюдался:

/root/mtproto_backup.json

Но актуальное назначение/использование MTProto на этом сервере не восстановлено.

Status: SAFE UNKNOWN.

4. Network / Traffic Architecture
Last known working Server A

Из доступной истории наиболее надёжно следует такая схема:

VPN client
    |
    | encrypted VPN connection
    v
<SERVER_IP> / wsp-cloud.com
    |
    v
Xray / 3X-UI managed inbound
    |
    | VLESS / REALITY
    v
Xray
    |
    v
Internet

Reality явно фигурировал как рабочая VPN-технология.

VLESS фигурировал в созданной эксплуатационной документации как текущая технология:

VLESS
REALITY
TCP
Vision

Confidence для полного набора VLESS + REALITY + TCP + Vision: MEDIUM, поскольку документ создавался на основе предыдущего inventory/истории, но raw inbound dump в доступном контексте отсутствует.

3X-UI panel path

Отдельный management traffic:

Browser
   |
   | HTTPS :5928
   v
wsp-cloud.com
   |
   v
3X-UI built-in web server
   |
   v
<3XUI_PANEL_PATH>

Нет надёжного evidence, что nginx сейчас стоит перед 3X-UI.

nginx / WS architecture

Текущий подтверждённый operator decision:

будущий nginx должен жить на отдельном VPS.

Следовательно:

Client
→ nginx
→ TLS
→ WebSocket
→ Xray

нельзя считать текущей архитектурой Server A.

Это:

PLANNED / NOT IMPLEMENTED — HIGH.

Evolution
CURRENT/LEGACY VPN
VLESS/Reality → Xray → Internet
         +
3X-UI direct management endpoint

              ↓ future plan

SEPARATE WEB MASK VPS
TLS + nginx + WS masking layer

              ↓ multi-region plan

independent VPN / mask / geo fallback nodes
Ports

Подтверждено:

5928/TCP — current known-good 3X-UI panel.
443/TCP — наблюдался 3X-UI web server во время проблемного состояния.
2096/TCP — наблюдался 3X-UI sub server во время проблемного состояния.
22/TCP — SSH/SFTP administration, MEDIUM.

Точный Reality/VLESS inbound port: SAFE UNKNOWN.

5. nginx
Current Server A

SAFE UNKNOWN / likely not part of current VPN path.

В доступной поздней истории оператор специально уточнил:

"будущий nginx; — тут да, для него я бы отдельный сервак сделал"

и:

"под всю конструкцию WS + TLS + nginx просто закажу на VEESP ещё один сервер. там где ЭТОТ VPN и где n8n — не трогаем."

Поэтому MARS не должен импортировать nginx как confirmed-current компонент MCA-VPN-001.

Planned role

PLANNED / NOT IMPLEMENTED

Предполагался отдельный web-mask contour:

Internet
   ↓
domain
   ↓
nginx
   ↓
TLS
   ↓
WebSocket
   ↓
Xray

Цель:

отдельная маскировочная transport-схема;
независимость от основного Reality/VPN узла;
диверсификация блокировочных признаков;
не вмешиваться в работающий Server A.
Known nginx configuration

Точные:

sites-available;
sites-enabled;
proxy_pass;
WebSocket path;
upstream port;
headers;
ACME location;
nginx logs;

из доступной истории надёжно не восстанавливаются.

Status: SAFE UNKNOWN.

MARS не должен генерировать legacy nginx config из предположений.

6. TLS / Certificates
Confirmed filesystem

При создании VPN backup архивировались:

/etc/letsencrypt
/root/cert

Это подтверждает наличие certificate material.

Status: CONFIRMED CURRENT/HISTORICAL — HIGH.

Panel HTTPS

3X-UI работал через HTTPS.

Known-good management URL после ремонта:

https://wsp-cloud.com:5928/<3XUI_PANEL_PATH>/

Status: CONFIRMED CURRENT — HIGH.

CA

Наличие /etc/letsencrypt сильно указывает на Let's Encrypt.

Status: CONFIRMED HISTORICAL — MEDIUM-HIGH.

certbot

Точный способ issuance/renewal:

SAFE UNKNOWN.

Нельзя автоматически утверждать:

standalone certbot;
nginx plugin;
webroot;
DNS challenge;
exact renewal timer.
Certificate locations

Known:

/etc/letsencrypt/
/root/cert/

Private keys внутри этих каталогов являются секретами:

<TLS_PRIVATE_KEY>

На Server B их не копировать как identity. Выпустить новый сертификат для нового домена.

Renewal

Current auto-renew mechanism:

SAFE UNKNOWN.

Перед Server B должен быть read-only verification:

certificate issuer;
expiry;
renewal mechanism;
timer/cron;
certificate references in x-ui settings.
7. 3X-UI / Xray / VPN Runtime
7.1 3X-UI
Installation

Known install root:

/usr/local/x-ui

Database:

/etc/x-ui/x-ui.db

Service/runtime управлялся через:

x-ui
systemctl
Version

Last identified:

3X-UI 3.4.1

CONFIRMED HISTORICAL — MEDIUM-HIGH.

Panel

Known-good:

HTTPS
Port 5928
Base Path <3XUI_PANEL_PATH>

Panel credentials:

<3XUI_ADMIN_LOGIN>
<3XUI_ADMIN_PASSWORD>

Не выводятся и не восстанавливаются.

Database

SQLite table settings была непосредственно проверена:

sqlite3 /etc/x-ui/x-ui.db ".tables"
sqlite3 /etc/x-ui/x-ui.db ".schema settings"

База читалась нормально.

Во время ремонта были изменены:

webPort
webBasePath

на known-good historical values.

Service logs

Рабочая команда:

x-ui log

В логах после запуска не было очевидной fatal panel error.

Наблюдалось:

Web server running HTTPS ...
Sub server running HTTPS ...
Xray ... started
Restart

Known-used:

systemctl restart x-ui

После возврата DB settings и restart панель заработала.

Critical warning

Нельзя без необходимости останавливать x-ui/связанные runtime components на единственном рабочем VPN VPS, через который оператор может зависеть от сети.

Во время диагностики одна из ранее предложенных команд привела к падению VPN, после чего оператору пришлось входить через аварийную VEESP browser console и перезагружать сервер.

Это должно стать hard operational rule для MARS.

7.2 Xray

Observed:

Xray 26.6.22 started

Install/runtime files присутствовали под:

/usr/local/x-ui/bin/

и backup включал:

/etc/xray

Configuration authority может быть 3X-UI-generated, а не /etc/xray как единственный runtime source.

Status: SAFE UNKNOWN для exact config authority.

Protocols

Supported by historical evidence:

VLESS — MEDIUM;
REALITY — HIGH/MEDIUM;
TCP — MEDIUM;
Vision — MEDIUM.

VMess: SAFE UNKNOWN.

Trojan: SAFE UNKNOWN.

WebSocket on Server A: SAFE UNKNOWN / not confirmed current.

Reality secrets

Существовали/требовались:

<XUI_CLIENT_UUID>
<REALITY_PRIVATE_KEY>
<REALITY_PUBLIC_KEY>
<REALITY_SHORT_ID>
<REALITY_SNI>
<REALITY_TARGET>

Private values не выводятся.

Для Server B должна генерироваться новая независимая Reality identity.

8. Client Compatibility
Windows

v2rayN — реально использовался.

Оператор после переустановки Windows отмечал проблемы самого клиента:

после reboot приложение некорректно восстанавливало ожидаемое состояние;
startup/minimize behavior был неудобным;
TUN после запуска требовал elevation;
первый enable TUN приводил к UAC, после чего TUN снова оказывался выключенным;
требовалось включить TUN второй раз.

Это стало причиной поиска альтернатив v2rayN.

Status: CONFIRMED HISTORICAL — HIGH.

Android

В созданной документации фигурировал:

v2rayNG

Confidence: MEDIUM.

Client requirement for Server B

APPROVED / INTENDED — HIGH

Клиентские приложения должны иметь:

Server A profile
Server B profile

и позволять вручную переключаться между ними.

Server B:

independent IP;
independent domain;
independent credentials;
independent VPN secrets;
independent certificates.

Failure Server A не должен затрагивать Server B.

Subscription format

Exact subscription URI/token:

SAFE UNKNOWN.

Любой subscription secret:

<SUBSCRIPTION_SECRET>

должен быть новым для Server B.

9. Filesystem Map
Path	Purpose	Backup required	Secrets	State
/usr/local/x-ui	3X-UI runtime/binaries/Xray assets	YES	Possible	CONFIRMED
/usr/local/x-ui/x-ui	3X-UI binary	YES	No direct credential expected	CONFIRMED
/usr/local/x-ui/bin/	Xray/runtime binaries	Useful	Possible config adjacency	CONFIRMED
/etc/x-ui/	3X-UI persistent data	YES	YES	CONFIRMED
/etc/x-ui/x-ui.db	Main SQLite DB	CRITICAL	YES	CONFIRMED
/etc/xray/	Xray-related configuration	YES	YES possible	CONFIRMED
/etc/letsencrypt/	Let's Encrypt certificates/state	YES	YES private keys	CONFIRMED
/root/cert/	certificate material	YES	YES	CONFIRMED
/root/MCA/	MCA operational structure	YES	Mixed	CONFIRMED
/root/MCA/backups/vpn/	VPN backups	YES/off-server	YES	CONFIRMED
/root/MCA/backups/server/	intended server backup area	YES	YES	CONFIRMED directory, archive semantics uncertain
/root/MCA/docs/	documentation	YES	Normally no	CONFIRMED
/root/MCA/inventory/	machine inventory	YES	May contain secrets	CONFIRMED
/root/MCA/inventory/xui-db.sql	SQLite dump	CRITICAL	YES	CONFIRMED
/root/MCA/scripts/	helper scripts	YES	Review	CONFIRMED
/root/MCA/secrets/	intended secret documentation	YES encrypted/off-server	YES	PLANNED/likely created
/root/mca-backups/	former backup location	Historical	YES	SUPERSEDED by /root/MCA/...
/root/3xui_full_backup.tar.gz	historical backup before move	Critical historical	YES	CONFIRMED HISTORICAL
/root/backup_3xui/	historical unpacked/working backup	Potentially	YES	CONFIRMED HISTORICAL
/root/xui-repair-backup/	temporary repair backup	No after verified replacement	YES	deletion approved
/root/docker_list.txt	historical inventory artifact	Optional	Low	CONFIRMED HISTORICAL
/root/mtproto_backup.json	MTProto-related backup artifact	Unknown	likely YES	CONFIRMED HISTORICAL

Important: xui-db.sql must be treated as a secret-bearing file because database dumps can contain client UUIDs, panel settings and other credentials.

10. Backup State
10.1 Historical backup

A pre-existing archive:

3xui_full_backup.tar.gz

was present locally and/or server-side.

User inspected its contents and specifically noted that it did not contain a /usr/local/x-ui/web directory, despite the web panel having worked when that backup was made and for a long period afterward.

This became important evidence disproving the erroneous hypothesis:

missing /usr/local/x-ui/web caused panel 404.

Status:

CONFIRMED HISTORICAL — HIGH.

This archive was intentionally preserved.

10.2 Temporary repair backup

During panel repair existed:

/root/xui-repair-backup

After successful recovery and newer backups, deletion was approved:

rm -rf /root/xui-repair-backup

Whether command was actually executed is not explicitly shown afterward.

Status: SAFE UNKNOWN final existence.

10.3 New VPN/service backup

A new archive was created approximately as:

mca-gate-full-2026-06-27-1845.tar.gz

The exact date embedded in filename is historical filesystem evidence; do not infer current calendar from it.

Creation command was effectively:

mkdir -p /root/mca-backups && tar --exclude='/root/mca-backups/*.tar.gz' -czpf /root/mca-backups/mca-gate-full-$(date +%F-%H%M).tar.gz /usr/local/x-ui /etc/xray /etc/x-ui /etc/letsencrypt /root/cert 2>/dev/null

Contents:

/usr/local/x-ui
/etc/xray
/etc/x-ui
/etc/letsencrypt
/root/cert

Archive size observed around:

80 MB
Critical correction

Despite the filename and earlier wording, this is NOT a full Ubuntu/server backup.

It is a VPN/application/config/certificate backup.

Status:

CONFIRMED CURRENT/HISTORICAL — HIGH.

10.4 Backup relocation

Structure created:

/root/MCA/
├── backups/
│   ├── server/
│   └── vpn/
├── docs/
├── inventory/
├── recovery/
└── scripts/

Commands used included:

mkdir -p /root/MCA/{backups/{server,vpn},docs,inventory,recovery,scripts}

and migration approximately:

mv /root/3xui_full_backup.tar.gz /root/MCA/backups/vpn/ && mv /root/mca-backups/*.tar.gz /root/MCA/backups/server/

Semantic problem: the second command moved mca-gate-full... into backups/server, although its contents were only VPN/application paths.

Therefore:

/root/MCA/backups/server/mca-gate-full-...

must not be trusted as a full-server backup merely because of directory placement.

10.5 Local copy

WinSCP was configured/planned via SFTP for local download.

User later had WinSCP access and inspected server files.

The new archive was intended to be downloaded locally.

Confidence that a local copy actually exists: MEDIUM, because the workflow strongly indicates it, but explicit final checksum confirmation is absent.

10.6 Checksums

SHA256/checksum generation was discussed for future MCA Toolkit but not proven implemented.

Status: PLANNED / NOT IMPLEMENTED.

10.7 Encryption

Backup encryption:

SAFE UNKNOWN / no evidence implemented.

10.8 True full server backup

A real archive of essentially the entire filesystem was discussed:

/
excluding:
  /proc
  /sys
  /dev
  /run
  /tmp
  /mnt
  /media
  /lost+found
  /swapfile

However, no successful creation/verification of such an archive appears in the accessible history.

Therefore:

FULL SERVER BACKUP = NOT CONFIRMED.

This is one of the most important handoff facts.

11. Restore / Disaster Recovery State
ACTUALLY TESTED RESTORE

A complete:

blank VPS
→ restore archive
→ working 3X-UI/Xray
→ client connects

restore was not tested.

Actually tested repair

What was demonstrated:

3X-UI database could be read with SQLite.
settings table existed.
Known-good panel values could be written directly.
systemctl restart x-ui successfully reloaded runtime.
Panel became reachable again on old port/path.
VPN continued functioning afterward.

This is a partial configuration recovery proof, not disaster recovery proof.

Planned restore

Conceptual recovery procedure documented:

new VPS
→ Ubuntu
→ SSH
→ upload backup
→ restore files
→ verify x-ui
→ verify Xray
→ verify certificates
→ verify firewall
→ verify panel
→ verify VPN client
→ create fresh backup

Status: PLANNED / NOT TESTED.

Important restore caveats

Do not assume extracting:

/usr/local/x-ui
/etc/x-ui
/etc/xray
/etc/letsencrypt
/root/cert

alone onto arbitrary new Ubuntu is sufficient.

Missing state could include:

packages;
users/groups;
permissions;
systemd unit differences;
firewall;
sysctl;
networking;
cron/timers;
certificate renewal configuration;
OS dependencies.

These need Server B/MARS validation.

12. Server Build History
Milestone 1 — Dedicated VPN server exists

CONFIRMED HISTORICAL

VEESP VPS used specifically for VPN.

Separate VEESP VPS exists for n8n/automation workloads.

Important durable decision:

do not merge these workloads.

Milestone 2 — VPN runtime established

CONFIRMED HISTORICAL

3X-UI + Xray configured and used successfully.

Reality became part of the VPN setup.

Windows client used v2rayN.

Milestone 3 — Domain/panel established

CONFIRMED HISTORICAL

Domain:

wsp-cloud.com

3X-UI management was historically reachable through HTTPS with a non-default port and secret base path.

Known-good port ultimately recovered:

5928
Milestone 4 — Historical backup created

CONFIRMED HISTORICAL

Archive:

3xui_full_backup.tar.gz

existed before the later incident.

This became forensic evidence during repair.

Milestone 5 — Windows reinstallation

CONFIRMED HISTORICAL

After Windows reinstall:

VPN itself remained a server-side service;
operator initially suspected local-PC side because panel access had worked before reinstall;
v2rayN behavior also became problematic.

This was a reasonable diagnostic clue but ultimately panel 404 required server-side configuration repair.

Milestone 6 — Lost 3X-UI panel access

CONFIRMED HISTORICAL

Remembered URL did not open.

Multiple candidate URLs/paths were tried.

Known historical port 5928 was later rediscovered from operator notes.

Milestone 7 — Panel diagnostics

Checks established:

x-ui running;
Xray running;
HTTPS listener active;
SQLite database readable;
settings table valid;
no obvious fatal error in x-ui log;
absence of /usr/local/x-ui/web was normal for the historical working backup.

Several incorrect hypotheses were eliminated.

Milestone 8 — Serious operational incident

CONFIRMED HISTORICAL

During troubleshooting, an unsafe service/SQL-related action suggested by the assistant caused VPN outage.

Operator lost normal access and had to:

use VEESP browser console;
work through degraded emergency access;
reboot the VPS.

This is the strongest operational lesson in the chat.

Milestone 9 — Correct panel recovery

CONFIRMED HISTORICAL — HIGH

SQLite settings were returned to:

webPort = 5928
webBasePath = <3XUI_PANEL_PATH>

then:

systemctl restart x-ui

After that:

https://wsp-cloud.com:5928/<3XUI_PANEL_PATH>/

worked.

Operator explicitly confirmed:

"заработал"

and noted the panel UI appearance had changed.

Milestone 10 — Backup refresh

CONFIRMED HISTORICAL

Historical backup retained.

Temporary/new earlier archive(s) removed/replaced.

Fresh VPN/application backup created from recovered known-good state.

Milestone 11 — WinSCP/SFTP operations

CONFIRMED HISTORICAL

WinSCP used to inspect/download server files.

Target connection model:

SFTP
Host: wsp-cloud.com or <SERVER_IP>
Port: 22
User: root
Credential: <SSH_PASSWORD_OR_KEY>
Milestone 12 — MCA structure

CONFIRMED HISTORICAL

Created:

/root/MCA/

with backup/docs/inventory/recovery/scripts structure.

Milestone 13 — Inventory

CONFIRMED HISTORICAL

Created /root/MCA/scripts/inventory.sh.

Initial execution failed because script had Windows CRLF:

/bin/bash^M: bad interpreter

Fixed with:

sed -i 's/\r$//' /root/MCA/scripts/inventory.sh

Direct execution remained odd, but:

bash /root/MCA/scripts/inventory.sh

worked.

Generated:

os.txt
kernel.txt
cpu.txt
memory.txt
disks.txt
network.txt
routes.txt
listening-ports.txt
enabled-services.txt
running-services.txt
packages.txt
xui-settings.txt
xui-version.txt
xui-db.sql
status.txt
Milestone 14 — Minimal documentation

CONFIRMED HISTORICAL

Documentation files prepared and user stated they were uploaded to server.

Included:

README.md
SERVER-PASSPORT-v1.md
VPN-SETUP-v1.md
BACKUPS-v1.md
RECOVERY-v1.md
CHANGELOG.md

Later additional documentation/archive was prepared around:

secrets/
TOPOLOGY-v1.md
TODO.md

Exact final upload state of these additional files is SAFE UNKNOWN.

Milestone 15 — Future infrastructure split

APPROVED / INTENDED

Operator chose not to alter current VPN or n8n VPS.

Future WS/TLS/nginx system gets a separate VPS.

Milestone 16 — Multi-region resilience plan

APPROVED / INTENDED

Selected conceptual map:

MAIN
Finland / Netherlands

WEB MASK
France

GEO FALLBACK
UAE / Serbia

Operator preference:

UAE first;
Serbia afterward;
Uzbekistan/Tajikistan considered as possible later alternatives;
political/jurisdiction diversification was part of reasoning.
13. Incident / Troubleshooting History
Incident A — 3X-UI panel inaccessible
Problem

VPN worked, but management panel did not open.

Symptoms

Candidate URLs produced no panel / 404.

Known remembered forms included:

https://wsp-cloud.com/<PANEL_PATH>/
https://wsp-cloud.com:5928/<PANEL_PATH>/
Root cause

Best-established practical root cause:

3X-UI panel settings were no longer on the historical known-good port/base-path combination.

Exact mechanism that changed them is not proven.

Possible association with 3X-UI update existed, but causality is MEDIUM, not absolute.

Fix

Direct SQLite update of:

webPort
webBasePath

followed by:

systemctl restart x-ui
Verification

Browser opened panel successfully.

Prevention

Before any 3X-UI upgrade preserve:

DB;
panel port;
panel base path;
certificate settings;
version;
service state;
known-good client connectivity.
Incident B — Incorrect /usr/local/x-ui/web hypothesis
Problem

Troubleshooting assumed missing web files caused 404.

Evidence disproving it

Historical backup made while panel worked also lacked the expected directory.

Root cause

Diagnostic assumption was wrong.

Fix

Abandon filesystem-web-directory hypothesis.

Prevention

Compare with known-good backup before declaring a missing path abnormal.

Incident C — Service outage during troubleshooting
Problem

A diagnostic/change action interrupted VPN runtime.

Symptoms

VPN dropped and operator lost normal access.

Recovery

VEESP emergency browser console + VPS reboot.

Root cause

Unsafe operational procedure on a production single-access VPN node.

Prevention

Hard rule:

READ-ONLY FIRST.
NO STOP/DISABLE/DB SERVICE MANIPULATION
without explicit impact analysis and recovery path.

Use restart only when justified and operator understands expected interruption.

Incident D — inventory.sh CRLF
Symptoms
/bin/bash^M: bad interpreter
Root cause

Windows CRLF line endings.

Fix
sed -i 's/\r$//' /root/MCA/scripts/inventory.sh

then:

bash /root/MCA/scripts/inventory.sh
Prevention

Server shell scripts must use LF.

Incident E — v2rayN post-Windows-reinstall UX
Symptoms
startup/minimize state unreliable;
TUN requires UAC;
first enable fails to remain enabled;
second enable works.
Root cause

Not established.

Status

Client-side issue; server not proven responsible.

14. Security State
Implemented / observed
HTTPS used for 3X-UI panel.
Non-default panel port 5928.
Secret/non-obvious panel base path.
TLS certificate material present.
Root SSH/SFTP administration used.
Backups contain sensitive credentials and must be protected.
Separate workloads across VPS rather than putting everything on VPN host.
SSH keys

SAFE UNKNOWN.

Root password authentication was considered/used for WinSCP instructions, but actual current authentication policy should not be inferred.

UFW / nftables / iptables

Inventory contains networking/listener information, but exact current firewall state is not reconstructed here.

SAFE UNKNOWN.

fail2ban

SAFE UNKNOWN.

Alternative SSH port

No confirmed alternative. Port 22 was used/planned.

Automatic OS updates

SAFE UNKNOWN.

Panel access restriction

Beyond:

HTTPS;
custom port;
secret path;

no confirmed IP allowlist/VPN-only restriction.

Backup security

Important:

/etc/x-ui/x-ui.db
/root/MCA/inventory/xui-db.sql
/etc/letsencrypt/
/root/cert/
backup archives

must be treated as secret-bearing.

Future Git repository must exclude them.

15. Reusable Commands / Procedures
Read-only system inspection
hostnamectl
uname -a
lscpu
free -h
df -h
ip addr
ip route
ss -tulpn
3X-UI

Logs:

x-ui log

Settings:

x-ui settings

Database tables:

sqlite3 /etc/x-ui/x-ui.db ".tables"

Schema:

sqlite3 /etc/x-ui/x-ui.db ".schema settings"
Restart
systemctl restart x-ui

RISK: causes service interruption. Use only with recovery path.

Direct DB modification

Historical known-good procedure conceptually used:

UPDATE settings SET ... WHERE key='webPort'
UPDATE settings SET ... WHERE key='webBasePath'

HIGH RISK.

Do not blindly reuse. Backup DB first and derive values from current authority.

Logs
x-ui log

When pager opens:

Shift+G

to reach end.

Backup — proven VPN/application scope

Sanitized known-used procedure:

tar -czpf <BACKUP_FILE> /usr/local/x-ui /etc/xray /etc/x-ui /etc/letsencrypt /root/cert

This is NOT full-server backup.

Inspect archive
tar -tf <BACKUP_FILE> | head -30
MCA tree without tree
find /root/MCA | sort
CRLF repair
sed -i 's/\r$//' /root/MCA/scripts/inventory.sh
Run inventory
bash /root/MCA/scripts/inventory.sh
SSH listener check
ss -tlnp | grep :22

Read-only.

HIGH RISK / DESTRUCTIVE

Examples that MARS must classify before execution:

rm -rf ...
systemctl stop x-ui
systemctl disable ...

direct SQLite UPDATE/DELETE;

restoring archive over live filesystem;

replacing certificates;

firewall flush;

network configuration changes;

reboot.

For production VPN these require:

current backup;
emergency console verified;
rollback;
operator confirmation.
16. Hosting / VPS Selection History
Existing provider

VEESP.

CONFIRMED CURRENT — HIGH.

At least two VEESP VPS existed:

VPN server;
n8n/automation server.

A third VEESP VPS was contemplated specifically for WS/TLS/nginx.

VEESP snapshots

Operator believed VEESP probably does not provide disk snapshots.

This was not independently verified.

Status:

SAFE UNKNOWN / NEEDS CURRENT WEB RESEARCH.

Existing VPN tariff

Exact commercial tariff name/price cannot be reliably reconstructed from accessible history.

Resources recovered from inventory:

1 vCPU
~1 GB RAM
~20 GB disk
Upgrade discussion

Operator considered increasing the VEESP tariff to improve performance and storage, while keeping existing VPN configuration.

Exact purchased upgrade/current resources after any upgrade are not proven beyond inventory.

Provider diversification research

A second provider was explicitly desired as a true alternative to VEESP:

if VEESP becomes unavailable, Provider B should have a good chance of remaining independently operational long enough to build another fallback.

Therefore provider diversity is more important than simply buying another VEESP node.

Regional plan

Approved/intended conceptual map:

Role	Location
MAIN	Finland / Netherlands
WEB MASK	France
GEO FALLBACK 1	UAE
GEO FALLBACK 2	Serbia

Additional exploratory possibilities:

Uzbekistan;
Tajikistan.
UAE reasoning

UAE was considered attractive partly because of geopolitical separation/relationship considerations relative to Russia.

No final provider purchase is confirmed.

Serbia reasoning

Operator explicitly considered Serbia politically durable as a fallback jurisdiction.

Again: this is planning reasoning, not a guarantee of network resilience.

Concrete alternative provider

No reliable final non-VEESP provider name can be reconstructed from accessible history.

Status:

SAFE UNKNOWN.

NEEDS CURRENT WEB RESEARCH

All of:

providers;
prices;
tariffs;
availability;
network quality;
AS ownership;
upstream diversity;
abuse policy;
VPN policy;
payment;
UAE/Serbia inventory;
Finland/NL inventory;
France inventory;
Russian reachability;
current regulatory blocking patterns.
17. Future Plans Previously Discussed
APPROVED / INTENDED
A. Preserve Server A

Current VPN remains working and should not be casually modernized.

B. Independent Server B

New VPS:

separate provider preferably;
separate IP;
separate domain;
new SSH identity;
new panel credentials;
new VPN identities;
new certificates;
independent failure domain.
C. Client-side dual profiles

Clients receive:

Server A
Server B

Manual switching initially is acceptable.

D. Separate WS/TLS/nginx node

Do not retrofit it into Server A as the first move.

Create dedicated VPS.

E. Multi-region map
MAIN       Finland / NL
WEB MASK   France
GEO        UAE
GEO        Serbia
F. UAE before Serbia

Explicit operator preference.

G. MCA Infrastructure Pilot

Future MARS project/chat should become canonical agent for:

Linux;
VPS;
Docker;
nginx;
VPN;
Xray;
Reality;
SSH;
backups;
disaster recovery;
monitoring.

This has now effectively evolved into:

MARS Server Ops & VPS Forge.

IDEA
Uzbekistan/Tajikistan fallback;
automated backup;
unified MCA CLI/toolkit;
automatic passport generation;
automated health checks;
Git-based server toolkit.
SUPERSEDED / DEFERRED

Building a sophisticated MCA Server Toolkit manually in this old chat was deferred.

Decision:

first create minimal documentation; later build proper infrastructure through MARS.

18. Server A → Server B Clone Matrix
CLONE AS-IS
Item	Decision
Dedicated VPN-only role	CLONE
Separation from n8n/application workloads	CLONE
3X-UI/Xray management model if still current/recommended	CLONE conceptually
VLESS/Reality compatibility	CLONE
Client compatibility	CLONE
HTTPS panel	CLONE
Backup-before-change discipline	CLONE
Inventory/passport/recovery documentation	CLONE
systemd operational model	CLONE conceptually
Independent local backup	CLONE
Non-default protected panel endpoint	CLONE conceptually
CLONE WITH NEW VALUES
Item	New value required
Public IP	YES
Domain	YES
Hostname	YES
SSH credentials	YES
TLS certificate	YES
Panel credentials	YES
Panel base path	YES
Xray UUID	YES
Reality keypair	YES
Reality ShortID	YES
subscription secrets	YES
backup identity	YES
server-specific DNS	YES
provider metadata	YES
DO NOT CLONE
stale 3X-UI DB wholesale merely to duplicate clients;
old panel path;
old passwords;
TLS private keys;
Reality private key;
temporary repair directories;
old logs;
old package cache;
accidental 443/2096 panel state;
assumptions around /usr/local/x-ui/web;
server-specific network state;
historical troubleshooting hacks;
potentially obsolete version 3.4.1 without research;
existing /etc/letsencrypt identity.
MUST RESEARCH AGAIN
provider;
region;
current Ubuntu LTS choice;
current stable 3X-UI;
current Xray;
current Reality recommendations;
fingerprint/blocking environment;
firewall baseline;
TLS practice;
panel exposure strategy;
WS/nginx relevance;
backup tooling.
19. New Secret / Identity Matrix
Entity	Reuse A?	Generate new B?	Why	Used by
SSH password	NO	YES	independent compromise domain	SSH/SFTP
SSH private key	NO	YES	server independence	SSH
Root credentials	NO	YES	independent security	OS
Hostname	NO	YES	unique identity	OS/DNS
Domain	NO	YES	independent routing	DNS/TLS/VPN
TLS certificate	NO	YES	domain/server identity	HTTPS
TLS private key	NO	YES	never clone identity	TLS
3X-UI admin login	Prefer NO	YES	independent panel	3X-UI
3X-UI password	NO	YES	security	3X-UI
Panel base path	NO	YES	endpoint secrecy	3X-UI
Xray client UUID	Prefer NO	YES	independent credential	VLESS
Reality private key	NO	YES	cryptographic identity	Reality
Reality public key	Derived	YES	paired with new private key	clients
Reality ShortID	NO	YES	independent identity	Reality
Reality SNI	Research/config-specific	Possibly	depends target	Reality
Reality target	Research	Possibly	environment-specific	Reality
WebSocket path	NO if used	YES	independent endpoint	WS/nginx
Subscription secret	NO	YES	credential isolation	clients
Client configs	NO raw clone	Build B profiles	contains new identities	clients
Backup encryption key	NO	YES or managed common vault	risk separation	backups
API tokens	NO	YES	independent service	APIs

Default rule:

Server B gets independent secrets.

20. Recommended Server B Architecture
DERIVED FROM OUR CURRENT WORKING SERVER

Lowest-risk first Server B:

                    ┌───────────────────────────┐
                    │        CLIENT DEVICE      │
                    │                           │
                    │ Profile A     Profile B   │
                    └──────┬─────────────┬──────┘
                           │             │
                           │             │
                    ┌──────▼─────┐ ┌────▼──────┐
                    │ SERVER A   │ │ SERVER B  │
                    │ existing   │ │ new       │
                    │            │ │           │
                    │ 3X-UI      │ │ 3X-UI     │
                    │ Xray       │ │ Xray      │
                    │ VLESS      │ │ VLESS     │
                    │ Reality    │ │ Reality   │
                    └──────┬─────┘ └────┬──────┘
                           │             │
                           └──────┬──────┘
                                  ▼
                              Internet

No dependency:

A ─X─ B

No shared:

DB;
private key;
certificate;
credentials;
filesystem;
control plane.
NEW RECOMMENDATION / NEEDS CURRENT RESEARCH

Before building B:

select genuinely independent provider;
choose jurisdiction/AS/upstream diversity;
verify current stable OS;
verify current 3X-UI/Xray releases;
determine whether Reality remains primary;
determine current blocking/fingerprinting conditions;
establish firewall baseline;
establish backup + restore proof before production;
avoid unnecessary architecture changes.
WS/TLS/nginx

Do not make Server B unnecessarily dependent on the future mask server.

Better failure domains:

VPN-A (Reality)          independent
VPN-B (Reality)          independent
WEB-MASK-FR (WS/TLS)     independent
GEO-UAE                  independent
GEO-RS                   independent

This reflects the operator's resilience objective better than one complex chain.

21. What Must Be Re-Researched Today

Before Server B procurement/build:

VEESP current offerings and limitations.
Independent alternatives to VEESP.
Finland vs Netherlands current network quality.
France VPS for Web Mask.
UAE providers.
Serbia providers.
Uzbekistan/Tajikistan only if still relevant.
AS/upstream/provider ownership relationships.
Current Russian reachability.
Current VPN/proxy blocking patterns.
Chrome fingerprint/TCP-RAW reports mentioned in recent news.
Current Reality resistance/recommendations.
Current WebSocket/TLS viability.
Current 3X-UI stable release.
Current Xray stable release.
Ubuntu 24.04 vs other supported baseline.
Current 3X-UI upgrade/migration behavior.
Current certificate renewal practices.
Provider snapshot/backup availability.
Anti-DDoS.
Traffic limits.
port restrictions.
payment methods.
abuse/VPN policies.
pricing.

Old prices/tariffs must not be reused.

22. Lessons Learned
WHAT WORKED WELL
Keeping VPN on a dedicated VPS.
Maintaining a historical 3X-UI backup.
Remembering/recording old panel port.
Comparing broken state with historical known-good state.
SQLite inspection of 3X-UI DB.
x-ui log.
Restoring only the relevant panel settings.
systemctl restart x-ui after targeted repair.
WinSCP/SFTP for file transfer.
Creating /root/MCA.
Generating inventory.
Preserving documentation outside memory/chat.
WHAT FAILED
Guessing that missing /usr/local/x-ui/web caused the panel failure.
Too many speculative commands before establishing authority.
Treating a VPN-specific archive as "full server backup".
Performing risky runtime changes while operator depended on the same VPN.
Multi-line console instructions despite VEESP console paste limitations.
Windows CRLF shell script.
WHAT WAS FRAGILE
Single active VPN path.
Dependence on browser emergency console during outage.
Panel configuration not initially documented.
No proven bare-metal/full-VPS restore.
Backups without confirmed checksum workflow.
Unknown firewall/security baseline.
v2rayN local startup/TUN behavior.
WHAT SHOULD BE STANDARDIZED

For every MCA/MARS VPS:

SERVER-PASSPORT
INVENTORY
BACKUP-MANIFEST
RECOVERY-GUIDE
CHANGELOG
SECRETS-MANIFEST

Before changes:

PRECHECK
BACKUP
VERIFY BACKUP
CHANGE
SMOKE
ROLLBACK READY
DOCUMENT
WHAT SHOULD NEVER BE REPEATED
stopping the only working VPN service during exploratory diagnostics;
destructive commands without impact classification;
assuming backup scope from filename;
modifying DB before preserving it;
treating plans as deployed state;
assuming nginx/WS exists merely because it was discussed;
printing secrets into reports/Git;
giving multi-line commands for the VEESP emergency console.
WHAT SHOULD BE IMPROVED ON SERVER B
independent provider;
documented emergency access;
fresh secrets;
explicit firewall baseline;
reproducible install;
verified backup manifest;
checksum;
actual restore rehearsal;
client A/B profiles;
documented upgrade procedure;
pre-upgrade panel settings export;
off-server backups.
23. SAFE UNKNOWN / Verification Needed
Missing fact	Why unknown	Later verification
Current VEESP tariff name	not recoverable	provider panel
Current monthly price	stale/not retained	provider panel
Datacenter city/country	not reliably retained	provider panel + IP/ASN
Exact current 3X-UI version	historical 3.4.1 only	read-only CLI/panel
Exact current Xray version	historical 26.6.22	read-only CLI/log
Reality inbound port	secret/config not reproduced	panel/read-only DB
Exact inbound config	not safely reconstructed	3X-UI read-only
Exact outbound config	not retained	3X-UI/Xray inspection
Routing rules	not retained	config inspection
DNS rules	not retained	config inspection
Reality SNI/target	credential/config sensitive	panel/config
Number of clients	not reliably retained	panel
Active client UUIDs	deliberately excluded	panel
Firewall	inventory not parsed here	nft/ufw read-only
fail2ban	not confirmed	systemctl/package inspection
SSH auth policy	not confirmed	sshd effective config
Docker usage on VPN VPS	ambiguous	docker/systemctl
nginx installed?	not current-path confirmed	package/systemctl
certbot renewal	not confirmed	timers/cron
Certificate expiry	dynamic	cert inspection
Full-server backup exists	not proven	archive manifest
Local backup copy current	no checksum confirmation	local storage inspection
Backup integrity	no checksum	tar -t + SHA256
Restore completeness	never tested	future isolated restore drill
/root/xui-repair-backup deletion	command approved, final state unseen	filesystem inspection
MCA extra docs/secrets upload	final state unclear	/root/MCA inspection
VEESP snapshots	operator believed absent	provider research
non-VEESP provider finalist	not recoverable	prior research / redo

No live verification is requested in this handoff.

24. MARS Documentation Recommendations

MARS Server Ops & VPS Forge should import this server as a legacy managed asset, not immediately "normalize" it.

Suggested canonical structure conceptually:

MCA-VPN-001/
├── README.md
├── SERVER-PASSPORT.md
├── CURRENT-STATE.md
├── NETWORK-TOPOLOGY.md
├── VPN-RUNTIME.md
├── BACKUP-MANIFEST.md
├── RECOVERY-RUNBOOK.md
├── INCIDENT-HISTORY.md
├── CHANGELOG.md
├── inventory/
└── secrets.local/

Secrets must remain local/non-Git.

First future MARS intake

Should be read-only.

Capture:

OS;
packages;
service units;
listeners;
network;
firewall;
SSH effective settings;
x-ui version;
Xray version;
sanitized x-ui settings;
certificate metadata;
timers;
backup manifests;
filesystem paths;
hashes;
disk usage.

Then compare live state against this legacy handoff.

Do not modify during intake

Especially:

x-ui DB;
Xray inbound;
firewall;
SSH;
DNS;
certificates;
panel port/path.

Only after current-state freeze should Server B build begin.

25. MARS SERVER OPS — LEGACY VPN KNOWLEDGE IMPORT PACK
PROJECT:
MARS Server Ops & VPS Forge

LEGACY ASSET:
MCA-VPN-001

ROLE:
Dedicated production VPN VPS.

PROVIDER:
VEESP.

SEPARATION RULE:
This VPS is VPN-only.
A separate VEESP VPS hosts n8n/automation-related workloads.
Do not merge them.
Future WS/TLS/nginx masking contour was intended for another dedicated VPS.

SERVER:
Ubuntu 22.04.5 LTS.
KVM.
Last inventory: ~1 vCPU / ~1 GB RAM / ~20 GB disk.
Hostname historically `wsp-cloud`.
Public domain `wsp-cloud.com`.
Public IP intentionally omitted from import pack.

VPN STACK:
3X-UI + Xray.
Historical 3X-UI version: 3.4.1.
Historical Xray log version: 26.6.22.
VLESS/REALITY is the known legacy VPN direction.
TCP/Vision appeared in the generated legacy documentation but should be live-verified.
Current WebSocket on Server A is NOT confirmed.

3X-UI:
Runtime root `/usr/local/x-ui`.
Persistent DB `/etc/x-ui/x-ui.db`.
Known-good panel protocol HTTPS.
Known-good historical/current panel port 5928.
Panel base path exists but is secret-bearing and intentionally omitted.
Do not expose panel credentials/path in Git/docs.

CERTIFICATES:
Certificate material existed under:
`/etc/letsencrypt`
`/root/cert`
Exact renewal mechanism requires live verification.

NGINX:
Do NOT assume nginx is part of Server A current traffic path.
The later operator decision was to put future WS + TLS + nginx on a separate VPS.

KEY INCIDENT:
3X-UI panel stopped opening while VPN/Xray remained operational.
Panel returned 404/no usable UI.
DB was readable and x-ui logs showed web/Xray startup without obvious fatal errors.
A wrong diagnostic hypothesis blamed missing `/usr/local/x-ui/web`; historical working backup proved this directory absence was not the cause.
Known-good old panel port 5928 was recovered from operator records.
Restoring `webPort=5928` and the historical secret `webBasePath` directly in `/etc/x-ui/x-ui.db`, then `systemctl restart x-ui`, restored panel access.
Operator confirmed panel worked afterward and UI appearance had changed.

CRITICAL INCIDENT:
During earlier troubleshooting an unsafe service/SQL-related action interrupted the working VPN.
Operator had to use VEESP emergency browser console and reboot.
Permanent operational rule:
READ-ONLY FIRST.
Never stop/disable the only working VPN runtime during exploratory diagnostics.
Every mutating operation requires impact analysis, emergency access, backup and rollback.

BACKUPS:
Historical `3xui_full_backup.tar.gz` exists/existed and was intentionally preserved.
A newer archive approximately `mca-gate-full-2026-06-27-1845.tar.gz` was created after panel recovery.
Its actual scope is:
`/usr/local/x-ui`
`/etc/xray`
`/etc/x-ui`
`/etc/letsencrypt`
`/root/cert`
It is NOT a proven full Ubuntu/server backup despite previous naming/location.
Do not classify it as bare-server backup.
No complete blank-VPS restore has been proven.

MCA SERVER STRUCTURE:
`/root/MCA/backups/vpn`
`/root/MCA/backups/server`
`/root/MCA/docs`
`/root/MCA/inventory`
`/root/MCA/recovery`
`/root/MCA/scripts`

INVENTORY:
Legacy inventory script generated:
os.txt
kernel.txt
cpu.txt
memory.txt
disks.txt
network.txt
routes.txt
listening-ports.txt
enabled-services.txt
running-services.txt
packages.txt
xui-settings.txt
xui-version.txt
xui-db.sql
status.txt

SECURITY NOTE:
`xui-db.sql`, `x-ui.db`, certificate private keys and backup archives are secret-bearing.
Never commit them.

CLIENTS:
Windows client definitely used v2rayN.
v2rayN had post-Windows-reinstall TUN/startup UX problems.
v2rayNG was recorded for Android but should be verified.
Future clients must carry independent Server A and Server B profiles.

SERVER B OBJECTIVE:
Create independent second VPN VPS.
Prefer a genuinely independent provider/failure domain from VEESP.
New:
IP
domain
hostname
SSH credentials
TLS certificate/private key
3X-UI admin credentials
panel base path
Xray UUID
Reality keypair
Reality ShortID
subscription secrets
client profile.

Do not clone private identities from Server A.

RESILIENCE MAP DISCUSSED:
MAIN: Finland / Netherlands.
WEB MASK: France.
GEO FALLBACK: UAE / Serbia.
Operator intended UAE first, Serbia afterward.
Uzbekistan/Tajikistan were exploratory alternatives.
No final non-VEESP provider purchase is confirmed.

SERVER B PRINCIPLE:
Compatibility and recoverability over novelty.
Do not modernize Server A simply because newer technologies exist.
First reproduce a compatible independent VPN node.
Keep Server A untouched while Server B is built and tested.

RESTORE STATE:
Targeted 3X-UI panel-settings recovery proven.
Full disaster recovery NOT proven.
No verified clean-VPS → restore → working VPN drill.

MARS FIRST ACTION:
Perform read-only live intake and reconcile this legacy handoff against actual Server A.
Do not mutate production during discovery.

RESEARCH REQUIRED:
Current providers/pricing.
VEESP snapshot capabilities.
Finland/NL/France/UAE/Serbia options.
Current 3X-UI.
Current Xray.
Current Reality/WS/TLS blocking environment.
Current OS/security baseline.
Firewall/SSH state.
Certificate renewal.
Backup completeness.
26. Final Handoff Verdict

HANDOFF COMPLETE WITH GAPS — MARS IMPORT READY, LIVE VERIFICATION REQUIRED
