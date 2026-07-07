#!/usr/bin/env php
<?php
/**
 * SITE-002 mail design system — local preview generator (no SMTP, no production).
 *
 * Usage:
 *   php site-002-mail-design-system-preview-01.php [--deployment-root PATH]
 */
declare(strict_types=1);

$options = getopt('', ['deployment-root::', 'renderer::']);
$deploymentRoot = $options['deployment-root']
	?? 'X:\\AI MARS STORAGE\\ocpilot\\project-sites\\site-002\\production\\deployments\\SITE-002-PROD-MAIL-DESIGN-SYSTEM-01';
$rendererPath = $options['renderer']
	?? dirname(__DIR__) . DIRECTORY_SEPARATOR . 'mail_renderer.php';

$deploymentRoot = rtrim(str_replace(['/', '\\'], DIRECTORY_SEPARATOR, $deploymentRoot), DIRECTORY_SEPARATOR);
$fixturesDir = $deploymentRoot . DIRECTORY_SEPARATOR . 'fixtures';
$previewDir = $deploymentRoot . DIRECTORY_SEPARATOR . 'preview';

if (!is_file($rendererPath)) {
	fwrite(STDERR, "Renderer not found: {$rendererPath}\n");
	exit(1);
}

require_once $rendererPath;

$renderer = new ZpmMailRenderer();
$jobs = array(
	'admin-form' => function () use ($renderer, $fixturesDir) {
		$data = load_fixture($fixturesDir . DIRECTORY_SEPARATOR . 'admin-form-sample.json');
		return $renderer->renderAdminForm($data);
	},
	'customer-form' => function () use ($renderer, $fixturesDir) {
		$data = load_fixture($fixturesDir . DIRECTORY_SEPARATOR . 'customer-form-sample.json');
		return $renderer->renderCustomerFormConfirmation($data);
	},
	'account' => function () use ($renderer, $fixturesDir) {
		$data = load_fixture($fixturesDir . DIRECTORY_SEPARATOR . 'account-sample.json');
		return $renderer->renderAccountMail($data);
	},
	'order' => function () use ($renderer, $fixturesDir) {
		$data = load_fixture($fixturesDir . DIRECTORY_SEPARATOR . 'order-sample.json');
		return $renderer->renderOrderMail($data);
	},
);

if (!is_dir($previewDir) && !mkdir($previewDir, 0777, true) && !is_dir($previewDir)) {
	fwrite(STDERR, "Cannot create preview dir: {$previewDir}\n");
	exit(1);
}

$manifest = array(
	'generated_at' => gmdate('c'),
	'renderer' => $rendererPath,
	'fixtures_dir' => $fixturesDir,
	'preview_dir' => $previewDir,
	'outputs' => array(),
);

foreach ($jobs as $slug => $callback) {
	$result = $callback();
	$htmlPath = $previewDir . DIRECTORY_SEPARATOR . "{$slug}-email.html";
	$textPath = $previewDir . DIRECTORY_SEPARATOR . "{$slug}-email.txt";
	file_put_contents($htmlPath, $result['html']);
	file_put_contents($textPath, $result['text']);
	$manifest['outputs'][] = array(
		'slug' => $slug,
		'html' => $htmlPath,
		'text' => $textPath,
		'subject' => $result['subject'],
	);
	echo "Wrote {$slug} preview\n";
}

file_put_contents(
	$previewDir . DIRECTORY_SEPARATOR . 'preview-manifest.json',
	json_encode($manifest, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . "\n"
);

echo "Preview generation complete.\n";
exit(0);

function load_fixture(string $path): array
{
	if (!is_file($path)) {
		fwrite(STDERR, "Fixture missing: {$path}\n");
		exit(1);
	}
	$data = json_decode((string) file_get_contents($path), true);
	if (!is_array($data)) {
		fwrite(STDERR, "Invalid fixture JSON: {$path}\n");
		exit(1);
	}
	return $data;
}
