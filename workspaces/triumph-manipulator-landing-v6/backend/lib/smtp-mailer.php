<?php

declare(strict_types=1);

/**
 * @param list<string> $recipients
 * @param list<string> $headers
 */
function triumph_smtp_send_message(
    array $smtpConfig,
    array $recipients,
    string $fromAddress,
    string $fromName,
    string $encodedSubject,
    array $headers,
    string $body
): bool {
    $host = trim((string) ($smtpConfig['host'] ?? ''));
    $port = (int) ($smtpConfig['port'] ?? 465);
    $username = trim((string) ($smtpConfig['username'] ?? ''));
    $password = (string) ($smtpConfig['password'] ?? '');
    $encryption = strtolower(trim((string) ($smtpConfig['encryption'] ?? 'ssl')));

    if ($host === '' || $username === '' || $password === '' || $recipients === []) {
        return false;
    }

    $transport = $encryption === 'ssl'
        ? 'ssl://' . $host . ':' . $port
        : $host . ':' . $port;

    $socket = @stream_socket_client(
        $transport,
        $errorCode,
        $errorMessage,
        20,
        STREAM_CLIENT_CONNECT
    );

    if ($socket === false) {
        return false;
    }

    stream_set_timeout($socket, 20);

    try {
        if (!triumph_smtp_expect($socket, [220])) {
            return false;
        }

        $ehloHost = preg_replace('/[^a-zA-Z0-9.\-]/', '', (string) ($_SERVER['SERVER_NAME'] ?? 'localhost')) ?: 'localhost';

        if (!triumph_smtp_command($socket, 'EHLO ' . $ehloHost, [250])) {
            return false;
        }

        if (!triumph_smtp_command($socket, 'AUTH LOGIN', [334])) {
            return false;
        }

        if (!triumph_smtp_command($socket, base64_encode($username), [334])) {
            return false;
        }

        if (!triumph_smtp_command($socket, base64_encode($password), [235])) {
            return false;
        }

        if (!triumph_smtp_command($socket, 'MAIL FROM:<' . $fromAddress . '>', [250])) {
            return false;
        }

        foreach ($recipients as $recipient) {
            if (!triumph_smtp_command($socket, 'RCPT TO:<' . $recipient . '>', [250, 251])) {
                return false;
            }
        }

        if (!triumph_smtp_command($socket, 'DATA', [354])) {
            return false;
        }

        $fromHeader = triumph_smtp_format_from($fromAddress, $fromName);
        $messageLines = array_merge(
            ['Subject: ' . $encodedSubject, 'To: ' . implode(', ', $recipients), 'From: ' . $fromHeader],
            $headers,
            [''],
            explode("\r\n", $body)
        );

        if (!triumph_smtp_write_data($socket, $messageLines)) {
            return false;
        }

        if (!triumph_smtp_expect($socket, [250])) {
            return false;
        }

        triumph_smtp_command($socket, 'QUIT', [221]);

        return true;
    } finally {
        fclose($socket);
    }
}

function triumph_smtp_format_from(string $fromAddress, string $fromName): string
{
    if ($fromName === '') {
        return $fromAddress;
    }

    return '=?UTF-8?B?' . base64_encode($fromName) . '?= <' . $fromAddress . '>';
}

/**
 * @param list<int> $expectedCodes
 */
function triumph_smtp_command($socket, string $command, array $expectedCodes): bool
{
    if (fwrite($socket, $command . "\r\n") === false) {
        return false;
    }

    return triumph_smtp_expect($socket, $expectedCodes);
}

/**
 * @param list<int> $expectedCodes
 */
function triumph_smtp_expect($socket, array $expectedCodes): bool
{
    $response = triumph_smtp_read($socket);

    if ($response === '') {
        return false;
    }

    $code = (int) substr($response, 0, 3);

    return in_array($code, $expectedCodes, true);
}

/**
 * @param resource $socket
 */
function triumph_smtp_read($socket): string
{
    $data = '';

    while (($line = fgets($socket, 515)) !== false) {
        $data .= $line;
        if (isset($line[3]) && $line[3] === ' ') {
            break;
        }
    }

    return $data;
}

/**
 * @param resource $socket
 * @param list<string> $lines
 */
function triumph_smtp_write_data($socket, array $lines): bool
{
    foreach ($lines as $line) {
        if (isset($line[0]) && $line[0] === '.') {
            $line = '.' . $line;
        }

        if (fwrite($socket, $line . "\r\n") === false) {
            return false;
        }
    }

    return fwrite($socket, ".\r\n") !== false;
}
