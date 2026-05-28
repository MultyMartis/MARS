<?php

declare(strict_types=1);

/**
 * Default mailer configuration (no secrets).
 * Optional override: config.local.php (same directory, not committed).
 */
return [
    'recipient' => 'client.leads@polygon-ws.ru',
    'from_local_part' => 'noreply',
    'subject_base' => 'Заявка с лендинга Триумф: аренда манипулятора',
    'max_field_length' => 2000,
    'max_phone_length' => 32,
    'max_name_length' => 120,
];
