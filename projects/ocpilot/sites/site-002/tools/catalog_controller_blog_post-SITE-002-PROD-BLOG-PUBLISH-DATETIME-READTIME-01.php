<?php
class ControllerBlogPost extends Controller {

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

		if (isset($this->request->get['blog_post_id'])) {
			$post_id = (int)$this->request->get['blog_post_id'];
		} else {
			$post_id = 0;
		}

		$post_info = $this->model_blog_blog->getPost($post_id);

		if ($post_info) {
			$this->model_blog_blog->updateViews($post_id);

			$this->document->setTitle($post_info['meta_title'] ? $post_info['meta_title'] : $post_info['title']);
			$this->document->setDescription($post_info['meta_description']);
			$this->document->setKeywords($post_info['meta_keyword']);

			$data['breadcrumbs'] = array();

			$data['breadcrumbs'][] = array(
				'text' => $this->language->get('text_home'),
				'href' => $this->url->link('common/home')
			);

			$category_info = $this->model_blog_blog->getCategory($post_info['category_id']);

			if ($category_info) {
				$data['breadcrumbs'][] = array(
					'text' => $category_info['name'],
					'href' => $this->url->link('blog/category', 'blog_category_id=' . $post_info['category_id'])
				);
			}

			$data['breadcrumbs'][] = array(
				'text' => $post_info['title'],
				'href' => $this->url->link('blog/post', 'blog_post_id=' . $post_id)
			);

			$data['heading_title'] = $post_info['title'];
			$data['content'] = html_entity_decode($post_info['content'], ENT_QUOTES, 'UTF-8');
			$data['date'] = date('d.m.Y', strtotime($post_info['date_added']));
			$data['views'] = $post_info['views'] + 1;
			$reading_minutes = isset($post_info['reading_time_minutes']) ? (int)$post_info['reading_time_minutes'] : 1;
			if ($reading_minutes < 1) {
				$reading_minutes = 1;
			}
			$data['reading_time_text'] = $this->formatReadingTimeText($reading_minutes);

			if (!empty($post_info['image'])) {
				$data['thumb'] = $this->model_tool_image->resizeCrop($post_info['image'], 1400, 700);
			} else {
				$data['thumb'] = '';
			}

			$breadcrumbs = new Breadcrumbs();
			$breadcrumbs->breadcrumbs = $data['breadcrumbs'];
			$this->document->setBreadcrumbs($breadcrumbs->render());

			$pageintro = new Pageintro();
			$pageintro->title = $post_info['title'];
			$pageintro->description = '';
			$this->document->setPageintro($pageintro->render());

			$this->document->setBodyClass('page--blog-list');

			$data['category_name'] = $category_info ? $category_info['name'] : 'Без рубрики';

			$other_results = $this->model_blog_blog->getOtherPosts($post_info['category_id'], $post_id, 6);
			$data['other_news_list'] = array();

			foreach ($other_results as $result) {
				if (!empty($result['image'])) {
					$other_thumb = $this->model_tool_image->resizeCrop($result['image'], 600, 400);
				} else {
					$other_thumb = $this->model_tool_image->resizeCrop('placeholder.png', 600, 400);
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

			$data['other_news_list_header'] = 'Другие статьи';
			$data['other_news'] = $this->load->view('blog/other_news', $data);

			$data['header'] = $this->load->controller('common/header');
			$data['footer'] = $this->load->controller('common/footer');
			$data['column_left'] = $this->load->controller('common/column_left');
			$data['column_right'] = $this->load->controller('common/column_right');
			$data['content_top'] = $this->load->controller('common/content_top');
			$data['content_bottom'] = $this->load->controller('common/content_bottom');

			$this->response->setOutput($this->load->view('blog/post', $data));
		} else {
			$this->response->redirect($this->url->link('error/not_found'));
		}
	}
}