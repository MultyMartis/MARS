   <?php

   $manufacturer_id = 11; // Заданный ID
   
    $xml_id = (string)$xml_item->Ид;
    $name = (string)$xml_item->Наименование;
    $model = (string)$xml_item->Артикул ?: '1C-' . $xml_id;

  // 1. Обработка изображения (РАБОТАЕТ И ДЛЯ INSERT, И ДЛЯ UPDATE)
        $image_path = '';
        $additional_images = [];

        if (isset($xml_item->Картинка)) {
            $img_counter = 0;
            
            // Перебираем все теги <Картинка>, сколько бы их ни было
            foreach ($xml_item->Картинка as $xml_img) {
                $processed_route = $this->processImage1C((string)$xml_img);
                
                if ($processed_route) {
                    if ($img_counter === 0) {
                        // Первая картинка идет как основная
                        $image_path = $processed_route;
                    } else {
                        // Остальные собираем в массив для таблицы product_image
                        $additional_images[] = $processed_route;
                    }
                    $img_counter++;
                }
            }
        }

   

    $sql = "SET xml_id = '" . $this->db->escape($xml_id) . "', model = '" . $this->db->escape($model) . "', ";
    if ($image_path) {    
            $sql .= " image = '" . $this->db->escape($image_path) . "', "; 
        }
    $sql .= " manufacturer_id = '" . (int)$manufacturer_id . "', status = 1, date_modified = NOW()";



    if ($mode == 'insert') {
        $this->db->query("INSERT INTO " . DB_PREFIX . "product " . $sql . ", date_added = NOW()");
        $product_id = $this->db->getLastId();
        $this->db->query("INSERT INTO " . DB_PREFIX . "product_to_store SET product_id = '" . (int)$product_id . "', store_id = 0");
    } else {
        $this->db->query("UPDATE " . DB_PREFIX . "product " . $sql . " WHERE product_id = '" . (int)$product_id . "'");
    }


     if ($mode == 'insert' || $mode == 'update') {

    // 2. Название (product_description)
    $description = isset($xml_item->Описание) ? (string)$xml_item->Описание : '';
    $description_html = $this->db->escape(nl2br(trim($description)));

    $this->db->query("DELETE FROM " . DB_PREFIX . "product_description WHERE product_id = '" . (int)$product_id . "'");
    $this->db->query("INSERT INTO " . DB_PREFIX . "product_description SET 
        product_id = '" . (int)$product_id . "', 
        language_id = '" . (int)$this->config->get('config_language_id') . "', 
        description = '" . $description_html . "',
        meta_description = '" . $this->db->escape(mb_substr(strip_tags($description), 0, 160)) . "',
        name = '" . $this->db->escape($name) . "', 
        meta_title = '" . $this->db->escape($name) . "'");

    // 3. Категории (Группы)
   $this->db->query("DELETE FROM " . DB_PREFIX . "product_to_category WHERE product_id = '" . (int)$product_id . "'");
   $categories_added = 0;
    $is_first = true;
   

    if (isset($xml_item->Группы->Ид)) {
            
        foreach ($xml_item->Группы->Ид as $group_id) {
            if (isset($this->xml_ids['categories'][(string)$group_id])) {
                $cat_id = $this->xml_ids['categories'][(string)$group_id];
                
                // Устанавливаем main_category = 1 только для первой итерации
                $main_category = $is_first ? 1 : 0;
                
                $this->db->query("INSERT INTO " . DB_PREFIX . "product_to_category SET 
                    product_id = '" . (int)$product_id . "', 
                    category_id = '" . (int)$cat_id . "', 
                    main_category = '" . (int)$main_category . "'");
                
                $is_first = false; 
                $categories_added++;
            }
        }
    }

    if ($categories_added === 0) {
        
        $default_category_id = 96; // Дефолтная категория
        
        $this->db->query("INSERT INTO " . DB_PREFIX . "product_to_category SET 
            product_id = '" . (int)$product_id . "', 
            category_id = '" . (int)$default_category_id . "', 
            main_category = 1"); // Так как она единственная, она же и главная
            
        echo "Предупреждение: Товар «" . $name . "» пришел без категории. Привязан к дефолтной (ID: $default_category_id).<br>";
    }

     $keyword = $this->translit($name); 
    // Если нужно сделать URL уникальным (на случай одинаковых имен), можно добавить ID:
    // $keyword = $toTranslit($name) . '-' . $product_id;

    // 3.5 Запись дополнительных изображений в галерею (product_image)
    $this->db->query("DELETE FROM " . DB_PREFIX . "seo_url WHERE query = 'product_id=" . (int)$product_id . "'");    
    $this->db->query("INSERT INTO " . DB_PREFIX . "seo_url SET         store_id = 0,         language_id = '" . (int)$this->config->get('config_language_id') . "',         query = 'product_id=" . (int)$product_id . "',         keyword = '" . $this->db->escape($keyword) . "'");

    $this->db->query("DELETE FROM " . DB_PREFIX . "product_image WHERE product_id = '" . (int)$product_id . "'");
    
    if (!empty($additional_images)) {
        $sort_order = 0;
        foreach ($additional_images as $add_img) {
            $this->db->query("INSERT INTO " . DB_PREFIX . "product_image SET 
                product_id = '" . (int)$product_id . "', 
                image = '" . $this->db->escape($add_img) . "', 
                sort_order = '" . (int)$sort_order . "'");
            $sort_order++;
        }
    }

         } //insert //update


         

    $product_data = [
        'weight' => 0,
        'width'  => 0,
        'height' => 0,
        'length' => 0,
        'status' => 1 // По умолчанию включен
    ];

   // 4. Атрибуты (ЗначенияСвойств)
    // ВНИМАНИЕ: Очищаем старые атрибуты ВСЕГДА, если товар обновляется. 
    // Если товар создается (insert), этот запрос безопасно отработает вхолостую.
    $this->db->query("DELETE FROM " . DB_PREFIX . "product_attribute WHERE product_id = '" . (int)$product_id . "'");

    if (isset($xml_item->ЗначенияСвойств->ЗначенияСвойства)) {
        foreach ($xml_item->ЗначенияСвойств->ЗначенияСвойства as $prop) {
            $prop_id = (string)$prop->Ид;
            $val = (string)$prop->Значение;

            // 1. Проверка на спец-атрибуты (вес, размеры, статус)
            if (isset($special_attributes[$prop_id])) {
                $field = $special_attributes[$prop_id];
                if ($field == 'status') {
                    $status_text = isset($this->xml_ids['attribute_values'][$val]) ? $this->xml_ids['attribute_values'][$val] : $val;
                    $product_data['status'] = (mb_strtolower(trim($status_text)) == 'publish') ? 1 : 0;
                } else {
                    $clean_val = str_replace([',', ' ', chr(194).chr(160)], ['.', '', ''], $val);
                    $product_data[$field] = (float)$clean_val;
                }               
                continue; 
            }

            // 2. Если не спец-атрибут — записываем как обычный атрибут
            // УБРАЛИ условие if ($mode == 'insert'), теперь запись работает для ВСЕХ товаров!
            if (isset($this->xml_ids['attributes'][$prop_id])) {
                $text_value = isset($this->xml_ids['attribute_values'][$val]) ? $this->xml_ids['attribute_values'][$val] : $val;
                
                $this->db->query("REPLACE INTO " . DB_PREFIX . "product_attribute SET 
                    product_id = '" . (int)$product_id . "', 
                    attribute_id = '" . (int)$this->xml_ids['attributes'][$prop_id] . "', 
                    language_id = '" . (int)$this->config->get('config_language_id') . "', 
                    text = '" . $this->db->escape($text_value) . "'");
            }
        }
    }

    // 5. Финальное обновление таблицы product (записываем особые поля)
    $this->db->query("UPDATE " . DB_PREFIX . "product SET 
        weight = '" . (float)$product_data['weight'] . "',
        width = '" . (float)$product_data['width'] . "',
        height = '" . (float)$product_data['height'] . "',
        length = '" . (float)$product_data['length'] . "',
        status = '" . (int)$product_data['status'] . "'
        WHERE product_id = '" . (int)$product_id . "'");

   

