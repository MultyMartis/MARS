<?php
/**
 * SITE-002 admin model — bridges to canonical MARS 1C runner (no secrets in responses).
 */
class ModelToolMars1cExchange extends Model {
    private function storageRoot() {
        // DIR_STORAGE is OpenCart storage root.
        return rtrim(DIR_STORAGE, '/\\');
    }

    private function paths() {
        $root = dirname($this->storageRoot()); // app root (parent of storage)
        // On Beget layout: storage and public_html are siblings under app root.
        return array(
            'current' => $this->storageRoot() . '/mars-tools/cron/current-run.json',
            'lock' => $this->storageRoot() . '/mars-tools/cron/mars_1c_import.lock',
            'wrapper' => $this->storageRoot() . '/mars-tools/cron/mars_1c_import_wrapper.php',
            'local_config' => $this->storageRoot() . '/mars-tools/cron/mars_1c_wrapper.local.php',
            'reports' => $this->storageRoot() . '/mars-tools/cron/reports',
            'app_root' => $root,
        );
    }

    private function readJson($path) {
        if (!is_file($path)) {
            return null;
        }
        $raw = file_get_contents($path);
        $data = json_decode($raw, true);
        return is_array($data) ? $data : null;
    }

    /**
     * Read-only Client Ops outbound dispatch kill-switch state (no secrets).
     * @return array{enabled:bool,ui:string,source_key:?string}
     */
    private function readDispatchKillSwitchState() {
        $paths = $this->paths();
        $enabled = true;
        $sourceKey = null;
        if (is_file($paths['local_config'])) {
            /** @noinspection PhpIncludeInspection */
            $local = include $paths['local_config'];
            if (is_array($local)) {
                foreach (array('CLIENT_OPS_DISPATCH_ENABLED', 'client_ops_dispatch_enabled', 'server_dispatch_enabled') as $key) {
                    if (!array_key_exists($key, $local)) {
                        continue;
                    }
                    $sourceKey = $key;
                    $v = $local[$key];
                    if (is_bool($v)) {
                        $enabled = $v;
                    } elseif (is_int($v) || is_float($v)) {
                        $enabled = ((int) $v) !== 0;
                    } elseif (is_string($v)) {
                        $n = strtolower(trim($v));
                        if (in_array($n, array('0', 'false', 'no', 'off', 'disabled'), true)) {
                            $enabled = false;
                        } elseif (in_array($n, array('1', 'true', 'yes', 'on', 'enabled'), true)) {
                            $enabled = true;
                        }
                    }
                    break;
                }
            }
        }
        return array(
            'enabled' => $enabled,
            'ui' => $enabled ? 'Включены' : 'Отключены',
            'source_key' => $sourceKey,
        );
    }

    public function getPublicStatus() {
        $paths = $this->paths();
        $state = $this->readJson($paths['current']);
        $lockRaw = is_file($paths['lock']) ? trim((string)file_get_contents($paths['lock'])) : '';
        $lock = $lockRaw !== '' ? (json_decode($lockRaw, true) ?: array('locked' => true)) : array('locked' => false);
        if ($lockRaw !== '' && empty($lock['run_id'])) {
            $lock = array('locked' => true);
        } elseif ($lockRaw !== '') {
            $lock['locked'] = true;
        }

        $ui = 'Не запущен';
        if (is_array($state)) {
            $ui = isset($state['ui_status']) ? $state['ui_status'] : $ui;
        }

        $active = !empty($lock['locked']) && empty($state['final_status']);
        if ($active && is_array($state) && empty($state['final_status'])) {
            $ui = 'Выполняется';
        }

        $dispatchRaw = is_array($state) ? ($state['report_dispatch_status'] ?? null) : null;
        $dispatchUi = is_array($state) ? ($state['report_dispatch_ui'] ?? null) : null;
        if ($dispatchUi === null || $dispatchUi === '') {
            switch ((string) $dispatchRaw) {
                case 'SENT':
                case 'ALREADY_DISPATCHED':
                case 'DELIVERED':
                    $dispatchUi = 'Отправлен';
                    break;
                case 'SENDING':
                    $dispatchUi = 'Отправляется';
                    break;
                case 'FAILED_RETRYABLE':
                case 'FAILED_FINAL':
                    $dispatchUi = 'Ошибка отправки';
                    break;
                case 'PENDING':
                case 'QUEUED':
                    $dispatchUi = 'Ожидает отправки';
                    break;
                case 'BLOCKED_BY_KILL_SWITCH':
                case 'SERVER_DISPATCH_DISABLED':
                    $dispatchUi = 'Отключено (kill switch)';
                    break;
                default:
                    $dispatchUi = $dispatchRaw;
            }
        }

        $kill = $this->readDispatchKillSwitchState();

        return array(
            'ok' => true,
            'ui_status' => $ui,
            'run_id' => is_array($state) ? ($state['run_id'] ?? null) : null,
            'trigger_source' => is_array($state) ? ($state['trigger_source'] ?? null) : null,
            'requested_at' => is_array($state) ? ($state['requested_at'] ?? null) : null,
            'started_at' => is_array($state) ? ($state['started_at'] ?? null) : null,
            'completed_at' => is_array($state) ? ($state['completed_at'] ?? null) : null,
            'current_phase' => is_array($state) ? ($state['current_phase'] ?? null) : null,
            'catalog_result' => is_array($state) && isset($state['catalog_phase_result']['status']) ? $state['catalog_phase_result']['status'] : null,
            'offers_result' => is_array($state) && isset($state['offers_phase_result']['status']) ? $state['offers_phase_result']['status'] : null,
            'final_status' => is_array($state) ? ($state['final_status'] ?? null) : null,
            'report_dispatch_status' => $dispatchRaw,
            'report_dispatch_ui' => $dispatchUi,
            'client_ops_dispatch_enabled' => !empty($kill['enabled']),
            'client_ops_dispatch_ui' => $kill['ui'],
            'sanitized_error_summary' => is_array($state) ? ($state['sanitized_error_summary'] ?? null) : null,
            'txt_report' => is_array($state) ? ($state['txt_report_path'] ?? null) : null,
            'import_active' => $active,
            'elapsed_seconds' => ($active && !empty($state['started_at'])) ? max(0, time() - strtotime($state['started_at'])) : null,
        );
    }

    public function enqueueManualImport() {
        $status = $this->getPublicStatus();
        if (!empty($status['import_active'])) {
            return array(
                'ok' => false,
                'accepted' => false,
                'error' => 'Импорт уже выполняется',
                'run_id' => $status['run_id'],
                'started_at' => $status['started_at'],
                'current_phase' => $status['current_phase'],
            );
        }

        $paths = $this->paths();
        $wrapper = $paths['wrapper'];
        if (!is_file($wrapper)) {
            return array('ok' => false, 'accepted' => false, 'error' => 'Runner unavailable');
        }

        $php = (defined('PHP_BINARY') && PHP_BINARY) ? PHP_BINARY : 'php';
        $cmd = escapeshellarg($php) . ' ' . escapeshellarg($wrapper) . ' --enqueue --trigger=ADMIN_MANUAL';
        $output = array();
        $code = 0;
        @exec($cmd . ' 2>&1', $output, $code);
        $joined = trim(implode("\n", $output));
        $json = json_decode($joined, true);
        if (!is_array($json)) {
            // Try last JSON object in output
            if (preg_match('/\{[\s\S]*\}\s*$/', $joined, $m)) {
                $json = json_decode($m[0], true);
            }
        }
        if (!is_array($json)) {
            return array('ok' => false, 'accepted' => false, 'error' => 'Не удалось поставить импорт в очередь');
        }
        if (empty($json['accepted'])) {
            return array(
                'ok' => false,
                'accepted' => false,
                'error' => isset($json['error']) ? $json['error'] : 'Импорт уже выполняется',
                'run_id' => isset($json['lock']['run_id']) ? $json['lock']['run_id'] : (isset($json['current_run']['run_id']) ? $json['current_run']['run_id'] : null),
                'started_at' => isset($json['current_run']['started_at']) ? $json['current_run']['started_at'] : null,
                'current_phase' => isset($json['current_run']['current_phase']) ? $json['current_run']['current_phase'] : null,
            );
        }
        return array(
            'ok' => true,
            'accepted' => true,
            'run_id' => $json['run_id'],
            'ui_status' => isset($json['ui_status']) ? $json['ui_status'] : 'Ожидает запуска',
            'trigger_source' => 'ADMIN_MANUAL',
            'message' => 'Импорт принят в очередь',
        );
    }
}
