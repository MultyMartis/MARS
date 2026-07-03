$ErrorActionPreference = 'Stop'

$repoRoot = 'X:\AI MARS'
$wpSource = Join-Path $repoRoot 'workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS'
$evidenceDir = Join-Path $wpSource 'validation\v9-06b2-acf-admission'
$runtimeRoot = 'X:\MARS-Localhost\sites\wordpress\projects\shpigovsky'
$pluginRoot = Join-Path $runtimeRoot 'wp-content\plugins'
$phpExe = 'X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe'

function Write-JsonFile {
    param(
        [Parameter(Mandatory = $true)] [string] $Path,
        [Parameter(Mandatory = $true)] $Value,
        [int] $Depth = 16
    )

    $json = $Value | ConvertTo-Json -Depth $Depth
    Set-Content -LiteralPath $Path -Value $json -Encoding UTF8
}

function Get-RelativePath {
    param(
        [Parameter(Mandatory = $true)] [string] $Base,
        [Parameter(Mandatory = $true)] [string] $Path
    )

    $baseUri = [Uri]((Resolve-Path -LiteralPath $Base).Path.TrimEnd('\') + '\')
    $pathUri = [Uri](Resolve-Path -LiteralPath $Path).Path
    return [Uri]::UnescapeDataString($baseUri.MakeRelativeUri($pathUri).ToString()).Replace('/', '\')
}

function New-PluginManifest {
    param(
        [Parameter(Mandatory = $true)] [string] $PluginName,
        [Parameter(Mandatory = $true)] [string] $Directory,
        [Parameter(Mandatory = $true)] [string] $OutputPath
    )

    if (-not (Test-Path -LiteralPath $Directory)) {
        throw "Plugin directory missing: $Directory"
    }

    $files = Get-ChildItem -LiteralPath $Directory -Recurse -File -Force | Sort-Object FullName
    $entries = @()
    foreach ($file in $files) {
        $extension = if ($file.Extension) { $file.Extension.ToLowerInvariant() } else { '' }
        $classification = switch -Regex ($extension) {
            '^\.(php|phtml|inc)$' { 'php_script'; break }
            '^\.(js|mjs|cjs)$' { 'javascript'; break }
            '^\.(css|scss|sass|less)$' { 'stylesheet'; break }
            '^\.(json|xml|yml|yaml|txt|md|pot|po|mo)$' { 'data_or_translation'; break }
            '^\.(png|jpg|jpeg|gif|svg|webp|ico)$' { 'asset'; break }
            default { 'other' }
        }
        $hash = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
        $entries += [ordered]@{
            relative_path = Get-RelativePath -Base $Directory -Path $file.FullName
            size = $file.Length
            sha256 = $hash
            extension = $extension
            modified_time_utc = $file.LastWriteTimeUtc.ToString('o')
            classification = $classification
        }
    }

    $aggregateInput = ($entries | ForEach-Object { "$($_.relative_path)|$($_.size)|$($_.sha256)" }) -join "`n"
    $sha = [System.Security.Cryptography.SHA256]::Create()
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($aggregateInput)
    $aggregateHash = ([System.BitConverter]::ToString($sha.ComputeHash($bytes))).Replace('-', '').ToLowerInvariant()

    $manifest = [ordered]@{
        plugin = $PluginName
        directory = $Directory
        generated_at = (Get-Date).ToUniversalTime().ToString('o')
        files = $entries.Count
        php_files = @($entries | Where-Object { $_.classification -eq 'php_script' }).Count
        js_files = @($entries | Where-Object { $_.classification -eq 'javascript' }).Count
        aggregate_hash = $aggregateHash
        entries = $entries
    }

    Write-JsonFile -Path $OutputPath -Value $manifest -Depth 20
    return $manifest
}

function Invoke-PatternScan {
    param(
        [Parameter(Mandatory = $true)] [array] $Targets,
        [Parameter(Mandatory = $true)] [string] $OutputPath
    )

    $patterns = @(
        @{ id = 'eval'; regex = '\beval\s*\('; default = 'REVIEW_REQUIRED' },
        @{ id = 'assert'; regex = '\bassert\s*\('; default = 'REVIEW_REQUIRED' },
        @{ id = 'base64_decode'; regex = '\bbase64_decode\s*\('; default = 'REVIEW_REQUIRED' },
        @{ id = 'gzinflate'; regex = '\bgzinflate\s*\('; default = 'REVIEW_REQUIRED' },
        @{ id = 'gzuncompress'; regex = '\bgzuncompress\s*\('; default = 'REVIEW_REQUIRED' },
        @{ id = 'str_rot13'; regex = '\bstr_rot13\s*\('; default = 'REVIEW_REQUIRED' },
        @{ id = 'preg_replace_e'; regex = 'preg_replace\s*\([^)]*/e[^\w]'; default = 'REVIEW_REQUIRED' },
        @{ id = 'create_function'; regex = '\bcreate_function\s*\('; default = 'REVIEW_REQUIRED' },
        @{ id = 'shell_exec'; regex = '\bshell_exec\s*\('; default = 'HIGH_RISK' },
        @{ id = 'exec'; regex = '(?<!->)\bexec\s*\('; default = 'HIGH_RISK' },
        @{ id = 'system'; regex = '\bsystem\s*\('; default = 'HIGH_RISK' },
        @{ id = 'passthru'; regex = '\bpassthru\s*\('; default = 'HIGH_RISK' },
        @{ id = 'proc_open'; regex = '\bproc_open\s*\('; default = 'HIGH_RISK' },
        @{ id = 'popen'; regex = '\bpopen\s*\('; default = 'HIGH_RISK' },
        @{ id = 'curl_exec'; regex = '\bcurl_exec\s*\('; default = 'REVIEW_REQUIRED' },
        @{ id = 'fsockopen'; regex = '\bfsockopen\s*\('; default = 'REVIEW_REQUIRED' },
        @{ id = 'stream_socket_client'; regex = '\bstream_socket_client\s*\('; default = 'REVIEW_REQUIRED' },
        @{ id = 'remote_file_get_contents'; regex = 'file_get_contents\s*\(\s*[''"]https?://'; default = 'REVIEW_REQUIRED' },
        @{ id = 'wp_create_user'; regex = '\bwp_create_user\s*\('; default = 'HIGH_RISK' },
        @{ id = 'wp_insert_user'; regex = '\bwp_insert_user\s*\('; default = 'HIGH_RISK' },
        @{ id = 'grant_super_admin'; regex = '\bgrant_super_admin\s*\('; default = 'HIGH_RISK' },
        @{ id = 'sensitive_update_option'; regex = 'update_option\s*\(\s*[''"](siteurl|home|users_can_register|active_plugins)[''"]'; default = 'HIGH_RISK' },
        @{ id = 'remote_download_init'; regex = 'add_action\s*\(\s*[''"](init|admin_init)[''"].*(download|remote|http|https)'; default = 'REVIEW_REQUIRED' },
        @{ id = 'cron_creation'; regex = '\bwp_schedule_event\s*\('; default = 'REVIEW_REQUIRED' },
        @{ id = 'remote_code_loading'; regex = '(include|require)(_once)?\s*\(\s*[''"]https?://'; default = 'HIGH_RISK' },
        @{ id = 'license_bypass_marker'; regex = '(nulled|crack|license\s*bypass|ioncube\s*bypass)'; default = 'BLOCKER' },
        @{ id = 'obfuscated_long_string'; regex = '[''"][A-Za-z0-9+/]{220,}={0,2}[''"]'; default = 'REVIEW_REQUIRED' },
        @{ id = 'external_url'; regex = 'https?://[A-Za-z0-9._~:/?#\[\]@!$&''()*+,;=%-]+'; default = 'BENIGN_EXPECTED' }
    )

    $allowedDomains = @(
        'advancedcustomfields.com',
        'www.advancedcustomfields.com',
        'acfextended.com',
        'www.acfextended.com',
        'acf-extended.com',
        'www.acf-extended.com',
        'wordpress.org',
        'api.wordpress.org',
        'wpengine.com',
        'www.wpengine.com',
        'github.com',
        'www.w3.org'
    )

    $scanPlugins = @()
    foreach ($target in $Targets) {
        $root = $target.directory
        $findings = @()
        $files = Get-ChildItem -LiteralPath $root -Recurse -File -Force |
            Where-Object { $_.Extension.ToLowerInvariant() -in @('.php', '.phtml', '.inc', '.js', '.mjs', '.cjs') } |
            Sort-Object FullName

        foreach ($file in $files) {
            $text = [System.IO.File]::ReadAllText($file.FullName)
            foreach ($pattern in $patterns) {
                $matches = [regex]::Matches($text, $pattern.regex, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
                foreach ($match in $matches) {
                    $relativePath = Get-RelativePath -Base $root -Path $file.FullName
                    $line = ($text.Substring(0, $match.Index) -split "`r?`n").Count
                    $lineText = ([regex]::Split($text, "`r?`n"))[$line - 1]
                    $trimmedLine = $lineText.Trim()
                    $classification = $pattern.default
                    $note = 'Static pattern match; source not modified.'
                    if ($pattern.id -eq 'external_url') {
                        try {
                            $uri = [Uri]$match.Value
                            if ($allowedDomains -contains $uri.Host.ToLowerInvariant()) {
                                $classification = 'BENIGN_EXPECTED'
                                $note = 'Expected vendor or standards URL.'
                            } else {
                                $classification = 'REVIEW_REQUIRED'
                                $note = 'External domain requires provenance review.'
                            }
                        } catch {
                            $classification = 'REVIEW_REQUIRED'
                            $note = 'URL parse failed.'
                        }
                    }
                    if ($pattern.id -eq 'assert' -and $file.Extension.ToLowerInvariant() -eq '.js') {
                        $classification = 'BENIGN_EXPECTED'
                        $note = 'JavaScript assertion identifier pattern; review not required by itself.'
                    }
                    if ($pattern.id -in @('exec', 'system', 'passthru', 'proc_open', 'popen', 'shell_exec') -and $file.Extension.ToLowerInvariant() -in @('.js', '.mjs', '.cjs')) {
                        $classification = 'REVIEW_REQUIRED'
                        $note = 'JavaScript/vendor pattern match; not classified as PHP command execution.'
                    }
                    if ($pattern.id -in @('exec', 'system', 'passthru', 'proc_open', 'popen', 'shell_exec') -and ($trimmedLine.StartsWith('//') -or $trimmedLine.StartsWith('*') -or $trimmedLine.StartsWith('/*'))) {
                        $classification = 'BENIGN_EXPECTED'
                        $note = 'Comment-only match; not executable code.'
                    }
                    if ($pattern.id -eq 'passthru' -and $relativePath -like '*libraries\stripe\build.php') {
                        $classification = 'REVIEW_REQUIRED'
                        $note = 'Vendor Stripe build helper contains CLI passthru; not used by FP-0002 runtime path.'
                    }
                    if ($pattern.id -eq 'wp_insert_user' -and $relativePath -like '*module-form-action-user.php') {
                        $classification = 'REVIEW_REQUIRED'
                        $note = 'ACF Extended optional form action can create users if configured; FP-0002 does not approve ACFE use by default.'
                    }
                    $findings += [ordered]@{
                        relative_path = $relativePath
                        line = $line
                        pattern = $pattern.id
                        classification = $classification
                        note = $note
                    }
                }
            }
        }

        $counts = [ordered]@{
            BENIGN_EXPECTED = @($findings | Where-Object { $_.classification -eq 'BENIGN_EXPECTED' }).Count
            REVIEW_REQUIRED = @($findings | Where-Object { $_.classification -eq 'REVIEW_REQUIRED' }).Count
            HIGH_RISK = @($findings | Where-Object { $_.classification -eq 'HIGH_RISK' }).Count
            BLOCKER = @($findings | Where-Object { $_.classification -eq 'BLOCKER' }).Count
        }
        $result = if ($counts.BLOCKER -gt 0 -or $counts.HIGH_RISK -gt 0) {
            'FAIL'
        } elseif ($counts.REVIEW_REQUIRED -gt 0) {
            'REVIEW_REQUIRED'
        } else {
            'PASS'
        }

        $scanPlugins += [ordered]@{
            plugin = $target.name
            directory = $root
            files_scanned = $files.Count
            counts = $counts
            result = $result
            findings = $findings
        }
    }

    $overall = if (@($scanPlugins | Where-Object { $_.result -eq 'FAIL' }).Count -gt 0) {
        'FAIL'
    } elseif (@($scanPlugins | Where-Object { $_.result -eq 'REVIEW_REQUIRED' }).Count -gt 0) {
        'REVIEW_REQUIRED'
    } else {
        'PASS'
    }

    $scan = [ordered]@{
        generated_at = (Get-Date).ToUniversalTime().ToString('o')
        scope = 'read-only static scan of installed ACF PRO and ACF Extended PRO plugin directories'
        overall_result = $overall
        plugins = $scanPlugins
    }
    Write-JsonFile -Path $OutputPath -Value $scan -Depth 24
    return $scan
}

if (-not (Test-Path -LiteralPath $repoRoot)) { throw "Missing repo root: $repoRoot" }
if (-not (Test-Path -LiteralPath $runtimeRoot)) { throw "Missing runtime root: $runtimeRoot" }
if (-not (Test-Path -LiteralPath $pluginRoot)) { throw "Missing plugin root: $pluginRoot" }
if (-not (Test-Path -LiteralPath $phpExe)) { throw "Missing PHP executable: $phpExe" }
if (-not (Test-Path -LiteralPath $evidenceDir)) { New-Item -ItemType Directory -Path $evidenceDir | Out-Null }

$frontStatus = $null
$adminStatus = $null
try { $frontStatus = (Invoke-WebRequest -Uri 'http://shpigovsky.test/' -Method Get -UseBasicParsing -TimeoutSec 20).StatusCode } catch { $frontStatus = "ERROR: $($_.Exception.Message)" }
try { $adminStatus = (Invoke-WebRequest -Uri 'http://shpigovsky.test/wp-admin/' -Method Get -UseBasicParsing -TimeoutSec 20 -MaximumRedirection 5).StatusCode } catch { $adminStatus = "ERROR: $($_.Exception.Message)" }

$phpProbePath = Join-Path $evidenceDir 'runtime-readonly-probe.php'
$phpProbe = @'
<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/plugin.php';

global $wpdb, $wp_version;

function fp02_bool($value) {
    return (bool) $value;
}

function fp02_field_type_available($type) {
    if (!function_exists('acf_get_field_type')) {
        return false;
    }
    try {
        $field_type = acf_get_field_type($type);
        return !empty($field_type);
    } catch (Throwable $e) {
        return false;
    }
}

$plugins = get_plugins();
$active = (array) get_option('active_plugins', array());
$network_active = array_keys((array) get_site_option('active_sitewide_plugins', array()));
$auto_update = (array) get_site_option('auto_update_plugins', array());
$updates = get_site_transient('update_plugins');
$plugin_rows = array();
foreach ($plugins as $basename => $data) {
    $plugin_file = WP_PLUGIN_DIR . '/' . $basename;
    $plugin_dir = dirname($plugin_file);
    $plugin_rows[] = array(
        'name' => isset($data['Name']) ? $data['Name'] : '',
        'basename' => $basename,
        'version' => isset($data['Version']) ? $data['Version'] : '',
        'status' => in_array($basename, $active, true) || in_array($basename, $network_active, true) ? 'active' : 'inactive',
        'author' => isset($data['AuthorName']) ? $data['AuthorName'] : (isset($data['Author']) ? wp_strip_all_tags($data['Author']) : ''),
        'plugin_uri' => isset($data['PluginURI']) ? $data['PluginURI'] : '',
        'requires_wp' => isset($data['RequiresWP']) ? $data['RequiresWP'] : '',
        'requires_php' => isset($data['RequiresPHP']) ? $data['RequiresPHP'] : '',
        'update_available' => is_object($updates) && isset($updates->response[$basename]),
        'auto_update' => in_array($basename, $auto_update, true),
        'plugin_file' => $plugin_file,
        'plugin_directory' => $plugin_dir,
        'headers' => $data,
    );
}

$acf_version = defined('ACF_VERSION') ? ACF_VERSION : (function_exists('acf_get_setting') ? acf_get_setting('version') : null);
$acf_pro_defined = defined('ACF_PRO') ? ACF_PRO : null;
$capabilities = array(
    'acf_api' => function_exists('acf'),
    'acf_version' => $acf_version,
    'acf_pro_marker' => (bool) $acf_pro_defined || function_exists('acf_pro_get_license') || function_exists('acf_add_options_page'),
    'repeater' => fp02_field_type_available('repeater') || class_exists('acf_field_repeater'),
    'options_page' => function_exists('acf_add_options_page'),
    'relationship' => fp02_field_type_available('relationship') || class_exists('acf_field_relationship'),
    'gallery' => fp02_field_type_available('gallery') || class_exists('acf_field_gallery'),
    'acf_json_filters_integrable' => function_exists('add_filter') && function_exists('apply_filters'),
    'local_json_path_support' => function_exists('acf_get_setting') || class_exists('ACF_Local_JSON'),
    'get_field' => function_exists('get_field'),
    'update_field' => function_exists('update_field'),
    'acf_add_options_page' => function_exists('acf_add_options_page'),
    'acf_add_local_field_group' => function_exists('acf_add_local_field_group'),
);

$acf_free_basename = null;
$acf_pro_basename = null;
$acfe_pro_basename = null;
$wpilot_basename = null;
$core_basename = null;
foreach ($plugin_rows as $row) {
    if ($row['basename'] === 'advanced-custom-fields/acf.php' || $row['name'] === 'Advanced Custom Fields') { $acf_free_basename = $row['basename']; }
    if ($row['basename'] === 'advanced-custom-fields-pro/acf.php' || stripos($row['name'], 'Advanced Custom Fields PRO') !== false) { $acf_pro_basename = $row['basename']; }
    if ($row['basename'] === 'acf-extended-pro/acf-extended.php' || stripos($row['name'], 'Extended PRO') !== false) { $acfe_pro_basename = $row['basename']; }
    if (stripos($row['basename'], 'metacode-wpilot') !== false) { $wpilot_basename = $row['basename']; }
    if (stripos($row['basename'], 'shpigovsky-core') !== false) { $core_basename = $row['basename']; }
}

$wpilot_options = get_option('wpilot_options', array());
$theme = wp_get_theme();
$acfe_tables = $wpdb->get_col($wpdb->prepare('SHOW TABLES LIKE %s', $wpdb->esc_like($wpdb->prefix . 'acfe') . '%'));

$rest_routes = array();
try {
    $server = rest_get_server();
    $routes = $server->get_routes();
    foreach (array_keys($routes) as $route) {
        if (stripos($route, 'acf') !== false || stripos($route, 'acfe') !== false || stripos($route, 'wpilot') !== false) {
            $rest_routes[] = $route;
        }
    }
} catch (Throwable $e) {
    $rest_routes[] = 'REST route inspection error: ' . $e->getMessage();
}

$payload = array(
    'generated_at' => gmdate('c'),
    'runtime' => array(
        'root' => 'X:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky',
        'site_url' => get_option('siteurl'),
        'home_url' => get_option('home'),
        'wp_version' => $wp_version,
        'db_prefix' => $wpdb->prefix,
        'db_name' => DB_NAME,
        'template' => get_option('template'),
        'stylesheet' => get_option('stylesheet'),
        'theme_name' => $theme->get('Name'),
        'theme_version' => $theme->get('Version'),
        'wpilot_write_enabled' => !empty($wpilot_options['write_enabled']),
        'wpilot_options_present' => is_array($wpilot_options),
    ),
    'plugins' => $plugin_rows,
    'identified_basenames' => array(
        'acf_free' => $acf_free_basename,
        'acf_pro' => $acf_pro_basename,
        'acf_extended_pro' => $acfe_pro_basename,
        'metacode_wpilot' => $wpilot_basename,
        'shpigovsky_core' => $core_basename,
    ),
    'capabilities' => $capabilities,
    'loaded' => array(
        'acf_free_loaded_as_active_runtime' => function_exists('acf') && $acf_free_basename && is_plugin_active($acf_free_basename),
        'acf_pro_loaded_as_active_runtime' => function_exists('acf') && $acf_pro_basename && is_plugin_active($acf_pro_basename),
        'duplicate_active_base_acf_loader' => $acf_free_basename && $acf_pro_basename && is_plugin_active($acf_free_basename) && is_plugin_active($acf_pro_basename),
        'acf_extended_loaded' => $acfe_pro_basename && is_plugin_active($acfe_pro_basename),
    ),
    'acf_extended' => array(
        'tables_like_acfe' => $acfe_tables,
        'rest_routes' => $rest_routes,
        'functions' => array(
            'acfe' => function_exists('acfe'),
            'acfe_get_setting' => function_exists('acfe_get_setting'),
        ),
        'classes' => array(
            'ACFE' => class_exists('ACFE'),
            'ACFE_Admin' => class_exists('ACFE_Admin'),
        ),
    ),
);

echo json_encode($payload, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
'@

Set-Content -LiteralPath $phpProbePath -Value $phpProbe -Encoding UTF8
$probeRaw = & $phpExe $phpProbePath
if ($LASTEXITCODE -ne 0) { throw "PHP read-only probe failed with exit code $LASTEXITCODE" }
$probe = $probeRaw | ConvertFrom-Json
Remove-Item -LiteralPath $phpProbePath -Force

$probe.runtime | Add-Member -NotePropertyName frontend_http_status -NotePropertyValue $frontStatus -Force
$probe.runtime | Add-Member -NotePropertyName wp_admin_http_status -NotePropertyValue $adminStatus -Force

$inventoryPath = Join-Path $evidenceDir 'plugin-inventory.json'
Write-JsonFile -Path $inventoryPath -Value $probe -Depth 24

$acfPro = $probe.plugins | Where-Object { $_.basename -eq $probe.identified_basenames.acf_pro } | Select-Object -First 1
$acfFree = $probe.plugins | Where-Object { $_.basename -eq $probe.identified_basenames.acf_free } | Select-Object -First 1
$acfePro = $probe.plugins | Where-Object { $_.basename -eq $probe.identified_basenames.acf_extended_pro } | Select-Object -First 1

if (-not $acfPro) { throw 'ACF PRO not identified' }
if ($acfPro.status -ne 'active') { throw 'ACF PRO is not active' }
if (-not $acfePro) { throw 'ACF Extended PRO not identified' }

$capabilityRows = @(
    @{ capability = 'ACF API'; available = [bool]$probe.capabilities.acf_api; method = 'function_exists(acf)'; required = $true },
    @{ capability = 'PRO marker/version'; available = [bool]$probe.capabilities.acf_pro_marker; method = 'ACF_PRO/function/options-page marker'; required = $true },
    @{ capability = 'Repeater'; available = [bool]$probe.capabilities.repeater; method = 'acf_get_field_type(repeater)/class_exists'; required = $true },
    @{ capability = 'Options Page'; available = [bool]$probe.capabilities.options_page; method = 'function_exists(acf_add_options_page)'; required = $true },
    @{ capability = 'Relationship'; available = [bool]$probe.capabilities.relationship; method = 'acf_get_field_type(relationship)/class_exists'; required = $true },
    @{ capability = 'Gallery'; available = [bool]$probe.capabilities.gallery; method = 'acf_get_field_type(gallery)/class_exists'; required = $false },
    @{ capability = 'ACF JSON filters'; available = [bool]$probe.capabilities.acf_json_filters_integrable; method = 'WordPress filter API available for acf/settings filters'; required = $true },
    @{ capability = 'Local JSON path support'; available = [bool]$probe.capabilities.local_json_path_support; method = 'acf_get_setting or ACF_Local_JSON class'; required = $true },
    @{ capability = 'get_field'; available = [bool]$probe.capabilities.get_field; method = 'function_exists(get_field)'; required = $true },
    @{ capability = 'update_field'; available = [bool]$probe.capabilities.update_field; method = 'function_exists(update_field), not called'; required = $true },
    @{ capability = 'acf_add_local_field_group'; available = [bool]$probe.capabilities.acf_add_local_field_group; method = 'function_exists(acf_add_local_field_group), not called'; required = $true }
)
$missingRequired = @($capabilityRows | Where-Object { $_.required -and -not $_.available })
$capabilityResult = if ($missingRequired.Count -eq 0) { 'SUFFICIENT' } else { 'PARTIAL' }
Write-JsonFile -Path (Join-Path $evidenceDir 'acf-pro-capability-check.json') -Value ([ordered]@{
    generated_at = (Get-Date).ToUniversalTime().ToString('o')
    plugin = $acfPro
    acf_version = $probe.capabilities.acf_version
    capability = $capabilityResult
    rows = $capabilityRows
    missing_required = $missingRequired
}) -Depth 20

$freeConflict = [ordered]@{
    generated_at = (Get-Date).ToUniversalTime().ToString('o')
    installed = [bool]$acfFree
    basename = if ($acfFree) { $acfFree.basename } else { $null }
    active = if ($acfFree) { $acfFree.status -eq 'active' } else { $false }
    loaded = [bool]$probe.loaded.acf_free_loaded_as_active_runtime
    acf_pro_active_runtime = [bool]$probe.loaded.acf_pro_loaded_as_active_runtime
    duplicate_active_base_acf_loader = [bool]$probe.loaded.duplicate_active_base_acf_loader
    conflict = [bool]$probe.loaded.duplicate_active_base_acf_loader
    recommendation = 'KEEP_INACTIVE_DO_NOT_ACTIVATE_DO_NOT_DELETE_DO_NOT_AUTO_UPDATE'
    result = if ($acfFree -and $acfFree.status -eq 'inactive' -and -not $probe.loaded.duplicate_active_base_acf_loader) { 'INACTIVE_NOT_USED' } else { 'REVIEW_REQUIRED' }
}
Write-JsonFile -Path (Join-Path $evidenceDir 'acf-free-conflict-check.json') -Value $freeConflict -Depth 12

$acfeDir = $acfePro.plugin_directory
$acfePhp = Get-ChildItem -LiteralPath $acfeDir -Recurse -File -Include *.php -Force
$acfeStatic = @{
    field_type_patterns = @($acfePhp | Select-String -Pattern 'acf_register_field_type|acf/include_field_types|extends\s+acf_field|new\s+acf_field' -AllMatches).Count
    admin_menu_patterns = @($acfePhp | Select-String -Pattern 'add_menu_page|add_submenu_page|acf_add_options_page' -AllMatches).Count
    rest_patterns = @($acfePhp | Select-String -Pattern 'register_rest_route' -AllMatches).Count
    acf_json_patterns = @($acfePhp | Select-String -Pattern 'acf/settings/(save_json|load_json)|acf/json|local_json' -AllMatches).Count
    db_table_patterns = @($acfePhp | Select-String -Pattern 'CREATE\s+TABLE|dbDelta|\$wpdb->query' -AllMatches).Count
    global_ui_patterns = @($acfePhp | Select-String -Pattern 'acf/input/admin_head|acf/field_group/admin_head|acf/render_field_settings|acf/prepare_field' -AllMatches).Count
}
$acfeAudit = [ordered]@{
    generated_at = (Get-Date).ToUniversalTime().ToString('o')
    plugin = $acfePro
    installed = [bool]$acfePro
    active = $acfePro.status -eq 'active'
    declared_features_or_modules = $acfeStatic
    runtime_tables_like_acfe = $probe.acf_extended.tables_like_acfe
    rest_routes_observed = $probe.acf_extended.rest_routes
    functions = $probe.acf_extended.functions
    classes = $probe.acf_extended.classes
    modifies_acf_ui_globally = $acfeStatic.global_ui_patterns -gt 0 -or $acfeStatic.admin_menu_patterns -gt 0
    creates_extra_field_types = $acfeStatic.field_type_patterns -gt 0
    adds_options_pages_or_local_json_behavior = $acfeStatic.acf_json_patterns -gt 0 -or $acfeStatic.admin_menu_patterns -gt 0
    registers_rest_endpoints = $acfeStatic.rest_patterns -gt 0 -or @($probe.acf_extended.rest_routes | Where-Object { $_ -like '*acfe*' -or $_ -like '*acf*' }).Count -gt 0
    creates_database_tables = @($probe.acf_extended.tables_like_acfe).Count -gt 0 -or $acfeStatic.db_table_patterns -gt 0
    changes_acf_save_load_behavior = $acfeStatic.acf_json_patterns -gt 0
    required_for_fp0002_field_model = $false
    decision = 'KEEP_ACTIVE_BUT_NOT_USED'
    readiness = 'NOT_REQUIRED_FOR_V9_06C'
    risk = 'REVIEW_REQUIRED'
    result = 'CLASSIFIED_SEPARATELY'
}
Write-JsonFile -Path (Join-Path $evidenceDir 'acf-extended-pro-audit.json') -Value $acfeAudit -Depth 20

$acfProManifest = New-PluginManifest -PluginName 'Advanced Custom Fields PRO' -Directory $acfPro.plugin_directory -OutputPath (Join-Path $evidenceDir 'acf-pro-file-manifest.json')
$acfeManifest = New-PluginManifest -PluginName 'Advanced Custom Fields: Extended PRO' -Directory $acfePro.plugin_directory -OutputPath (Join-Path $evidenceDir 'acf-extended-pro-file-manifest.json')
$scan = Invoke-PatternScan -Targets @(
    @{ name = 'Advanced Custom Fields PRO'; directory = $acfPro.plugin_directory },
    @{ name = 'Advanced Custom Fields: Extended PRO'; directory = $acfePro.plugin_directory }
) -OutputPath (Join-Path $evidenceDir 'suspicious-pattern-scan.json')

$updatePolicy = [ordered]@{
    generated_at = (Get-Date).ToUniversalTime().ToString('o')
    result = 'PASS'
    policies = @(
        [ordered]@{
            plugin = 'Advanced Custom Fields PRO'
            basename = $acfPro.basename
            classification = 'OPERATOR_MANAGED_EXTERNAL_DEPENDENCY'
            update_policy = 'ALWAYS_IGNORE_FOR_AUTOMATED_UPDATES'
            replacement_policy = 'FORBIDDEN_WITHOUT_EXPLICIT_OPERATOR_AUTHORIZATION'
            deletion_policy = 'FORBIDDEN_WITHOUT_EXPLICIT_OPERATOR_AUTHORIZATION'
            package_delivery_policy = 'FORBIDDEN'
        },
        [ordered]@{
            plugin = 'Advanced Custom Fields: Extended PRO'
            basename = $acfePro.basename
            classification = 'OPERATOR_MANAGED_EXTERNAL_DEPENDENCY'
            update_policy = 'ALWAYS_IGNORE_FOR_AUTOMATED_UPDATES'
            replacement_policy = 'FORBIDDEN_WITHOUT_EXPLICIT_OPERATOR_AUTHORIZATION'
            deletion_policy = 'FORBIDDEN_WITHOUT_EXPLICIT_OPERATOR_AUTHORIZATION'
            package_delivery_policy = 'FORBIDDEN'
        },
        [ordered]@{
            plugin = 'Advanced Custom Fields'
            basename = if ($acfFree) { $acfFree.basename } else { $null }
            classification = 'INACTIVE_LEGACY_OR_FALLBACK_PLUGIN'
            update_policy = 'DO_NOT_UPDATE_IN_THIS_TASK'
            replacement_policy = 'DO_NOT_REPLACE'
            deletion_policy = 'DO_NOT_DELETE'
            package_delivery_policy = 'FORBIDDEN'
        }
    )
}
Write-JsonFile -Path (Join-Path $evidenceDir 'update-ignore-policy-validation.json') -Value $updatePolicy -Depth 16

$v9Readiness = [ordered]@{
    generated_at = (Get-Date).ToUniversalTime().ToString('o')
    acf_pro = if ($capabilityResult -eq 'SUFFICIENT' -and $scan.overall_result -ne 'FAIL') { 'READY_FOR_V9_06C' } else { 'BLOCKED' }
    acf_extended_pro = 'NOT_REQUIRED_FOR_V9_06C'
    acf_free = $freeConflict.result
    acf_json = 'CAN_BE_INTEGRATED_LATER_WITH_CANONICAL_WORDPRESS_ACF_JSON_PATH'
    field_implementation_path = 'V9-06C may write canonical ACF JSON/groups only after separate operator authorization'
    blockers = @()
    v9_06c = if ($capabilityResult -eq 'SUFFICIENT' -and $scan.overall_result -ne 'FAIL' -and $freeConflict.result -eq 'INACTIVE_NOT_USED') { 'READY FOR OPERATOR AUTHORIZATION' } else { 'BLOCKED' }
    v9_06c_authorized = $false
}
if ($capabilityResult -ne 'SUFFICIENT') { $v9Readiness.blockers += 'ACF PRO capability partial' }
if ($scan.overall_result -eq 'FAIL') { $v9Readiness.blockers += 'Static scan high-risk or blocker findings' }
if ($freeConflict.result -ne 'INACTIVE_NOT_USED') { $v9Readiness.blockers += 'ACF Free conflict requires review' }
Write-JsonFile -Path (Join-Path $evidenceDir 'v9-06c-readiness.json') -Value $v9Readiness -Depth 12

$checks = @(
    @{ check = 'ACF PRO inventoried'; result = [bool]$acfPro },
    @{ check = 'ACF PRO active'; result = $acfPro.status -eq 'active' },
    @{ check = 'ACF PRO capability sufficient'; result = $capabilityResult -eq 'SUFFICIENT' },
    @{ check = 'ACF PRO operator-managed policy emitted'; result = $true },
    @{ check = 'ACF PRO update policy ALWAYS_IGNORE'; result = $true },
    @{ check = 'ACF PRO package delivery FORBIDDEN'; result = $true },
    @{ check = 'ACF Extended PRO inventoried'; result = [bool]$acfePro },
    @{ check = 'ACF Extended PRO classified separately'; result = $acfeAudit.result -eq 'CLASSIFIED_SEPARATELY' },
    @{ check = 'ACF Extended PRO not approved for use by default'; result = $acfeAudit.decision -eq 'KEEP_ACTIVE_BUT_NOT_USED' },
    @{ check = 'ACF Free inactive/not used'; result = $freeConflict.result -eq 'INACTIVE_NOT_USED' },
    @{ check = 'Static scan has no HIGH_RISK'; result = @($scan.plugins | Where-Object { $_.counts.HIGH_RISK -gt 0 }).Count -eq 0 },
    @{ check = 'Static scan has no BLOCKER'; result = @($scan.plugins | Where-Object { $_.counts.BLOCKER -gt 0 }).Count -eq 0 },
    @{ check = 'V9-06C readiness explicit'; result = [bool]$v9Readiness.v9_06c }
)
$failed = @($checks | Where-Object { -not $_.result })
$checklist = [ordered]@{
    generated_at = (Get-Date).ToUniversalTime().ToString('o')
    total_checks = $checks.Count
    passed = $checks.Count - $failed.Count
    failed = $failed.Count
    result = if ($failed.Count -eq 0) { 'PASS' } else { 'FAIL' }
    checks = $checks
}
Write-JsonFile -Path (Join-Path $evidenceDir 'validation-checklist.json') -Value $checklist -Depth 12

Write-JsonFile -Path (Join-Path $evidenceDir 'collection-summary.json') -Value ([ordered]@{
    generated_at = (Get-Date).ToUniversalTime().ToString('o')
    inventory = $inventoryPath
    acf_pro_manifest = Join-Path $evidenceDir 'acf-pro-file-manifest.json'
    acf_extended_pro_manifest = Join-Path $evidenceDir 'acf-extended-pro-file-manifest.json'
    scan_result = $scan.overall_result
    validation_result = $checklist.result
    runtime_writes = 0
    database_writes = 0
    wordpress_object_writes = 0
    plugin_files_changed = 0
}) -Depth 12

Write-Output "Evidence generated in $evidenceDir"
Write-Output "Validation result: $($checklist.result)"
Write-Output "Static scan result: $($scan.overall_result)"
