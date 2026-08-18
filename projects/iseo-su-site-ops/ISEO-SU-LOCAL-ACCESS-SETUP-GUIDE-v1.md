# ISEO-SU — Инструкция по заполнению локальных файлов доступа (v1)

**Программа:** ISEO-SU-SITE-OPS  
**Задача:** PHASE 2A — WAVE A REVIEW AND LOCAL ACCESS BOOTSTRAP  
**Аудитория:** оператор (Андрей)  
**Статус:** ACTIVE — заполнение локальных файлов  
**Подключение к production:** **НЕ РАЗРЕШЕНО** этой инструкцией  

Секреты **не** вставлять в чат Cursor, REPORT, Web-GPT или Git-файлы.

---

## 1. Какие файлы открыть

Откройте **оба** файла в обычном текстовом редакторе (Блокнот, VS Code / Cursor как редактор файлов — **без** вставки содержимого в чат):

1. `X:\AI MARS\local\sites\iseo-su-production\site-profile.json`  
   — метаданные без паролей (уже частично заполнены из Wave A).

2. `X:\AI MARS\local\sites\iseo-su-production\secrets.local.md`  
   — **основной файл для паролей и учётных данных** (сейчас пустой шаблон).

Работать нужно в первую очередь с **`secrets.local.md`**.

---

## 2. Важная классификация URL

| URL | Что это |
|-----|---------|
| `https://i-seo.su/wp-admin/` | **Админка WordPress** (не панель Beget) |
| URL панели Beget | **Панель хостинга Beget** — отдельный адрес; пока **SAFE UNKNOWN**, пока вы его не укажете |

Не путать WordPress Admin и Beget.

---

## 3. Поля в `site-profile.json` (метаданные)

| Поле | Что сделать | Откуда взять |
|------|-------------|--------------|
| `site_url` | Уже заполнено | Wave A |
| `environment` | Уже `production` | Wave A |
| `hosting_provider` | Уже `Beget` | Wave A |
| `wordpress_admin_url` | Уже заполнено | Wave A |
| `hosting_panel_url` | Заполнить, когда узнаете URL панели Beget | Браузерная закладка / письмо Beget / после входа в личный кабинет (только URL, без пароля сюда — пароль в secrets) |
| Флаги доступа | Уже `true` по возможностям | Wave A |
| `secret_file_references` | Не менять | Пути на локальные секреты / будущий токен |

В этот JSON **не** вписывать пароли и токены.

---

## 4. Поля в `secrets.local.md` — по разделам

### 4.1 SITE METADATA

| Поле | Обязательно сейчас? | Откуда |
|------|---------------------|--------|
| `site_url` / `environment` / `hosting_provider` / `wordpress_admin_url` | Уже подставлены | Wave A |
| `hosting_panel_url` | Можно оставить пустым | Когда узнаете URL панели Beget |

### 4.2 BEGET CONTROL PANEL

| Поле | Обязательно для будущего A3? | Откуда взять | Можно пустым? |
|------|------------------------------|--------------|---------------|
| `beget_login_or_account_id` | Да, когда будете готовить panel access | Логин / ID аккаунта Beget (личный кабинет) | Да, пока не готовы |
| `beget_password` | Да, для panel access | Пароль Beget (менеджер паролей / ваш сейф) | Да, пока не готовы |
| `beget_2fa_note_without_backup_codes` | Нет | Кратко: «2FA включена / нет» — **без** backup-кодов | Да |
| `beget_panel_url` | Желательно | Точный URL панели Beget | Да, пока UNKNOWN |

### 4.3 FTP OR SFTP

| Поле | Обязательно для будущего A5? | Откуда взять в Beget | Можно пустым? |
|------|------------------------------|----------------------|---------------|
| `ftp_or_sftp_protocol` | Да | Раздел FTP / SSH / «Доступ по FTP» — `ftp` или `sftp` | Да пока |
| `ftp_or_sftp_host` | Да | Хост из карточки FTP Beget | Да пока |
| `ftp_or_sftp_port` | Да | Порт из Beget (часто 21 для FTP / 22 для SFTP — сверьте у себя) | Да пока |
| `ftp_or_sftp_username` | Да | FTP-логин Beget | Да пока |
| `ftp_or_sftp_password` | Да | FTP-пароль Beget | Да пока |
| `ftp_or_sftp_remote_root_or_initial_directory` | Желательно | Домашний / корневой каталог сайта в Beget | Да пока |
| `ftp_passive_mode_if_ftp` | Только для FTP | Настройка клиента / рекомендация Beget (`yes`/`no`) | Да |
| `sftp_host_key_fingerprint_if_known` | Только если SFTP и вы знаете отпечаток | Клиент SFTP при первом подключении | Да (обычно пусто) |

### 4.4 WORDPRESS ADMIN

| Поле | Обязательно для будущего A4? | Откуда | Можно пустым? |
|------|------------------------------|--------|---------------|
| `wordpress_login_url` | Уже заполнено | `https://i-seo.su/wp-admin/` | — |
| `wordpress_username` | Да, для WP admin | Логин WP (лучше **отдельный** MARS-аккаунт — см. §6) | Да пока |
| `wordpress_password` | Да | Пароль WP | Да пока |
| `wordpress_role_note` | Нет | Например: `administrator` | Да |
| `wordpress_dedicated_mars_account` | Нет | `yes` / `no` | Можно оставить `no` до создания отдельного аккаунта |

---

## 5. Что можно оставить пустым

До отдельного чартера подключения можно оставить пустыми:

- URL панели Beget (если ещё не определили);
- любые поля Beget / FTP / WordPress, которые вы ещё не готовы переносить из менеджера паролей;
- 2FA note;
- passive mode;
- SFTP fingerprint;
- role note.

Минимум для **следующего** гейта Phase 2B (проверка **присутствия** файлов и непустых обязательных полей **локально**, без подключения):  
оператор сам решает, какие классы доступа уже заполнены, и сообщает только имена классов (см. §8).

---

## 6. Отдельный WordPress-аккаунт для MARS (рекомендация)

**Рекомендуется** завести отдельного администратора WordPress для MARS.

В **этой** задаче аккаунт **не создавать**.

Позже (отдельный HITL):

- уникальный username, не из личных аккаунтов;
- уникальный пароль;
- роль administrator — только если нужна задачей;
- recovery email под контролем оператора;
- audit-friendly display name;
- удалить или понизить роль, когда аккаунт не нужен.

Итоговый username **не** назначать заранее в документации.

---

## 7. Что никогда не вписывать

- cookies / активные сессии;
- 2FA backup codes;
- пароль почтового ящика (без отдельного чартера);
- содержимое `wp-config.php`;
- пароль БД (без чартера DB);
- посторонние API-токены;
- токен WPilot (отдельный файл и отдельный гейт; сейчас **не** создавать);
- любые секреты в чат Cursor / REPORT / Web-GPT / Git.

---

## 8. Как сохранить и как подтвердить без секретов

1. Сохраните оба файла на диск (`Ctrl+S`).  
2. **Не** присылайте содержимое файлов в чат.  
3. Ответьте в чат **только** так:

```text
ACCESS FILES FILLED
- Beget: yes/no
- FTP/SFTP: yes/no
- WordPress admin: yes/no
- hosting_panel_url known: yes/no
```

Пример:

```text
ACCESS FILES FILLED
- Beget: yes
- FTP/SFTP: yes
- WordPress admin: no
- hosting_panel_url known: no
```

---

## 9. Что это НЕ разрешает

Заполнение файлов **не** даёт права:

- логиниться в Beget / WordPress;
- открывать FTP/SFTP;
- ставить WPilot;
- делать REST;
- трогать production.

Следующий гейт: **PHASE 2B LOCAL ACCESS FILE PRESENCE REVIEW** — локальная проверка наличия/заполненности, **без** сетевого подключения, пока нет отдельного external-access charter.

---

*ISEO-SU LOCAL ACCESS SETUP GUIDE v1 · 2026-07-22 · без секретов в репозитории.*
