<?php
class ControllerProductKatalog extends Controller {
	private $error = array();

	public function index() {
		require_once(DIR_SYSTEM . 'library/zpm/category_visibility.php');
		$visibility = new CategoryVisibility();

		$this->load->language('product/product');
		$this->load->model('catalog/category');
		$this->load->model('catalog/product');
		$this->load->model('tool/image');



		$this->document->setTitle('Каталог оборудования для общепита | ООО «ЗПМ»');
		$this->document->setDescription('Каталог оборудования для ресторанов, кафе и пищевых производств от Завода пищевого машиностроения. Профессиональное оборудование для кухни и предприятий общественного питания.');
		$this->document->setKeywords('Каталог');

		$this->document->setBodyClass('page--inner');

		$data['heading_title'] = 'Каталог оборудования';

		$data['breadcrumbs'] = array();

		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_home'),
			'href' => '',
			'pos' => 1
		);

		$data['breadcrumbs'][] = array(
			'text' => 'Каталог',
			'href' => '',
			'pos' => 9

		);

		$breadcrumbs = new Breadcrumbs();
		$breadcrumbs->breadcrumbs  = $data['breadcrumbs'];
		$this->document->setBreadcrumbs( $breadcrumbs->render() );

		$pageintro = new Pageintro();
		$pageintro->title = "Каталог оборудования для общепита";
		$pageintro->description = "Для предприятий общественного питания и пищевой промышленности";
		$this->document->setPageintro( $pageintro->render() );






		$catlist= $this->cache->get('cat-list-header'); 
		if (!$catlist) {
			
			$data['catlist'] = array();
			$this->load->model('catalog/category');
			$this->load->model('tool/image');
			$results = $this->model_catalog_category->getCategories(0);

			foreach ($results as $result) {		

					$children = array();
					$result_child= $this->model_catalog_category->getCategories($result['category_id']);
					foreach ($result_child as $r) {	
						$thumb = $this->model_tool_image->resize($r['image'],  160, 160);
						$thumb200 = $this->model_tool_image->resize($r['image'],  200, 200);
						$children[] = array(
							'category_id' => $r['category_id'],
							'name' => $r['name'],
							'href' => $this->url->link('product/category',  'path=' . '_' . $r['category_id'] ),
							'thumb'	=> $thumb,
							'thumb200'	=> $thumb200,
						);
					}
					$thumb = $this->model_tool_image->resize($result['image'], 160, 160);
					$thumb200 = $this->model_tool_image->resize($result['image'], 200, 200);
					$data['catlist'][] = array(
						'category_id' => $result['category_id'],
						'name' => $result['name'],
						'href' => $this->url->link('product/category',  'path=' . '_' . $result['category_id'] ),
						'has_children' => (!empty($children)),
						'children'	=> $children,
						'thumb'	=> $thumb,
						'thumb200'	=> $thumb200,
						'short_description' => html_entity_decode($result['short_description'], ENT_QUOTES, 'UTF-8'),
					);
				};
		 	$this->cache->set('cat-list-header', serialize($data['catlist'])); 


		}
		else $data['catlist'] = unserialize($catlist);

		if (!empty($data['catlist']))
		{
			foreach ($data['catlist'] as $key=>$val)
			{
				$filter_data = array(
					'filter_category_id'  => $val['category_id'],
					'filter_sub_category' => true
				);

				$c = $this->model_catalog_product->getTotalProducts($filter_data);
				$data['catlist'][$key]['count'] = $c;
				$data['catlist'][$key]['tovar'] = $this->true_wordform($c, 'товар', 'товара', 'товаров');

			}
		}

		$visibility->applyCatalogNavData($data);

		//print_r($data['catlist']);

		//   @@include('partials/sections/about-teaser.html')
		// 	@@include('partials/sections/block-advantages-top.html')
		// 	@@include('partials/sections/block-dealers-form.html')
		// 	@@include('partials/sections/block-advantages-bottom.html')
		// 	@@include('partials/sections/seo-text.html')

  		$data['certificates'] = $this->load->view('sections/certificates');
		$data['blockadvantagestop'] = $this->load->view('sections/blockadvantagestop');
		$data['blockdealersform'] = $this->load->view('sections/blockdealersform');
		$data['blockadvantagesbottom'] = $this->load->view('sections/blockadvantagesbottom');
		
		$data['seotext'] = $this->load->view('sections/seotext');

		$data['footer'] = $this->load->controller('common/footer');
		$data['header'] = $this->load->controller('common/header');
		$this->response->setOutput($this->load->view('product/katalog', $data));



	
	}


	private function true_wordform($num, $form_for_1, $form_for_2, $form_for_5){
		$num = abs($num) % 100; // берем число по модулю и сбрасываем сотни (делим на 100, а остаток присваиваем переменной $num)
		$num_x = $num % 10; // сбрасываем десятки и записываем в новую переменную
		if ($num > 10 && $num < 20) // если число принадлежит отрезку [11;19]
			return $form_for_5;
		if ($num_x > 1 && $num_x < 5) // иначе если число оканчивается на 2,3,4
			return $form_for_2;
		if ($num_x == 1) // иначе если оканчивается на 1
			return $form_for_1;
		return $form_for_5;
	}


}
