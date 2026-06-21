<?php
class ControllerAccountWishList extends Controller {
	public function index() {
		// if (!$this->customer->isLogged()) {
		// 	$this->session->data['redirect'] = $this->url->link('account/wishlist', '', true);

		// 	$this->response->redirect($this->url->link('account/login', '', true));
		// }

		$this->load->language('account/wishlist');

		$this->load->model('account/wishlist');

		$this->load->model('catalog/product');

		$this->load->model('tool/image');

		if (isset($this->request->get['remove'])) {
			// Remove Wishlist
			$this->model_account_wishlist->deleteWishlist($this->request->get['remove']);
			$this->session->data['success'] = $this->language->get('text_remove');
			$this->response->redirect($this->url->link('account/wishlist'));
		}



		$this->document->setTitle('Избранные товары');

		$data['breadcrumbs'] = array();

		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_home'),
			'href' => $this->url->link('common/home')
		);

		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_account'),
			'href' => $this->url->link('account/account', '', true)
		);

		$data['breadcrumbs'][] = array(
			'text' => 'Избранные товары',
			'href' => $this->url->link('account/wishlist')
		);




		$this->document->setBodyClass('page--favorites');
			$breadcrumbs = new Breadcrumbs();
			$breadcrumbs->breadcrumbs  = $data['breadcrumbs'];
			$this->document->setBreadcrumbs( $breadcrumbs->render() );

			$pageintro = new Pageintro();
			$pageintro->title = 'Избранные товары';
			$pageintro->description = '';
			$this->document->setPageintro( $pageintro->render() );



		if (isset($this->session->data['success'])) {
			$data['success'] = $this->session->data['success'];

			unset($this->session->data['success']);
		} else {
			$data['success'] = '';
		}

		$data['products'] = array();
		$data['productcards'] = array();

		$ids = $this->model_account_wishlist->getWishlist();

$results = array();

if (!empty($ids)) {
	foreach ($ids as $id) {
		$product = $this->model_catalog_product->getProduct((int)$id['product_id']);

		if ($product && is_array($product)) {
			$results[] = $product;
		}
	}

	if ($results) {
		include(DIR_APPLICATION . 'controller/product/product_results.php');
	}
}





		$data['continue'] = $this->url->link('account/account', '', true);

		$data['column_left'] = $this->load->controller('common/column_left');
		$data['column_right'] = $this->load->controller('common/column_right');
		$data['content_top'] = $this->load->controller('common/content_top');
		$data['content_bottom'] = $this->load->controller('common/content_bottom');
		$data['footer'] = $this->load->controller('common/footer');
		$data['header'] = $this->load->controller('common/header');

		$this->response->setOutput($this->load->view('account/wishlist', $data));
	}

	public function add() {
		$this->load->language('account/wishlist');

		$json = array();

		if (isset($this->request->post['product_id'])) {
			$product_id = $this->request->post['product_id'];
		} else {
			$product_id = 0;
		}

		$this->load->model('catalog/product');


		$product_info = $this->model_catalog_product->getProduct($product_id);

		$this->load->model('account/wishlist');
		$this->model_account_wishlist->addWishlist($this->request->post['product_id']);
		$json['success'] = sprintf($this->language->get('text_success'), $this->url->link('product/product', 'product_id=' . (int)$this->request->post['product_id']), $product_info['name'], $this->url->link('account/wishlist'));
		$json['total'] =  $this->model_account_wishlist->getTotalWishlist();

		if ($product_info) {
			$this->load->model('account/wishlist');
			$this->model_account_wishlist->addWishlist($this->request->post['product_id']);
			$json['success'] = sprintf($this->language->get('text_success'), $this->url->link('product/product', 'product_id=' . (int)$this->request->post['product_id']), $product_info['name'], $this->url->link('account/wishlist'));
			$json['total'] = $this->model_account_wishlist->getTotalWishlist();

			/*if ($this->customer->isLogged()) {
				// Edit customers cart
				$this->load->model('account/wishlist');
				$this->model_account_wishlist->addWishlist($this->request->post['product_id']);
				$json['success'] = sprintf($this->language->get('text_success'), $this->url->link('product/product', 'product_id=' . (int)$this->request->post['product_id']), $product_info['name'], $this->url->link('account/wishlist'));
				$json['total'] = $this->model_account_wishlist->getTotalWishlist();
			} else {
				if (!isset($this->session->data['wishlist'])) {
					$this->session->data['wishlist'] = array();
				}

				$this->session->data['wishlist'][] = $this->request->post['product_id'];
				$this->session->data['wishlist'] = array_unique($this->session->data['wishlist']); 
				$json['wishlist'] = print_r($this->session->data['wishlist'], true);

				$json['success'] = sprintf($this->language->get('text_login'), $this->url->link('account/login', '', true), $this->url->link('account/register', '', true), $this->url->link('product/product', 'product_id=' . (int)$this->request->post['product_id']), $product_info['name'], $this->url->link('account/wishlist'));

				$json['total'] =(isset($this->session->data['wishlist']) ? count($this->session->data['wishlist']) : 0);
			}*/
		}

		$this->response->addHeader('Content-Type: application/json');
		$this->response->setOutput(json_encode($json));
	}

	public function remove() {
		$this->load->language('account/wishlist');

		$json = array();

		if (isset($this->request->post['product_id'])) {
			$product_id = $this->request->post['product_id'];
		} else {
			$product_id = 0;
		}

			$this->load->model('account/wishlist');
			$this->model_account_wishlist->deleteWishlist($product_id);
			$json['total'] = $this->model_account_wishlist->getTotalWishlist();

		/*if ($this->customer->isLogged()) {
			$this->load->model('account/wishlist');
			$this->model_account_wishlist->deleteWishlist($product_id);
			$json['total'] = $this->model_account_wishlist->getTotalWishlist();
		} else {

			$key = array_search($product_id, $this->session->data['wishlist']);
			if ($key !== false) {
				unset($this->session->data['wishlist'][$key]);
			}
			$json['total'] =  count($this->session->data['wishlist']);
		
		}*/

		$this->response->addHeader('Content-Type: application/json');
		$this->response->setOutput(json_encode($json));
	}
}
