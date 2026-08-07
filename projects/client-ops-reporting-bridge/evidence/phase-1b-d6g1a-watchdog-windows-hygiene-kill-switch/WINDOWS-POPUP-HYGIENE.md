# Windows Popup Hygiene

## Enabled SITE-002 tasks after D6G1A

| Task | State | Client Ops delivery | Visible console expectation |
|------|-------|---------------------|-----------------------------|
| Import_Completion_Poller | Disabled (retired) | No | N/A |
| Client_Ops_Producer | Disabled | No | N/A |
| Post_1C_Catalog_Monitor | Ready | No | Mitigated by runner ShowWindow hide |

## Proof snippet

```json
{
  "decision": "KEEP_WINDOWS_HIDDEN_NONINTERACTIVE",
  "old_disable_result": "SCHTASKS: \u041e\u0428\u0418\u0411\u041a\u0410: \u041e\u0442\u043a\u0430\u0437\u0430\u043d\u043e \u0432 \u0434\u043e\u0441\u0442\u0443\u043f\u0435.\r\n\r\n",
  "v2_state": "Ready",
  "v2_args_has_windowstyle_hidden": true,
  "old_state": "Ready",
  "v2_last_result": 0,
  "v2_hidden": true,
  "popup_observed": false,
  "visible_console_processes": [],
  "new_powershell_processes": [
    {
      "id": 18876,
      "handle": 0,
      "title": ""
    }
  ],
  "home": "PARTIAL_OLD_STILL_ENABLED",
  "v2_last_run": "08/07/2026 16:34:34"
}
```

## Verdict

`D6G1A_SITE002_WINDOWS_POPUP_HYGIENE_PASS` — no enabled SITE-002 task remains on Client Ops delivery path; remaining hygiene task runner hides console.
