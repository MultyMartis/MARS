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

// 1. Получаем все существующие категории OC для сопоставления по имени
$oc_categories = [];
$query = $this->db->query("SELECT category_id, name FROM " . DB_PREFIX . "category_description WHERE language_id = '" . (int)$this->config->get('config_language_id') . "'");
foreach ($query->rows as $row) {
    $oc_categories[mb_strtolower($row['name'])] = $row['category_id'];
}

// 2. Рекурсивная функция парсинга
$map_1c_to_oc = []; // Здесь сохраним Ид (1С) => category_id (OC)

$parseGroups = function($groups, $parentId = 0) use (&$parseGroups, &$map_1c_to_oc, $oc_categories, $manual_map) {
    foreach ($groups->Группа as $item) {
        $id1c = (string)$item->Ид;
        $name1c = (string)$item->Наименование;
        $nameLower = mb_strtolower(trim($name1c));

        // 1. Ищем в справочнике, если нет - берем родное имя 1С
        $searchName = isset($manual_map[$nameLower]) ? mb_strtolower($manual_map[$nameLower]) : $nameLower;

        if (isset($oc_categories[$searchName])) {
            $map_1c_to_oc[$id1c] = $oc_categories[$searchName];
        } else {
            // 2. Создаем категорию, если не нашли
            $category_data = [
                'parent_id' => $parentId,
                'top' => ($parentId == 0 ? 1 : 0),
                'column' => 1,
                'sort_order' => 0,
                'status' => 1,
                'category_description' => [
                    $this->config->get('config_language_id') => [
                        'name' => $name1c,
                        'meta_title' => $name1c,
                        'meta_description' => '',
                        'meta_keyword' => '',
                        'description' => ''
                    ]
                ],
                'category_store' => [0]
            ];


            
            $new_id = $this->model_catalog_cronjob->addCategory($category_data);
           $map_1c_to_oc[$id1c] = $new_id;

           $keyword = $this->translit($name1c); 
           $this->db->query("INSERT INTO " . DB_PREFIX . "seo_url SET         store_id = 0,         language_id = '" . (int)$this->config->get('config_language_id') . "',         query = 'category_id=" . (int)$new_id . "',         keyword = '" . $this->db->escape($keyword) . "'");
            
           // Обновляем локальный кеш имен, чтобы не плодить дубли в одном цикле
           $oc_categories[$nameLower] = $new_id;
        }

        if (isset($item->Группы)) {
            $parseGroups($item->Группы, $map_1c_to_oc[$id1c]); // передаем созданный OC ID как родителя
        }
    }
};

// Запуск
if (isset($xml->Классификатор->Группы)) {
    $parseGroups($xml->Классификатор->Группы);
    $this->xml_ids['categories'] = $map_1c_to_oc;
}


echo "Группы обработаны. Найдено соответствий: " . count(array_filter($map_1c_to_oc));


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