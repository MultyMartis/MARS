<?php
class ModelCatalogProduct extends Model {
	public function updateViewed($product_id) {
		$this->db->query("UPDATE " . DB_PREFIX . "product SET viewed = (viewed + 1) WHERE product_id = '" . (int)$product_id . "'");
	}
public function getProduct($product_id) {
    // 1. Добавляем p.price2, p.price3, p.discount1c в SELECT
    $query = $this->db->query("SELECT DISTINCT *, pd.name AS name, p.image, m.name AS manufacturer, p.price2, p.price3, p.discount1c, (SELECT price FROM " . DB_PREFIX . "product_discount pd2 WHERE pd2.product_id = p.product_id AND pd2.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "' AND pd2.quantity = '1' AND ((pd2.date_start = '0000-00-00' OR pd2.date_start < NOW()) AND (pd2.date_end = '0000-00-00' OR pd2.date_end > NOW())) ORDER BY pd2.priority ASC, pd2.price ASC LIMIT 1) AS discount, (SELECT price FROM " . DB_PREFIX . "product_special ps WHERE ps.product_id = p.product_id AND ps.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "' AND ((ps.date_start = '0000-00-00' OR ps.date_start < NOW()) AND (ps.date_end = '0000-00-00' OR ps.date_end > NOW())) ORDER BY ps.priority ASC, ps.price ASC LIMIT 1) AS special, (SELECT points FROM " . DB_PREFIX . "product_reward pr WHERE pr.product_id = p.product_id AND pr.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "') AS reward, (SELECT ss.name FROM " . DB_PREFIX . "stock_status ss WHERE ss.stock_status_id = p.stock_status_id AND ss.language_id = '" . (int)$this->config->get('config_language_id') . "') AS stock_status, (SELECT wcd.unit FROM " . DB_PREFIX . "weight_class_description wcd WHERE p.weight_class_id = wcd.weight_class_id AND wcd.language_id = '" . (int)$this->config->get('config_language_id') . "') AS weight_class, (SELECT lcd.unit FROM " . DB_PREFIX . "length_class_description lcd WHERE p.length_class_id = lcd.length_class_id AND lcd.language_id = '" . (int)$this->config->get('config_language_id') . "') AS length_class, (SELECT AVG(rating) AS total FROM " . DB_PREFIX . "review r1 WHERE r1.product_id = p.product_id AND r1.status = '1' GROUP BY r1.product_id) AS rating, (SELECT COUNT(*) AS total FROM " . DB_PREFIX . "review r2 WHERE r2.product_id = p.product_id AND r2.status = '1' GROUP BY r2.product_id) AS reviews, p.sort_order FROM " . DB_PREFIX . "product p LEFT JOIN " . DB_PREFIX . "product_description pd ON (p.product_id = pd.product_id) LEFT JOIN " . DB_PREFIX . "product_to_store p2s ON (p.product_id = p2s.product_id) LEFT JOIN " . DB_PREFIX . "manufacturer m ON (p.manufacturer_id = m.manufacturer_id) WHERE p.product_id = '" . (int)$product_id . "' AND pd.language_id = '" . (int)$this->config->get('config_language_id') . "' AND p.status = '1' AND p.date_available <= NOW() AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "'");

    if ($query->num_rows) {
        // --- ЛОГИКА РАСЧЕТА PRICE ---
        $customer_group_id = (int)$this->customer->getGroupId();
        
        if ($customer_group_id == 3) {
            $base_price = $query->row['price2']; // Дилер
        } elseif ($customer_group_id == 4) {
            $base_price = $query->row['price3']; // Оптовик
        } else {
            $base_price = $query->row['price'];  // Обычный
        }

        // Если есть discount (скидка от количества 1), приоритет ей, иначе базовой цене
        $final_price = ($query->row['discount'] ? $query->row['discount'] : $base_price);
        
        if ($final_price < 0) $final_price = 0;

      // --- ЛОГИКА РАСЧЕТА SPECIAL ---
$final_special = false;

// Уровень 1: discount1c (процент скидки)
if (isset($query->row['discount1c']) && (float)$query->row['discount1c'] > 0) {
    $percent = (float)$query->row['discount1c'];
    $final_special = $final_price - ($final_price * ($percent / 100));
} 
// Уровень 2: Стандартный special из базы (строгая проверка, что цена > 0)
elseif (isset($query->row['special']) && (float)$query->row['special'] > 0) {
    $final_special = (float)$query->row['special'];
} 
// Уровень 3: Скидка из категории
else {
    $category_discount_query = $this->db->query("
        SELECT MAX(c.discount) as max_discount 
        FROM " . DB_PREFIX . "product_to_category p2c 
        LEFT JOIN " . DB_PREFIX . "category c ON (p2c.category_id = c.category_id) 
        WHERE p2c.product_id = '" . (int)$product_id . "'
    ");
    
    // Проверяем, что запрос вернул результат и max_discount действительно больше 0
    if ($category_discount_query->num_rows && (float)$category_discount_query->row['max_discount'] > 0) {
        $max_cat_discount = (float)$category_discount_query->row['max_discount'];
        $final_special = $final_price - ($final_price * ($max_cat_discount / 100));
    }
}

// Финальная проверка: если спеццена была рассчитана, она не может быть меньше 0
// Если $final_special остался false, это условие пропустится
if ($final_special !== false && $final_special < 0) {
    $final_special = 0;
}

        return array(
            'product_id'       => $query->row['product_id'],
            'name'             => $query->row['name'],
            'description'      => $query->row['description'],
            'meta_title'       => $query->row['meta_title'],
            'meta_description' => $query->row['meta_description'],
            'meta_keyword'     => $query->row['meta_keyword'],
            'tag'              => $query->row['tag'],
            'model'            => $query->row['model'],
            'sku'              => $query->row['sku'],
            'upc'              => $query->row['upc'],
            'ean'              => $query->row['ean'],
            'jan'              => $query->row['jan'],
            'isbn'             => $query->row['isbn'],
            'mpn'              => $query->row['mpn'],
            'location'         => $query->row['location'],
            'quantity'         => $query->row['quantity'],
            'stock_status'     => $query->row['stock_status'],
            'image'            => $query->row['image'],
            'manufacturer_id'  => $query->row['manufacturer_id'],
            'manufacturer'     => $query->row['manufacturer'],
            'price'            => $final_price, // Наш расчет
            'special'          => $final_special, // Наш расчет
            'reward'           => $query->row['reward'],
            'points'           => $query->row['points'],
            'tax_class_id'     => $query->row['tax_class_id'],
            'date_available'   => $query->row['date_available'],
            'weight'           => $query->row['weight'],
            'weight_class_id'  => $query->row['weight_class_id'],
            'length'           => $query->row['length'],
            'width'            => $query->row['width'],
            'height'           => $query->row['height'],
            'length_class_id'  => $query->row['length_class_id'],
            'subtract'         => $query->row['subtract'],
            'rating'           => round(($query->row['rating']===null) ? 0 : $query->row['rating']),
            'reviews'          => $query->row['reviews'] ? $query->row['reviews'] : 0,
            'minimum'          => $query->row['minimum'],
            'sort_order'       => $query->row['sort_order'],
            'status'           => $query->row['status'],
            'date_added'       => $query->row['date_added'],
            'date_modified'    => $query->row['date_modified'],
            'viewed'           => $query->row['viewed']
        );
    } else {
        return false;
    }
}



	public function getProducts($data = array()) {
    // 1. Логика групп пользователей
    $customer_group_id = (int)$this->config->get('config_customer_group_id');
    if (!in_array($customer_group_id, [3, 4])) {
        $customer_group_id = 2;
    }


    $sql = "SELECT p.product_id, 
            (SELECT AVG(rating) AS total FROM " . DB_PREFIX . "review r1 WHERE r1.product_id = p.product_id AND r1.status = '1' GROUP BY r1.product_id) AS rating, 
            (SELECT price FROM " . DB_PREFIX . "product_discount pd2 WHERE pd2.product_id = p.product_id AND pd2.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "' AND pd2.quantity = '1' AND ((pd2.date_start = '0000-00-00' OR pd2.date_start < NOW()) AND (pd2.date_end = '0000-00-00' OR pd2.date_end > NOW())) ORDER BY pd2.priority ASC, pd2.price ASC LIMIT 1) AS discount, 
            (SELECT price FROM " . DB_PREFIX . "product_special ps WHERE ps.product_id = p.product_id AND ps.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "' AND ((ps.date_start = '0000-00-00' OR ps.date_start < NOW()) AND (ps.date_end = '0000-00-00' OR ps.date_end > NOW())) ORDER BY ps.priority ASC, ps.price ASC LIMIT 1) AS special";


    if (!empty($data['filter_category_id'])) {
        if (!empty($data['filter_sub_category'])) {
            $sql .= " FROM " . DB_PREFIX . "category_path cp LEFT JOIN " . DB_PREFIX . "product_to_category p2c ON (cp.category_id = p2c.category_id)";
        } else {
            $sql .= " FROM " . DB_PREFIX . "product_to_category p2c";
        }

        if (!empty($data['filter_filter'])) {
            $sql .= " LEFT JOIN " . DB_PREFIX . "product_filter pf ON (p2c.product_id = pf.product_id) LEFT JOIN " . DB_PREFIX . "product p ON (pf.product_id = p.product_id)";
        } else {
            $sql .= " LEFT JOIN " . DB_PREFIX . "product p ON (p2c.product_id = p.product_id)";
        }
    } else {
        $sql .= " FROM " . DB_PREFIX . "product p";
    }

    $sql .= " LEFT JOIN " . DB_PREFIX . "product_price_index ppi ON (p.product_id = ppi.product_id AND ppi.customer_group_id = '" . (int)$customer_group_id . "')";


    $sql .= " LEFT JOIN " . DB_PREFIX . "product_description pd ON (p.product_id = pd.product_id) 
              LEFT JOIN " . DB_PREFIX . "product_to_store p2s ON (p.product_id = p2s.product_id) 
              WHERE pd.language_id = '" . (int)$this->config->get('config_language_id') . "' 
              AND p.status = '1' 
              AND p.date_available <= NOW() 
              AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "'";


    if (!empty($data['filter_category_id'])) {
        if (!empty($data['filter_sub_category'])) {
            $sql .= " AND cp.path_id = '" . (int)$data['filter_category_id'] . "'";
        } else {
            $sql .= " AND p2c.category_id = '" . (int)$data['filter_category_id'] . "'";
        }
       if (!empty($data['filter_filter'])) {
            $implode = array();
            $filters = explode(',', $data['filter_filter']);
            foreach ($filters as $filter_id) {
                $implode[] = (int)$filter_id;
            }
            $sql .= " AND pf.filter_id IN (" . implode(',', $implode) . ")";
        }
    }

    // 6. Поиск по названию/тегам
    if (!empty($data['filter_name']) || !empty($data['filter_tag'])) {
        $sql .= " AND (";
        if (!empty($data['filter_name'])) {
            $implode = array();
            $words = explode(' ', trim(preg_replace('/\s+/', ' ', $data['filter_name'])));
            foreach ($words as $word) {
                $implode[] = "pd.name LIKE '%" . $this->db->escape($word) . "%'";
            }
            if ($implode) {
                $sql .= " " . implode(" AND ", $implode) . "";
            }
            if (!empty($data['filter_description'])) {
                $sql .= " OR pd.description LIKE '%" . $this->db->escape($data['filter_name']) . "%'";
            }
        }

        if (!empty($data['filter_name']) && !empty($data['filter_tag'])) {
            $sql .= " OR ";
        }

        if (!empty($data['filter_tag'])) {
            $implode = array();
            $words = explode(' ', trim(preg_replace('/\s+/', ' ', $data['filter_tag'])));
            foreach ($words as $word) {
                $implode[] = "pd.tag LIKE '%" . $this->db->escape($word) . "%'";
            }
            if ($implode) {
                $sql .= " " . implode(" AND ", $implode) . "";
            }
        }

        if (!empty($data['filter_name'])) {
            $sql .= " OR LCASE(p.model) LIKE '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "%'";
            $sql .= " OR LCASE(p.sku) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
            $sql .= " OR LCASE(p.upc) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
            $sql .= " OR LCASE(p.ean) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
            $sql .= " OR LCASE(p.jan) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
            $sql .= " OR LCASE(p.isbn) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
            $sql .= " OR LCASE(p.mpn) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
        }
        $sql .= ")";
    }

    if (!empty($data['filter_manufacturer_id'])) {
        $sql .= " AND p.manufacturer_id = '" . (int)$data['filter_manufacturer_id'] . "'";
    }

    // 7. НАШИ КАСТОМНЫЕ ФИЛЬТРЫ (filter_custom)
    if (!empty($data['filter_custom'])) {
        $f = $data['filter_custom'];
        $effective_price = "IFNULL(ppi.special, ppi.price)";

        if (isset($f['only_with_price']))
            {
                if ((!isset($f['price_from'])) OR (intval($f['price_from']==0))) $f['price_from']='1';
            } 
        if (isset($f['preorder_only'])) $sql .= " AND p.quantity = 0";
        if (isset($f['in_stock'])) $sql .= " AND p.quantity > 0";
        if (isset($f['only_discount'])) $sql .= " AND ppi.special > 0";

        // Фильтр по цене
        if (isset($f['price_from']) && $f['price_from'] !== '') {
            $sql .= " AND " . $effective_price . " >= '" . (float)$f['price_from'] . "'";
        }
        if (isset($f['price_to']) && $f['price_to'] !== '') {
            $sql .= " AND " . $effective_price . " <= '" . (float)$f['price_to'] . "'";
        }

         

        // Габариты
        $dims = ['len' => 'p.length', 'w' => 'p.width', 'h' => 'p.height'];
        foreach ($dims as $key => $col) {
            if (isset($f[$key . '_from']) && $f[$key . '_from'] !== '') $sql .= " AND " . $col . " >= '" . (float)$f[$key . '_from'] . "'";
            if (isset($f[$key . '_to']) && $f[$key . '_to'] !== '') $sql .= " AND " . $col . " <= '" . (float)$f[$key . '_to'] . "'";
        }

        // Категории
                if (!empty($f['s']) && is_array($f['s'])) {
                    $category_ids = array_map('intval', $f['s']);
                    if ($category_ids) {
                        $sql .= " AND EXISTS (SELECT 1 FROM " . DB_PREFIX . "product_to_category p2c_s WHERE p2c_s.product_id = p.product_id AND p2c_s.category_id IN (" . implode(',', $category_ids) . "))";
                    }
                }

        // Атрибуты
        if (!empty($f['attr']) && is_array($f['attr'])) {
            foreach ($f['attr'] as $attr_slug => $values) {
                if (!is_array($values)) continue;
                $implode = array();
                foreach ($values as $val) {
                    if (trim($val) !== '') $implode[] = "pa.text = '" . $this->db->escape(trim($val)) . "'";
                }
                if ($implode) {
                    $sql .= " AND EXISTS (
                        SELECT 1 FROM " . DB_PREFIX . "product_attribute pa 
                        LEFT JOIN " . DB_PREFIX . "attribute_description ad ON (pa.attribute_id = ad.attribute_id)
                        WHERE pa.product_id = p.product_id 
                        AND ad.filter_name = '" . $this->db->escape($attr_slug) . "' 
                        AND (" . implode(" OR ", $implode) . ")
                        AND ad.language_id = '" . (int)$this->config->get('config_language_id') . "'
                    )";
                }
            }
        }
    }

    $sql .= " GROUP BY p.product_id";

    // 8. СОРТИРОВКА (Обновляем логику цены)
    $sort_data = array('pd.name', 'p.model', 'p.quantity', 'p.price', 'rating', 'p.sort_order', 'p.date_added');

    if (isset($data['sort']) && in_array($data['sort'], $sort_data)) {
        if ($data['sort'] == 'pd.name' || $data['sort'] == 'p.model') {
            $sql .= " ORDER BY LCASE(" . $data['sort'] . ")";
        } elseif ($data['sort'] == 'p.price') {
            // ИСПОЛЬЗУЕМ PPI ДЛЯ СОРТИРОВКИ (так точнее и быстрее)
            $sql .= " ORDER BY IFNULL(ppi.special, ppi.price)";
        } else {
            $sql .= " ORDER BY " . $data['sort'];
        }
    } else {
        $sql .= " ORDER BY p.sort_order";
    }

    if (isset($data['order']) && ($data['order'] == 'DESC')) {
        $sql .= " DESC, LCASE(pd.name) DESC";
    } else {
        $sql .= " ASC, LCASE(pd.name) ASC";
    }

    // 9. ЛИМИТЫ
    if (isset($data['start']) || isset($data['limit'])) {
        $start = (isset($data['start']) && $data['start'] > 0) ? (int)$data['start'] : 0;
        $limit = (isset($data['limit']) && $data['limit'] > 0) ? (int)$data['limit'] : 20;
        $sql .= " LIMIT " . $start . "," . $limit;
    }


     //echo $sql; die();

    $product_data = array();
    $query = $this->db->query($sql);

    foreach ($query->rows as $result) {
        $product_data[$result['product_id']] = $this->getProduct($result['product_id']);
    }

    return $product_data;
}

	public function getProductSpecials($data = array()) {
		$sql = "SELECT DISTINCT ps.product_id, (SELECT AVG(rating) FROM " . DB_PREFIX . "review r1 WHERE r1.product_id = ps.product_id AND r1.status = '1' GROUP BY r1.product_id) AS rating FROM " . DB_PREFIX . "product_special ps LEFT JOIN " . DB_PREFIX . "product p ON (ps.product_id = p.product_id) LEFT JOIN " . DB_PREFIX . "product_description pd ON (p.product_id = pd.product_id) LEFT JOIN " . DB_PREFIX . "product_to_store p2s ON (p.product_id = p2s.product_id) WHERE p.status = '1' AND p.date_available <= NOW() AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "' AND ps.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "' AND ((ps.date_start = '0000-00-00' OR ps.date_start < NOW()) AND (ps.date_end = '0000-00-00' OR ps.date_end > NOW())) GROUP BY ps.product_id";

		$sort_data = array(
			'pd.name',
			'p.model',
			'ps.price',
			'rating',
			'p.sort_order'
		);

		if (isset($data['sort']) && in_array($data['sort'], $sort_data)) {
			if ($data['sort'] == 'pd.name' || $data['sort'] == 'p.model') {
				$sql .= " ORDER BY LCASE(" . $data['sort'] . ")";
			} else {
				$sql .= " ORDER BY " . $data['sort'];
			}
		} else {
			$sql .= " ORDER BY p.sort_order";
		}

		if (isset($data['order']) && ($data['order'] == 'DESC')) {
			$sql .= " DESC, LCASE(pd.name) DESC";
		} else {
			$sql .= " ASC, LCASE(pd.name) ASC";
		}

		if (isset($data['start']) || isset($data['limit'])) {
			if ($data['start'] < 0) {
				$data['start'] = 0;
			}

			if ($data['limit'] < 1) {
				$data['limit'] = 20;
			}

			$sql .= " LIMIT " . (int)$data['start'] . "," . (int)$data['limit'];
		}

		$product_data = array();

		$query = $this->db->query($sql);

		foreach ($query->rows as $result) {
			$product_data[$result['product_id']] = $this->getProduct($result['product_id']);
		}

		return $product_data;
	}

	public function getLatestProducts($limit) {
		$product_data = $this->cache->get('product.latest.' . (int)$this->config->get('config_language_id') . '.' . (int)$this->config->get('config_store_id') . '.' . $this->config->get('config_customer_group_id') . '.' . (int)$limit);

		if (!$product_data) {
			$product_data = array();
			$query = $this->db->query("SELECT p.product_id FROM " . DB_PREFIX . "product p LEFT JOIN " . DB_PREFIX . "product_to_store p2s ON (p.product_id = p2s.product_id) WHERE p.status = '1' AND p.date_available <= NOW() AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "' ORDER BY p.date_added DESC LIMIT " . (int)$limit);

			foreach ($query->rows as $result) {
				$product_data[$result['product_id']] = $this->getProduct($result['product_id']);
			}

			$this->cache->set('product.latest.' . (int)$this->config->get('config_language_id') . '.' . (int)$this->config->get('config_store_id') . '.' . $this->config->get('config_customer_group_id') . '.' . (int)$limit, $product_data);
		}

		return $product_data;
	}

	public function getPopularProducts($limit) {
		$product_data = $this->cache->get('product.popular.' . (int)$this->config->get('config_language_id') . '.' . (int)$this->config->get('config_store_id') . '.' . $this->config->get('config_customer_group_id') . '.' . (int)$limit);
	
		if (!$product_data) {
			$product_data = array();
			$query = $this->db->query("SELECT p.product_id FROM " . DB_PREFIX . "product p LEFT JOIN " . DB_PREFIX . "product_to_store p2s ON (p.product_id = p2s.product_id) WHERE p.status = '1' AND p.date_available <= NOW() AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "' ORDER BY p.viewed DESC, p.date_added DESC LIMIT " . (int)$limit);
	
			foreach ($query->rows as $result) {
				$product_data[$result['product_id']] = $this->getProduct($result['product_id']);
			}
			
			$this->cache->set('product.popular.' . (int)$this->config->get('config_language_id') . '.' . (int)$this->config->get('config_store_id') . '.' . $this->config->get('config_customer_group_id') . '.' . (int)$limit, $product_data);
		}
		
		return $product_data;
	}

	public function getBestSellerProducts($limit) {
		$product_data = $this->cache->get('product.bestseller.' . (int)$this->config->get('config_language_id') . '.' . (int)$this->config->get('config_store_id') . '.' . $this->config->get('config_customer_group_id') . '.' . (int)$limit);

		if (!$product_data) {
			$product_data = array();

			$query = $this->db->query("SELECT op.product_id, SUM(op.quantity) AS total FROM " . DB_PREFIX . "order_product op LEFT JOIN `" . DB_PREFIX . "order` o ON (op.order_id = o.order_id) LEFT JOIN `" . DB_PREFIX . "product` p ON (op.product_id = p.product_id) LEFT JOIN " . DB_PREFIX . "product_to_store p2s ON (p.product_id = p2s.product_id) WHERE o.order_status_id > '0' AND p.status = '1' AND p.date_available <= NOW() AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "' GROUP BY op.product_id ORDER BY total DESC LIMIT " . (int)$limit);

			foreach ($query->rows as $result) {
				$product_data[$result['product_id']] = $this->getProduct($result['product_id']);
			}

			$this->cache->set('product.bestseller.' . (int)$this->config->get('config_language_id') . '.' . (int)$this->config->get('config_store_id') . '.' . $this->config->get('config_customer_group_id') . '.' . (int)$limit, $product_data);
		}

		return $product_data;
	}

	public function getProductAttributes($product_id) {
		$product_attribute_group_data = array();

		$product_attribute_group_query = $this->db->query("SELECT ag.attribute_group_id, agd.name FROM " . DB_PREFIX . "product_attribute pa LEFT JOIN " . DB_PREFIX . "attribute a ON (pa.attribute_id = a.attribute_id) LEFT JOIN " . DB_PREFIX . "attribute_group ag ON (a.attribute_group_id = ag.attribute_group_id) LEFT JOIN " . DB_PREFIX . "attribute_group_description agd ON (ag.attribute_group_id = agd.attribute_group_id) WHERE pa.product_id = '" . (int)$product_id . "' AND agd.language_id = '" . (int)$this->config->get('config_language_id') . "' GROUP BY ag.attribute_group_id ORDER BY ag.sort_order, agd.name");

		foreach ($product_attribute_group_query->rows as $product_attribute_group) {
			$product_attribute_data = array();

			$product_attribute_query = $this->db->query("SELECT a.attribute_id, ad.name, pa.text FROM " . DB_PREFIX . "product_attribute pa LEFT JOIN " . DB_PREFIX . "attribute a ON (pa.attribute_id = a.attribute_id) LEFT JOIN " . DB_PREFIX . "attribute_description ad ON (a.attribute_id = ad.attribute_id) WHERE pa.product_id = '" . (int)$product_id . "' AND a.attribute_group_id = '" . (int)$product_attribute_group['attribute_group_id'] . "' AND ad.language_id = '" . (int)$this->config->get('config_language_id') . "' AND pa.language_id = '" . (int)$this->config->get('config_language_id') . "' ORDER BY a.sort_order, ad.name");

			foreach ($product_attribute_query->rows as $product_attribute) {
				$product_attribute_data[] = array(
					'attribute_id' => $product_attribute['attribute_id'],
					'name'         => $product_attribute['name'],
					'text'         => $product_attribute['text']
				);
			}

			$product_attribute_group_data[] = array(
				'attribute_group_id' => $product_attribute_group['attribute_group_id'],
				'name'               => $product_attribute_group['name'],
				'attribute'          => $product_attribute_data
			);
		}

		return $product_attribute_group_data;
	}

	public function getProductOptions($product_id) {
		$product_option_data = array();

		$product_option_query = $this->db->query("SELECT * FROM " . DB_PREFIX . "product_option po LEFT JOIN `" . DB_PREFIX . "option` o ON (po.option_id = o.option_id) LEFT JOIN " . DB_PREFIX . "option_description od ON (o.option_id = od.option_id) WHERE po.product_id = '" . (int)$product_id . "' AND od.language_id = '" . (int)$this->config->get('config_language_id') . "' ORDER BY o.sort_order");

		foreach ($product_option_query->rows as $product_option) {
			$product_option_value_data = array();

			$product_option_value_query = $this->db->query("SELECT * FROM " . DB_PREFIX . "product_option_value pov LEFT JOIN " . DB_PREFIX . "option_value ov ON (pov.option_value_id = ov.option_value_id) LEFT JOIN " . DB_PREFIX . "option_value_description ovd ON (ov.option_value_id = ovd.option_value_id) WHERE pov.product_id = '" . (int)$product_id . "' AND pov.product_option_id = '" . (int)$product_option['product_option_id'] . "' AND ovd.language_id = '" . (int)$this->config->get('config_language_id') . "' ORDER BY ov.sort_order");

			foreach ($product_option_value_query->rows as $product_option_value) {
				$product_option_value_data[] = array(
					'product_option_value_id' => $product_option_value['product_option_value_id'],
					'option_value_id'         => $product_option_value['option_value_id'],
					'name'                    => $product_option_value['name'],
					'image'                   => $product_option_value['image'],
					'quantity'                => $product_option_value['quantity'],
					'subtract'                => $product_option_value['subtract'],
					'price'                   => $product_option_value['price'],
					'price_prefix'            => $product_option_value['price_prefix'],
					'weight'                  => $product_option_value['weight'],
					'weight_prefix'           => $product_option_value['weight_prefix']
				);
			}

			$product_option_data[] = array(
				'product_option_id'    => $product_option['product_option_id'],
				'product_option_value' => $product_option_value_data,
				'option_id'            => $product_option['option_id'],
				'name'                 => $product_option['name'],
				'type'                 => $product_option['type'],
				'value'                => $product_option['value'],
				'required'             => $product_option['required']
			);
		}

		return $product_option_data;
	}

	public function getProductDiscounts($product_id) {
		$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "product_discount WHERE product_id = '" . (int)$product_id . "' AND customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "' AND quantity > 1 AND ((date_start = '0000-00-00' OR date_start < NOW()) AND (date_end = '0000-00-00' OR date_end > NOW())) ORDER BY quantity ASC, priority ASC, price ASC");

		return $query->rows;
	}

	public function getProductImages($product_id) {
		$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "product_image WHERE product_id = '" . (int)$product_id . "' ORDER BY sort_order ASC");

		return $query->rows;
	}

	public function getProductRelated($product_id) {
		$product_data = array();

		$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "product_related pr LEFT JOIN " . DB_PREFIX . "product p ON (pr.related_id = p.product_id) LEFT JOIN " . DB_PREFIX . "product_to_store p2s ON (p.product_id = p2s.product_id) WHERE pr.product_id = '" . (int)$product_id . "' AND p.status = '1' AND p.date_available <= NOW() AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "'");

		foreach ($query->rows as $result) {
			$product_data[$result['related_id']] = $this->getProduct($result['related_id']);
		}

		return $product_data;
	}

	public function getProductLayoutId($product_id) {
		$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "product_to_layout WHERE product_id = '" . (int)$product_id . "' AND store_id = '" . (int)$this->config->get('config_store_id') . "'");

		if ($query->num_rows) {
			return (int)$query->row['layout_id'];
		} else {
			return 0;
		}
	}

	public function getCategories($product_id) {
		$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "product_to_category WHERE product_id = '" . (int)$product_id . "'");

		return $query->rows;
	}

	public function getTotalProducts($data = array()) {

			$customer_group_id = (int)$this->config->get('config_customer_group_id');
		if (!in_array($customer_group_id, [3, 4])) {
			$customer_group_id = 2;
		}

		$sql = "SELECT COUNT(DISTINCT p.product_id) AS total";

		if (!empty($data['filter_category_id'])) {
			if (!empty($data['filter_sub_category'])) {
				$sql .= " FROM " . DB_PREFIX . "category_path cp LEFT JOIN " . DB_PREFIX . "product_to_category p2c ON (cp.category_id = p2c.category_id)";
			} else {
				$sql .= " FROM " . DB_PREFIX . "product_to_category p2c";
			}

			if (!empty($data['filter_filter'])) {
				$sql .= " LEFT JOIN " . DB_PREFIX . "product_filter pf ON (p2c.product_id = pf.product_id) LEFT JOIN " . DB_PREFIX . "product p ON (pf.product_id = p.product_id)";
			} else {
				$sql .= " LEFT JOIN " . DB_PREFIX . "product p ON (p2c.product_id = p.product_id)";
			}
		} else {
			$sql .= " FROM " . DB_PREFIX . "product p";
		}


		$sql .= " LEFT JOIN " . DB_PREFIX . "product_price_index ppi ON (p.product_id = ppi.product_id AND ppi.customer_group_id = '" . (int)$customer_group_id . "')";


		$sql .= " LEFT JOIN " . DB_PREFIX . "product_description pd ON (p.product_id = pd.product_id) LEFT JOIN " . DB_PREFIX . "product_to_store p2s ON (p.product_id = p2s.product_id) WHERE pd.language_id = '" . (int)$this->config->get('config_language_id') . "' AND p.status = '1' AND p.date_available <= NOW() AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "'";

	

		if (!empty($data['filter_category_id'])) {
			if (!empty($data['filter_sub_category'])) {
				$sql .= " AND cp.path_id = '" . (int)$data['filter_category_id'] . "'";
			} else {
				$sql .= " AND p2c.category_id = '" . (int)$data['filter_category_id'] . "'";
			}

			if (!empty($data['filter_filter'])) {
				$implode = array();

				$filters = explode(',', $data['filter_filter']);

				foreach ($filters as $filter_id) {
					$implode[] = (int)$filter_id;
				}

				$sql .= " AND pf.filter_id IN (" . implode(',', $implode) . ")";
			}
		}

		if (!empty($data['filter_name']) || !empty($data['filter_tag'])) {
			$sql .= " AND (";

			if (!empty($data['filter_name'])) {
				$implode = array();

				$words = explode(' ', trim(preg_replace('/\s+/', ' ', $data['filter_name'])));

				foreach ($words as $word) {
					$implode[] = "pd.name LIKE '%" . $this->db->escape($word) . "%'";
				}

				if ($implode) {
					$sql .= " " . implode(" AND ", $implode) . "";
				}

				if (!empty($data['filter_description'])) {
					$sql .= " OR pd.description LIKE '%" . $this->db->escape($data['filter_name']) . "%'";
				}
			}

			if (!empty($data['filter_name']) && !empty($data['filter_tag'])) {
				$sql .= " OR ";
			}

			if (!empty($data['filter_tag'])) {
				$implode = array();

				$words = explode(' ', trim(preg_replace('/\s+/', ' ', $data['filter_tag'])));

				foreach ($words as $word) {
					$implode[] = "pd.tag LIKE '%" . $this->db->escape($word) . "%'";
				}

				if ($implode) {
					$sql .= " " . implode(" AND ", $implode) . "";
				}
			}

			if (!empty($data['filter_name'])) {
				$sql .= " OR LCASE(p.model) LIKE '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "%'";
				$sql .= " OR LCASE(p.sku) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
				$sql .= " OR LCASE(p.upc) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
				$sql .= " OR LCASE(p.ean) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
				$sql .= " OR LCASE(p.jan) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
				$sql .= " OR LCASE(p.isbn) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
				$sql .= " OR LCASE(p.mpn) = '" . $this->db->escape(utf8_strtolower($data['filter_name'])) . "'";
			}

			$sql .= ")";
		}

		if (!empty($data['filter_manufacturer_id'])) {
			$sql .= " AND p.manufacturer_id = '" . (int)$data['filter_manufacturer_id'] . "'";
		}

		// --- Начало доработки фильтра ---
	if (!empty($data['filter_custom'])) {
				$f = $data['filter_custom']; 
				$effective_price = "IFNULL(ppi.special, ppi.price)";

                  if (isset($f['only_with_price']))
                        {
                            if ((!isset($f['price_from'])) OR (intval($f['price_from']==0))) $f['price_from']='1';
                        } 
                    if (isset($f['preorder_only'])) $sql .= " AND p.quantity = 0";
                    if (isset($f['in_stock'])) $sql .= " AND p.quantity > 0";
                    if (isset($f['only_discount'])) $sql .= " AND ppi.special > 0";

				// Цена
				if (isset($f['price_from']) && $f['price_from'] !== '') {
					$sql .= " AND " . $effective_price . " >= '" . (float)$f['price_from'] . "'";
				}
				if (isset($f['price_to']) && $f['price_to'] !== '') {
					$sql .= " AND " . $effective_price . " <= '" . (float)$f['price_to'] . "'";
				}

				// Габариты
				$dims = ['len' => 'p.length', 'w' => 'p.width', 'h' => 'p.height'];
				foreach ($dims as $key => $col) {
					if (isset($f[$key . '_from']) && $f[$key . '_from'] !== '') {
						$sql .= " AND " . $col . " >= '" . (float)$f[$key . '_from'] . "'";
					}
					if (isset($f[$key . '_to']) && $f[$key . '_to'] !== '') {
						$sql .= " AND " . $col . " <= '" . (float)$f[$key . '_to'] . "'";
					}
				}

                // Категории
                if (!empty($f['s']) && is_array($f['s'])) {
                    $category_ids = array_map('intval', $f['s']);
                    if ($category_ids) {
                        $sql .= " AND EXISTS (SELECT 1 FROM " . DB_PREFIX . "product_to_category p2c_s WHERE p2c_s.product_id = p.product_id AND p2c_s.category_id IN (" . implode(',', $category_ids) . "))";
                    }
                }

			// 2. Обработка атрибутов через slug/filter_name
			if (!empty($f['attr']) && is_array($f['attr'])) {
				foreach ($f['attr'] as $attr_slug => $values) {
					if (!is_array($values)) continue;

					$implode = array();
					foreach ($values as $val) {
						$clean_val = trim($val);
						if ($clean_val !== '') {
							// Экранируем значение для безопасности
							$implode[] = "pa.text = '" . $this->db->escape($clean_val) . "'";
						}
					}

					if (!empty($implode)) {
						/* Используем EXISTS: это исключает дублирование строк товара в выборке
						и позволяет пагинации работать точно.
						Связываемся по колонке 'slug' (или 'filter_name'), которую ты добавил в описание.
						*/
						$sql .= " AND EXISTS (
							SELECT 1 FROM " . DB_PREFIX . "product_attribute pa 
							LEFT JOIN " . DB_PREFIX . "attribute_description ad ON (pa.attribute_id = ad.attribute_id)
							WHERE pa.product_id = p.product_id 
							AND ad.filter_name = '" . $this->db->escape($attr_slug) . "' 
							AND (" . implode(" OR ", $implode) . ")
							AND ad.language_id = '" . (int)$this->config->get('config_language_id') . "'
						)";
					}
				}
			}
		}
		// --- Конец доработки фильтра ---



		$query = $this->db->query($sql);

		return $query->row['total'];
	}

	public function getProfile($product_id, $recurring_id) {
		$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "recurring r JOIN " . DB_PREFIX . "product_recurring pr ON (pr.recurring_id = r.recurring_id AND pr.product_id = '" . (int)$product_id . "') WHERE pr.recurring_id = '" . (int)$recurring_id . "' AND status = '1' AND pr.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "'");

		return $query->row;
	}

	public function getProfiles($product_id) {
		$query = $this->db->query("SELECT rd.* FROM " . DB_PREFIX . "product_recurring pr JOIN " . DB_PREFIX . "recurring_description rd ON (rd.language_id = " . (int)$this->config->get('config_language_id') . " AND rd.recurring_id = pr.recurring_id) JOIN " . DB_PREFIX . "recurring r ON r.recurring_id = rd.recurring_id WHERE pr.product_id = " . (int)$product_id . " AND status = '1' AND pr.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "' ORDER BY sort_order ASC");

		return $query->rows;
	}

	public function getTotalProductSpecials() {
		$query = $this->db->query("SELECT COUNT(DISTINCT ps.product_id) AS total FROM " . DB_PREFIX . "product_special ps LEFT JOIN " . DB_PREFIX . "product p ON (ps.product_id = p.product_id) LEFT JOIN " . DB_PREFIX . "product_to_store p2s ON (p.product_id = p2s.product_id) WHERE p.status = '1' AND p.date_available <= NOW() AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "' AND ps.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "' AND ((ps.date_start = '0000-00-00' OR ps.date_start < NOW()) AND (ps.date_end = '0000-00-00' OR ps.date_end > NOW()))");

		if (isset($query->row['total'])) {
			return $query->row['total'];
		} else {
			return 0;
		}
	}

	public function checkProductCategory($product_id, $category_ids) {
		
		$implode = array();

		foreach ($category_ids as $category_id) {
			$implode[] = (int)$category_id;
		}
		
		$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "product_to_category WHERE product_id = '" . (int)$product_id . "' AND category_id IN(" . implode(',', $implode) . ")");
  	    return $query->row;
	}

	    /**
     * Получает уникальные документы для всех категорий, к которым принадлежит товар
     *
     * @param int $product_id
     * @return array
     */
    public function getProductDocuments($product_id) {

        if (!$product_id) {
            return [];
        }
        $language_id =1; 
   

        $sql = "SELECT DISTINCT cd.filename, cdd.name, cd.date_added
                FROM `" . DB_PREFIX . "category_docs` cd
                LEFT JOIN `" . DB_PREFIX . "category_doc_description` cdd ON (cd.doc_id = cdd.doc_id)
                LEFT JOIN `" . DB_PREFIX . "product_to_category` ptc ON (cd.category_id = ptc.category_id)
                WHERE ptc.product_id = '" . (int)$product_id . "'
                AND cdd.language_id = '" . (int)$language_id . "'
                GROUP BY cd.filename, cdd.name
                ORDER BY cd.date_added DESC";

        $query = $this->db->query($sql);

        $documents = [];

        foreach ($query->rows as $result) {
            $documents[] = [
                //'doc_id'      => $result['doc_id'],
                'filename'    =>  HTTPS_SERVER . 'Product_DOCs/'.$result['filename'],
                'name'        => $result['name'],
                'date_added'  => $result['date_added']
            ];
        }

        return $documents;
    }


    public function getCategoryDocuments($category_id) {
    if (!$category_id) {
        return [];
    }
    
    $language_id = 1; 

    $sql = "SELECT DISTINCT cd.filename, cdd.name, cd.date_added
            FROM `" . DB_PREFIX . "category_docs` cd
            LEFT JOIN `" . DB_PREFIX . "category_doc_description` cdd ON (cd.doc_id = cdd.doc_id)
            WHERE cd.category_id = '" . (int)$category_id . "'
            AND cdd.language_id = '" . (int)$language_id . "'
            GROUP BY cd.filename, cdd.name
            ORDER BY cd.date_added DESC";

    $query = $this->db->query($sql);

    $documents = [];

    foreach ($query->rows as $result) {
        $documents[] = [
            'filename'    => HTTPS_SERVER . 'Product_DOCs/' . $result['filename'],
            'name'        => $result['name'],
            'date_added'  => $result['date_added']
        ];
    }

    return $documents;
}

	public function isWishlisted($product_id) {
		if ($this->customer->isLogged()) {
			$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "customer_wishlist WHERE customer_id = '" . (int)$this->customer->getId() . "' AND product_id = '" . (int)$product_id . "'  LIMIT 1");		 
			return $query->num_rows > 0;
		} else {
			if (!isset($this->session->data['guest_hash'])) return false;
			$guest_hash = $this->session->data['guest_hash'];
			if ($guest_hash) {
				$query = $this->db->query("SELECT * FROM " . DB_PREFIX . "customer_wishlist WHERE  guest_hash = '" . $this->db->escape($guest_hash) . "' AND product_id = '" . (int)$product_id . "'  LIMIT 1");		 
				return $query->num_rows > 0;
			}
		}		
	}

	public function isCompared($product_id) { 

		if (!isset($this->session->data['compare'])) return false;
 		
		if (empty($this->session->data['compare'])) return false;
		
		return in_array($product_id, $this->session->data['compare']);
	}

public function getCategoryPriceRange($data = array()) {
    $customer_group_id = (int)$this->customer->getGroupId();

	if (!in_array($customer_group_id, [3, 4]))  $customer_group_id = 2;
    
    $sql = "SELECT 
                MIN(IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)) AS min_price, 
                MAX(IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)) AS max_price 
            FROM " . DB_PREFIX . "product_price_index ppi
            INNER JOIN " . DB_PREFIX . "product p ON (ppi.product_id = p.product_id)
            INNER JOIN " . DB_PREFIX . "product_to_store p2s ON (p.product_id = p2s.product_id)
            INNER JOIN " . DB_PREFIX . "product_to_category p2c ON (p.product_id = p2c.product_id)";

    // Если нужно учитывать подкатегории
    if (!empty($data['filter_sub_category'])) {
        $sql .= " INNER JOIN " . DB_PREFIX . "category_path cp ON (p2c.category_id = cp.category_id) 
                  WHERE cp.path_id = '" . (int)$data['filter_category_id'] . "'";
    } else {
        $sql .= " WHERE p2c.category_id = '" . (int)$data['filter_category_id'] . "'";
    }

    $sql .= " AND ppi.customer_group_id = '" . (int)$customer_group_id . "'
              AND p.status = '1'
              AND p.date_available <= NOW()
              AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "'";

    // Фильтрация по атрибутам (сужение границ цен при выборе фильтров)
    if (!empty($data['filter_attributes'])) {
        foreach ($data['filter_attributes'] as $attribute_id => $values) {
            $sql .= " AND p.product_id IN (SELECT product_id FROM " . DB_PREFIX . "product_attribute WHERE attribute_id = '" . (int)$attribute_id . "' AND text IN ('" . implode("','", array_map(array($this->db, 'escape'), $values)) . "'))";
        }
    }



    $query = $this->db->query($sql);

    return array(
        'min' => $query->row['min_price'] ? (float)$query->row['min_price'] : 0,
        'max' => $query->row['max_price'] ? (float)$query->row['max_price'] : 0
    );
}
	


	public function refreshPriceIndex($product_id = 0) {
			// 1. Получаем список всех групп пользователей
			$customer_groups = $this->db->query("SELECT customer_group_id FROM " . DB_PREFIX . "customer_group")->rows;

			// 2. Если передан product_id, обновляем один товар, иначе — все
			$sql = "SELECT product_id FROM " . DB_PREFIX . "product";
			if ($product_id > 0) {
				$sql .= " WHERE product_id = '" . (int)$product_id . "'";
			}
			
			$products = $this->db->query($sql)->rows;

			foreach ($products as $p) {
				// Очищаем старые записи для этого товара перед обновлением
				$this->db->query("DELETE FROM " . DB_PREFIX . "product_price_index WHERE product_id = '" . (int)$p['product_id'] . "'");

				foreach ($customer_groups as $group) {
					// Эмуляция сессии для конкретной группы, чтобы getProduct отработал корректно
					// Временный хак, если getProduct завязан на $this->customer->getGroupId()
					$this->session->data['customer_group_id_override'] = $group['customer_group_id'];

					// Вызываем ваш существующий метод
					$product_info = $this->getProductForIndex($p['product_id'], $group['customer_group_id']);

					if ($product_info) {
						$this->db->query("INSERT INTO " . DB_PREFIX . "product_price_index SET 
							product_id = '" . (int)$p['product_id'] . "',
							customer_group_id = '" . (int)$group['customer_group_id'] . "',
							price = '" . (float)$product_info['price'] . "',
							special = '" . ($product_info['special'] !== false ? (float)$product_info['special'] : "NULL") . "'");
					}
				}
			}
			unset($this->session->data['customer_group_id_override']);
	}

		// Вспомогательный метод (копия вашего getProduct, но принимающая GroupID аргументом)
	private function getProductForIndex($product_id, $customer_group_id) {
			$query = $this->db->query("SELECT DISTINCT *, pd.name AS name, p.image, m.name AS manufacturer, p.price2, p.price3, p.discount1c, (SELECT price FROM " . DB_PREFIX . "product_discount pd2 WHERE pd2.product_id = p.product_id AND pd2.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "' AND pd2.quantity = '1' AND ((pd2.date_start = '0000-00-00' OR pd2.date_start < NOW()) AND (pd2.date_end = '0000-00-00' OR pd2.date_end > NOW())) ORDER BY pd2.priority ASC, pd2.price ASC LIMIT 1) AS discount, (SELECT price FROM " . DB_PREFIX . "product_special ps WHERE ps.product_id = p.product_id AND ps.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "' AND ((ps.date_start = '0000-00-00' OR ps.date_start < NOW()) AND (ps.date_end = '0000-00-00' OR ps.date_end > NOW())) ORDER BY ps.priority ASC, ps.price ASC LIMIT 1) AS special, (SELECT points FROM " . DB_PREFIX . "product_reward pr WHERE pr.product_id = p.product_id AND pr.customer_group_id = '" . (int)$this->config->get('config_customer_group_id') . "') AS reward, (SELECT ss.name FROM " . DB_PREFIX . "stock_status ss WHERE ss.stock_status_id = p.stock_status_id AND ss.language_id = '" . (int)$this->config->get('config_language_id') . "') AS stock_status, (SELECT wcd.unit FROM " . DB_PREFIX . "weight_class_description wcd WHERE p.weight_class_id = wcd.weight_class_id AND wcd.language_id = '" . (int)$this->config->get('config_language_id') . "') AS weight_class, (SELECT lcd.unit FROM " . DB_PREFIX . "length_class_description lcd WHERE p.length_class_id = lcd.length_class_id AND lcd.language_id = '" . (int)$this->config->get('config_language_id') . "') AS length_class, (SELECT AVG(rating) AS total FROM " . DB_PREFIX . "review r1 WHERE r1.product_id = p.product_id AND r1.status = '1' GROUP BY r1.product_id) AS rating, (SELECT COUNT(*) AS total FROM " . DB_PREFIX . "review r2 WHERE r2.product_id = p.product_id AND r2.status = '1' GROUP BY r2.product_id) AS reviews, p.sort_order FROM " . DB_PREFIX . "product p LEFT JOIN " . DB_PREFIX . "product_description pd ON (p.product_id = pd.product_id) LEFT JOIN " . DB_PREFIX . "product_to_store p2s ON (p.product_id = p2s.product_id) LEFT JOIN " . DB_PREFIX . "manufacturer m ON (p.manufacturer_id = m.manufacturer_id) WHERE p.product_id = '" . (int)$product_id . "' AND pd.language_id = '" . (int)$this->config->get('config_language_id') . "' AND p.status = '1' AND p.date_available <= NOW() AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "'");

    if ($query->num_rows) {
        // --- ЛОГИКА РАСЧЕТА PRICE ---
       
        
        if ($customer_group_id == 3) {
            $base_price = $query->row['price2']; // Дилер
        } elseif ($customer_group_id == 4) {
            $base_price = $query->row['price3']; // Оптовик
        } else {
            $base_price = $query->row['price'];  // Обычный
        }

        // Если есть discount (скидка от количества 1), приоритет ей, иначе базовой цене
        $final_price = ($query->row['discount'] ? $query->row['discount'] : $base_price);
        
        if ($final_price < 0) $final_price = 0;

      // --- ЛОГИКА РАСЧЕТА SPECIAL ---
$final_special = false;

// Уровень 1: discount1c (процент скидки)
if (isset($query->row['discount1c']) && (float)$query->row['discount1c'] > 0) {
    $percent = (float)$query->row['discount1c'];
    $final_special = $final_price - ($final_price * ($percent / 100));
} 
// Уровень 2: Стандартный special из базы (строгая проверка, что цена > 0)
elseif (isset($query->row['special']) && (float)$query->row['special'] > 0) {
    $final_special = (float)$query->row['special'];
} 
// Уровень 3: Скидка из категории
else {
    $category_discount_query = $this->db->query("
        SELECT MAX(c.discount) as max_discount 
        FROM " . DB_PREFIX . "product_to_category p2c 
        LEFT JOIN " . DB_PREFIX . "category c ON (p2c.category_id = c.category_id) 
        WHERE p2c.product_id = '" . (int)$product_id . "'
    ");
    
    // Проверяем, что запрос вернул результат и max_discount действительно больше 0
    if ($category_discount_query->num_rows && (float)$category_discount_query->row['max_discount'] > 0) {
        $max_cat_discount = (float)$category_discount_query->row['max_discount'];
        $final_special = $final_price - ($final_price * ($max_cat_discount / 100));
    }
}

// Финальная проверка: если спеццена была рассчитана, она не может быть меньше 0
// Если $final_special остался false, это условие пропустится
if ($final_special !== false && $final_special < 0) {
    $final_special = 0;
}

        return array(
            'product_id'       => $query->row['product_id'],
            'name'             => $query->row['name'],
            'description'      => $query->row['description'],
            'meta_title'       => $query->row['meta_title'],
            'meta_description' => $query->row['meta_description'],
            'meta_keyword'     => $query->row['meta_keyword'],
            'tag'              => $query->row['tag'],
            'model'            => $query->row['model'],
            'sku'              => $query->row['sku'],
            'upc'              => $query->row['upc'],
            'ean'              => $query->row['ean'],
            'jan'              => $query->row['jan'],
            'isbn'             => $query->row['isbn'],
            'mpn'              => $query->row['mpn'],
            'location'         => $query->row['location'],
            'quantity'         => $query->row['quantity'],
            'stock_status'     => $query->row['stock_status'],
            'image'            => $query->row['image'],
            'manufacturer_id'  => $query->row['manufacturer_id'],
            'manufacturer'     => $query->row['manufacturer'],
            'price'            => $final_price, // Наш расчет
            'special'          => $final_special, // Наш расчет
            'reward'           => $query->row['reward'],
            'points'           => $query->row['points'],
            'tax_class_id'     => $query->row['tax_class_id'],
            'date_available'   => $query->row['date_available'],
            'weight'           => $query->row['weight'],
            'weight_class_id'  => $query->row['weight_class_id'],
            'length'           => $query->row['length'],
            'width'            => $query->row['width'],
            'height'           => $query->row['height'],
            'length_class_id'  => $query->row['length_class_id'],
            'subtract'         => $query->row['subtract'],
            'rating'           => round(($query->row['rating']===null) ? 0 : $query->row['rating']),
            'reviews'          => $query->row['reviews'] ? $query->row['reviews'] : 0,
            'minimum'          => $query->row['minimum'],
            'sort_order'       => $query->row['sort_order'],
            'status'           => $query->row['status'],
            'date_added'       => $query->row['date_added'],
            'date_modified'    => $query->row['date_modified'],
            'viewed'           => $query->row['viewed']
        );
    } else {
        return false;
    }
}


public function getAttributesByCategory($category_ids) {
    if (empty($category_ids)) return [];
    
    // Превращаем массив ID в строку для SQL: "1,2,3,4"
    $implode = array();
    foreach ((array)$category_ids as $category_id) {
        $implode[] = (int)$category_id;
    }
    $category_list = implode(',', $implode);

    $language_id = (int)$this->config->get('config_language_id');
    
    // Кэшируем по строке из ID категорий, чтобы для каждой ветки был свой кэш
    $cache_key = 'category.attributes.' . md5($category_list) . '.' . $language_id;
    $attribute_data = $this->cache->get($cache_key);

    if (!$attribute_data) {
        $sql = "SELECT 
                    ad.filter_name, 
                    ad.name AS attribute_name, 
                    a.attribute_id, 
                    pa.text 
                FROM " . DB_PREFIX . "product_attribute pa 
                INNER JOIN " . DB_PREFIX . "attribute a ON (pa.attribute_id = a.attribute_id) 
                INNER JOIN " . DB_PREFIX . "attribute_description ad ON (a.attribute_id = ad.attribute_id) 
                INNER JOIN " . DB_PREFIX . "product_to_category p2c ON (pa.product_id = p2c.product_id)
                INNER JOIN " . DB_PREFIX . "product p ON (pa.product_id = p.product_id)
                WHERE p2c.category_id IN (" . $category_list . ") 
                    AND ad.language_id = '" . $language_id . "'
                    AND p.status = '1'
                GROUP BY a.attribute_id, pa.text
                ORDER BY a.sort_order, ad.name";

        $query = $this->db->query($sql);
        $attribute_data = [];

        foreach ($query->rows as $result) {
            $key = $result['filter_name'] ?: $result['attribute_id'];
            
            // Чистим текст (важно для группировки)
            $text_value = trim($result['text']);
            if ($text_value === '') continue;

            if (!isset($attribute_data[$key])) {
                $attribute_data[$key] = [
                    'attribute_id' => $result['attribute_id'],
                    'name'         => $result['attribute_name'],
                    'values'       => []
                ];
            }
            
            // Чтобы не дублировать значения из разных подкатегорий
            if (!in_array($text_value, $attribute_data[$key]['values'])) {
                $attribute_data[$key]['values'][] = $text_value;
            }
        }

        $this->cache->set($cache_key, $attribute_data);
    }

    return $attribute_data;
}

public function getCategoryPhysicalLimits($category_ids) {
    if (empty($category_ids)) return [];

    $category_list = implode(',', array_map('intval', (array)$category_ids));

    $sql = "SELECT 
                MIN(p.length) as min_length, MAX(p.length) as max_length,
                MIN(p.width) as min_width, MAX(p.width) as max_width,
                MIN(p.height) as min_height, MAX(p.height) as max_height,
                MIN(p.weight) as min_weight, MAX(p.weight) as max_weight
            FROM " . DB_PREFIX . "product p
            INNER JOIN " . DB_PREFIX . "product_to_category p2c ON (p.product_id = p2c.product_id)
            WHERE p2c.category_id IN (" . $category_list . ") 
            AND p.status = '1'";

    $query = $this->db->query($sql);

    return $query->row;
}





}
