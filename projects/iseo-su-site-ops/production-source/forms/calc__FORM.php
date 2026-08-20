<?php
require_once __DIR__ . "/iseo-form-security.php";

$form_id = "calc";
iseo_form_guard_request($form_id);

$st = array();
for ($i = 1; $i <= 5; $i++) {
    $k = sprintf("radio_st_%02d", $i);
    $v = iseo_form_post_scalar($k, 200);
    if ($v === null) {
        iseo_form_reject($form_id, "array");
    }
    $st[$i] = $v;
}
$username = iseo_form_first_scalar(array("calc_name"), 120);
$method = iseo_form_first_scalar(array("calc_contact"), 80);
$contact = iseo_form_first_scalar(array("calc_phone"), 120);
$site = iseo_form_first_scalar(array("calc_site"), 300);
if ($username === null || $method === null || $contact === null || $site === null) {
    iseo_form_reject($form_id, "array");
}
$page = iseo_form_page_meta();
if ($page === null) {
    iseo_form_reject($form_id, "page_meta");
}
list($page_title, $page_link) = $page;

$all = array_merge(array_values($st), array($username, $method, $contact, $site, $page_title, $page_link));
foreach ($all as $v) {
    if (iseo_form_has_injection($v)) {
        iseo_form_reject($form_id, "injection");
    }
}
if (!iseo_form_is_meaningful($username, 2) || !iseo_form_is_meaningful($method, 2) || !iseo_form_contact_ok($method, $contact)) {
    iseo_form_reject($form_id, "required");
}
if (iseo_form_spam_heuristic($all)) {
    iseo_form_reject($form_id, "heuristic");
}
$norm = mb_strtolower($username . "|" . $method . "|" . $contact . "|" . $site . "|" . implode("|", $st), "UTF-8");
if (iseo_form_duplicate_check($form_id, $norm) === "dup") {
    iseo_form_reject($form_id, "duplicate");
}

$subject = "Заявка из калькулятора";
$msg = "<html><body style='font-family:Tahoma,sans-serif;'>";
$msg .= "<h2 style='font-weight:bold;border-bottom:1px dotted #ccc;padding-bottom:10px;margin-bottom:10px;'>Заявка из калькулятора</h2>\r\n";
$msg .= "<p><strong>Ваше имя:</strong> " . iseo_form_h($username) . "</p>\r\n";
$msg .= "<p><strong>Способ связи:</strong> " . iseo_form_h($method) . "</p>\r\n";
$msg .= "<p><strong>Контакт:</strong> " . iseo_form_h($contact) . "</p>\r\n";
$msg .= "<p><strong>Адрес сайта:</strong> " . iseo_form_h($site) . "</p>\r\n";
$labels = array(1 => "Этап продвижения", 2 => "Количество продвигаемых запросов", 3 => "Количество запросов в топ-10 сейчас", 4 => "Тип сайта", 5 => "Регион");
foreach ($st as $i => $v) {
    $label = isset($labels[$i]) ? $labels[$i] : ("Этап " . $i);
    $msg .= "<p><strong>" . iseo_form_h($label) . ":</strong> " . iseo_form_h($v) . "</p>\r\n";
}
$msg .= "<p><strong>Отправлено со страницы:</strong> <a href='" . iseo_form_h($page_link) . "' target='_blank'>" . iseo_form_h($page_title) . "</a></p>\r\n";
$msg .= "<p><strong>IP:</strong> " . iseo_form_h(iseo_form_client_ip()) . "</p>\r\n";
$msg .= "</body></html>";

if (!iseo_form_send_mail($subject, $msg)) {
    iseo_form_reject($form_id, "mail_fail");
}
iseo_form_duplicate_mark($form_id, $norm);
iseo_form_finish_ok($form_id);
