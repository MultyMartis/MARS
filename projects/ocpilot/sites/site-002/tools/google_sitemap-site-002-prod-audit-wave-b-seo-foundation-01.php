<?php
class ControllerExtensionFeedGoogleSitemap extends Controller {
	public function index() {
		if ($this->config->get('feed_google_sitemap_status')) {
			$output  = '<?xml version="1.0" encoding="UTF-8"?>';
			$output .= '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">';

			$this->load->model('catalog/product');
			$this->load->model('tool/image');

			$products = $this->model_catalog_product->getProducts();

			foreach ($products as $product) {
				$output .= '<url>';
				$output .= '  <loc>' . $this->url->link('product/product', 'product_id=' . $product['product_id']) . '</loc>';
				$output .= '  <changefreq>weekly</changefreq>';
				$output .= '  <lastmod>' . date('Y-m-d\TH:i:sP', strtotime($product['date_modified'])) . '</lastmod>';
				$output .= '  <priority>1.0</priority>';

				if ($product['image']) {
					$output .= '  <image:image>';
					$output .= '  <image:loc>' . $this->model_tool_image->resize($product['image'], $this->config->get('theme_' . $this->config->get('config_theme') . '_image_popup_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_popup_height')) . '</image:loc>';
					$output .= '  <image:caption>' . $product['name'] . '</image:caption>';
					$output .= '  <image:title>' . $product['name'] . '</image:title>';
					$output .= '  </image:image>';
				}

				$output .= '</url>';
			}

			$this->load->model('catalog/category');

			$output .= $this->getCategories(0);

			$this->load->model('catalog/manufacturer');

			$manufacturers = $this->model_catalog_manufacturer->getManufacturers();

			foreach ($manufacturers as $manufacturer) {
				$output .= '<url>';
				$output .= '  <loc>' . $this->url->link('product/manufacturer/info', 'manufacturer_id=' . $manufacturer['manufacturer_id']) . '</loc>';
				$output .= '  <changefreq>weekly</changefreq>';
				$output .= '  <priority>0.7</priority>';
				$output .= '</url>';
			}

			$this->load->model('catalog/information');

			// SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01 — route-based information URLs
			$store_id = (int)$this->config->get('config_store_id');
			$language_id = (int)$this->config->get('config_language_id');

			$route_query = $this->db->query("SELECT DISTINCT query FROM " . DB_PREFIX . "seo_url WHERE store_id = '" . $store_id . "' AND language_id = '" . $language_id . "' AND query LIKE 'information/%' AND query NOT LIKE 'information/information%' ORDER BY query");

			$emitted_routes = array();

			foreach ($route_query->rows as $seo_row) {
				$route = $seo_row['query'];

				if (in_array($route, $emitted_routes, true)) {
					continue;
				}

				$emitted_routes[] = $route;

				$output .= '<url>';
				$output .= '  <loc>' . $this->url->link($route) . '</loc>';
				$output .= '  <changefreq>weekly</changefreq>';
				$output .= '  <priority>0.5</priority>';
				$output .= '</url>';
			}

			$informations = $this->model_catalog_information->getInformations();

			foreach ($informations as $information) {
				$migrated_ids = array(6, 9, 10, 11, 12, 13, 14);

				if (in_array((int)$information['information_id'], $migrated_ids, true)) {
					continue;
				}

				$legacy_check = $this->db->query("SELECT seo_url_id FROM " . DB_PREFIX . "seo_url WHERE store_id = '" . $store_id . "' AND language_id = '" . $language_id . "' AND query = 'information_id=" . (int)$information['information_id'] . "' LIMIT 1");

				if ($legacy_check->num_rows) {
					$output .= '<url>';
					$output .= '  <loc>' . $this->url->link('information/information', 'information_id=' . $information['information_id']) . '</loc>';
					$output .= '  <changefreq>weekly</changefreq>';
					$output .= '  <priority>0.5</priority>';
					$output .= '</url>';
				}
			}

			$output .= '</urlset>';

			$this->response->addHeader('Content-Type: application/xml');
			$this->response->setOutput($output);
		}
	}

	protected function getCategories($parent_id) {
		$output = '';

		$results = $this->model_catalog_category->getCategories($parent_id);

		foreach ($results as $result) {
			$output .= '<url>';
			$output .= '  <loc>' . $this->url->link('product/category', 'path=' . $result['category_id']) . '</loc>';
			$output .= '  <changefreq>weekly</changefreq>';
			$output .= '  <priority>0.7</priority>';
			$output .= '</url>';

			$output .= $this->getCategories($result['category_id']);
		}

		return $output;
	}
}
