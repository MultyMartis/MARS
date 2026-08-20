<?php
require_once __DIR__ . "/iseo-form-security.php";

$form_id = "bonus";
iseo_form_guard_request($form_id);

$username = iseo_form_first_scalar(array("bf_name"), 120);
$method = iseo_form_first_scalar(array("bf_contact"), 80);
$contact = iseo_form_first_scalar(array("bf_phone"), 120);
$comment = iseo_form_first_scalar(array("bf_comment"), 2000);
if ($username === null || $method === null || $contact === null || $comment === null) {
    iseo_form_reject($form_id, "array");
}
$page = iseo_form_page_meta();
if ($page === null) {
    iseo_form_reject($form_id, "page_meta");
}
list($page_title, $page_link) = $page;
foreach (array($username, $method, $contact, $comment, $page_title, $page_link) as $v) {
    if (iseo_form_has_injection($v)) {
        iseo_form_reject($form_id, "injection");
    }
}
if (!iseo_form_is_meaningful($username, 2) || !iseo_form_is_meaningful($method, 2) || !iseo_form_contact_ok($method, $contact)) {
    iseo_form_reject($form_id, "required");
}
if (iseo_form_spam_heuristic(array($username, $method, $contact, $comment))) {
    iseo_form_reject($form_id, "heuristic");
}
$norm = mb_strtolower($username . "|" . $method . "|" . $contact . "|" . $comment, "UTF-8");
if (iseo_form_duplicate_check($form_id, $norm) === "dup") {
    iseo_form_reject($form_id, "duplicate");
}

$subject = "Заявка на бонус / акцию";
$msg = "<html><body style='font-family:Tahoma,sans-serif;'>";
$msg .= "<h2 style='font-weight:bold;border-bottom:1px dotted #ccc;padding-bottom:10px;margin-bottom:10px;'>Заявка на бонус / акцию</h2>\r\n";
$msg .= "<p><strong>Ваше имя:</strong> " . iseo_form_h($username) . "</p>\r\n";
$msg .= "<p><strong>Способ связи:</strong> " . iseo_form_h($method) . "</p>\r\n";
$msg .= "<p><strong>Контакт:</strong> " . iseo_form_h($contact) . "</p>\r\n";
$msg .= "<p><strong>Комментарий:</strong> " . iseo_form_h($comment) . "</p>\r\n";
$msg .= "<p><strong>Отправлено со страницы:</strong> <a href='" . iseo_form_h($page_link) . "' target='_blank'>" . iseo_form_h($page_title) . "</a></p>\r\n";
$msg .= "<p><strong>IP:</strong> " . iseo_form_h(iseo_form_client_ip()) . "</p>\r\n";
$msg .= "</body></html>";

if (!iseo_form_send_mail($subject, $msg)) {
    iseo_form_reject($form_id, "mail_fail");
}
iseo_form_duplicate_mark($form_id, $norm);
iseo_form_finish_ok($form_id);
