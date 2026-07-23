<?php
// Путь к файлу
//$import_directory = DIR_ROOT . '1c_exchange/'; 

$import_directory = DIR_ROOT . '1c_incoming/webdata/'; 

$files = glob($import_directory . 'import0_*.xml');

if (empty($files)) {
    echo "Файлы для импорта не найдены в директории " . $import_directory;
    return false;
}

// Справочник: 'имя в 1с' => 'имя на сайте'
$manual_map = [
    'ванны моечные' => 'Моечные ванны',
    // ... другие пары
];

// Справочник атрибутов 1С - сайт
$manual_attr_map_raw = [
    '55 Количество' => 'Количество',
    '41 Тип крепления' => 'Тип крепления',
    '49 Упаковка (Длина, мм)' => 'Упаковка (Длина, мм)',
    '56 Производитель' => 'Производитель',
    '04 Выгрузка' => 'Выгрузка',
    
    '51 Упаковка (Ширина, мм)' => 'Упаковка (Ширина, мм)',
    '48 Упаковка (Высота, мм)' => 'Упаковка (Высота, мм)',
    '47 Упаковка (вес брутто, кг)' => 'Количество',
    '02 Вес (нетто, кг)' => 'Вес (нетто, кг)',
    '57 Комплект отгрузки' => 'Комплект отгрузки',
    '21 Обвязка' => 'Обвязка',
    '01 В комплекте' => 'В комплекте',
];


sort($files);
echo "Найдено файлов для обработки: " . count($files) . "<br>";

$processed_product_ids = [];



// 3. Запускаем цикл по всем найденным файлам
foreach ($files as $file) {
    echo "<b>Начало обработки файла: " . basename($file) . "</b><br>";

    if (!file_exists($file)) {
        echo "Файл пропал в процессе обработки: " . $file . "<br>";
        continue;
    }

    // Загружаем текущий XML-файл в итерации
    $xml = simplexml_load_file($file);
    
    if (!$xml) {
        echo "Ошибка чтения XML в файле: " . basename($file) . "<br>";
        continue;
    }

// === MARS SITE-002-PROD-1C-IMPORTER-GUID-PATH-PATCH-01 BEGIN ===
// Category resolution: GUID map -> path hash -> DB full path -> safe leaf (non-collision) -> review
// Auto-create DISABLED in Phase A (report-only).
$mars_1c_category_auto_create = false;
$mars_legacy_collision_ids = array(154, 159, 165);
$mars_legacy_root_id = 153;
$mars_tech_path_marker = 'ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ';
$mars_lang_id = (int)$this->config->get('config_language_id');

$mars_map_by_guid = array();
$mars_map_by_path_hash = array();
$mars_map_q = $this->db->query(
    "SELECT source_group_id, source_full_path, source_full_path_hash, category_id FROM " . DB_PREFIX . "mars_1c_category_map WHERE status = 'active'"
);
if ($mars_map_q->num_rows) {
    foreach ($mars_map_q->rows as $row) {
        $gid = (string)$row['source_group_id'];
        $cid = (int)$row['category_id'];
        if ($gid !== '') {
            $mars_map_by_guid[$gid] = $cid;
        }
        $ph = (string)$row['source_full_path_hash'];
        if ($ph !== '') {
            $mars_map_by_path_hash[$ph] = $cid;
        }
    }
}

$mars_category_active = array();
$mars_category_paths = array(); // category_id => set of path_ids
$mars_fullpath_to_id = array(); // normalized "name > name" => category_id (unique only)
$mars_fullpath_counts = array();

$oc_categories = array();
$oc_categories_multi = array(); // name => list of category_ids
$query = $this->db->query("SELECT cd.category_id, cd.name, c.status, c.parent_id FROM " . DB_PREFIX . "category_description cd LEFT JOIN " . DB_PREFIX . "category c ON (c.category_id = cd.category_id) WHERE cd.language_id = '" . $mars_lang_id . "'");
foreach ($query->rows as $row) {
    $cid = (int)$row['category_id'];
    $n = mb_strtolower(trim($row['name']));
    $oc_categories[$n] = $cid;
    if (!isset($oc_categories_multi[$n])) {
        $oc_categories_multi[$n] = array();
    }
    $oc_categories_multi[$n][] = $cid;
    if ((int)$row['status'] == 1) {
        $mars_category_active[$cid] = true;
    }
}

$cp_q = $this->db->query("SELECT category_id, path_id, level FROM " . DB_PREFIX . "category_path ORDER BY category_id, level");
foreach ($cp_q->rows as $row) {
    $cid = (int)$row['category_id'];
    $pid = (int)$row['path_id'];
    if (!isset($mars_category_paths[$cid])) {
        $mars_category_paths[$cid] = array();
    }
    $mars_category_paths[$cid][$pid] = true;
}

// Build OC full path name strings for exact match fallback (single query)
$mars_path_names = array(); // category_id => [level => name]
$lq = $this->db->query("SELECT cp.category_id, cp.level, cd.name FROM " . DB_PREFIX . "category_path cp LEFT JOIN " . DB_PREFIX . "category_description cd ON (cd.category_id = cp.path_id AND cd.language_id = '" . $mars_lang_id . "') ORDER BY cp.category_id, cp.level ASC");
foreach ($lq->rows as $lr) {
    $cid = (int)$lr['category_id'];
    if (!isset($mars_path_names[$cid])) {
        $mars_path_names[$cid] = array();
    }
    $mars_path_names[$cid][(int)$lr['level']] = trim($lr['name']);
}
foreach ($mars_path_names as $cid => $by_level) {
    ksort($by_level);
    $names = array_values($by_level);
    if ($names) {
        $fp = implode(' > ', $names);
        $fp_norm = mb_strtolower($fp);
        if (!isset($mars_fullpath_counts[$fp_norm])) {
            $mars_fullpath_counts[$fp_norm] = 0;
            $mars_fullpath_to_id[$fp_norm] = $cid;
        }
        $mars_fullpath_counts[$fp_norm]++;
    }
}
foreach ($mars_fullpath_counts as $fp_norm => $cnt) {
    if ($cnt > 1) {
        unset($mars_fullpath_to_id[$fp_norm]);
    }
}

$mars_is_legacy_collision = function($source_full_path, $candidate_category_id) use ($mars_legacy_collision_ids, $mars_legacy_root_id, $mars_tech_path_marker, $mars_category_paths) {
    $cid = (int)$candidate_category_id;
    $path_u = mb_strtoupper(trim((string)$source_full_path));
    $marker_u = mb_strtoupper($mars_tech_path_marker);
    $under_tech = ($path_u === $marker_u) || (mb_strpos($path_u, $marker_u . ' >') === 0) || (mb_strpos($path_u, $marker_u . '>') === 0);
    if (!$under_tech) {
        return false;
    }
    if (in_array($cid, $mars_legacy_collision_ids, true)) {
        return true;
    }
    if (isset($mars_category_paths[$cid][$mars_legacy_root_id])) {
        return true;
    }
    return false;
};

$mars_log = function($code, $msg) {
    echo $code . ': ' . $msg . "<br>\n";
};

$map_1c_to_oc = array();
$mars_category_resolution = array();
$mars_category_review = array();

$parseGroups = function($groups, $parentId = 0, $pathParts = array()) use (
    &$parseGroups,
    &$map_1c_to_oc,
    &$oc_categories,
    &$mars_category_resolution,
    &$mars_category_review,
    $manual_map,
    $mars_map_by_guid,
    $mars_map_by_path_hash,
    $mars_fullpath_to_id,
    $mars_category_active,
    $mars_is_legacy_collision,
    $mars_1c_category_auto_create,
    $mars_log,
    $oc_categories_multi
) {
    foreach ($groups->Группа as $item) {
        $id1c = (string)$item->Ид;
        $name1c = (string)$item->Наименование;
        $nameLower = mb_strtolower(trim($name1c));
        $searchName = isset($manual_map[$nameLower]) ? mb_strtolower($manual_map[$nameLower]) : $nameLower;
        $pathPartsNext = array_merge($pathParts, array(trim($name1c)));
        $source_full_path = implode(' > ', $pathPartsNext);
        $source_full_path_hash = hash('sha256', $source_full_path);
        $source_full_path_norm = mb_strtolower($source_full_path);
        $resolved = null;
        $method = '';

        if (isset($mars_map_by_guid[$id1c])) {
            $cand = (int)$mars_map_by_guid[$id1c];
            if (!$mars_is_legacy_collision($source_full_path, $cand)) {
                $resolved = $cand;
                $method = 'GUID_MATCH';
                $mars_log('MARS_CATEGORY_GUID_MATCH', $id1c . ' => ' . $cand . ' path=' . $source_full_path);
            } else {
                $mars_log('MARS_CATEGORY_COLLISION_GUARD_BLOCKED', 'GUID map candidate ' . $cand . ' blocked for ' . $source_full_path);
            }
        }

        if ($resolved === null && isset($mars_map_by_path_hash[$source_full_path_hash])) {
            $cand = (int)$mars_map_by_path_hash[$source_full_path_hash];
            if (!$mars_is_legacy_collision($source_full_path, $cand)) {
                $resolved = $cand;
                $method = 'PATH_MATCH';
                $mars_log('MARS_CATEGORY_PATH_MATCH', $source_full_path . ' => ' . $cand);
            } else {
                $mars_log('MARS_CATEGORY_COLLISION_GUARD_BLOCKED', 'path-hash candidate ' . $cand . ' blocked for ' . $source_full_path);
            }
        }

        if ($resolved === null && isset($mars_fullpath_to_id[$source_full_path_norm])) {
            $cand = (int)$mars_fullpath_to_id[$source_full_path_norm];
            if (!$mars_is_legacy_collision($source_full_path, $cand)) {
                $resolved = $cand;
                $method = 'FULLPATH_DB_MATCH';
                $mars_log('MARS_CATEGORY_FULLPATH_DB_MATCH', $source_full_path . ' => ' . $cand);
            } else {
                $mars_log('MARS_CATEGORY_COLLISION_GUARD_BLOCKED', 'DB fullpath candidate ' . $cand . ' blocked for ' . $source_full_path);
            }
        }

        if ($resolved === null && isset($oc_categories[$searchName])) {
            $cand = (int)$oc_categories[$searchName];
            $multi = isset($oc_categories_multi[$searchName]) ? $oc_categories_multi[$searchName] : array($cand);
            $ambiguous = count(array_unique($multi)) > 1;
            if ($mars_is_legacy_collision($source_full_path, $cand) || $ambiguous) {
                $mars_log('MARS_CATEGORY_COLLISION_GUARD_BLOCKED', 'leaf-name candidate ' . $cand . ' blocked/ambiguous for ' . $source_full_path);
                $mars_log('MARS_CATEGORY_REVIEW_REQUIRED', 'group ' . $id1c . ' name=' . $name1c . ' leaf-only unsafe');
                $mars_category_review[$id1c] = array(
                    'name' => $name1c,
                    'path' => $source_full_path,
                    'candidate' => $cand,
                    'reason' => $ambiguous ? 'AMBIGUOUS_LEAF' : 'LEGACY_COLLISION'
                );
            } else {
                $resolved = $cand;
                $method = 'LEAF_NAME_SAFE';
                $mars_log('MARS_CATEGORY_LEAF_SAFE', $name1c . ' => ' . $cand);
            }
        }

        if ($resolved === null) {
            if ($mars_1c_category_auto_create) {
                $mars_log('MARS_CATEGORY_CREATE_DRYRUN', 'would create under parent OC ' . (int)$parentId . ' name=' . $name1c);
            } else {
                $mars_log('MARS_CATEGORY_CREATE_DISABLED', 'group ' . $id1c . ' path=' . $source_full_path);
            }
            if (!isset($mars_category_review[$id1c])) {
                $mars_log('MARS_CATEGORY_REVIEW_REQUIRED', 'unresolved group ' . $id1c . ' path=' . $source_full_path);
                $mars_category_review[$id1c] = array(
                    'name' => $name1c,
                    'path' => $source_full_path,
                    'candidate' => 0,
                    'reason' => 'UNRESOLVED'
                );
            }
        } else {
            $map_1c_to_oc[$id1c] = (int)$resolved;
            $mars_category_resolution[$id1c] = array(
                'category_id' => (int)$resolved,
                'method' => $method,
                'path' => $source_full_path
            );
            $mars_log('MARS_PRODUCT_CATEGORY_RESOLVED', 'group ' . $id1c . ' => ' . (int)$resolved . ' via ' . $method);
        }

        $nextParent = isset($map_1c_to_oc[$id1c]) ? (int)$map_1c_to_oc[$id1c] : (int)$parentId;
        if (isset($item->Группы)) {
            $parseGroups($item->Группы, $nextParent, $pathPartsNext);
        }
    }
};

if (isset($xml->Классификатор->Группы)) {
    $parseGroups($xml->Классификатор->Группы);
    $this->xml_ids['categories'] = $map_1c_to_oc;
    $this->xml_ids['category_resolution'] = $mars_category_resolution;
    $this->xml_ids['category_review'] = $mars_category_review;
}

echo "Группы обработаны. Найдено соответствий: " . count(array_filter($map_1c_to_oc)) . "; review=" . count($mars_category_review);
// === MARS SITE-002-PROD-1C-IMPORTER-GUID-PATH-PATCH-01 END ===



// Функция для формирования filter_name





// 1. Получаем существующие атрибуты OC (name -> attribute_id)
$oc_attributes = [];
$query = $this->db->query("SELECT attribute_id, name FROM " . DB_PREFIX . "attribute_description WHERE language_id = '" . (int)$this->config->get('config_language_id') . "'");
foreach ($query->rows as $row) {
    $oc_attributes[mb_strtolower(trim($row['name']))] = $row['attribute_id'];
}

$clearStr = function($str) {
    $str = str_replace(chr(194).chr(160), ' ', $str); // Удаляем UTF-8 неразрывный пробел
    return mb_strtolower(trim(preg_replace('/\s+/', ' ', $str))); // Схлопываем пробелы до одного
};

// 2. Группа атрибутов по умолчанию (создайте "Характеристики", если её нет)
$attribute_group_id = 13; 

$properties_map = []; // Ид (1С) => attribute_id (OC)
$values_map = [];     // ИдЗначения (1С) => Текст значения

$manual_attr_map = [];
foreach ($manual_attr_map_raw as $key => $val) {
    $manual_attr_map[$clearStr($key)] = $val;
}

if (isset($xml->Классификатор->Свойства->Свойство)) {
foreach ($xml->Классификатор->Свойства->Свойство as $prop) {
    $id1c = (string)$prop->Ид;
    $name1c = (string)$prop->Наименование;
    $nameClean = $clearStr($name1c);

    // 1. Маппинг имени
    $cleanName = isset($manual_attr_map[$nameClean]) ? $manual_attr_map[$nameClean] : $name1c;
    $cleanNameLower = $clearStr($cleanName); // "тип крепления"

    // 2. Поиск или создание атрибута
    if (isset($oc_attributes[$cleanNameLower])) {
        $attr_id = $oc_attributes[$cleanNameLower];
    } else {
        $this->db->query("INSERT INTO " . DB_PREFIX . "attribute SET attribute_group_id = '" . (int)$attribute_group_id . "', sort_order = 0");
        $attr_id = $this->db->getLastId();
        
        $filter_name = $this->translit($cleanName);
        
        $this->db->query("INSERT INTO " . DB_PREFIX . "attribute_description SET 
            attribute_id = '" . (int)$attr_id . "', 
            language_id = '" . (int)$this->config->get('config_language_id') . "', 
            name = '" . $this->db->escape($cleanName) . "',
            filter_name = '" . $this->db->escape($filter_name) . "'");
        
        $oc_attributes[$cleanNameLower] = $attr_id;
    }

    $properties_map[$id1c] = $attr_id;

    // 3. Сбор значений справочника
    if (isset($prop->ВариантыЗначений->Справочник)) {
        foreach ($prop->ВариантыЗначений->Справочник as $val) {
            $values_map[(string)$val->ИдЗначения] = (string)$val->Значение;
        }
    }
}

$this->xml_ids['attributes'] = $properties_map;
$this->xml_ids['attribute_values'] = $values_map;
}

$cache_file = DIR_CACHE . '1c_classifier_map.json';

if (isset($xml->Классификатор)) {
    // Если классификатор пришел в текущем файле (как в 1.txt), записываем его в файл кэша
    $classifier_data = [
        'categories'       => $this->xml_ids['categories'],
        'attributes'       => $this->xml_ids['attributes'],
        'attribute_values' => $this->xml_ids['attribute_values']
    ];
    file_put_contents($cache_file, json_encode($classifier_data));
    echo " Классификатор сохранен в кэш. ";
} else {
    // Если классификатора в файле НЕТ (как в 2.txt), подгружаем его из кэша!
    if (file_exists($cache_file)) {
        $classifier_data = json_decode(file_get_contents($cache_file), true);
        $this->xml_ids['categories']       = $classifier_data['categories'] ?? [];
        $this->xml_ids['attributes']       = $classifier_data['attributes'] ?? [];
        $this->xml_ids['attribute_values'] = $classifier_data['attribute_values'] ?? [];
        echo " Классификатор успешно загружен из кэша. ";
    } else {
        echo " Внимание: Файл изменений, но кэш классификатора не найден! ";
    }
}


echo "   Свойства обработаны. Всего: " . count($properties_map);

// Создаем карту: [xml_id => product_id]
$existing_products = [];
$query = $this->db->query("SELECT product_id, xml_id FROM " . DB_PREFIX . "product WHERE xml_id IS NOT NULL AND xml_id <> ''");

foreach ($query->rows as $row) {
    $existing_products[$row['xml_id']] = $row['product_id'];
}

$target_xml_ids = array(
    'b767cb10-d552-11e5-84ef-60a44cac3e7c', // ID товаров для теста
     '1e812008-df21-11e3-94f9-60a44cac3e7c',
     '1b31c3d1-aaf1-11e6-84cc-60a44cac3e7c',
     '1ace2dd6-48cb-11e6-98dc-60a44cac3e7c',
     '0901b28e-df21-11e3-94f9-60a44cac3e7c',
    
);

$created = 0;
$updated = 0;

foreach ($xml->Каталог->Товары->Товар as $item) {
    $xml_id = (string)$item->Ид;
    
    // Если в Ид есть решетка (характеристика), берем только Ид товара
    if (strpos($xml_id, '#') !== false) {
        $parts = explode('#', $xml_id);
        $xml_id = $parts[0];
    }

 
    //if ( !in_array($xml_id, $target_xml_ids) ) continue; //тесты


    if (isset($existing_products[$xml_id])) {
        // ТОВАР НАЙДЕН — ОБНОВЛЯЕМ
        $product_id = $existing_products[$xml_id];  // echo " Обновляем ".$xml_id;
        $this->processProduct1C($product_id, $item, 'update');
        $updated++;
    } else {
        // ТОВАР НОВЫЙ — СОЗДАЕМ
        $product_id = $this->processProduct1C(0, $item, 'insert'); // echo " Создаем ".$xml_id;
        $existing_products[$xml_id] = $product_id; // Добавляем в кеш, чтобы избежать дублей в рамках одного файла
        $created++;
    }
    $processed_product_ids[] = $product_id;
}


echo "Создано ".$created." Обновлено ".$updated."  ";




$fullImport = ((string)$xml->Каталог['СодержитТолькоИзменения'] === 'false');
if ($fullImport && !empty($processed_product_ids)) {
    // Выключаем все товары, которые имеют xml_id, но не попали в текущую выгрузку
    $this->db->query("UPDATE " . DB_PREFIX . "product SET status = 0 WHERE xml_id IS NOT NULL AND xml_id <> '' AND product_id NOT IN (" . implode(',', array_map('intval', $processed_product_ids)) . ")");
    
    echo "Неактуальные товары скрыты.";
}

echo "<b>Файл " . basename($file) . " успешно обработан.</b><br><br>";
unset($xml); // Уничтожаем XML-объект текущего файла
gc_collect_cycles();
}//Раш по файлам

// --- Очистка кэша SeoPro ---
$cache_dir = DIR_CACHE; 
$seo_pro_cache = $cache_dir . 'cache.seo_pro';

// Проверяем наличие файлов кэша SeoPro
$files = glob($cache_dir . 'cache.seo_pro.*');

if ($files) {
    foreach ($files as $file) {
        if (is_file($file)) {
            unlink($file);
        }
    }
    echo "Кэш SeoPro успешно очищен.<br>";
}

// На всякий случай чистим и общий кэш запросов к БД, 
// так как там могут быть старые данные по товарам
$product_cache = glob($cache_dir . 'cache.product.*');
if ($product_cache) {
    foreach ($product_cache as $file) {
        unlink($file);
    }
}

$itsOK = true;