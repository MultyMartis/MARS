<?php
class ControllerCommonFooter extends Controller {
	public function index() {
		require_once(DIR_SYSTEM . 'library/zpm/category_visibility.php');
		$visibility = new CategoryVisibility();

		$this->load->language('common/footer');

		$this->load->model('catalog/information');

		$data['informations'] = array();

		foreach ($this->model_catalog_information->getInformations() as $result) {
			if ($result['bottom']) {
				$data['informations'][] = array(
					'title' => $result['title'],
					'href'  => $this->url->link('information/information', 'information_id=' . $result['information_id'])
				);
			}
		}

			$data['categories'] = array();
		$catlist= $this->cache->get('cat-list-header'); 
		if ($catlist) {
			$data['categories'] = $visibility->filterRootCategories(unserialize($catlist));
		}

		$data['catalog_primary_entry'] = $visibility->getPrimaryCatalogEntry();
		$data['launch_mode'] = $visibility->isLaunchMode();
		$data['year'] = date('Y');

		$data['contact'] = $this->url->link('information/contact');
		$data['return'] = $this->url->link('account/return/add', '', true);
		$data['sitemap'] = $this->url->link('information/sitemap');
		$data['tracking'] = $this->url->link('information/tracking');
		$data['manufacturer'] = $this->url->link('product/manufacturer');
		$data['voucher'] = $this->url->link('account/voucher', '', true);
		$data['affiliate'] = $this->url->link('affiliate/login', '', true);
		$data['special'] = $this->url->link('product/special');
		$data['account'] = $this->url->link('account/account', '', true);
		$data['order'] = $this->url->link('account/order', '', true);
		$data['wishlist'] = $this->url->link('account/wishlist', '', true);
		$data['newsletter'] = $this->url->link('account/newsletter', '', true);

		$data['powered'] = sprintf($this->language->get('text_powered'), $this->config->get('config_name'), date('Y', time()));

		// Whos Online
		if ($this->config->get('config_customer_online')) {
			$this->load->model('tool/online');

			if (isset($this->request->server['REMOTE_ADDR'])) {
				$ip = $this->request->server['REMOTE_ADDR'];
			} else {
				$ip = '';
			}

			if (isset($this->request->server['HTTP_HOST']) && isset($this->request->server['REQUEST_URI'])) {
				$url = ($this->request->server['HTTPS'] ? 'https://' : 'http://') . $this->request->server['HTTP_HOST'] . $this->request->server['REQUEST_URI'];
			} else {
				$url = '';
			}

			if (isset($this->request->server['HTTP_REFERER'])) {
				$referer = $this->request->server['HTTP_REFERER'];
			} else {
				$referer = '';
			}

			$this->model_tool_online->addOnline($ip, $this->customer->getId(), $url, $referer);
		}

		$data['scripts'] = $this->document->getScripts('footer');
		$data['styles'] = $this->document->getStyles('footer');


		$data['reCAPTCHA_open'] = reCAPTCHA_open;

		$data['offcanvasmenu'] = $this->load->view('sections/offcanvasmenu', $data);
		$data['citypopup'] = $this->load->view('sections/citypopup', $data);
		$data['minicart'] = $this->load->view('sections/minicart', $data);
		$data['fancyboxforms'] = $this->load->view('sections/fancyboxforms', $data);
		$data['svgsprite'] = $this->load->view('sections/svgsprite', $data);
		
		return $this->load->view('common/footer', $data);
	}
}
