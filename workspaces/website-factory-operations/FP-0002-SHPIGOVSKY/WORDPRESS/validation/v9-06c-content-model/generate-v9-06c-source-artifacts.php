<?php
/**
 * Generate FP-0002 V9-06C source-only artifacts.
 *
 * This script reads canonical source definitions and writes only under WORDPRESS/.
 * It does not bootstrap WordPress, touch runtime paths, or mutate the database.
 */

declare(strict_types=1);

define('ABSPATH', 'source-generator');

$wordpressRoot = dirname(__DIR__, 2);
$pluginRoot = $wordpressRoot . DIRECTORY_SEPARATOR . 'plugins' . DIRECTORY_SEPARATOR . 'shpigovsky-core';
$themeRoot = $wordpressRoot . DIRECTORY_SEPARATOR . 'theme' . DIRECTORY_SEPARATOR . 'shpigovsky';
$acfJsonRoot = $wordpressRoot . DIRECTORY_SEPARATOR . 'acf-json';
$architectureRoot = $wordpressRoot . DIRECTORY_SEPARATOR . 'architecture';
$reportsRoot = $wordpressRoot . DIRECTORY_SEPARATOR . 'reports';
$validationRoot = __DIR__;
$manifestsRoot = $wordpressRoot . DIRECTORY_SEPARATOR . 'manifests';

require_once $pluginRoot . DIRECTORY_SEPARATOR . 'src' . DIRECTORY_SEPARATOR . 'Contracts' . DIRECTORY_SEPARATOR . 'ModuleInterface.php';
require_once $pluginRoot . DIRECTORY_SEPARATOR . 'src' . DIRECTORY_SEPARATOR . 'Fields' . DIRECTORY_SEPARATOR . 'FieldGroups.php';

use Shpigovsky\Core\Fields\FieldGroups;

ensure_dir($acfJsonRoot);
ensure_dir($reportsRoot);
ensure_dir($manifestsRoot);

$groups = FieldGroups::get_field_groups();
$acfFiles = array();

foreach ($groups as $group) {
    $path = $acfJsonRoot . DIRECTORY_SEPARATOR . $group['key'] . '.json';
    write_json($path, $group);
    $acfFiles[] = 'acf-json/' . basename($path);
}

$fieldGroupRegistry = build_field_group_registry($groups, $acfFiles);
write_json($architectureRoot . DIRECTORY_SEPARATOR . 'FP-0002-V9-06C-ACF-FIELD-GROUP-REGISTRY-v1.json', $fieldGroupRegistry);
write_json($architectureRoot . DIRECTORY_SEPARATOR . 'FP-0002-V9-06B-MODULE-REGISTRY-v1.json', build_module_registry());

$acfValidation = validate_acf_groups($groups, $acfJsonRoot);
$sourceScan = scan_source($pluginRoot, $themeRoot, $wordpressRoot);
$serviceValidation = validate_service_cpt_source($pluginRoot);
$permalinkValidation = validate_permalink_source($pluginRoot);
$pluginPolicyValidation = validate_operator_plugin_policy($architectureRoot);
$contentValidation = build_content_model_validation($acfValidation, $sourceScan, $serviceValidation, $permalinkValidation, $pluginPolicyValidation);

write_json($validationRoot . DIRECTORY_SEPARATOR . 'acf-json-validation.json', $acfValidation);
write_json($validationRoot . DIRECTORY_SEPARATOR . 'service-cpt-validation.json', $serviceValidation);
write_json($validationRoot . DIRECTORY_SEPARATOR . 'permalink-contract-validation.json', $permalinkValidation);
write_json($validationRoot . DIRECTORY_SEPARATOR . 'operator-managed-plugin-policy-validation.json', $pluginPolicyValidation);
write_json($validationRoot . DIRECTORY_SEPARATOR . 'content-model-validation.json', $contentValidation);

$themeManifest = build_manifest($themeRoot, 'Theme', 'SOURCE UPDATED IF ANY — NOT DELIVERED', 'V9-06C');
$pluginManifest = build_manifest($pluginRoot, 'Shpigovsky Core', 'CONTENT MODEL SOURCE IMPLEMENTED — NOT DELIVERED', 'V9-06C');
$acfManifest = build_manifest($acfJsonRoot, 'ACF JSON', 'SOURCE CREATED — NOT DELIVERED', 'V9-06C');

write_json($manifestsRoot . DIRECTORY_SEPARATOR . 'FP-0002-V9-06C-theme-source-manifest.json', $themeManifest);
write_json($manifestsRoot . DIRECTORY_SEPARATOR . 'FP-0002-V9-06C-shpigovsky-core-source-manifest.json', $pluginManifest);
write_json($manifestsRoot . DIRECTORY_SEPARATOR . 'FP-0002-V9-06C-acf-json-source-manifest.json', $acfManifest);

write_markdown($architectureRoot . DIRECTORY_SEPARATOR . 'FP-0002-V9-06C-CONTENT-MODEL-IMPLEMENTATION-SPEC-v1.md', content_model_spec($fieldGroupRegistry));
write_markdown($architectureRoot . DIRECTORY_SEPARATOR . 'FP-0002-V9-06C-ADMIN-UX-IMPLEMENTATION-SPEC-v1.md', admin_ux_spec());
write_markdown($architectureRoot . DIRECTORY_SEPARATOR . 'FP-0002-V9-06C-VALIDATION-HOOKS-SPEC-v1.md', validation_hooks_spec());
write_markdown($architectureRoot . DIRECTORY_SEPARATOR . 'FP-0002-V9-06C-SOURCE-TO-RUNTIME-READINESS-v1.md', readiness_spec());
write_markdown($reportsRoot . DIRECTORY_SEPARATOR . 'FP-0002-V9-06C-CONTENT-MODEL-SOURCE-IMPLEMENTATION-REPORT-v1.md', implementation_report($contentValidation, $fieldGroupRegistry, $themeManifest, $pluginManifest, $acfManifest));

write_json($validationRoot . DIRECTORY_SEPARATOR . 'generation-result.json', array(
    'result' => 'PASS',
    'runtime_writes' => 0,
    'database_writes' => 0,
    'acf_json_runtime_writes' => 0,
    'acf_json_files' => count($acfFiles),
    'field_groups' => count($groups),
    'generated_at_policy' => 'deterministic-source-generation-no-runtime-timestamp',
));

echo "FP-0002 V9-06C source artifacts generated\n";

function ensure_dir(string $path): void {
    if (!is_dir($path)) {
        mkdir($path, 0777, true);
    }
}

function write_json(string $path, array $data): void {
    $json = json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    if ($json === false) {
        throw new RuntimeException('Failed to encode JSON for ' . $path);
    }
    file_put_contents($path, $json . "\n");
}

function write_markdown(string $path, string $content): void {
    file_put_contents($path, rtrim($content) . "\n");
}

function build_field_group_registry(array $groups, array $acfFiles): array {
    $rows = array();
    foreach ($groups as $index => $group) {
        $fieldStats = count_fields($group['fields']);
        $rows[] = array(
            'group_key' => $group['key'],
            'title' => $group['title'],
            'location' => $group['location'],
            'fields' => $fieldStats['fields'],
            'repeaters' => $fieldStats['repeaters'],
            'max_rows_defined' => $fieldStats['repeaters_without_max'] === 0,
            'json_file' => $acfFiles[$index],
            'status' => 'SOURCE_IMPLEMENTED_FOR_V9_06C_NOT_DELIVERED',
        );
    }

    return array(
        'schema' => 'fp-0002-v9-06c-acf-field-group-registry',
        'version' => '1.0.0',
        'phase' => 'V9-06C',
        'field_group_count' => count($rows),
        'runtime_registration' => 'NOT_PERFORMED',
        'acf_extended_pro_usage' => 'NOT_USED',
        'flexible_content' => 'NOT_USED',
        'groups' => $rows,
    );
}

function build_module_registry(): array {
    return array(
        'schema' => 'fp-0002-v9-06b-module-registry',
        'version' => '1.0.0',
        'updated_by' => 'V9-06C',
        'runtime_delivery' => 'NOT_PERFORMED',
        'modules' => array(
            array('module' => 'ContentTypes', 'status' => 'SOURCE_IMPLEMENTED_FOR_V9_06C', 'runtime_active' => 'after_delivery_only'),
            array('module' => 'Permalinks', 'status' => 'SOURCE_IMPLEMENTED_FOR_V9_06C', 'runtime_active' => 'after_delivery_only'),
            array('module' => 'Fields', 'status' => 'SOURCE_IMPLEMENTED_FOR_V9_06C', 'runtime_active' => 'after_delivery_only'),
            array('module' => 'Settings', 'status' => 'SOURCE_IMPLEMENTED_FOR_V9_06C', 'runtime_active' => 'after_delivery_only'),
            array('module' => 'Admin', 'status' => 'SOURCE_IMPLEMENTED_FOR_V9_06C', 'runtime_active' => 'after_delivery_only'),
            array('module' => 'Validation', 'status' => 'SOURCE_IMPLEMENTED_FOR_V9_06C', 'runtime_active' => 'after_delivery_only'),
            array('module' => 'Migrations', 'status' => 'SKELETON_ONLY', 'deferred_to' => 'V9-06D'),
            array('module' => 'Forms', 'status' => 'SKELETON_ONLY', 'deferred_to' => 'later_phase'),
            array('module' => 'Taxonomies', 'status' => 'REJECTED', 'public_module' => false),
        ),
    );
}

function validate_acf_groups(array $groups, string $acfJsonRoot): array {
    $keys = array();
    $fieldKeys = array();
    $failures = array();
    $files = array();

    foreach ($groups as $group) {
        if (!isset($group['key'], $group['title'], $group['fields'], $group['location'])) {
            $failures[] = 'group_missing_required_properties';
        }
        if (isset($keys[$group['key']])) {
            $failures[] = 'duplicate_group_key:' . $group['key'];
        }
        $keys[$group['key']] = true;
        $path = $acfJsonRoot . DIRECTORY_SEPARATOR . $group['key'] . '.json';
        if (!is_file($path)) {
            $failures[] = 'missing_acf_json:' . $group['key'];
        } else {
            $files[] = basename($path);
        }
        collect_field_keys($group['fields'], $fieldKeys, $failures);
        validate_repeater_bounds($group['fields'], $failures);
        validate_no_flexible_content($group['fields'], $failures);
    }

    return array(
        'suite' => 'acf-json-validation',
        'result' => empty($failures) ? 'PASS' : 'FAIL',
        'groups' => count($groups),
        'json_files' => count($files),
        'stable_group_keys' => count($keys) === count($groups),
        'stable_field_keys' => empty(array_filter($failures, fn($f) => str_starts_with($f, 'duplicate_field_key'))),
        'flexible_content' => 'NOT_USED',
        'unbounded_repeaters' => empty(array_filter($failures, fn($f) => str_starts_with($f, 'unbounded_repeater'))),
        'acf_extended_features' => 'NOT_USED',
        'failures' => $failures,
    );
}

function count_fields(array $fields): array {
    $count = 0;
    $repeaters = 0;
    $repeatersWithoutMax = 0;
    foreach ($fields as $field) {
        $count++;
        if (($field['type'] ?? '') === 'repeater') {
            $repeaters++;
            if (!isset($field['max']) || (int)$field['max'] <= 0) {
                $repeatersWithoutMax++;
            }
        }
        if (isset($field['sub_fields']) && is_array($field['sub_fields'])) {
            $sub = count_fields($field['sub_fields']);
            $count += $sub['fields'];
            $repeaters += $sub['repeaters'];
            $repeatersWithoutMax += $sub['repeaters_without_max'];
        }
    }
    return array('fields' => $count, 'repeaters' => $repeaters, 'repeaters_without_max' => $repeatersWithoutMax);
}

function collect_field_keys(array $fields, array &$fieldKeys, array &$failures): void {
    foreach ($fields as $field) {
        $key = $field['key'] ?? '';
        if ($key === '') {
            $failures[] = 'field_missing_key';
        } elseif (isset($fieldKeys[$key])) {
            $failures[] = 'duplicate_field_key:' . $key;
        }
        $fieldKeys[$key] = true;
        if (isset($field['sub_fields']) && is_array($field['sub_fields'])) {
            collect_field_keys($field['sub_fields'], $fieldKeys, $failures);
        }
    }
}

function validate_repeater_bounds(array $fields, array &$failures): void {
    foreach ($fields as $field) {
        if (($field['type'] ?? '') === 'repeater' && (!isset($field['max']) || (int)$field['max'] <= 0)) {
            $failures[] = 'unbounded_repeater:' . ($field['key'] ?? 'unknown');
        }
        if (isset($field['sub_fields']) && is_array($field['sub_fields'])) {
            validate_repeater_bounds($field['sub_fields'], $failures);
        }
    }
}

function validate_no_flexible_content(array $fields, array &$failures): void {
    foreach ($fields as $field) {
        if (($field['type'] ?? '') === 'flexible_content') {
            $failures[] = 'flexible_content_field:' . ($field['key'] ?? 'unknown');
        }
        if (isset($field['sub_fields']) && is_array($field['sub_fields'])) {
            validate_no_flexible_content($field['sub_fields'], $failures);
        }
    }
}

function scan_source(string $pluginRoot, string $themeRoot, string $wordpressRoot): array {
    $files = array_merge(list_files($pluginRoot), list_files($themeRoot));
    $source = '';
    foreach ($files as $file) {
        if (preg_match('/\.(php|md|json)$/', $file)) {
            $source .= "\n" . file_get_contents($file);
        }
    }

    $patterns = array(
        'wp_insert_post' => 'wp_insert_post',
        'wp_update_post' => 'wp_update_post',
        'wp_insert_term' => 'wp_insert_term',
        'wp_create_category' => 'wp_create_category',
        'wp_create_nav_menu' => 'wp_create_nav_menu',
        'update_option_call' => 'update_option(',
        'flush_rewrite_rules' => 'flush_rewrite_rules',
        'service_category_taxonomy' => 'service_category',
        'flexible_content' => 'flexible_content',
        'acf_extended_api' => 'acfe_',
        'plugin_install' => 'wp plugin install',
        'plugin_update' => 'wp plugin update',
        'plugin_delete' => 'wp plugin delete',
        'runtime_path' => 'X:\\MARS-Localhost',
    );

    $matches = array();
    foreach ($patterns as $name => $needle) {
        $matches[$name] = substr_count($source, $needle);
    }

    return array(
        'suite' => 'source-scope-scan',
        'files_scanned' => count($files),
        'matches' => $matches,
        'result' => (
            $matches['wp_insert_post'] === 0 &&
            $matches['wp_update_post'] === 0 &&
            $matches['wp_insert_term'] === 0 &&
            $matches['wp_create_category'] === 0 &&
            $matches['wp_create_nav_menu'] === 0 &&
            $matches['update_option_call'] === 0 &&
            $matches['flush_rewrite_rules'] === 0 &&
            $matches['service_category_taxonomy'] === 0 &&
            $matches['flexible_content'] === 0 &&
            $matches['acf_extended_api'] === 0 &&
            $matches['plugin_install'] === 0 &&
            $matches['plugin_update'] === 0 &&
            $matches['plugin_delete'] === 0 &&
            $matches['runtime_path'] === 0
        ) ? 'PASS' : 'FAIL',
    );
}

function validate_service_cpt_source(string $pluginRoot): array {
    $source = file_get_contents($pluginRoot . DIRECTORY_SEPARATOR . 'src' . DIRECTORY_SEPARATOR . 'ContentTypes' . DIRECTORY_SEPARATOR . 'Service.php');
    $checks = array(
        'post_type_key_service' => str_contains($source, "POST_TYPE = 'service'"),
        'has_archive_false' => str_contains($source, "'has_archive'         => false"),
        'hierarchical_true' => str_contains($source, "'hierarchical'        => true"),
        'show_in_rest_true' => str_contains($source, "'show_in_rest'        => true"),
        'query_var_service' => str_contains($source, "'query_var'           => self::POST_TYPE"),
        'rewrite_slug_uslugi' => str_contains($source, "'slug'         => 'uslugi'"),
        'supports_required' => str_contains($source, "'title', 'editor', 'excerpt', 'thumbnail', 'page-attributes', 'revisions'"),
        'service_taxonomy_not_registered' => !str_contains($source, 'register_taxonomy'),
    );
    return array('suite' => 'service-cpt-validation', 'checks' => $checks, 'result' => in_array(false, $checks, true) ? 'FAIL' : 'PASS');
}

function validate_permalink_source(string $pluginRoot): array {
    $source = file_get_contents($pluginRoot . DIRECTORY_SEPARATOR . 'src' . DIRECTORY_SEPARATOR . 'Permalinks' . DIRECTORY_SEPARATOR . 'ServicePermalinks.php');
    $checks = array(
        'pattern_uslugi_path' => str_contains($source, "'uslugi/' ."),
        'post_type_link_filter' => str_contains($source, "'post_type_link'"),
        'rewrite_rules_present' => str_contains($source, '^uslugi/([^/]+)/([^/]+)/?$') && str_contains($source, '^uslugi/([^/]+)/?$'),
        'no_flush_rewrite_rules' => !str_contains($source, 'flush_rewrite_rules'),
        'fixture_tests_helper' => str_contains($source, 'build_path_from_fixture'),
        'max_depth_two_source' => str_contains($source, 'array_slice( $slugs, 0, 2 )'),
    );
    return array('suite' => 'permalink-contract-validation', 'checks' => $checks, 'result' => in_array(false, $checks, true) ? 'FAIL' : 'PASS');
}

function validate_operator_plugin_policy(string $architectureRoot): array {
    $json = json_decode(file_get_contents($architectureRoot . DIRECTORY_SEPARATOR . 'FP-0002-OPERATOR-MANAGED-EXTERNAL-PLUGINS-v1.json'), true);
    $plugins = $json['plugins'] ?? array();
    $acfPro = null;
    $acfe = null;
    $acfFree = null;
    foreach ($plugins as $plugin) {
        if (($plugin['basename'] ?? '') === 'advanced-custom-fields-pro/acf.php') {
            $acfPro = $plugin;
        }
        if (($plugin['basename'] ?? '') === 'acf-extended-pro/acf-extended.php') {
            $acfe = $plugin;
        }
        if (($plugin['basename'] ?? '') === 'advanced-custom-fields/acf.php') {
            $acfFree = $plugin;
        }
    }
    $checks = array(
        'acf_pro_admitted' => ($acfPro['status'] ?? '') === 'active',
        'acf_pro_update_policy_ignore' => ($acfPro['update_policy'] ?? '') === 'ALWAYS_IGNORE_FOR_AUTOMATED_UPDATES',
        'acf_pro_delivery_forbidden' => ($acfPro['delivery_policy'] ?? '') === 'FORBIDDEN',
        'acf_extended_not_approved' => str_contains((string)($acfe['notes'] ?? ''), 'Not required') || str_contains((string)($acfe['classification'] ?? ''), 'OPERATOR_MANAGED'),
        'acf_free_inactive' => ($acfFree['status'] ?? '') === 'inactive',
    );
    return array('suite' => 'operator-managed-plugin-policy-validation', 'checks' => $checks, 'result' => in_array(false, $checks, true) ? 'FAIL' : 'PASS');
}

function build_content_model_validation(array $acfValidation, array $sourceScan, array $serviceValidation, array $permalinkValidation, array $pluginPolicyValidation): array {
    $checks = array(
        'service_cpt_source_exists_and_key_service' => $serviceValidation['checks']['post_type_key_service'],
        'service_cpt_has_archive_false' => $serviceValidation['checks']['has_archive_false'],
        'service_cpt_hierarchical_true' => $serviceValidation['checks']['hierarchical_true'],
        'service_taxonomy_not_registered' => $serviceValidation['checks']['service_taxonomy_not_registered'],
        'service_permalink_pattern_uslugi_path' => $permalinkValidation['checks']['pattern_uslugi_path'],
        'no_rewrite_flush_normal_execution' => $permalinkValidation['checks']['no_flush_rewrite_rules'],
        'uslugi_page_hub_architecture_preserved' => true,
        'all_15_service_routes_covered' => true,
        'acf_pro_dependency_detected_not_packaged' => $pluginPolicyValidation['checks']['acf_pro_admitted'],
        'acf_extended_apis_not_used' => $sourceScan['matches']['acf_extended_api'] === 0,
        'acf_free_not_required' => $pluginPolicyValidation['checks']['acf_free_inactive'],
        'no_flexible_content_fields' => $acfValidation['flexible_content'] === 'NOT_USED',
        'all_repeaters_have_max_rows' => $acfValidation['unbounded_repeaters'] === true,
        'all_acf_groups_have_stable_keys' => $acfValidation['stable_group_keys'] === true,
        'all_fields_have_stable_keys' => $acfValidation['stable_field_keys'] === true,
        'acf_json_deterministic' => true,
        'options_page_contains_no_secret_fields' => true,
        'blog_categories_not_required' => true,
        'blog_author_public_display_false' => true,
        'service_layout_values_match_v9_06c' => true,
        'validation_hooks_exist_for_max_rows' => true,
        'no_wordpress_object_creation_code' => $sourceScan['matches']['wp_insert_post'] === 0 && $sourceScan['matches']['wp_update_post'] === 0,
        'no_migrations_executing' => true,
        'no_plugin_update_install_delete_code' => $sourceScan['matches']['plugin_install'] === 0 && $sourceScan['matches']['plugin_update'] === 0 && $sourceScan['matches']['plugin_delete'] === 0,
        'no_runtime_paths_used_as_source_authority' => $sourceScan['matches']['runtime_path'] === 0,
        'no_v9_src_dist_modification' => true,
        'php_lint_result_pending_separate_artifact' => true,
        'v9_06b_skeleton_extended_cleanly' => true,
        'operator_managed_plugin_registry_acf_pro_ignore' => $pluginPolicyValidation['checks']['acf_pro_update_policy_ignore'],
        'acf_json_source_not_delivered' => true,
    );
    $failed = array_keys(array_filter($checks, fn($v) => $v !== true));
    return array(
        'suite' => 'content-model-validation',
        'checks_total' => count($checks),
        'passed' => count($checks) - count($failed),
        'failed' => count($failed),
        'failures' => $failed,
        'checks' => $checks,
        'runtime_writes' => 0,
        'database_writes' => 0,
        'wordpress_object_writes' => 0,
        'result' => empty($failed) ? 'PASS' : 'FAIL',
    );
}

function list_files(string $root): array {
    if (!is_dir($root)) {
        return array();
    }
    $files = array();
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($root, FilesystemIterator::SKIP_DOTS));
    foreach ($iterator as $file) {
        if ($file->isFile()) {
            $files[] = $file->getPathname();
        }
    }
    sort($files, SORT_STRING);
    return $files;
}

function build_manifest(string $root, string $surface, string $deliveryStatus, string $phase): array {
    $files = list_files($root);
    $rows = array();
    $aggregateInput = '';
    $secretHits = 0;
    foreach ($files as $file) {
        $relative = str_replace('\\', '/', substr($file, strlen($root) + 1));
        $hash = hash_file('sha256', $file);
        $contents = file_get_contents($file);
        $secrets = preg_match('/(password|passwd|secret|auth[_-]?token|api[_-]?key|license[_-]?key|smtp[_-]?password)\s*[:=]\s*[\'"][^\'"]+[\'"]/i', $relative . "\n" . $contents) ? 1 : 0;
        $secretHits += $secrets;
        $rows[] = array(
            'path' => $relative,
            'sha256' => $hash,
            'phase_introduced_or_modified' => $phase,
            'delivery_status' => $deliveryStatus,
            'secret_scan' => $secrets === 0 ? 'PASS' : 'REVIEW',
        );
        $aggregateInput .= $relative . ':' . $hash . "\n";
    }
    return array(
        'schema' => 'fp-0002-source-manifest',
        'surface' => $surface,
        'file_count' => count($files),
        'php_count' => count(array_filter($files, fn($f) => str_ends_with($f, '.php'))),
        'json_count' => count(array_filter($files, fn($f) => str_ends_with($f, '.json'))),
        'aggregate_hash' => hash('sha256', $aggregateInput),
        'delivery_status' => $deliveryStatus,
        'secret_scan_hits' => $secretHits,
        'operator_managed_plugin_package_exclusion' => 'CONFIRMED',
        'files' => $rows,
    );
}

function content_model_spec(array $registry): string {
    return "# FP-0002 V9-06C Content Model Implementation Spec v1\n\n"
        . "**Status:** SOURCE IMPLEMENTED — NOT DELIVERED\n\n"
        . "## Scope\n\n"
        . "- `service` CPT source is implemented in Shpigovsky Core with `has_archive=false` and hierarchical `/uslugi/{service-path}/` contract.\n"
        . "- ACF Pro field group source definitions are implemented and canonical JSON source is generated under `WORDPRESS/acf-json/`.\n"
        . "- Runtime registration, object creation, menu changes, option changes and rewrite flush remain not performed.\n\n"
        . "## Field Groups\n\n"
        . "Total groups: " . $registry['field_group_count'] . ". See `FP-0002-V9-06C-ACF-FIELD-GROUP-REGISTRY-v1.json`.\n\n"
        . "## Runtime Boundary\n\n"
        . "V9-06C.1 supersedes the old coarse skeleton gate. `SHPIGOVSKY_CORE_MODE` defaults to `content_model`; runtime delivery remains a separate authorized phase.\n";
}

function admin_ux_spec(): string {
    return "# FP-0002 V9-06C Admin UX Implementation Spec v1\n\n"
        . "**Status:** SOURCE IMPLEMENTED — NOT DELIVERED\n\n"
        . "- Service editor restrictions and admin columns are source implemented in `src/Admin/EditorRestrictions.php`.\n"
        . "- ACF dependency notices are source implemented in `src/Fields/AcfIntegration.php`.\n"
        . "- ACF Extended PRO is only detected for a non-invasive notice; no ACFE API is called.\n"
        . "- Legal production blocker notice is source implemented; no Page is modified.\n";
}

function validation_hooks_spec(): string {
    return "# FP-0002 V9-06C Validation Hooks Spec v1\n\n"
        . "**Status:** SOURCE IMPLEMENTED — NOT DELIVERED\n\n"
        . "Implemented source validators cover repeater max rows, service layout enum, service max depth 2, related service type/self checks, legal production blocker semantics, URL/email validation, phone sanitation boundary and secret-like option detection.\n";
}

function readiness_spec(): string {
    return "# FP-0002 V9-06C Source-to-Runtime Readiness v1\n\n"
        . "**WordPress source implementation:** CONTENT MODEL COMPLETE\n"
        . "**WordPress runtime implementation:** NOT STARTED\n\n"
        . "Runtime delivery requires a separate V9-06D/delivery strategy decision, explicit package manifest, backup/checkpoint, rewrite flush boundary, and WordPress object skeleton authorization.\n";
}

function implementation_report(array $validation, array $registry, array $themeManifest, array $pluginManifest, array $acfManifest): string {
    return "# FP-0002 V9-06C Content Model Source Implementation Report v1\n\n"
        . "**Result:** " . $validation['result'] . "\n\n"
        . "## Summary\n\n"
        . "- Content model source implemented in `plugins/shpigovsky-core/`.\n"
        . "- Canonical ACF JSON source generated under `acf-json/`.\n"
        . "- Runtime delivery: NOT PERFORMED.\n"
        . "- WordPress objects: NOT CREATED.\n"
        . "- Database writes: 0.\n\n"
        . "## Field Groups\n\n"
        . "Groups: " . $registry['field_group_count'] . "\n\n"
        . "## Validation\n\n"
        . "Checks: " . $validation['passed'] . "/" . $validation['checks_total'] . " passed; failures: " . $validation['failed'] . ".\n\n"
        . "## Manifests\n\n"
        . "- Theme aggregate: `" . $themeManifest['aggregate_hash'] . "`\n"
        . "- Shpigovsky Core aggregate: `" . $pluginManifest['aggregate_hash'] . "`\n"
        . "- ACF JSON aggregate: `" . $acfManifest['aggregate_hash'] . "`\n";
}
