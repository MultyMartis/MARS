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
    'to' => 'client.leads@polygon-ws.ru',
    'from_address' => 'no-reply@polygon-ws.ru',
    'from_name' => 'Triumph Manipulator',
    'subject_prefix' => '[Triumph]',
    'use_smtp' => false,
    'smtp' => [
        'host' => '',
        'port' => 587,
        'encryption' => 'tls',
        'username' => '',
        'password' => '',
    ],
];
