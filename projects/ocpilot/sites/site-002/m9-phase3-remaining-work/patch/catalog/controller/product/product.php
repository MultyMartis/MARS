<?php
class ControllerProductProduct extends Controller {
	private $error = array();

	public function index() {
		$this->load->language('product/product');

		$documents = [];
		$this->load->model('catalog/product');


		$data['breadcrumbs'] = array();

		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_home'),
			'href' => $this->url->link('common/home')
		);

		$this->setProductCategoryBodyClasses();

		$this->load->model('catalog/category');

		if (isset($this->request->get['path'])) {
			$path = '';

			$parts = explode('_', (string)$this->request->get['path']);

			$category_id = (int)array_pop($parts);
			

			foreach ($parts as $path_id) {
				if (!$path) {
					$path = $path_id;
				} else {
					$path .= '_' . $path_id;
				}

				$category_info = $this->model_catalog_category->getCategory($path_id);

				if ($category_info) {
					$data['breadcrumbs'][] = array(
						'text' => $category_info['name'],
						'href' => $this->url->link('product/category', 'path=' . $path)
					);
					$docs = $this->model_catalog_product->getCategoryDocuments($path_id);
					if (is_array($docs)) $documents = array_merge($documents, $docs);
				}
			}



			// Set the last category breadcrumb
			$category_info = $this->model_catalog_category->getCategory($category_id);

			if ($category_info) {
				$url = '';

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
					'text' => $category_info['name'],
					'href' => $this->url->link('product/category', 'path=' . $this->request->get['path'] . $url)
				);
				$docs = $this->model_catalog_product->getCategoryDocuments($category_id); 
					if (is_array($docs)) $documents = array_merge($documents, $docs);
			}
		}

		$this->load->model('catalog/manufacturer');

		if (isset($this->request->get['manufacturer_id'])) {
			$data['breadcrumbs'][] = array(
				'text' => $this->language->get('text_brand'),
				'href' => $this->url->link('product/manufacturer')
			);

			$url = '';

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

			$manufacturer_info = $this->model_catalog_manufacturer->getManufacturer($this->request->get['manufacturer_id']);

			if ($manufacturer_info) {
				$data['breadcrumbs'][] = array(
					'text' => $manufacturer_info['name'],
					'href' => $this->url->link('product/manufacturer/info', 'manufacturer_id=' . $this->request->get['manufacturer_id'] . $url)
				);
			}
		}

		if (isset($this->request->get['search']) || isset($this->request->get['tag'])) {
			$url = '';

			if (isset($this->request->get['search'])) {
				$url .= '&search=' . $this->request->get['search'];
			}

			if (isset($this->request->get['tag'])) {
				$url .= '&tag=' . $this->request->get['tag'];
			}

			if (isset($this->request->get['description'])) {
				$url .= '&description=' . $this->request->get['description'];
			}

			if (isset($this->request->get['category_id'])) {
				$url .= '&category_id=' . $this->request->get['category_id'];
			}

			if (isset($this->request->get['sub_category'])) {
				$url .= '&sub_category=' . $this->request->get['sub_category'];
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
				'text' => $this->language->get('text_search'),
				'href' => $this->url->link('product/search', $url)
			);
		}

		if (isset($this->request->get['product_id'])) {
			$product_id = (int)$this->request->get['product_id'];
		} else {
			$product_id = 0;
		}

		




		

		$product_info = $this->model_catalog_product->getProduct($product_id);

		$cartproducts = $this->cart->getProducts();
		$cartqty = 0;
		if (!empty($cartproducts))
					{
						foreach ($cartproducts as $cp)
							{
								if ($cp['product_id'] == $product_id) $cartqty = $cp['quantity'];
							}
					}



		//check product page open from cateory page
		if (isset($this->request->get['path'])) {
			$parts = explode('_', (string)$this->request->get['path']);
						
			if(empty($this->model_catalog_product->checkProductCategory($product_id, $parts))) {
				$product_info = array();
			}
		}

		//check product page open from manufacturer page
		if (isset($this->request->get['manufacturer_id']) && !empty($product_info)) {
			if($product_info['manufacturer_id'] !=  $this->request->get['manufacturer_id']) {
				$product_info = array();
			}
		}

		if ($product_info) {
			$url = '';

			if (isset($this->request->get['path'])) {
				$url .= '&path=' . $this->request->get['path'];
			}

			if (isset($this->request->get['filter'])) {
				$url .= '&filter=' . $this->request->get['filter'];
			}

			if (isset($this->request->get['manufacturer_id'])) {
				$url .= '&manufacturer_id=' . $this->request->get['manufacturer_id'];
			}

			if (isset($this->request->get['search'])) {
				$url .= '&search=' . $this->request->get['search'];
			}

			if (isset($this->request->get['tag'])) {
				$url .= '&tag=' . $this->request->get['tag'];
			}

			if (isset($this->request->get['description'])) {
				$url .= '&description=' . $this->request->get['description'];
			}

			if (isset($this->request->get['category_id'])) {
				$url .= '&category_id=' . $this->request->get['category_id'];
			}

			if (isset($this->request->get['sub_category'])) {
				$url .= '&sub_category=' . $this->request->get['sub_category'];
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
				'text' => $product_info['name'],
				'href' => $this->url->link('product/product', $url . '&product_id=' . $this->request->get['product_id'])
			);

			$breadcrumbs = new Breadcrumbs();
			$breadcrumbs->breadcrumbs  = $data['breadcrumbs'];
			$this->document->setBreadcrumbs( $breadcrumbs->render() );
			$this->document->setProductid( $product_id );

		

			$this->document->setTitle($product_info['meta_title']);

			$attribute_groups = $this->model_catalog_product->getProductAttributes($this->request->get['product_id']);
			$meta_description = $this->resolveProductMetaDescription($product_info, $data['breadcrumbs'], $attribute_groups);
			$meta_keywords = $this->resolveProductMetaKeywords($product_info, $data['breadcrumbs'], $attribute_groups);

			$this->document->setDescription($meta_description);
			$this->document->setKeywords($meta_keywords);
			$this->document->addLink($this->url->link('product/product', 'product_id=' . $this->request->get['product_id']), 'canonical');


			$data['heading_title'] = $product_info['name'];

			$data['text_minimum'] = sprintf($this->language->get('text_minimum'), $product_info['minimum']);
			$data['text_login'] = sprintf($this->language->get('text_login'), $this->url->link('account/login', '', true), $this->url->link('account/register', '', true));

			$this->load->model('catalog/review');

			$data['tab_review'] = sprintf($this->language->get('tab_review'), $product_info['reviews']);

			$data['product_id'] = (int)$this->request->get['product_id'];
			$data['manufacturer'] = $product_info['manufacturer'];
			$data['manufacturers'] = $this->url->link('product/manufacturer/info', 'manufacturer_id=' . $product_info['manufacturer_id']);
			$data['model'] = $product_info['model'];
			$data['reward'] = $product_info['reward'];
			$data['points'] = $product_info['points'];
			$data['description'] = html_entity_decode($product_info['description'], ENT_QUOTES, 'UTF-8');

			$data['heading_subtitle'] = "это надо сделать дополнительным мини-описанием товара";

			if ($product_info['quantity'] <= 0) {
				$data['stock'] = $product_info['stock_status'];
			} elseif ($this->config->get('config_stock_display')) {
				$data['stock'] = $product_info['quantity'];
			} else {
				$data['stock'] = $this->language->get('text_instock');
			}

			$data['incart'] = $cartqty;

			$this->load->model('tool/image');

			if ($product_info['image']) {
				$data['popup'] = $this->model_tool_image->resize($product_info['image'], $this->config->get('theme_' . $this->config->get('config_theme') . '_image_popup_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_popup_height'));
				$this->document->setImage( $data['popup'] );
			} else {
				$data['popup'] = $this->model_tool_image->resize('placeholder.png', $this->config->get('theme_' . $this->config->get('config_theme') . '_image_popup_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_popup_height'));;
			}

			if ($product_info['image']) {
				$data['thumb'] = $this->model_tool_image->resize($product_info['image'], $this->config->get('theme_' . $this->config->get('config_theme') . '_image_thumb_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_thumb_height'));
			} else {
				$data['thumb'] = $this->model_tool_image->resize('placeholder.png', $this->config->get('theme_' . $this->config->get('config_theme') . '_image_thumb_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_thumb_height'));
			}

			$data['images'] = array();

			$results = $this->model_catalog_product->getProductImages($this->request->get['product_id']);

			foreach ($results as $result) {
				$data['images'][] = array(
					'popup' => $this->model_tool_image->resize($result['image'], $this->config->get('theme_' . $this->config->get('config_theme') . '_image_popup_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_popup_height')),
					'thumb' => $this->model_tool_image->resize($result['image'], $this->config->get('theme_' . $this->config->get('config_theme') . '_image_additional_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_additional_height'))
				);
			}

			$pricecalc = 0; $priceoldcalc = 0; $data['priceproc'] =false;

			if ($this->customer->isLogged() || !$this->config->get('config_customer_price')) {
				$pricecalc = $product_info['price'];
				$data['price'] = $this->currency->format($this->tax->calculate($product_info['price'], $product_info['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency']);
			} else {
				$data['price'] = false;
			}

			if ($product_info['special'] !== false && (float)$product_info['special'] > 0) {



				$priceoldcalc = $product_info['price'];  
				if ($product_info['price']!=0)
					$data['priceproc'] = "-".intval(( $product_info['price'] - $product_info['special']) /  $product_info['price'] *100)."%";
				else $data['priceproc'] = false;
				$priceold = $this->currency->format($this->tax->calculate($product_info['price'], $product_info['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency']);
				$data['price'] = $this->currency->format($this->tax->calculate($product_info['special'], $product_info['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency']);
				$tax_price = (float)$product_info['special'];
			} else {
				$data['special'] = false;
				$tax_price = (float)$product_info['price'];
				$priceold = false;
			}

			if ($this->config->get('config_tax')) {
				$data['tax'] = $this->currency->format($tax_price, $this->session->data['currency']);
			} else {
				$data['tax'] = false;
			}

			$discounts = $this->model_catalog_product->getProductDiscounts($this->request->get['product_id']);

			$data['discounts'] = array();

			foreach ($discounts as $discount) {
				$data['discounts'][] = array(
					'quantity' => $discount['quantity'],
					'price'    => $this->currency->format($this->tax->calculate($discount['price'], $product_info['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency'])
				);
			}

			$canCart = true;
			$statusText = "Цена по запросу";
			$deliveryText = '';
			$ctaText = "ctaText";

			

			if ($product_info['quantity']>0) {
						$statusText = "В наличии: ".$product_info['quantity']." шт.";						
						
					} else {

						$statusText = "Под заказ";
						if ($pricecalc >0)
							$deliveryText = "Срок поставки: от 5–10 дней";
						$canCart = true;
						
				}

				if ($pricecalc == 0) {
						$canCart = false;
						
						$data['price'] = 'По запросу';
						$data['showrequest'] = true;
				
				}


			$data['cancart'] = $canCart;
			$data['statusText'] = $statusText;
			$data['deliveryText'] = $deliveryText;
			$data['priceold'] = $priceold;

			$data['wishlisted'] = $this->model_catalog_product->isWishlisted($this->request->get['product_id']);
			$data['compared'] = $this->model_catalog_product->isCompared($this->request->get['product_id']);



			$data['options'] = array();

			foreach ($this->model_catalog_product->getProductOptions($this->request->get['product_id']) as $option) {
				$product_option_value_data = array();

				foreach ($option['product_option_value'] as $option_value) {
					if (!$option_value['subtract'] || ($option_value['quantity'] > 0)) {
						if ((($this->config->get('config_customer_price') && $this->customer->isLogged()) || !$this->config->get('config_customer_price')) && (float)$option_value['price']) {
							$price = $this->currency->format($this->tax->calculate($option_value['price'], $product_info['tax_class_id'], $this->config->get('config_tax') ? 'P' : false), $this->session->data['currency']);
						} else {
							$price = false;
						}

						$product_option_value_data[] = array(
							'product_option_value_id' => $option_value['product_option_value_id'],
							'option_value_id'         => $option_value['option_value_id'],
							'name'                    => $option_value['name'],
							'image'                   => $this->model_tool_image->resize($option_value['image'], 50, 50),
							'price'                   => $price,
							'price_prefix'            => $option_value['price_prefix']
						);
					}
				}

				$data['options'][] = array(
					'product_option_id'    => $option['product_option_id'],
					'product_option_value' => $product_option_value_data,
					'option_id'            => $option['option_id'],
					'name'                 => $option['name'],
					'type'                 => $option['type'],
					'value'                => $option['value'],
					'required'             => $option['required']
				);
			}

			if ($product_info['minimum']) {
				$data['minimum'] = $product_info['minimum'];
			} else {
				$data['minimum'] = 1;
			}

			$data['review_status'] = $this->config->get('config_review_status');

			if ($this->config->get('config_review_guest') || $this->customer->isLogged()) {
				$data['review_guest'] = true;
			} else {
				$data['review_guest'] = false;
			}

			if ($this->customer->isLogged()) {
				$data['customer_name'] = $this->customer->getFirstName() . '&nbsp;' . $this->customer->getLastName();
			} else {
				$data['customer_name'] = '';
			}

			$data['reviews'] = sprintf($this->language->get('text_reviews'), (int)$product_info['reviews']);
			$data['rating'] = (int)$product_info['rating'];

			// Captcha
			if ($this->config->get('captcha_' . $this->config->get('config_captcha') . '_status') && in_array('review', (array)$this->config->get('config_captcha_page'))) {
				$data['captcha'] = $this->load->controller('extension/captcha/' . $this->config->get('config_captcha'));
			} else {
				$data['captcha'] = '';
			}

			$data['share'] = $this->url->link('product/product', 'product_id=' . (int)$this->request->get['product_id']);

			$data['attribute_groups'] = $attribute_groups;

			$data['super_atts'] =[];
			if ($product_info['length'] > 0) $data['super_atts'][] = array('name'=>"Длина, мм", "text" => intval($product_info['length']), 'attribute_id' => 0);
			if ($product_info['width'] > 0) $data['super_atts'][] = array('name'=>"Ширина, мм", "text" => intval($product_info['width']), 'attribute_id' => 0);
			if ($product_info['height'] > 0) $data['super_atts'][] = array('name'=>"Высота, мм", "text" => intval($product_info['height']), 'attribute_id' => 0);
			if ($product_info['weight'] > 0) $data['super_atts'][] = array('name'=>"Масса, кг", "text" => round((float)$product_info['weight'], 2), 'attribute_id' => 0);

			if (!empty($data['attribute_groups']))
				{
					if (!empty($data['super_atts']) )
						array_unshift($data['attribute_groups'], array('attribute_group_id'=>0, 'name'=>'', 'attribute'=>$data['super_atts']));

					// SITE-002-PROD-PDP-HERO-SPECS-STELLAZHI-86-01 — family hero specs resolver
				$hero_attr_map = array();

				foreach ($data['attribute_groups'] as $ag) {
					foreach ($ag['attribute'] as $a) {
						$aid = (int)$a['attribute_id'];

						if ($aid && trim($a['text']) !== '' && !isset($hero_attr_map[$aid])) {
							$hero_attr_map[$aid] = $a;
						}
					}
				}

				$hero_seen = array();

				foreach ($data['super_atts'] as $a) {
					if (!empty($a['attribute_id'])) {
						$hero_seen[(int)$a['attribute_id']] = true;
					}
				}

				$path_category_id = 0;

				if (isset($this->request->get['path']) && $this->request->get['path'] !== '') {
					$path_parts = explode('_', (string)$this->request->get['path']);
					$path_category_id = (int)array_pop($path_parts);
				}

				$hero_resolver_file = DIR_SYSTEM . 'library/zpm/product_hero_specs_resolver.php';

				if (is_file($hero_resolver_file)) {
					require_once($hero_resolver_file);
					$hero_specs_resolver = new ProductHeroSpecsResolver($this->db);
					$hero_attr_ids = $hero_specs_resolver->resolveAttributeIds((int)$product_id, $path_category_id);
				} elseif (defined('SUPER_ATTS') && is_array(SUPER_ATTS)) {
					$hero_attr_ids = SUPER_ATTS;
				} else {
					$hero_attr_ids = array();
				}

				foreach ($hero_attr_ids as $super_attr_id) {
					$super_attr_id = (int)$super_attr_id;

					if ($super_attr_id && isset($hero_attr_map[$super_attr_id]) && !isset($hero_seen[$super_attr_id])) {
						$data['super_atts'][] = $hero_attr_map[$super_attr_id];
						$hero_seen[$super_attr_id] = true;
					}
				}
				}

			// SITE-002 — PDP extra info display extraction (Run 4.218).
			$data['extra_info_attribute'] = array();

			if (!empty($data['attribute_groups'])) {
				foreach ($data['attribute_groups'] as $group_index => $attribute_group) {
					if (empty($attribute_group['attribute']) || !is_array($attribute_group['attribute'])) {
						continue;
					}

					$filtered_attributes = array();

					foreach ($attribute_group['attribute'] as $attribute) {
						if (trim($attribute['name']) === 'Дополнительные сведения') {
							if (trim($attribute['text']) !== '') {
								$data['extra_info_attribute'] = $attribute;
							}
							continue;
						}

						$filtered_attributes[] = $attribute;
					}

					$data['attribute_groups'][$group_index]['attribute'] = $filtered_attributes;
				}

				$data['attribute_groups'] = array_values(array_filter($data['attribute_groups'], function ($group) {
					return !empty($group['attribute']);
				}));
			}

			
			$data['documents'] = [];

			foreach ($documents as $document) {
				$extension = strtolower(pathinfo($document['filename'], PATHINFO_EXTENSION));
				$type = 'unknown'; 
				if (in_array($extension, ['pdf'])) {
					$type = 'pdf';
				} elseif (in_array($extension, ['doc', 'docx', 'rtf'])) {
					$type = 'word';
				} elseif (in_array($extension, ['xls', 'xlsx', 'csv'])) {
					$type = 'excel';
				} elseif (in_array($extension, ['jpg', 'jpeg'])) {
					$type = 'jpg'; 
				} elseif (in_array($extension, ['png'])) {
					$type = 'png'; 
				}	elseif (in_array($extension, ['webp'])) {
					$type = 'webp'; 
				}

				$data['documents'][] = array(
					'name'     => $document['name'],
					'filename' => $document['filename'],
					'type'     => $type 
				);
			}



			$data['products'] = array();

			$results = $this->model_catalog_product->getProductRelated($this->request->get['product_id']);

			foreach ($results as $result) {
				if ($result['image']) {
					$image = $this->model_tool_image->resize($result['image'], $this->config->get('theme_' . $this->config->get('config_theme') . '_image_related_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_related_height'));
				} else {
					$image = $this->model_tool_image->resize('placeholder.png', $this->config->get('theme_' . $this->config->get('config_theme') . '_image_related_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_related_height'));
				}

				if ($this->customer->isLogged() || !$this->config->get('config_customer_price')) {
					$price = $this->currency->format($this->tax->calculate($result['price'], $result['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency']);
				} else {
					$price = false;
				}

				if (!is_null($result['special']) && (float)$result['special'] >= 0) {
					$special = $this->currency->format($this->tax->calculate($result['special'], $result['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency']);
					$tax_price = (float)$result['special'];
				} else {
					$special = false;
					$tax_price = (float)$result['price'];
				}
	
				if ($this->config->get('config_tax')) {
					$tax = $this->currency->format($tax_price, $this->session->data['currency']);
				} else {
					$tax = false;
				}

				if ($this->config->get('config_review_status')) {
					$rating = (int)$result['rating'];
				} else {
					$rating = false;
				}

				$data['products'][] = array(
					'product_id'  => $result['product_id'],
					'thumb'       => $image,
					'name'        => $result['name'],
					'description' => utf8_substr(trim(strip_tags(html_entity_decode($result['description'], ENT_QUOTES, 'UTF-8'))), 0, $this->config->get('theme_' . $this->config->get('config_theme') . '_product_description_length')) . '..',
					'price'       => $price,
					'special'     => $special,
					'tax'         => $tax,
					'minimum'     => $result['minimum'] > 0 ? $result['minimum'] : 1,
					'rating'      => $rating,
					'href'        => $this->url->link('product/product', 'product_id=' . $result['product_id'])
				);
			}

			$data['tags'] = array();

			if ($product_info['tag']) {
				$tags = explode(',', $product_info['tag']);

				foreach ($tags as $tag) {
					$data['tags'][] = array(
						'tag'  => trim($tag),
						'href' => $this->url->link('product/search', 'tag=' . trim($tag))
					);
				}
			}

			$data['recurrings'] = $this->model_catalog_product->getProfiles($this->request->get['product_id']);

			$this->model_catalog_product->updateViewed($this->request->get['product_id']);
			
			$data['column_left'] = $this->load->controller('common/column_left');
			$data['column_right'] = $this->load->controller('common/column_right');
			$data['content_top'] = $this->load->controller('common/content_top');
			$data['content_bottom'] = $this->load->controller('common/content_bottom');
			$data['footer'] = $this->load->controller('common/footer');
			$data['header'] = $this->load->controller('common/header');

			$data['relproducts'] = $this->load->controller('product/relproducts'); 

			$data['producthero'] = $this->load->view('product/producthero', $data);
			$data['producttabs'] = $this->load->view('product/producttabs', $data);

			$this->response->setOutput($this->load->view('product/product', $data));
		} else {
			$url = '';

			if (isset($this->request->get['path'])) {
				$url .= '&path=' . $this->request->get['path'];
			}

			if (isset($this->request->get['filter'])) {
				$url .= '&filter=' . $this->request->get['filter'];
			}

			if (isset($this->request->get['manufacturer_id'])) {
				$url .= '&manufacturer_id=' . $this->request->get['manufacturer_id'];
			}

			if (isset($this->request->get['search'])) {
				$url .= '&search=' . $this->request->get['search'];
			}

			if (isset($this->request->get['tag'])) {
				$url .= '&tag=' . $this->request->get['tag'];
			}

			if (isset($this->request->get['description'])) {
				$url .= '&description=' . $this->request->get['description'];
			}

			if (isset($this->request->get['category_id'])) {
				$url .= '&category_id=' . $this->request->get['category_id'];
			}

			if (isset($this->request->get['sub_category'])) {
				$url .= '&sub_category=' . $this->request->get['sub_category'];
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
				'href' => $this->url->link('product/product', $url . '&product_id=' . $product_id)
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

	public function review() {
		$this->load->language('product/product');

		$this->load->model('catalog/review');

		if (isset($this->request->get['page'])) {
			$page = (int)$this->request->get['page'];
		} else {
			$page = 1;
		}

		$data['reviews'] = array();

		$review_total = $this->model_catalog_review->getTotalReviewsByProductId($this->request->get['product_id']);

		$results = $this->model_catalog_review->getReviewsByProductId($this->request->get['product_id'], ($page - 1) * 5, 5);

		foreach ($results as $result) {
			$data['reviews'][] = array(
				'author'     => $result['author'],
				'text'       => nl2br($result['text']),
				'rating'     => (int)$result['rating'],
				'date_added' => date($this->language->get('date_format_short'), strtotime($result['date_added']))
			);
		}

		$pagination = new Pagination();
		$pagination->total = $review_total;
		$pagination->page = $page;
		$pagination->limit = 5;
		$pagination->url = $this->url->link('product/product/review', 'product_id=' . $this->request->get['product_id'] . '&page={page}');

		$data['pagination'] = $pagination->render();

		$data['results'] = sprintf($this->language->get('text_pagination'), ($review_total) ? (($page - 1) * 5) + 1 : 0, ((($page - 1) * 5) > ($review_total - 5)) ? $review_total : ((($page - 1) * 5) + 5), $review_total, ceil($review_total / 5));

		$this->response->setOutput($this->load->view('product/review', $data));
	}

	public function write() {
		$this->load->language('product/product');

		$json = array();

		if (isset($this->request->get['product_id']) && $this->request->get['product_id']) {
			if ($this->request->server['REQUEST_METHOD'] == 'POST') {
				if ((utf8_strlen($this->request->post['name']) < 3) || (utf8_strlen($this->request->post['name']) > 25)) {
					$json['error'] = $this->language->get('error_name');
				}

				if ((utf8_strlen($this->request->post['text']) < 25) || (utf8_strlen($this->request->post['text']) > 1000)) {
					$json['error'] = $this->language->get('error_text');
				}
			
				if (empty($this->request->post['rating']) || $this->request->post['rating'] < 0 || $this->request->post['rating'] > 5) {
					$json['error'] = $this->language->get('error_rating');
				}

				// Captcha
				if ($this->config->get('captcha_' . $this->config->get('config_captcha') . '_status') && in_array('review', (array)$this->config->get('config_captcha_page'))) {
					$captcha = $this->load->controller('extension/captcha/' . $this->config->get('config_captcha') . '/validate');

					if ($captcha) {
						$json['error'] = $captcha;
					}
				}

				if (!isset($json['error'])) {
					$this->load->model('catalog/review');

					$this->model_catalog_review->addReview($this->request->get['product_id'], $this->request->post);

					$json['success'] = $this->language->get('text_success');
				}
			}
		} else {
			$json['error'] = $this->language->get('error_product');
		} 

		$this->response->addHeader('Content-Type: application/json');
		$this->response->setOutput(json_encode($json));
	}

	public function getRecurringDescription() {
		$this->load->language('product/product');
		$this->load->model('catalog/product');

		if (isset($this->request->post['product_id'])) {
			$product_id = $this->request->post['product_id'];
		} else {
			$product_id = 0;
		}

		if (isset($this->request->post['recurring_id'])) {
			$recurring_id = $this->request->post['recurring_id'];
		} else {
			$recurring_id = 0;
		}

		if (isset($this->request->post['quantity'])) {
			$quantity = $this->request->post['quantity'];
		} else {
			$quantity = 1;
		}

		$product_info = $this->model_catalog_product->getProduct($product_id);
		
		$recurring_info = $this->model_catalog_product->getProfile($product_id, $recurring_id);

		$json = array();

		if ($product_info && $recurring_info) {
			if (!$json) {
				$frequencies = array(
					'day'        => $this->language->get('text_day'),
					'week'       => $this->language->get('text_week'),
					'semi_month' => $this->language->get('text_semi_month'),
					'month'      => $this->language->get('text_month'),
					'year'       => $this->language->get('text_year'),
				);

				if ($recurring_info['trial_status'] == 1) {
					$price = $this->currency->format($this->tax->calculate($recurring_info['trial_price'] * $quantity, $product_info['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency']);
					$trial_text = sprintf($this->language->get('text_trial_description'), $price, $recurring_info['trial_cycle'], $frequencies[$recurring_info['trial_frequency']], $recurring_info['trial_duration']) . ' ';
				} else {
					$trial_text = '';
				}

				$price = $this->currency->format($this->tax->calculate($recurring_info['price'] * $quantity, $product_info['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency']);

				if ($recurring_info['duration']) {
					$text = $trial_text . sprintf($this->language->get('text_payment_description'), $price, $recurring_info['cycle'], $frequencies[$recurring_info['frequency']], $recurring_info['duration']);
				} else {
					$text = $trial_text . sprintf($this->language->get('text_payment_cancel'), $price, $recurring_info['cycle'], $frequencies[$recurring_info['frequency']], $recurring_info['duration']);
				}

				$json['success'] = $text;
			}
		}

		$this->response->addHeader('Content-Type: application/json');
		$this->response->setOutput(json_encode($json));
	}


	/**
	 * SITE-002 — runtime PDP meta fallback generator (Run 4.201; keywords v1.1 Run 4.202).
	 * Preserves meaningful manual/import meta; generates description/keywords when weak or empty.
	 */
	private function normalizeMetaText($text) {
		$text = html_entity_decode(strip_tags((string)$text), ENT_QUOTES, 'UTF-8');
		$text = preg_replace('/\s+/u', ' ', trim($text));

		return $text;
	}

	private function looksLikeImportStubMeta($meta_description, $product_info) {
		$desc = $this->normalizeMetaText($meta_description);

		if ($desc === '') {
			return false;
		}

		$len = mb_strlen($desc, 'UTF-8');

		if ($len < 145 || $len > 170) {
			return false;
		}

		if (preg_match('/[.!?…]$/u', $desc)) {
			return false;
		}

		if (mb_stripos($desc, 'купить', 0, 'UTF-8') !== false) {
			return false;
		}

		$product_desc = $this->normalizeMetaText(isset($product_info['description']) ? $product_info['description'] : '');

		if ($product_desc !== '') {
			$prefix = mb_substr($product_desc, 0, min(40, mb_strlen($product_desc, 'UTF-8')), 'UTF-8');

			if ($prefix !== '' && mb_stripos($desc, $prefix, 0, 'UTF-8') === 0) {
				return true;
			}
		}

		return ($len >= 155 && $len <= 165);
	}

	private function isUsefulProductMetaDescription($meta_description, $product_info) {
		$desc = $this->normalizeMetaText($meta_description);

		if ($desc === '') {
			return false;
		}

		if (mb_strlen($desc, 'UTF-8') < 80) {
			return false;
		}

		if ($this->looksLikeImportStubMeta($desc, $product_info)) {
			return false;
		}

		$lower = mb_strtolower($desc, 'UTF-8');

		if (preg_match('/^(открытые|закрытые|с полками)\s+(настенные\s+)?полки/u', $lower)) {
			return false;
		}

		if (preg_match('/^(закрытые\s+)?производственные\s+шкафы/u', $lower)) {
			return false;
		}

		return true;
	}

	private function trimMetaDescription($text, $max = 170) {
		$text = $this->normalizeMetaText($text);

		if (mb_strlen($text, 'UTF-8') <= $max) {
			return $text;
		}

		$cut = mb_substr($text, 0, $max, 'UTF-8');

		if (preg_match('/^(.+)[\s,.;:-][^\s,.;:-]*$/u', $cut, $m)) {
			return rtrim($m[1], ' ,.;:-');
		}

		return rtrim($cut);
	}

	private function detectCategoryFamily(array $breadcrumbs) {
		$haystack = '';

		if (isset($this->request->server['REQUEST_URI'])) {
			$haystack .= ' ' . mb_strtolower($this->request->server['REQUEST_URI'], 'UTF-8');
		}

		foreach ($breadcrumbs as $bc) {
			$haystack .= ' ' . mb_strtolower($bc['text'] . ' ' . $bc['href'], 'UTF-8');
		}

		$map = array(
			'stoly' => 'stoly',
			'/stoly/' => 'stoly',
			'polki' => 'polki',
			'telezhki' => 'telezhki',
			'protivn' => 'telezhki',
			'shkaf' => 'shkafy_lari',
			'lari' => 'shkafy_lari',
			'podstavk' => 'podstavki',
			'podtovarnik' => 'podstavki',
			'stellazh' => 'stellazhi',
			'moechn' => 'moechnye_vanny',
			'kotlomoy' => 'moechnye_vanny',
			'vanna' => 'moechnye_vanny',
			'zont' => 'zonty',
			'servirov' => 'telezhki_servirovochnye',
		);

		foreach ($map as $needle => $family) {
			if (mb_strpos($haystack, $needle, 0, 'UTF-8') !== false) {
				return $family;
			}
		}

		return 'generic';
	}

	private function formatProductDimensions($product_info) {
		$l = (float)(isset($product_info['length']) ? $product_info['length'] : 0);
		$w = (float)(isset($product_info['width']) ? $product_info['width'] : 0);
		$h = (float)(isset($product_info['height']) ? $product_info['height'] : 0);

		if ($l > 0 && $w > 0 && $h > 0) {
			return intval($l) . '×' . intval($w) . '×' . intval($h) . ' мм';
		}

		$name = isset($product_info['name']) ? $product_info['name'] : '';

		if (preg_match('/\((\d+)х(\d+)х(\d+)\)/u', $name, $m)) {
			return $m[1] . '×' . $m[2] . '×' . $m[3] . ' мм';
		}

		return '';
	}

	private function flattenProductAttributes(array $attribute_groups) {
		$flat = array();

		foreach ($attribute_groups as $group) {
			if (empty($group['attribute']) || !is_array($group['attribute'])) {
				continue;
			}

			foreach ($group['attribute'] as $attr) {
				$name = isset($attr['name']) ? $this->normalizeMetaText($attr['name']) : '';
				$text = isset($attr['text']) ? $this->normalizeMetaText($attr['text']) : '';

				if ($name !== '' && $text !== '') {
					$flat[] = array('name' => $name, 'text' => $text);
				}
			}
		}

		return $flat;
	}

	private function pickAttributePhrase(array $attributes, array $needles, $max_len = 60) {
		foreach ($attributes as $attr) {
			$combined = mb_strtolower($attr['name'] . ' ' . $attr['text'], 'UTF-8');

			foreach ($needles as $needle) {
				if (mb_strpos($combined, mb_strtolower($needle, 'UTF-8'), 0, 'UTF-8') !== false) {
					$phrase = $attr['text'];

					if (mb_strlen($phrase, 'UTF-8') > $max_len) {
						$phrase = mb_substr($phrase, 0, $max_len, 'UTF-8');
					}

					return $phrase;
				}
			}
		}

		return '';
	}

	private function collectProductMetaSpecs($product_info, array $breadcrumbs, array $attribute_groups) {
		$family = $this->detectCategoryFamily($breadcrumbs);
		$attributes = $this->flattenProductAttributes($attribute_groups);
		$specs = array();
		$seen = array();

		$add = function($phrase) use (&$specs, &$seen) {
			$phrase = $this->normalizeMetaText($phrase);

			if ($phrase === '' || isset($seen[mb_strtolower($phrase, 'UTF-8')])) {
				return;
			}

			$seen[mb_strtolower($phrase, 'UTF-8')] = true;
			$specs[] = $phrase;
		};

		$dims = $this->formatProductDimensions($product_info);

		if ($dims !== '') {
			$add('размер ' . $dims);
		}

		$family_needles = array(
			'stoly' => array('полк', 'борт', 'нержав', 'столеш'),
			'polki' => array('настен', 'настоль', 'ярус', 'гастро', 'gn', 'нержав'),
			'telezhki' => array('колес', 'ярус', 'гастро', 'gn', 'противн', 'шpil'),
			'shkafy_lari' => array('двер', 'полк', 'нержав'),
			'podstavki' => array('уровн', 'gn', 'нагруз', 'нержав'),
			'stellazhi' => array('полк', 'ярус', 'ярус', 'нержав'),
			'moechnye_vanny' => array('секц', 'чаш', 'мойк', 'нержав'),
			'zonty' => array('вытяж', 'фильтр', 'нержав'),
			'generic' => array('нержав', 'материал', 'сталь'),
		);

		$needles = isset($family_needles[$family]) ? $family_needles[$family] : $family_needles['generic'];

		foreach ($needles as $needle) {
			if (count($specs) >= 3) {
				break;
			}

			$phrase = $this->pickAttributePhrase($attributes, array($needle));

			if ($phrase !== '') {
				$add($phrase);
			}
		}

		if (empty($specs)) {
			$material = $this->pickAttributePhrase($attributes, array('материал', 'нержав', 'сталь'));

			if ($material !== '') {
				$add($material);
			}
		}

		return array_slice($specs, 0, 3);
	}

	private function getCategoryLabel(array $breadcrumbs) {
		if (count($breadcrumbs) < 2) {
			return 'нейтральное оборудование';
		}

		$text = $breadcrumbs[count($breadcrumbs) - 2]['text'];

		return $this->normalizeMetaText($text);
	}

	private function buildProductMetaDescription($product_info, array $breadcrumbs, array $attribute_groups) {
		$name = $this->normalizeMetaText(isset($product_info['name']) ? $product_info['name'] : '');

		if ($name === '') {
			$name = 'оборудование';
		}

		$specs = $this->collectProductMetaSpecs($product_info, $breadcrumbs, $attribute_groups);
		$spec_sentence = '';

		if (!empty($specs)) {
			$spec_sentence = implode(', ', $specs) . '.';
		}

		$name_len = mb_strlen($name, 'UTF-8');

		if ($name_len > 70) {
			$base = 'Купить ' . $name . ' для общепита.';
		} else {
			$base = 'Купить ' . $name . ' ЗПМ из нержавеющей стали для общепита.';
		}

		if ($spec_sentence !== '') {
			$base .= ' ' . $spec_sentence;
		}

		$base .= ' Производство и поставка по России.';

		return $this->trimMetaDescription($base, 170);
	}

	private function isGenericMetaKeywords($keywords) {
		$kw = $this->normalizeMetaText($keywords);

		if ($kw === '') {
			return true;
		}

		$parts = array_filter(array_map('trim', explode(',', mb_strtolower($kw, 'UTF-8'))));

		if (count($parts) <= 2) {
			$generic = array('оборудование', 'кухня', 'общепит', 'нержавеющая сталь');

			if (count(array_intersect($parts, $generic)) >= count($parts)) {
				return true;
			}
		}

		return false;
	}

private function normalizeMetaKeywordPhrase($phrase) {
		return $this->normalizeMetaText($phrase);
	}

	private function isNumericOnlyMetaKeyword($phrase) {
		$phrase = $this->normalizeMetaKeywordPhrase($phrase);

		if ($phrase === '') {
			return true;
		}

		$trimmed = trim($phrase);

		if (preg_match('/^\d+$/u', $trimmed)) {
			return true;
		}

		if (preg_match('/^\d+([,.]\d+)?$/u', $trimmed)) {
			return true;
		}

		$compact = preg_replace('/[\s]/u', '', $trimmed);

		if (preg_match('/^\d+([×xх]\d+)+$/ui', $compact)) {
			return true;
		}

		return false;
	}

	private function isUsefulMetaKeywordPhrase($phrase, $product_name = '') {
		$phrase = $this->normalizeMetaKeywordPhrase($phrase);

		if ($phrase === '') {
			return false;
		}

		if ($this->isNumericOnlyMetaKeyword($phrase)) {
			return false;
		}

		$lower = mb_strtolower($phrase, 'UTF-8');
		$len = mb_strlen($phrase, 'UTF-8');

		if ($len < 3) {
			$allowed_short = array('gn');

			if (!in_array($lower, $allowed_short, true)) {
				return false;
			}
		}

		if (preg_match('/^[\s,.;:\-\/\\\\]+$/u', $phrase)) {
			return false;
		}

		$junk = array('есть', 'нет', 'да', 'без', '—', '-');

		if (in_array($lower, $junk, true)) {
			return false;
		}

		if ($len > 80) {
			if ($product_name === '' || $lower !== mb_strtolower($product_name, 'UTF-8')) {
				return false;
			}
		}

		return true;
	}

	private function trimMetaKeywords(array $phrases, $max_phrases = 18, $max_chars = 300) {
		$phrases = array_slice($phrases, 0, $max_phrases);
		$result = implode(', ', $phrases);

		if (mb_strlen($result, 'UTF-8') <= $max_chars) {
			return $result;
		}

		while (count($phrases) > 6 && mb_strlen(implode(', ', $phrases), 'UTF-8') > $max_chars) {
			array_pop($phrases);
		}

		return implode(', ', $phrases);
	}

	private function addUniqueMetaKeyword(array &$phrases, array &$seen, $phrase, $product_name = '') {
		if (!$this->isUsefulMetaKeywordPhrase($phrase, $product_name)) {
			return false;
		}

		$phrase = $this->normalizeMetaKeywordPhrase($phrase);
		$key = mb_strtolower($phrase, 'UTF-8');

		if (isset($seen[$key])) {
			return false;
		}

		$seen[$key] = true;
		$phrases[] = $phrase;

		return true;
	}

	private function buildProductMetaKeywords($product_info, array $breadcrumbs, array $attribute_groups) {
		$name = $this->normalizeMetaText(isset($product_info['name']) ? $product_info['name'] : '');
		$category = $this->getCategoryLabel($breadcrumbs);
		$family = $this->detectCategoryFamily($breadcrumbs);
		$attributes = $this->flattenProductAttributes($attribute_groups);
		$phrases = array();
		$seen = array();
		$attr_added = 0;
		$dim_added = 0;

		$this->addUniqueMetaKeyword($phrases, $seen, $name, $name);
		$this->addUniqueMetaKeyword($phrases, $seen, $category, $name);
		$this->addUniqueMetaKeyword($phrases, $seen, 'купить', $name);
		$this->addUniqueMetaKeyword($phrases, $seen, 'ЗПМ', $name);
		$this->addUniqueMetaKeyword($phrases, $seen, 'нержавеющая сталь', $name);
		$this->addUniqueMetaKeyword($phrases, $seen, 'нейтральное оборудование', $name);

		$family_kw = array(
			'stoly' => array('стол производственный', 'стол из нержавеющей стали', 'купить стол'),
			'polki' => array('полка настенная', 'полка для кухни', 'купить полку'),
			'telezhki' => array('тележка для кухни', 'противень нержавеющий'),
			'telezhki_servirovochnye' => array('тележка сервировочная', 'купить тележку'),
			'shkafy_lari' => array('шкаф кухонный', 'шкаф из нержавеющей стали'),
			'podstavki' => array('подставка под оборудование', 'подтоварник'),
			'stellazhi' => array('стеллаж кухонный', 'стеллаж из нержавеющей стали'),
			'moechnye_vanny' => array('моечная ванна', 'котломойка'),
			'zonty' => array('вытяжной зонт', 'зонт для кухни'),
		);

		if (isset($family_kw[$family])) {
			foreach ($family_kw[$family] as $phrase) {
				if (count($phrases) >= 16) {
					break;
				}

				$this->addUniqueMetaKeyword($phrases, $seen, $phrase, $name);
			}
		}

		$family_attr_needles = array(
			'stoly' => array('борт', 'полк', 'столеш', 'сварн', 'разбор'),
			'polki' => array('настен', 'настоль', 'ярус', 'гастро', 'gn', 'рамк'),
			'telezhki' => array('колес', 'ярус', 'гастро', 'gn', 'противн', 'шпил'),
			'telezhki_servirovochnye' => array('колес', 'полк', 'ярус', 'сервиров'),
			'shkafy_lari' => array('двер', 'полк', 'замок'),
			'podstavki' => array('уровн', 'gn', 'нагруз', 'секц'),
			'stellazhi' => array('полк', 'ярус', 'уровн'),
			'moechnye_vanny' => array('секц', 'чаш', 'мойк', 'котломой'),
			'zonty' => array('вытяж', 'фильтр', 'пристен', 'остров'),
			'generic' => array('материал', 'нержав', 'сталь'),
		);

		$needles = isset($family_attr_needles[$family]) ? $family_attr_needles[$family] : $family_attr_needles['generic'];

		foreach ($needles as $needle) {
			if ($attr_added >= 5 || count($phrases) >= 16) {
				break;
			}

			$phrase = $this->pickAttributePhrase($attributes, array($needle), 50);

			if ($phrase !== '' && $this->addUniqueMetaKeyword($phrases, $seen, $phrase, $name)) {
				$attr_added++;
			}
		}

		$dims = $this->formatProductDimensions($product_info);

		if ($dims !== '' && $dim_added < 2) {
			if ($this->addUniqueMetaKeyword($phrases, $seen, 'габариты ' . $dims, $name)) {
				$dim_added++;
			} elseif ($this->addUniqueMetaKeyword($phrases, $seen, 'размер ' . $dims, $name)) {
				$dim_added++;
			}
		}

		return $this->trimMetaKeywords($phrases, 18, 300);
	}

	private function resolveProductMetaDescription($product_info, array $breadcrumbs, array $attribute_groups) {
		$stored = isset($product_info['meta_description']) ? $product_info['meta_description'] : '';

		if ($this->isUsefulProductMetaDescription($stored, $product_info)) {
			return $this->normalizeMetaText($stored);
		}

		return $this->buildProductMetaDescription($product_info, $breadcrumbs, $attribute_groups);
	}

	private function resolveProductMetaKeywords($product_info, array $breadcrumbs, array $attribute_groups) {
		$stored = isset($product_info['meta_keyword']) ? $product_info['meta_keyword'] : '';

		if (!$this->isGenericMetaKeywords($stored)) {
			return $this->normalizeMetaText($stored);
		}

		return $this->buildProductMetaKeywords($product_info, $breadcrumbs, $attribute_groups);
	}

	/**
	 * SITE-002 — PDP body classes from OpenCart category path (path query param).
	 * Adds category-root-{id} and category-parent-{id} when the chain is available.
	 */
	private function setProductCategoryBodyClasses() {
		$body_class = 'page page--product';

		if (!isset($this->request->get['path']) || $this->request->get['path'] === '') {
			$this->document->setBodyClass($body_class);

			return;
		}

		$path_parts = array();

		foreach (explode('_', (string)$this->request->get['path']) as $part) {
			$id = (int)$part;

			if ($id > 0) {
				$path_parts[] = $id;
			}
		}

		if (!empty($path_parts)) {
			$body_class .= ' category-root-' . (int)$path_parts[0];

			if (isset($path_parts[1]) && (int)$path_parts[1] > 0) {
				$body_class .= ' category-parent-' . (int)$path_parts[1];
			}
		}

		$this->document->setBodyClass($body_class);
	}
}
