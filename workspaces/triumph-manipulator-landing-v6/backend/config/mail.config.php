<?php

declare(strict_types=1);

/**
 * Mail routing — operator may enable SMTP on hosting later.
 *
 * @return array{
 *   to: string,
 *   from_address: string,
 *   from_name: string,
 *   subject_prefix: string,
 *   use_smtp: bool,
 *   smtp: array<string, mixed>
 * }
 */
return [
    'to' => 'info@manipulator-triumph.ru',
    'from_address' => 'noreply@manipulator-triumph.ru',
    'from_name' => 'Триумф',
    'subject_prefix' => '[Triumph]',
    'use_smtp' => true,
    'smtp' => [
        'host' => 'smtp.beget.com',
        'port' => 465,
        'encryption' => 'ssl',
        'username' => 'noreply@manipulator-triumph.ru',
        'password' => '',
    ],
];
