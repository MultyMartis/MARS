<?php
class ControllerBlogCategory extends Controller {

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
		$this->load->language('blog/category');
		$this->load->model('blog/blog');
		$this->load->model('tool/image');

		$data['breadcrumbs'] = array();
		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_home'),
			'href' => $this->url->link('common/home')
		);

		if (isset($this->request->get['blog_category_id'])) {
			$category_id = (int)$this->request->get['blog_category_id'];
		} else {
			$category_id = 0;
		}

		$category_info = $this->model_blog_blog->getCategory($category_id);

		if ($category_info) {
			$this->document->setTitle($category_info['name']);
			$data['heading_title'] = $category_info['name'];
			$data['breadcrumbs'][] = array(
				'text' => $category_info['name'],
				'href' => $this->url->link('blog/category', 'blog_category_id=' . $category_id)
			);
            
            if (!empty($category_info['meta_description'])) {
                $this->document->setDescription($category_info['meta_description']);
            } elseif (isset($category_info['name']) && $category_info['name'] === 'Новости') {
                $this->document->setDescription('Новости ЗПМ: обновления каталога, производство оборудования из нержавеющей стали, полезные материалы для общепита и пищевых предприятий.');
            }
		    if (isset($category_info['meta_keyword'])) $this->document->setKeywords($category_info['meta_keyword']);

		} else {
            // Если мы на главной странице Блога
            $this->document->setTitle("Блог и новости"); // Можно вынести в языковой файл
            $this->document->setDescription('Блог и новости ЗПМ: материалы о нейтральном оборудовании, производстве, нержавеющей стали и решениях для общепита.'); // Можно вынести в языковой файл
            $data['heading_title'] = "Блог";
            // Крошка уже содержит "Главная", можно добавить просто "Блог"
            $data['breadcrumbs'][] = array(
                'text' => "Блог",
                'href' => $this->url->link('blog/category')
            );
        }

        $breadcrumbs = new Breadcrumbs();
        $breadcrumbs->breadcrumbs  = $data['breadcrumbs'];
        $this->document->setBreadcrumbs( $breadcrumbs->render() );

        $pageintro = new Pageintro();
        $pageintro->title = $data['heading_title'];
        $pageintro->description = '';
        $this->document->setPageintro( $pageintro->render() );

        $this->document->setBodyClass('page--blog-list');

		



		$page = isset($this->request->get['page']) ? (int)$this->request->get['page'] : 1;
		$limit = 10;

		$filter_data = array(
			'filter_category_id' => $category_id,
			'start'              => ($page - 1) * $limit,
			'limit'              => $limit
		);

		$post_total = $this->model_blog_blog->getTotalPosts($filter_data);
		$results = $this->model_blog_blog->getPosts($filter_data);

		$data['posts'] = array();

	    foreach ($results as $result) {
            if ($result['image']) {
                $image = $this->model_tool_image->resizeCrop($result['image'], 600, 400);
            } else {
                $image = false;
            }

            $reading_minutes = isset($result['reading_time_minutes']) ? (int)$result['reading_time_minutes'] : 1;
            if ($reading_minutes < 1) {
                $reading_minutes = 1;
            }
            $data['posts'][] = array(
                'title'         => $result['title'],
                'category_name' => $result['category_name'] ? $result['category_name'] : 'Без рубрики',
                'date'          => date('d.m.Y', strtotime($result['date_added'])),
                'views'         => $result['views'],
                'reading_time_text' => $this->formatReadingTimeText($reading_minutes),
                'thumb'         => $image,
                'short'         => html_entity_decode($result['short_description'], ENT_QUOTES, 'UTF-8'),
                'href'          => $this->url->link('blog/post', 'blog_post_id=' . $result['id'])
            );
        }

        $other_results = $this->model_blog_blog->getOtherPosts($category_id, 0, 6);
        $data['other_news_list'] = array();

        foreach ($other_results as $result) {
            // Обработка изображения
            if ($result['image']) {
                $other_thumb = $this->model_tool_image->resizeCrop($result['image'], 600, 400);
            } else {
                $other_thumb = $this->model_tool_image->resizeCrop('placeholder.png', 600, 400); // или false
            }

            $other_minutes = isset($result['reading_time_minutes']) ? (int)$result['reading_time_minutes'] : 1;
            if ($other_minutes < 1) {
                $other_minutes = 1;
            }
            $data['other_news_list'][] = array(
                'title'         => $result['title'],
                'category_name' => $result['category_name'] ? $result['category_name'] : 'Без рубрики',
                'date'          => date('d.m.Y', strtotime($result['date_added'])),
                'views'         => $result['views'],
                'reading_time_text' => $this->formatReadingTimeText($other_minutes),
                'short'         => utf8_substr(strip_tags(html_entity_decode($result['short_description'], ENT_QUOTES, 'UTF-8')), 0, 150) . '..',
                'thumb'         => $other_thumb,
                'href'          => $this->url->link('blog/post', 'blog_post_id=' . $result['id'])
            );
        }
        $data['other_news_list_header'] ="Другие статьи";


        // Рендерим отдельный шаблон в переменную
        $data['other_news'] = $this->load->view('blog/other_news', $data);

		$pagination = new Pagination();
		$pagination->total = $post_total;
		$pagination->page = $page;
		$pagination->limit = $limit;
	    if ($category_id > 0) {
            // Если мы в категории
            $pagination->url = $this->url->link('blog/category', 'blog_category_id=' . $category_id . '&page={page}');
        } else {
            // Если мы на главной странице блога (без ID)
            $pagination->url = $this->url->link('blog/category', 'page={page}');
        }

		$data['pagination'] = $pagination->render();
		$data['results'] = sprintf($this->language->get('text_pagination'), ($post_total) ? (($page - 1) * $limit) + 1 : 0, ((($page - 1) * $limit) > ($post_total - $limit)) ? $post_total : ((($page - 1) * $limit) + $limit), $post_total, ceil($post_total / $limit));

		$data['header'] = $this->load->controller('common/header');
		$data['footer'] = $this->load->controller('common/footer');
		$data['column_left'] = $this->load->controller('common/column_left');
		$data['column_right'] = $this->load->controller('common/column_right');
		$data['content_top'] = $this->load->controller('common/content_top');
		$data['content_bottom'] = $this->load->controller('common/content_bottom');

		$this->response->setOutput($this->load->view('blog/category', $data));
	}
}