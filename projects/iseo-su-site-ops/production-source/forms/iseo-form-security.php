<?php
/**
 * Shared server-side validation + anti-spam for i-seo.su public forms.
 * Authoritative; browser validation is UX only.
 */

if (!function_exists("iseo_form_cfg")) {
    function iseo_form_cfg() {
        static $cfg = null;
        if ($cfg === null) {
            $cfg = require __DIR__ . "/iseo-form-config.php";
        }
        return $cfg;
    }
}

if (!function_exists("iseo_form_runtime_dir")) {
    function iseo_form_runtime_dir() {
        $cfg = iseo_form_cfg();
        $dir = $cfg["runtime_dir"];
        if (!is_dir($dir)) {
            @mkdir($dir, 0750, true);
            if (!is_file($dir . "/.htaccess")) {
                @file_put_contents($dir . "/.htaccess", "Deny from all\n");
            }
        }
        return $dir;
    }
}

if (!function_exists("iseo_form_client_ip")) {
    function iseo_form_client_ip() {
        $ip = isset($_SERVER["REMOTE_ADDR"]) ? (string)$_SERVER["REMOTE_ADDR"] : "0.0.0.0";
        return substr($ip, 0, 64);
    }
}

if (!function_exists("iseo_form_ip_hash")) {
    function iseo_form_ip_hash() {
        $cfg = iseo_form_cfg();
        return hash_hmac("sha256", iseo_form_client_ip(), $cfg["hmac_secret"]);
    }
}

if (!function_exists("iseo_form_post_scalar")) {
    function iseo_form_post_scalar($key, $max = 2000) {
        if (!isset($_POST[$key])) {
            return "";
        }
        $v = $_POST[$key];
        if (is_array($v)) {
            return null; // signal reject
        }
        $v = (string)$v;
        $v = str_replace(array("\r\n", "\r"), "\n", $v);
        $v = trim($v);
        if (strlen($v) > $max) {
            $v = substr($v, 0, $max);
        }
        return $v;
    }
}

if (!function_exists("iseo_form_first_scalar")) {
    function iseo_form_first_scalar($keys, $max = 2000) {
        foreach ($keys as $key) {
            if (!isset($_POST[$key])) {
                continue;
            }
            $v = iseo_form_post_scalar($key, $max);
            if ($v === null) {
                return null;
            }
            if ($v !== "") {
                return $v;
            }
        }
        // all empty but present or absent
        foreach ($keys as $key) {
            if (isset($_POST[$key])) {
                $v = iseo_form_post_scalar($key, $max);
                return $v;
            }
        }
        return "";
    }
}

if (!function_exists("iseo_form_is_meaningful")) {
    function iseo_form_is_meaningful($v, $min_len = 2) {
        if ($v === null || $v === "") {
            return false;
        }
        $compact = preg_replace('/[\s\p{P}\p{S}]+/u', "", $v);
        if ($compact === null) {
            $compact = preg_replace('/\s+/', "", $v);
        }
        if ($compact === "" || strlen($compact) < $min_len) {
            return false;
        }
        return true;
    }
}

if (!function_exists("iseo_form_looks_phone")) {
    function iseo_form_looks_phone($v) {
        $digits = preg_replace('/\D+/', "", $v);
        $len = strlen($digits);
        return $len >= 10 && $len <= 15;
    }
}

if (!function_exists("iseo_form_looks_email")) {
    function iseo_form_looks_email($v) {
        return (bool)filter_var($v, FILTER_VALIDATE_EMAIL);
    }
}

if (!function_exists("iseo_form_looks_telegram")) {
    function iseo_form_looks_telegram($v) {
        if (preg_match('/^@?[A-Za-z0-9_]{5,32}$/', $v)) {
            return true;
        }
        if (preg_match('/^(t\.me|telegram\.me)\//i', $v)) {
            return true;
        }
        // phone used as Telegram contact
        if (iseo_form_looks_phone($v)) {
            return true;
        }
        return false;
    }
}

if (!function_exists("iseo_form_contact_ok")) {
    function iseo_form_contact_ok($method, $contact) {
        if (!iseo_form_is_meaningful($contact, 3)) {
            return false;
        }
        $m = mb_strtolower($method, "UTF-8");
        if ($m === "" || $m === "телефон" || $m === "phone" || mb_strpos($m, "телефон") !== false) {
            return iseo_form_looks_phone($contact) || iseo_form_looks_email($contact) || iseo_form_looks_telegram($contact);
        }
        if (mb_strpos($m, "mail") !== false || mb_strpos($m, "почт") !== false || mb_strpos($m, "e-mail") !== false) {
            return iseo_form_looks_email($contact);
        }
        if (mb_strpos($m, "telegram") !== false || mb_strpos($m, "телеграм") !== false || $m === "tg") {
            return iseo_form_looks_telegram($contact) || iseo_form_looks_phone($contact);
        }
        if (mb_strpos($m, "whatsapp") !== false || mb_strpos($m, "ватсап") !== false || mb_strpos($m, "вацап") !== false) {
            return iseo_form_looks_phone($contact) || iseo_form_looks_telegram($contact);
        }
        // unknown method: accept phone/email/telegram-like
        return iseo_form_looks_phone($contact) || iseo_form_looks_email($contact) || iseo_form_looks_telegram($contact);
    }
}

if (!function_exists("iseo_form_has_injection")) {
    function iseo_form_has_injection($v) {
        if ($v === null || $v === "") {
            return false;
        }
        if (preg_match('/[\r\n].*(to|cc|bcc|content-type|mime-version)\s*:/i', $v)) {
            return true;
        }
        if (preg_match('/<\s*script\b/i', $v)) {
            return true;
        }
        return false;
    }
}

if (!function_exists("iseo_form_spam_heuristic")) {
    function iseo_form_spam_heuristic($fields) {
        $joined = "";
        foreach ($fields as $v) {
            if (!is_string($v)) {
                continue;
            }
            $joined .= " " . $v;
            if (preg_match('/(.)\1{9,}/u', $v)) {
                return true;
            }
            if (preg_match('/https?:\/\//i', $v) && substr_count(mb_strtolower($v, "UTF-8"), "http") >= 3) {
                return true;
            }
        }
        if (preg_match('/<\s*(script|iframe)\b/i', $joined)) {
            return true;
        }
        return false;
    }
}

if (!function_exists("iseo_form_h")) {
    function iseo_form_h($v) {
        return htmlspecialchars((string)$v, ENT_QUOTES | ENT_SUBSTITUTE, "UTF-8");
    }
}

if (!function_exists("iseo_form_recipients")) {
    function iseo_form_recipients() {
        $cfg = iseo_form_cfg();
        if (!empty($cfg["test_mode"])) {
            return $cfg["test_recipients"];
        }
        return $cfg["production_recipients"];
    }
}

if (!function_exists("iseo_form_verify_timing")) {
    function iseo_form_verify_timing() {
        $cfg = iseo_form_cfg();
        $ts = iseo_form_post_scalar("iseo_ft", 32);
        $sig = iseo_form_post_scalar("iseo_fs", 128);
        $tid = iseo_form_post_scalar("iseo_fid", 64);
        if ($ts === null || $sig === null || $tid === null) {
            return "reject";
        }
        if ($ts === "" || $sig === "" || $tid === "" || !ctype_digit($ts)) {
            return "reject";
        }
        $payload = $tid . "|" . $ts;
        $expect = hash_hmac("sha256", $payload, $cfg["hmac_secret"]);
        if (!hash_equals($expect, $sig)) {
            return "reject";
        }
        $age = time() - (int)$ts;
        if ($age < (int)$cfg["min_fill_seconds"]) {
            return "too_fast";
        }
        if ($age > (int)$cfg["max_fill_seconds"]) {
            return "reject";
        }
        return "ok";
    }
}

if (!function_exists("iseo_form_issue_token")) {
    function iseo_form_issue_token() {
        $cfg = iseo_form_cfg();
        $ts = (string)time();
        $tid = bin2hex(random_bytes(8));
        $sig = hash_hmac("sha256", $tid . "|" . $ts, $cfg["hmac_secret"]);
        return array("t" => $ts, "s" => $sig, "id" => $tid);
    }
}

if (!function_exists("iseo_form_rate_check")) {
    function iseo_form_rate_check($form_id) {
        $cfg = iseo_form_cfg();
        $dir = iseo_form_runtime_dir();
        $ip_h = iseo_form_ip_hash();
        $now = time();
        $file = $dir . "/rl_" . hash("sha256", $ip_h . "|" . $form_id) . ".json";
        $fp = @fopen($file, "c+");
        if (!$fp) {
            return "ok"; // fail open lightly? prefer fail closed for spam
        }
        flock($fp, LOCK_EX);
        $raw = stream_get_contents($fp);
        $data = $raw ? json_decode($raw, true) : array();
        if (!is_array($data)) {
            $data = array();
        }
        $events = isset($data["e"]) && is_array($data["e"]) ? $data["e"] : array();
        $events = array_values(array_filter($events, function ($t) use ($now, $cfg) {
            return is_int($t) && ($now - $t) < max($cfg["rate_limit_hour_window"], $cfg["rate_limit_burst_window"]);
        }));
        $burst = 0;
        $hour = 0;
        foreach ($events as $t) {
            if (($now - $t) < $cfg["rate_limit_burst_window"]) {
                $burst++;
            }
            if (($now - $t) < $cfg["rate_limit_hour_window"]) {
                $hour++;
            }
        }
        if ($burst >= $cfg["rate_limit_burst_max"] || $hour >= $cfg["rate_limit_hour_max"]) {
            flock($fp, LOCK_UN);
            fclose($fp);
            return "rate";
        }
        $events[] = $now;
        $data = array("e" => $events);
        ftruncate($fp, 0);
        rewind($fp);
        fwrite($fp, json_encode($data));
        fflush($fp);
        flock($fp, LOCK_UN);
        fclose($fp);
        return "ok";
    }
}

if (!function_exists("iseo_form_duplicate_paths")) {
    function iseo_form_duplicate_paths($form_id, $normalized) {
        $cfg = iseo_form_cfg();
        $dir = iseo_form_runtime_dir();
        $ip_h = iseo_form_ip_hash();
        $digest = hash_hmac("sha256", $form_id . "|" . $normalized, $cfg["hmac_secret"]);
        return $dir . "/dup_" . hash("sha256", $ip_h . "|" . $digest) . ".json";
    }
}

if (!function_exists("iseo_form_duplicate_check")) {
    function iseo_form_duplicate_check($form_id, $normalized) {
        $cfg = iseo_form_cfg();
        $file = iseo_form_duplicate_paths($form_id, $normalized);
        $now = time();
        if (is_file($file)) {
            $prev = json_decode(@file_get_contents($file), true);
            if (is_array($prev) && isset($prev["t"]) && ($now - (int)$prev["t"]) < $cfg["duplicate_window"]) {
                return "dup";
            }
        }
        return "ok";
    }
}

if (!function_exists("iseo_form_duplicate_mark")) {
    function iseo_form_duplicate_mark($form_id, $normalized) {
        $file = iseo_form_duplicate_paths($form_id, $normalized);
        @file_put_contents($file, json_encode(array("t" => time())), LOCK_EX);
    }
}

if (!function_exists("iseo_form_log")) {
    function iseo_form_log($form_id, $class, $result) {
        $dir = iseo_form_runtime_dir();
        $line = json_encode(array(
            "ts" => gmdate("c"),
            "form" => $form_id,
            "class" => $class,
            "result" => $result,
            "ip_h" => substr(iseo_form_ip_hash(), 0, 16),
        ), JSON_UNESCAPED_UNICODE);
        @file_put_contents($dir . "/events.log", $line . "\n", FILE_APPEND | LOCK_EX);
    }
}

if (!function_exists("iseo_form_send_mail")) {
    function iseo_form_send_mail($subject, $html_body) {
        $cfg = iseo_form_cfg();
        $recipients = iseo_form_recipients();
        if (!$recipients) {
            return false;
        }
        // Prevent recipient / header injection via subject
        $subject = str_replace(array("\r", "\n"), "", $subject);
        $from = $cfg["from_email"];
        $headers = "From: " . $from . "\r\n";
        $headers .= "Reply-To: " . $from . "\r\n";
        $headers .= "MIME-Version: 1.0\r\n";
        $headers .= "Content-Type: text/html; charset=utf-8\r\n";
        $ok_all = true;
        foreach ($recipients as $to) {
            $to = str_replace(array("\r", "\n"), "", (string)$to);
            if ($to === "" || !filter_var($to, FILTER_VALIDATE_EMAIL)) {
                $ok_all = false;
                continue;
            }
            $ok = @mail($to, "=?UTF-8?B?" . base64_encode($subject) . "?=", $html_body, $headers);
            if (!$ok) {
                $ok_all = false;
            }
        }
        return $ok_all;
    }
}

if (!function_exists("iseo_form_reject")) {
    function iseo_form_reject($form_id, $class) {
        iseo_form_log($form_id, $class, "reject");
        header("Content-Type: text/plain; charset=utf-8");
        echo "false";
        exit;
    }
}

if (!function_exists("iseo_form_guard_request")) {
    function iseo_form_guard_request($form_id) {
        if (($_SERVER["REQUEST_METHOD"] ?? "") !== "POST") {
            iseo_form_reject($form_id, "method");
        }
        $cfg = iseo_form_cfg();
        $hp = $cfg["honeypot_field"];
        $hp_val = isset($_POST[$hp]) ? $_POST[$hp] : null;
        if ($hp_val === null) {
            // Direct bot POST without rendered form/JS
            iseo_form_reject($form_id, "honeypot_missing");
        }
        if (is_array($hp_val) || trim((string)$hp_val) !== "") {
            iseo_form_reject($form_id, "honeypot");
        }
        $timing = iseo_form_verify_timing();
        if ($timing !== "ok") {
            iseo_form_reject($form_id, $timing === "too_fast" ? "too_fast" : "timing");
        }
        $rl = iseo_form_rate_check($form_id);
        if ($rl !== "ok") {
            iseo_form_reject($form_id, "rate");
        }
    }
}

if (!function_exists("iseo_form_page_meta")) {
    function iseo_form_page_meta() {
        $title = iseo_form_post_scalar("pf_page_title", 300);
        $link = iseo_form_post_scalar("pf_page_link", 500);
        if ($title === null || $link === null) {
            return null;
        }
        if (iseo_form_has_injection($title) || iseo_form_has_injection($link)) {
            return null;
        }
        return array($title, $link);
    }
}

if (!function_exists("iseo_form_finish_ok")) {
    function iseo_form_finish_ok($form_id) {
        iseo_form_log($form_id, "accept", "mail");
        header("Content-Type: text/plain; charset=utf-8");
        echo "true";
        exit;
    }
}
