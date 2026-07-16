<?php
class ControllerCommonHome extends Controller {

	protected function formatReadingTimeText($minutes) {
		$n = (int)$minutes;
		if ($n < 1) {
			$n = 1;
		}
		$mod10 = $n % 10;
		$mod100 = $n % 100;
		if ($mod10 == 1 && $mod100 != 11) {
			$word = 'минута';
		} elseif (in_array($mod10, array(2, 3, 4)) && !in_array($mod100, array(12, 13, 14))) {
			$word = 'минуты';
		} else {
			$word = 'минут';
		}
		return 'Время на чтение: ' . $n . ' ' . $word . '.';
	}

	public function index() {
		require_once(DIR_SYSTEM . 'library/zpm/category_visibility.php');
		$visibility = new CategoryVisibility();

		$this->document->setTitle('Оборудование для общепита и пищевых производств | ООО «ЗПМ»');
		$this->document->setDescription($this->config->get('config_meta_description'));
		$this->document->setKeywords($this->config->get('config_meta_keyword'));

		$this->document->setBodyClass('page--home');

		if (isset($this->request->get['route'])) {
			$this->document->addLink($this->config->get('config_url'), 'canonical');
		}

		$data['heroslider'] =$this->load->view('sections/heroslider');
		$data['oneslider'] =$this->load->view('sections/oneslider');

		$data['categories'] = array();

		if ($visibility->isLaunchMode()) {
			$data['categories'] = $visibility->buildHomepageCategoryCards($this);
		} else {
			$catlist = $this->cache->get('cat-list-header');
			if ($catlist) {
				$data['categories'] = $visibility->filterRootCategories(unserialize($catlist));
			}
		}

		$data['catalog_primary_entry'] = $visibility->getPrimaryCatalogEntry();
		$data['launch_mode'] = $visibility->isLaunchMode();

		$this->load->model('blog/blog');
		$this->load->model('tool/image');
		$other_results = $this->model_blog_blog->getSliderPosts(0, 24);
        $data['other_news_list'] = array();

        foreach ($other_results as $result) {
            // Обработка изображения
            if ($result['image']) {
                $other_thumb = $this->model_tool_image->resize($result['image'], 600, 400);
            } else {
                $other_thumb = $this->model_tool_image->resize('placeholder.png', 600, 400); // или false
            }

            $data['other_news_list'][] = array(
                'title'         => $result['title'],
                'category_name' => $result['category_name'] ? $result['category_name'] : 'Без рубрики',
                'date'          => date('d.m.Y', strtotime($result['date_added'])),
                'views'         => $result['views'],
				'reading_time_text' => $this->formatReadingTimeText(isset($result['reading_time_minutes']) ? (int)$result['reading_time_minutes'] : 1),
                'short'         => utf8_substr(strip_tags(html_entity_decode($result['short_description'], ENT_QUOTES, 'UTF-8')), 0, 150) . '..',
                'thumb'         => $other_thumb,
                'href'          => $this->url->link('blog/post', 'blog_post_id=' . $result['id'])
            );
        }
		$data['other_news_list_header'] ="Новости";


		$data['catalogsections'] =$this->load->view('sections/catalogsections', $data);
		$data['relproducts'] = $this->load->controller('product/relproducts');
		$data['aboutteaser'] =$this->load->view('sections/aboutteaser');
		$data['certificates'] =$this->load->view('sections/certificates');
		$data['blockadvantagestop'] =$this->load->view('sections/blockadvantagestop');
		$data['blockdealersform'] = $this->load->view('sections/blockcommercialtrust_home');
		$data['blockadvantagesbottom'] =$this->load->view('sections/blockadvantagesbottom');

		$data['relarticles'] =$this->load->view('blog/other_news',  $data);

		$data['seotext'] =$this->load->view('sections/seotext');
		$data['yandexmap'] =$this->load->view('sections/yandexmap');		


		$data['column_left'] = $this->load->controller('common/column_left');
		$data['column_right'] = $this->load->controller('common/column_right');
		$data['content_top'] = $this->load->controller('common/content_top');
		$data['content_bottom'] = $this->load->controller('common/content_bottom');
		$data['footer'] = $this->load->controller('common/footer');
		$data['header'] = $this->load->controller('common/header');

		$this->response->setOutput($this->load->view('common/home', $data));
	}
}
