# Server Deployment

Operation: `SITE-002-PROD-D6G1A-WATCHDOG-KILL-SWITCH-01`

```json
{
  "operation": "SITE-002-PROD-D6G1A-WATCHDOG-KILL-SWITCH-01",
  "deployed_at": "2026-08-07T09:36:28+00:00",
  "files": [
    {
      "local": "projects/ocpilot/sites/site-002/tools/mars_1c_import_wrapper.php",
      "remote": "/storage/mars-tools/cron/mars_1c_import_wrapper.php",
      "sha256": "fe7532b072c73285bb57378605f2c337a6bfba9122a341c2390d379796f91d7b",
      "verified": true,
      "bytes": 48201
    },
    {
      "local": "projects/ocpilot/sites/site-002/tools/mars_1c_import_run_contract.php",
      "remote": "/storage/mars-tools/cron/mars_1c_import_run_contract.php",
      "sha256": "c67ff78d866ab355a00a455dc65dd2001211c2a00af295a22088fa1bb727b8cc",
      "verified": true,
      "bytes": 10623
    },
    {
      "local": "projects/ocpilot/sites/site-002/tools/mars_1c_completion_dispatch.php",
      "remote": "/storage/mars-tools/cron/mars_1c_completion_dispatch.php",
      "sha256": "3b86aa6868c0f56e4c1c31c4461ce594c5e122a48d653f584b4549cf8b2d135a",
      "verified": true,
      "bytes": 23191
    },
    {
      "local": "projects/ocpilot/sites/site-002/tools/mars_1c_no_import_watchdog.php",
      "remote": "/storage/mars-tools/cron/mars_1c_no_import_watchdog.php",
      "sha256": "f98904ba1830b43734c7e12da26699f22ff13696201d50509880f5e099ee5ce7",
      "verified": true,
      "bytes": 12356
    },
    {
      "local": "projects/ocpilot/sites/site-002/tools/mars_1c_watchdog_http_gateway.php",
      "remote": "/public_html/mars-tools/cron/mars_1c_watchdog_http_gateway.php",
      "sha256": "f15c6023751adfa04bbfabac346033197f53a8bf3733f9c460d4545776b2e004",
      "verified": true,
      "bytes": 1264
    },
    {
      "local": "projects/ocpilot/sites/site-002/tools/mars_1c_d6g1a_offline_regression.php",
      "remote": "/storage/mars-tools/cron/mars_1c_d6g1a_offline_regression.php",
      "sha256": "5b24e4c523f14f3797309ed890edab5de649414c649fa18a1ca98d464e728ca0",
      "verified": true,
      "bytes": 4914
    },
    {
      "local": "projects/ocpilot/sites/site-002/opencart-admin/mars_1c_exchange/admin/model/tool/mars_1c_exchange.php",
      "remote": "/public_html/admin/model/tool/mars_1c_exchange.php",
      "sha256": "e033ee808ccfae9d06877730ec92c8434b00680172babd7ab6ed1469686d6dec",
      "verified": true,
      "bytes": 9441
    },
    {
      "local": "projects/ocpilot/sites/site-002/opencart-admin/mars_1c_exchange/admin/view/template/tool/mars_1c_exchange.twig",
      "remote": "/public_html/admin/view/template/tool/mars_1c_exchange.twig",
      "sha256": "5f00f18d6613ddb5a13b70fa1fde1024855520517e32b59d95257813016c6442",
      "verified": true,
      "bytes": 5343
    }
  ],
  "local_config": {
    "changes": {
      "added_client_ops_key": true,
      "forced_true": false,
      "already_ok": false
    },
    "CLIENT_OPS_DISPATCH_ENABLED": true,
    "server_dispatch_enabled": true
  },
  "modification_php_cleared": 0
}
```

PHP lint (php8.3): PASS  
Offline regression: PASS  
Production kill switch restored: `CLIENT_OPS_DISPATCH_ENABLED=true`
