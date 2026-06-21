<?php

declare(strict_types=1);

/**
 * Default mailer configuration (no secrets).
 * Optional override: config.local.php (same directory, not committed).
 */
return [
    'recipient' => 'info@manipulator-triumph.ru',
    'recipients' => [
        'info@manipulator-triumph.ru',
        'opergt@gktriumph.ru',
    ],
    'from_address' => 'noreply@manipulator-triumph.ru',
    'from_name' => 'Триумф',
    'from_local_part' => 'noreply',
    'subject_base' => 'Заявка с лендинга Триумф: аренда манипулятора',
    'max_field_length' => 2000,
    'max_phone_length' => 32,
    'max_name_length' => 120,
    'use_smtp' => true,
    'smtp' => [
        'host' => 'smtp.beget.com',
        'port' => 465,
        'encryption' => 'ssl',
        'username' => 'noreply@manipulator-triumph.ru',
        'password' => '',
    ],
];
