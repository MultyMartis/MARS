<?php
class ControllerProductCategory extends Controller {
	public function index() {
		require_once(DIR_SYSTEM . 'library/zpm/category_visibility.php');
		$visibility = new CategoryVisibility();

		$this->load->language('product/category');

		$this->load->model('catalog/category');

		$this->load->model('catalog/product');

		$this->load->model('tool/image');

		$this->document->setBodyClass('page page--category');

		$filter_attributes = [];

		if (isset($this->request->get['filter'])) {
			$filter = $this->request->get['filter'];
		} else {
			$filter = '';
		}



		if (isset($this->request->get['sort'])) {
			$sort = $this->request->get['sort'];
		} else {
			$sort = 'p.date_added';
		}

		if (isset($this->request->get['order'])) {
			$order = $this->request->get['order'];
		} else {
			$order = 'DESC';
		}

		$data['sorttext'] = 'Умолчанию';
		if (($sort == 'p.price') AND ($order == 'ASC')) $data['sorttext'] = 'Сначала дешевле';
		if (($sort == 'p.price') AND ($order == 'DESC')) $data['sorttext'] = 'Сначала дороже';
		if (($sort == 'pd.name') AND ($order == 'ASC')) $data['sorttext'] = 'Название - от А до Я';
		if (($sort == 'pd.name') AND ($order == 'DESC')) $data['sorttext'] = 'Название - от Я до А';


		if (isset($this->request->get['page'])) {
			$page = (int)$this->request->get['page'];
		} else {
			$page = 1;
		}

		if (isset($this->request->get['limit'])) {
			$limit = (int)$this->request->get['limit'];
		} else {
			$limit = $this->config->get('theme_' . $this->config->get('config_theme') . '_product_limit');
		}

		$data['breadcrumbs'] = array();

		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_home'),
			'href' => $this->url->link('common/home')
		);

		$data['breadcrumbs'][] = array(
			'text' => 'Каталог',
			'href' => $visibility->isLaunchMode() ? $visibility->getPrimaryCatalogEntry() : '/katalog',

		);

		if (isset($this->request->get['path'])) {
			$url = '';

			if (isset($this->request->get['sort'])) {
				$url .= '&sort=' . $this->request->get['sort'];
			}

			if (isset($this->request->get['order'])) {
				$url .= '&order=' . $this->request->get['order'];
			}

			if (isset($this->request->get['limit'])) {
				$url .= '&limit=' . $this->request->get['limit'];
			}

			$path = '';

			$parts = explode('_', (string)$this->request->get['path']);

			$category_id = (int)array_pop($parts);

			foreach ($parts as $path_id) {
				if (!$path) {
					$path = (int)$path_id;
				} else {
					$path .= '_' . (int)$path_id;
				}

				$category_info = $this->model_catalog_category->getCategory($path_id);

				if ($category_info) {
					$data['breadcrumbs'][] = array(
						'text' => $category_info['name'],
						'href' => $this->url->link('product/category', 'path=' . $path . $url)
					);
				}
			}
		} else {
			$category_id = 0;
		}

		$category_info = $this->model_catalog_category->getCategory($category_id);

		if ($category_info) {
			$this->document->setTitle($category_info['meta_title']);
			$this->document->setDescription($category_info['meta_description']);
			$this->document->setKeywords($category_info['meta_keyword']);

			$data['heading_title'] = $category_info['name'];

			$data['text_compare'] = sprintf($this->language->get('text_compare'), (isset($this->session->data['compare']) ? count($this->session->data['compare']) : 0));

			// Set the last category breadcrumb
			$data['breadcrumbs'][] = array(
				'text' => $category_info['name'],
				'href' => $this->url->link('product/category', 'path=' . $this->request->get['path'])
			);

			$breadcrumbs = new Breadcrumbs();
			$breadcrumbs->breadcrumbs  = $data['breadcrumbs'];
			$this->document->setBreadcrumbs( $breadcrumbs->render() );

			$pageintro = new Pageintro();
			$pageintro->title = $data['heading_title'];
			$pageintro->description = '';
			$this->document->setPageintro($pageintro->render());


			if ($category_info['image']) {
				$data['thumb'] = $this->model_tool_image->resize($category_info['image'], $this->config->get('theme_' . $this->config->get('config_theme') . '_image_category_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_category_height'));
			} else {
				$data['thumb'] = '';
			}

			$data['description'] = html_entity_decode($category_info['description'], ENT_QUOTES, 'UTF-8');
			$data['compare'] = $this->url->link('product/compare');

			$url = '';

			if (isset($this->request->get['filter'])) {
				$url .= '&filter=' . $this->request->get['filter'];
			}

			if (isset($this->request->get['sort'])) {
				$url .= '&sort=' . $this->request->get['sort'];
			}

			if (isset($this->request->get['order'])) {
				$url .= '&order=' . $this->request->get['order'];
			}

			if (isset($this->request->get['limit'])) {
				$url .= '&limit=' . $this->request->get['limit'];
			}

			$data['categories'] = array();

			$results = $this->model_catalog_category->getCategories($category_id);

			foreach ($results as $result) {
				$filter_data = array(
					'filter_category_id'  => $result['category_id'],
					'filter_sub_category' => true
				);

				if ($result['image']) {
					$thumb = $this->model_tool_image->resize($result['image'], $this->config->get('theme_' . $this->config->get('config_theme') . '_image_category_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_category_height'));
				} else {
					$thumb =  $this->model_tool_image->resize('placeholder.png', $this->config->get('theme_' . $this->config->get('config_theme') . '_image_category_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_category_height'));;
				}

				$totalsub = $this->model_catalog_product->getTotalProducts($filter_data);

				if ($totalsub > 0)

					$data['categories'][] = array(
						'name' => $result['name'] . ($this->config->get('config_product_count') ? ' (' . $totalsub . ')' : ''),
						'href' => $this->url->link('product/category', 'path=' . $this->request->get['path'] . '_' . $result['category_id'] . $url),
						'thumb'	=> $thumb,

					);
			}

			//print_r($data['categories']);


			$data['products'] = array();
			$data['productcards'] = array();

		$custom_filters = array();

		$selected_attributes = [];


		if (isset($this->request->get['filters'])) {
			$filter_string = html_entity_decode($this->request->get['filters']);
			// Обратная замена разделителя
			$filter_string = str_replace(';', '&', $filter_string);
			
			parse_str($filter_string, $custom_filters);

		

			if (isset($custom_filters['attr']) && is_array($custom_filters['attr'])) {
				// Получаем все ключи (bort, gb и т.д.) из подмассива attr
				$selected_attributes = array_keys($custom_filters['attr']);
			}
						
			// Чистим только числовые диапазоны
			$numeric_keys = ['price_from', 'price_to', 'len_from', 'len_to', 'w_from', 'w_to', 'h_from', 'h_to'];
			
			foreach ($custom_filters as $key => &$value) {
				if (is_array($value)) {
					continue; 
				}
				if (in_array($key, $numeric_keys)) {
					// Убираем пробелы (из-за fmtInt в JS) и превращаем в число
					$value = (float)str_replace(' ', '', $value);					
				}
				if ($key == 'price_from') $data['min_price_selected'] = $value;
				if ($key == 'price_to') $data['max_price_selected'] = $value;
				if ($key == 'in_stock') $data['filter_in_stock'] = $value;
				if ($key == 'preorder_only') $data['filter_preorder_only'] = $value;
				if ($key == 'only_with_price') $data['filter_only_with_price'] = $value;
				if ($key == 'only_discount') $data['filter_only_discount'] = $value;
				
			}
			unset($value);
		}





			$filter_data = array(
				'filter_category_id' => $category_id,
				'filter_sub_category' => true,
				'filter_filter'      => $filter,
				'filter_custom'       => $custom_filters,
				'sort'               => $sort,
				'order'              => $order,
				'start'              => ($page - 1) * $limit,
				'limit'              => $limit
			);

			$product_total = $this->model_catalog_product->getTotalProducts($filter_data);

			$results = $this->model_catalog_product->getProducts($filter_data);

			//print_r($results);

			include('product_results.php');


			// Получаем границы цен для этой категории

			$price_range_data = array(
				'filter_category_id'  => $category_id,
				'filter_sub_category' => true, // Это то самое условие
				'filter_attributes'   => $filter_attributes // Атрибуты из GET
			);

			$price_limits = $this->model_catalog_product->getCategoryPriceRange($price_range_data);


			$data['min_price'] = floor($price_limits['min']);
			$data['max_price'] = ceil($price_limits['max']);

			if (!isset($data['min_price_selected'])) $data['min_price_selected'] = $data['min_price'];
			if (!isset($data['max_price_selected'])) $data['max_price_selected'] = $data['max_price'];

		

			$data['filter_groups'] = [];
			$data['filter_secondary_groups'] = [];
			$data['filter_secondary_open'] = false;

			require_once(DIR_SYSTEM . 'library/zpm/filter_profile_resolver.php');
			$filter_profile_resolver = new FilterProfileResolver($this->db);
			$active_filter_profile = $filter_profile_resolver->resolveForCategory($category_id);
			$data['filter_profile_active'] = !empty($active_filter_profile);
			$data['filter_profile_id'] = $active_filter_profile ? (int)$active_filter_profile['profile_id'] : 0;

			$category_ids = array($category_id);
			$query = $this->db->query("SELECT category_id FROM " . DB_PREFIX . "category_path WHERE path_id = '" . (int)$category_id . "'");

			foreach ($query->rows as $result) {
				$category_ids[] = $result['category_id'];
			}

			$filter_attributes = $this->model_catalog_product->getAttributesByCategory($category_ids, $category_id);

		

			foreach ($filter_attributes as $slug => $attribute) {
				$values = [];
				
				foreach ($attribute['values'] as $value) {
					$is_checked = isset($custom_filters['attr'][$slug]) && 
                      is_array($custom_filters['attr'][$slug]) && 
                      in_array($value, $custom_filters['attr'][$slug]);

					$values[] = [
						'text'    => $value,
						'slug'    => $value,
						'checked' => $is_checked
					];
				}

				$group = [
					'attribute_id' => $attribute['attribute_id'],
					'group_slug'   => $slug,
					'name'         => $attribute['name'],
					'values'       => $values,
					'expanded'		=>  in_array($slug, $selected_attributes),
				];

				if ($data['filter_profile_active'] && !empty($attribute['tier']) && $attribute['tier'] === FilterProfileResolver::TIER_SECONDARY) {
					$data['filter_secondary_groups'][] = $group;
					if ($group['expanded']) {
						$data['filter_secondary_open'] = true;
					}
				} else {
					$data['filter_groups'][] = $group;
				}
			}

			// $category_ids у нас уже есть из предыдущего шага (через category_path)
			$physical_limits = $this->model_catalog_product->getCategoryPhysicalLimits($category_ids);

			// Длина
			$data['min_length'] = floor($physical_limits['min_length']);
			$data['max_length'] = ceil($physical_limits['max_length']);

			// Ширина
			$data['min_width'] = floor($physical_limits['min_width']);
			$data['max_width'] = ceil($physical_limits['max_width']);

			// Высота
			$data['min_height'] = floor($physical_limits['min_height']);
			$data['max_height'] = ceil($physical_limits['max_height']);

			// Вес
			$data['min_weight'] = floor($physical_limits['min_weight']);
			$data['max_weight'] = ceil($physical_limits['max_weight']);

			// Получаем выбранные подкатегории из GET (если есть)

			$selected_subcategories = isset($custom_filters['s']) ? (array)$custom_filters['s'] : [];

			if (!empty($selected_subcategories)) $data['subcat_open'] = 1;


			$data['filter_subcategories'] = [];
			$children = $this->model_catalog_category->getCategories($category_id);

			foreach ($children as $child) {
				$is_checked = in_array((string)$child['category_id'], $selected_subcategories);

				$data['filter_subcategories'][] = [
					'category_id' => $child['category_id'],
					'name'        => $child['name'],
					'checked'     => $is_checked,
					'keyword'     => $child['keyword'] ?? $child['category_id'] 
				];
			}




		

			$url = '';

			if (isset($this->request->get['filter'])) {
				$url .= '&filter=' . $this->request->get['filter'];
			}

			if (isset($this->request->get['limit'])) {
				$url .= '&limit=' . $this->request->get['limit'];
			}

			$data['sorts'] = array();

			$data['sorts'][] = array(
				'text'  => $this->language->get('text_default'),
				'value' => 'p.sort_order-ASC',
				'href'  => $this->url->link('product/category', 'path=' . $this->request->get['path'] . '&sort=p.sort_order&order=ASC' . $url)
			);

			$data['sorts'][] = array(
				'text'  => $this->language->get('text_name_asc'),
				'value' => 'pd.name-ASC',
				'href'  => $this->url->link('product/category', 'path=' . $this->request->get['path'] . '&sort=pd.name&order=ASC' . $url)
			);

			$data['sorts'][] = array(
				'text'  => $this->language->get('text_name_desc'),
				'value' => 'pd.name-DESC',
				'href'  => $this->url->link('product/category', 'path=' . $this->request->get['path'] . '&sort=pd.name&order=DESC' . $url)
			);

			$data['sorts'][] = array(
				'text'  => $this->language->get('text_price_asc'),
				'value' => 'p.price-ASC',
				'href'  => $this->url->link('product/category', 'path=' . $this->request->get['path'] . '&sort=p.price&order=ASC' . $url)
			);

			$data['sorts'][] = array(
				'text'  => $this->language->get('text_price_desc'),
				'value' => 'p.price-DESC',
				'href'  => $this->url->link('product/category', 'path=' . $this->request->get['path'] . '&sort=p.price&order=DESC' . $url)
			);

			if ($this->config->get('config_review_status')) {
				$data['sorts'][] = array(
					'text'  => $this->language->get('text_rating_desc'),
					'value' => 'rating-DESC',
					'href'  => $this->url->link('product/category', 'path=' . $this->request->get['path'] . '&sort=rating&order=DESC' . $url)
				);

				$data['sorts'][] = array(
					'text'  => $this->language->get('text_rating_asc'),
					'value' => 'rating-ASC',
					'href'  => $this->url->link('product/category', 'path=' . $this->request->get['path'] . '&sort=rating&order=ASC' . $url)
				);
			}

			$data['sorts'][] = array(
				'text'  => $this->language->get('text_model_asc'),
				'value' => 'p.model-ASC',
				'href'  => $this->url->link('product/category', 'path=' . $this->request->get['path'] . '&sort=p.model&order=ASC' . $url)
			);

			$data['sorts'][] = array(
				'text'  => $this->language->get('text_model_desc'),
				'value' => 'p.model-DESC',
				'href'  => $this->url->link('product/category', 'path=' . $this->request->get['path'] . '&sort=p.model&order=DESC' . $url)
			);

			$url = '';

			if (isset($this->request->get['filter'])) {
				$url .= '&filter=' . $this->request->get['filter'];
			}

			if (isset($this->request->get['sort'])) {
				$url .= '&sort=' . $this->request->get['sort'];
			}

			if (isset($this->request->get['order'])) {
				$url .= '&order=' . $this->request->get['order'];
			}

			$data['limits'] = array();

			$limits = array_unique(array($this->config->get('theme_' . $this->config->get('config_theme') . '_product_limit'), 25, 50, 75, 100));

			sort($limits);

			foreach($limits as $value) {
				$data['limits'][] = array(
					'text'  => $value,
					'value' => $value,
					'href'  => $this->url->link('product/category', 'path=' . $this->request->get['path'] . $url . '&limit=' . $value)
				);
			}

			$url = '';

			if (isset($this->request->get['filter'])) {
				$url .= '&filter=' . $this->request->get['filter'];
			}

			if (isset($this->request->get['sort'])) {
				$url .= '&sort=' . $this->request->get['sort'];
			}

			if (isset($this->request->get['order'])) {
				$url .= '&order=' . $this->request->get['order'];
			}

			if (isset($this->request->get['limit'])) {
				$url .= '&limit=' . $this->request->get['limit'];
			}

			$pagination = new Pagination();
			$pagination->total = $product_total;
			$pagination->page = $page;
			$pagination->limit = $limit;
			$url = str_replace(array('%3D', '%3B', '%20'), array('=', ';', ' '), $url);
			$pagination->url = $this->url->link('product/category', 'path=' . $this->request->get['path'] . $url . '&page={page}');

			$data['pagination'] = $pagination->render();

			$data['results'] = sprintf($this->language->get('text_pagination'), ($product_total) ? (($page - 1) * $limit) + 1 : 0, ((($page - 1) * $limit) > ($product_total - $limit)) ? $product_total : ((($page - 1) * $limit) + $limit), $product_total, ceil($product_total / $limit));


			if ($page == 1) {
			    $this->document->addLink($this->url->link('product/category', 'path=' . $category_info['category_id']), 'canonical');
			} else {
				$this->document->addLink($this->url->link('product/category', 'path=' . $category_info['category_id'] . '&page='. $page), 'canonical');
			}
			
			if ($page > 1) {
			    $this->document->addLink($this->url->link('product/category', 'path=' . $category_info['category_id'] . (($page - 2) ? '&page='. ($page - 1) : '')), 'prev');
			}

			if ($limit && ceil($product_total / $limit) > $page) {
			    $this->document->addLink($this->url->link('product/category', 'path=' . $category_info['category_id'] . '&page='. ($page + 1)), 'next');
			}

			$data['sort'] = $sort;
			$data['order'] = $order;
			$data['limit'] = $limit;



			$data['filter'] = $this->load->view('sections/filterssidebar', $data);

			$data['certificates'] = $this->load->view('sections/certificates');
			$data['aboutteaser'] = $this->load->view('sections/aboutteaser');
			$data['blockadvantagestop'] = $this->load->view('sections/blockadvantagestop');
			$data['blockdealersform'] = $this->load->view('sections/blockdealersform');
			$data['blockadvantagesbottom'] = $this->load->view('sections/blockadvantagesbottom');

			$data['continue'] = $this->url->link('common/home');

			$data['column_left'] = $this->load->controller('common/column_left');
			$data['column_right'] = $this->load->controller('common/column_right');
			$data['content_top'] = $this->load->controller('common/content_top');
			$data['content_bottom'] = $this->load->controller('common/content_bottom');
			$data['footer'] = $this->load->controller('common/footer');
			$data['header'] = $this->load->controller('common/header');

			$this->response->setOutput($this->load->view('product/category', $data));
		} else {
			$url = '';

			if (isset($this->request->get['path'])) {
				$url .= '&path=' . $this->request->get['path'];
			}

			if (isset($this->request->get['filter'])) {
				$url .= '&filter=' . $this->request->get['filter'];
			}

			if (isset($this->request->get['sort'])) {
				$url .= '&sort=' . $this->request->get['sort'];
			}

			if (isset($this->request->get['order'])) {
				$url .= '&order=' . $this->request->get['order'];
			}

			if (isset($this->request->get['page'])) {
				$url .= '&page=' . $this->request->get['page'];
			}

			if (isset($this->request->get['limit'])) {
				$url .= '&limit=' . $this->request->get['limit'];
			}

			$data['breadcrumbs'][] = array(
				'text' => $this->language->get('text_error'),
				'href' => $this->url->link('product/category', $url)
			);

			$this->document->setTitle($this->language->get('text_error'));

			$data['continue'] = $this->url->link('common/home');

			$this->response->addHeader($this->request->server['SERVER_PROTOCOL'] . ' 404 Not Found');

			$data['column_left'] = $this->load->controller('common/column_left');
			$data['column_right'] = $this->load->controller('common/column_right');
			$data['content_top'] = $this->load->controller('common/content_top');
			$data['content_bottom'] = $this->load->controller('common/content_bottom');
			$data['footer'] = $this->load->controller('common/footer');
			$data['header'] = $this->load->controller('common/header');

			$this->response->setOutput($this->load->view('error/not_found', $data));
		}
	}
}
