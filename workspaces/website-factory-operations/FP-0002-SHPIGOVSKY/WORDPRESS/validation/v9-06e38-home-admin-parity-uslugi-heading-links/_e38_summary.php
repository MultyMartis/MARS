<?php
$j = json_decode(file_get_contents('X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e38-home-admin-parity-uslugi-heading-links/e38-result.json'), true);
echo 'stripped=' . count($j['imsc42_stripped']) . "\n";
$trash = 0; $already = 0;
foreach ($j['fields_trashed'] as $t) {
  if (($t['action'] ?? '') === 'trash') { $trash++; }
  if (($t['action'] ?? '') === 'already_trash') { $already++; }
}
echo "trashed_new=$trash already=$already\n";
echo 'db_writes=' . $j['db_writes'] . "\n";
echo 'home_imsc42=' . $j['validation']['home_imsc42_count'] . "\n";
echo 'gallery_slides=' . $j['validation']['home_gallery_slides'] . "\n";
echo 'accordion=' . $j['validation']['accordion_groups'] . "\n";
echo "stripped_keys=\n";
foreach ($j['imsc42_stripped'] as $s) {
  echo '- ' . $s['meta_key'] . ' | ' . $s['before'] . ' => ' . $s['after'] . "\n";
}
echo "trashed_names=\n";
$names = array();
foreach ($j['fields_trashed'] as $t) {
  if (($t['action'] ?? '') === 'trash') {
    $names[$t['name'] . '|' . $t['key']] = true;
  }
}
foreach (array_keys($names) as $n) { echo "- $n\n"; }
