<?php
$ev = "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e62c-ocentre-service-admin-review-anchor-final-regression";
$j = json_decode(file_get_contents("$ev/db-writes.json"), true);
$csv = "scope,action,detail\n";
foreach ($j["writes"] as $w) {
  $csv .= ($w["scope"] ?? "") . "," . ($w["action"] ?? ($w["result"]["updated"] ?? "")) . "," . str_replace(array("\n",","), array(" ",";"), wp_json_encode($w, JSON_UNESCAPED_UNICODE)) . "\n";
}
file_put_contents("$ev/db-writes.csv", $csv);
echo "OK\n";
