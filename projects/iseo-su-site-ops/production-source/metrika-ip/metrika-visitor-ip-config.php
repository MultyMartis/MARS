<?php
/**
 * ISEO-SU Metrika visitor IP param — global feature switch.
 *
 * Kill switch: set "enabled" => false
 * When OFF: endpoint returns 204 / no IP; JS does not send ipaddress to Metrika.
 * Normal Yandex Metrika init / clickmap / Webvisor / goals remain unchanged.
 *
 * Do not commit secrets here. This file is intentionally minimal.
 */
if (!defined("ISEO_METRIKA_VISITOR_IP_CONFIG_LOADED")) {
    define("ISEO_METRIKA_VISITOR_IP_CONFIG_LOADED", true);
}

return array(
    // METRIKA_VISITOR_IP_ENABLED — set false to disable the addon globally.
    "enabled" => true,

    // Active production counter (discovered on i-seo.su; not Denis example 39163020).
    "counter_id" => 54287016,
);
