<?php
$home_id = (int) get_post_meta(4, 'home_clinic_landscape_image', true);
if ($home_id <= 0) { $home_id = 1239; }
$seed_ids = array(73, 77, 84);
$seeded = array();
foreach ($seed_ids as $pid) {
  $existing = get_post_meta($pid, 'section_clinic_landscape_image', true);
  $had = ('' !== $existing && null !== $existing && false !== $existing && 0 !== (int) $existing);
  if (!$had) {
    if (function_exists('update_field')) {
      update_field('section_clinic_landscape_image', $home_id, $pid);
    } else {
      update_post_meta($pid, 'section_clinic_landscape_image', $home_id);
      update_post_meta($pid, '_section_clinic_landscape_image', 'field_fp02_section_clinic_landscape_image');
    }
  }
  $seeded[] = array(
    'post_id' => $pid,
    'had_value' => $had,
    'value_after' => (int) get_post_meta($pid, 'section_clinic_landscape_image', true),
    'footer_meta' => get_post_meta($pid, 'section_program_footer_label', true),
    'post_content_len' => strlen((string) get_post($pid)->post_content),
  );
}

// Refresh local ACF field group registration inventory
$group = null;
if (class_exists('Shpigovsky\\Core\\Fields\\ServiceSectionParity')) {
  $group = \Shpigovsky\Core\Fields\ServiceSectionParity::group();
}
$names = array();
if (is_array($group) && !empty($group['fields'])) {
  foreach ($group['fields'] as $f) {
    $names[] = isset($f['name']) ? $f['name'] : '';
  }
}

$out = array(
  'home_landscape_id' => $home_id,
  'seeded' => $seeded,
  'has_footer_field' => in_array('section_program_footer_label', $names, true),
  'has_section_landscape_image' => in_array('section_clinic_landscape_image', $names, true),
  'landscape_notice' => '',
  'field_count' => count($names),
);
foreach (($group['fields'] ?? array()) as $f) {
  if (($f['name'] ?? '') === 'section_clinic_landscape_notice') {
    $out['landscape_notice'] = wp_strip_all_tags($f['message'] ?? '');
  }
}

// FE resolve check for #73
$img = function_exists('shpigovsky_section_image_or_asset')
  ? shpigovsky_section_image_or_asset(73, 'section_clinic_landscape_image', 'img/content/pre-reviews/shpigovsky-clinic-landscape.webp', 'alt', 1139, 584)
  : null;
$out['resolve_73'] = $img;

file_put_contents('X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/_v9-06e46-fix04-seed-result.json', wp_json_encode($out, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT));
echo wp_json_encode($out, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT), "\n";
