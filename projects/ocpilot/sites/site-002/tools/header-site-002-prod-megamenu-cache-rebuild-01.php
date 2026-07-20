<?php
class ControllerCommonHeader extends Controller {
	public function index() {
		// ZPM SEO: technical/account routes should not be indexed
		$route = isset($this->request->get['route']) ? (string)$this->request->get['route'] : '';
		$request_uri = isset($this->request->server['REQUEST_URI']) ? strtolower((string)$this->request->server['REQUEST_URI']) : '';
		$noindex_routes = array(
			'checkout/cart', 'checkout/checkout', 'product/search', 'product/compare',
			'account/wishlist', 'account/login', 'account/register', 'account/forgotten', 'account/account'
		);
		$noindex_paths = array('/cart', '/checkout', '/search', '/compare-products', '/wishlist', '/my-account', '/account/');
		$zpm_seo_noindex_guard = in_array($route, $noindex_routes, true);
		if (!$zpm_seo_noindex_guard && strpos($route, 'account/') === 0) {
			$zpm_seo_noindex_guard = true;
		}
		if (!$zpm_seo_noindex_guard) {
			foreach ($noindex_paths as $noindex_path) {
				if ($request_uri === $noindex_path || strpos($request_uri, $noindex_path . '?') === 0 || strpos($request_uri, $noindex_path . '/') === 0) {
					$zpm_seo_noindex_guard = true;
					break;
				}
			}
		}
		if ($zpm_seo_noindex_guard) {
			$this->response->addHeader('X-Robots-Tag: noindex, follow');
		}


		require_once(DIR_SYSTEM . 'library/zpm/category_visibility.php');
		$visibility = new CategoryVisibility();

		// Analytics
		$this->load->model('setting/extension');

		// Wishlist
		$this->load->model('account/wishlist');

		$data['analytics'] = array();

		$analytics = $this->model_setting_extension->getExtensions('analytics');

		foreach ($analytics as $analytic) {
			if ($this->config->get('analytics_' . $analytic['code'] . '_status')) {
				$data['analytics'][] = $this->load->controller('extension/analytics/' . $analytic['code'], $this->config->get('analytics_' . $analytic['code'] . '_status'));
			}
		}

		if ($this->request->server['HTTPS']) {
			$server = $this->config->get('config_ssl');
		} else {
			$server = $this->config->get('config_url');
		}

		if (is_file(DIR_IMAGE . $this->config->get('config_icon'))) {
			$this->document->addLink($server . 'image/' . $this->config->get('config_icon'), 'icon');
		}

		//Логин по токену
		if (!$this->customer->isLogged() && isset($this->request->cookie['remember_me'])) {
			$old_token = $this->request->cookie['remember_me'];
			$this->load->model('account/customer');
		
			if ($this->customer->loginByToken($old_token)) {
				

				$this->model_account_customer->deleteRememberToken($old_token);
				

				$new_token = bin2hex(random_bytes(32));
				

				$this->model_account_customer->addRememberToken($this->customer->getId(), $new_token);
				

				setcookie('remember_me', $new_token, time() + 2592000, '/', $this->request->server['HTTP_HOST'], true, true);
				
			} else {
				
				setcookie('remember_me', '', time() - 3600, '/', $this->request->server['HTTP_HOST']);
			}
		}

		$data['title'] = $this->document->getTitle();

		$data['bodyclass'] = $this->document->getBodyClass();
		$data['pageintro'] = $this->document->getPageintro();
		$data['breadcrumbs'] = $this->document->getBreadcrumbs();

		$data['base'] = $server;
		$data['description'] = $this->document->getDescription();
		$data['keywords'] = $this->document->getKeywords();
		$data['links'] = $this->document->getLinks();
		$data['styles'] = $this->document->getStyles();
		$data['scripts'] = $this->document->getScripts('header');
		$data['lang'] = $this->language->get('code');
		$data['direction'] = $this->language->get('direction');

		$data['image'] = $this->document->getImage();

		

		$data['totalcart'] = $this->cart->countProducts();

		$data['reCAPTCHA_open'] = reCAPTCHA_open;

		$data['server'] = HTTPS_SERVER;
		
		if (!isset($this->session->data['compare'])) 
			$data['comparecount'] = false;
		else 
			$data['comparecount'] = count($this->session->data['compare']);

		if ($this->customer->isLogged() && !empty($this->request->cookie['oc_guest_hash'])) {
				$guest_hash = $this->request->cookie['oc_guest_hash'];
				$this->model_account_wishlist->mergeGuestWishlist($guest_hash);

				setcookie('oc_guest_hash', '', time() - 3600, '/', ''); 
				unset($this->request->cookie['oc_guest_hash']);
			}

		 if (!$this->customer->isLogged()) {
                if (!isset($this->request->cookie['oc_guest_hash']) || empty($this->request->cookie['oc_guest_hash'])) {
                    $hash = bin2hex(random_bytes(32)); // 64 символа, криптографически стойкий
                    setcookie('oc_guest_hash', $hash, [
                        'expires' => time() + (30 * 24 * 60 * 60), // 30 дней
                        'path' => '/',
                        'domain' => '', // текущий домен
                        'secure' => $this->request->server['HTTPS'] ?? false,
                        'httponly' => true,
                        'samesite' => 'Lax'
                    ]);
                    $this->session->data['guest_hash'] = $hash;
                } else {
                    $this->session->data['guest_hash'] =  $this->request->cookie['oc_guest_hash'];
                }
            }

		if (empty( $this->session->data['csrf_token'])) {
    			 $this->session->data['csrf_token'] = bin2hex(random_bytes(32));
		}

		$data['csrf_token'] =  htmlspecialchars($this->session->data['csrf_token']);	

	

		$data['name'] = $this->config->get('config_name');

		if (is_file(DIR_IMAGE . $this->config->get('config_logo'))) {
			$data['logo'] = $server . 'image/' . $this->config->get('config_logo');
		} else {
			$data['logo'] = '';
		}

		$this->load->language('common/header');

		// Wishlist
		
		$data['wishcont'] =  $this->model_account_wishlist->getTotalWishlist();

		$data['text_logged'] = sprintf($this->language->get('text_logged'), $this->url->link('account/account', '', true), $this->customer->getFirstName(), $this->url->link('account/logout', '', true));
		
		$data['home'] = $this->url->link('common/home');
		$data['wishlist'] = $this->url->link('account/wishlist', '', true);
		$data['logged'] = $this->customer->isLogged();
		$data['account'] = $this->url->link('account/account', '', true);
		$data['register'] = $this->url->link('account/register', '', true);
		$data['login'] = $this->url->link('account/login', '', true);
		$data['order'] = $this->url->link('account/order', '', true);
		$data['transaction'] = $this->url->link('account/transaction', '', true);
		$data['download'] = $this->url->link('account/download', '', true);
		$data['logout'] = $this->url->link('account/logout', '', true);
		$data['shopping_cart'] = $this->url->link('checkout/cart');
		$data['checkout'] = $this->url->link('checkout/checkout', '', true);
		$data['contact'] = $this->url->link('information/contact');
		$data['telephone'] = $this->config->get('config_telephone');
		
		$data['language'] = $this->load->controller('common/language');
		$data['currency'] = $this->load->controller('common/currency');
		$data['search'] = $this->load->controller('common/search');
		$data['cart'] = $this->load->controller('common/cart');
		$data['menu'] = $this->load->controller('common/menu');

		$data['categories'] = array();
		$data['catDesktop'] = array();
		$data['catalog_primary_entry'] = $visibility->getPrimaryCatalogEntry();
		$data['launch_mode'] = $visibility->isLaunchMode();

		$catlist= $this->cache->get('cat-list-header');
		// SITE-002-PROD-MEGAMENU-AND-CACHE-PLUGIN-DIAGNOSTIC-01:
		// Rebuild cat-list-header on miss (katalog.php parity). After storage/cache
		// clear, header previously left mega menu empty until /katalog was visited.
		if (!$catlist) {
			$this->load->model('catalog/category');
			$this->load->model('catalog/product');
			$this->load->model('tool/image');
			$built = array();
			$results = $this->model_catalog_category->getCategories(0);

			foreach ($results as $result) {
				$children = array();
				$result_child = $this->model_catalog_category->getCategories($result['category_id']);

				foreach ($result_child as $r) {
					$filter_data = array(
						'filter_category_id'  => $r['category_id'],
						'filter_sub_category' => true
					);
					$child_count = $this->model_catalog_product->getTotalProducts($filter_data);

					if ($child_count <= 0) {
						continue;
					}

					$thumb = $this->model_tool_image->resize($r['image'], 160, 160);
					$thumb200 = $this->model_tool_image->resize($r['image'], 200, 200);

					if ($r['image']) {
						$thumb300 = $this->model_tool_image->resize($r['image'], 300, 300);
					} else {
						$thumb300 = $this->model_tool_image->resize('placeholder.png', 300, 300);
					}

					$children[] = array(
						'category_id' => $r['category_id'],
						'name' => $r['name'],
						'href' => $this->url->link('product/category', 'path=' . '_' . $r['category_id']),
						'thumb' => $thumb,
						'thumb200' => $thumb200,
						'thumb300' => $thumb300,
						'count' => $child_count,
						'has_children' => false,
					);
				}

				$thumb = $this->model_tool_image->resize($result['image'], 160, 160);
				$thumb200 = $this->model_tool_image->resize($result['image'], 200, 200);
				$built[] = array(
					'category_id' => $result['category_id'],
					'name' => $result['name'],
					'href' => $this->url->link('product/category', 'path=' . '_' . $result['category_id']),
					'has_children' => (!empty($children)),
					'children' => $children,
					'thumb' => $thumb,
					'thumb200' => $thumb200,
					'short_description' => html_entity_decode(isset($result['short_description']) ? $result['short_description'] : '', ENT_QUOTES, 'UTF-8'),
				);
			}

			$this->cache->set('cat-list-header', serialize($built));
			$catlist = serialize($built);
		}

		if ($catlist) {
			$categories = $visibility->prepareMegamenuCategories(unserialize($catlist), $this);
			$data['categories'] = $visibility->filterRootCategories($categories);

			foreach ($data['categories'] as $c)
			{
				// SITE-002-PROD-REGRESSION-HOTFIX-01: prepareMegamenuCategories() sets
				// has_children on roots only; nested children / empty roots may omit key.
				if (!empty($c['has_children']))
				{
					$k = 0;
					foreach ($c['children'] as $c1)
					{
						$k++;
						if (!empty($c1['has_children']))
							$k = $k + count($c1['children']);			

					}



					$p = ceil($k / 4);

					$c['desktop'] = array();
				
						$col = array(); $j=0;
						foreach ($c['children'] as $c1)
							{
								$col[] = $c1;
								$j++;
								if (!empty($c1['has_children']))
								{
									$j = $j + count($c1['children']);
								}

								if ($j>=$p)
								{
									$c['desktop'][] = $col;
									$j = 0;
									$col = array(); 
								}					

							}

						if (!empty($col)) $c['desktop'][] = $col;

				}

				$data['catDesktop'][] = $c;
			}

		}


		$data['quicksearch'] = $this->load->view('common/quicksearch', $data);
		$data['megamenu'] = $this->load->view('common/megamenu', $data);
		$data['qsearchmobilepanel'] = $this->load->view('common/qsearchmobilepanel', $data);

		return $this->load->view('common/header', $data);
	}
}
