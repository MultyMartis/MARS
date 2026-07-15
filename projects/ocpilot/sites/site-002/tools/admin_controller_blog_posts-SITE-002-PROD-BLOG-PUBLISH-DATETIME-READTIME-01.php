<?php
class ControllerBlogPosts extends Controller {
	private $error = array();

	public function index() {
		$this->load->language('blog/posts');
		$this->document->setTitle($this->language->get('heading_title'));
		$this->load->model('blog/blog');

		$this->getList();
	}

	public function add() {
		$this->load->language('blog/posts');
		$this->document->setTitle($this->language->get('heading_title'));
		$this->load->model('blog/blog');

		if (($this->request->server['REQUEST_METHOD'] == 'POST') && $this->validateForm()) {
			$this->model_blog_blog->addPost($this->request->post);
			$this->session->data['success'] = $this->language->get('text_success');
			$this->response->redirect($this->url->link('blog/posts', 'user_token=' . $this->session->data['user_token'], true));
		}

		$this->getForm();
	}

	public function edit() {
		$this->load->language('blog/posts');
		$this->document->setTitle($this->language->get('heading_title'));
		$this->load->model('blog/blog');

		if (($this->request->server['REQUEST_METHOD'] == 'POST') && $this->validateForm()) {
			$this->model_blog_blog->editPost($this->request->get['post_id'], $this->request->post);
			$this->session->data['success'] = $this->language->get('text_success');
			$this->response->redirect($this->url->link('blog/posts', 'user_token=' . $this->session->data['user_token'], true));
		}

		$this->getForm();
	}

	public function delete() {
		$this->load->language('blog/posts');
		$this->document->setTitle($this->language->get('heading_title'));
		$this->load->model('blog/blog');

		if (isset($this->request->post['selected']) && $this->validateDelete()) {
			foreach ($this->request->post['selected'] as $post_id) {
				$this->model_blog_blog->deletePost($post_id);
			}
			$this->session->data['success'] = $this->language->get('text_success');
			$this->response->redirect($this->url->link('blog/posts', 'user_token=' . $this->session->data['user_token'], true));
		}

		$this->getList();
	}

	protected function getList() {
		// Стандартные хлебные крошки
		$data['breadcrumbs'] = array();
		$data['breadcrumbs'][] = array('text' => $this->language->get('text_home'), 'href' => $this->url->link('common/dashboard', 'user_token=' . $this->session->data['user_token'], true));
		$data['breadcrumbs'][] = array('text' => $this->language->get('heading_title'), 'href' => $this->url->link('blog/posts', 'user_token=' . $this->session->data['user_token'], true));

		$data['add'] = $this->url->link('blog/posts/add', 'user_token=' . $this->session->data['user_token'], true);
		$data['delete'] = $this->url->link('blog/posts/delete', 'user_token=' . $this->session->data['user_token'], true);

		$data['posts'] = array();
		
		// Пагинация (упрощенно)
		$filter_data = array('start' => 0, 'limit' => 20);
		$results = $this->model_blog_blog->getPosts($filter_data);

		foreach ($results as $result) {
			$data['posts'][] = array(
				'post_id' => $result['id'],
				'title'   => $result['title'],
				'category'=> $result['category_name'],
				'status'  => ($result['active']) ? $this->language->get('text_enabled') : $this->language->get('text_disabled'),
				'date'    => date('d.m.Y H:i', strtotime($result['date_added'])),
				'edit'    => $this->url->link('blog/posts/edit', 'user_token=' . $this->session->data['user_token'] . '&post_id=' . $result['id'], true)
			);
		}

		$data['user_token'] = $this->session->data['user_token'];
		$data['header'] = $this->load->controller('common/header');
		$data['column_left'] = $this->load->controller('common/column_left');
		$data['footer'] = $this->load->controller('common/footer');

		$this->response->setOutput($this->load->view('blog/posts_list', $data));
	}

	protected function getForm() {
		// Подключаем скрипты редактора и менеджера картинок
		$this->document->addScript('view/javascript/codemirror/lib/codemirror.js');
		$this->document->addScript('view/javascript/codemirror/lib/xml.js');
		$this->document->addScript('view/javascript/codemirror/formatting.js');
		$this->document->addScript('view/javascript/summernote/summernote.js');
		$this->document->addScript('view/javascript/summernote/summernote-image-attributes.js');
		$this->document->addScript('view/javascript/summernote/opencart.js');
		$this->document->addStyle('view/javascript/codemirror/lib/codemirror.css');
		$this->document->addStyle('view/javascript/codemirror/theme/monokai.css');
		$this->document->addStyle('view/javascript/summernote/summernote.css');
		$this->document->addScript('view/javascript/jquery/datetimepicker/moment/moment.min.js');
		$this->document->addScript('view/javascript/jquery/datetimepicker/moment/moment-with-locales.min.js');
		$this->document->addScript('view/javascript/jquery/datetimepicker/bootstrap-datetimepicker.min.js');
		$this->document->addStyle('view/javascript/jquery/datetimepicker/bootstrap-datetimepicker.min.css');

		$data['text_form'] = !isset($this->request->get['post_id']) ? $this->language->get('text_add') : $this->language->get('text_edit');
		$data['user_token'] = $this->session->data['user_token'];

		$post_info = array();
		if (isset($this->request->get['post_id'])) {
			$post_info = $this->model_blog_blog->getPost($this->request->get['post_id']);
		}

		// Поля формы (название, текст, мета-теги и т.д.)
		$fields = array('title', 'short_description', 'content', 'image', 'category_id', 'active', 'keyword', 'meta_title', 'meta_description', 'meta_keyword');
		foreach ($fields as $field) {
			if (isset($this->request->post[$field])) {
				$data[$field] = $this->request->post[$field];
			} elseif (!empty($post_info)) {
				$data[$field] = $post_info[$field];
			} else {
				$data[$field] = ($field == 'active') ? 1 : '';
			}
		}

		// Обработка изображения (превью)
		$this->load->model('tool/image');
		$data['placeholder'] = $this->model_tool_image->resize('no_image.png', 100, 100);
		if (!empty($data['image'])) {
			$data['thumb'] = $this->model_tool_image->resize($data['image'], 100, 100);
		} else {
			$data['thumb'] = $data['placeholder'];
		}

		// Список категорий для выбора
		$data['categories'] = $this->model_blog_blog->getCategories();

		if (!empty($post_info) && !empty($post_info['date_added'])) {
			$data['modified'] = date('Y-m-d H:i', strtotime($post_info['date_added']));
		} elseif (isset($this->request->post['modified'])) {
			$data['modified'] = $this->request->post['modified'];
		} else {
			$data['modified'] = date('Y-m-d H:i');
		}

		if (!empty($post_info) && isset($post_info['reading_time_minutes'])) {
			$data['reading_time_minutes'] = (int)$post_info['reading_time_minutes'];
		} else {
			$data['reading_time_minutes'] = 0;
		}

		$data['action'] = !isset($this->request->get['post_id']) ? 
			$this->url->link('blog/posts/add', 'user_token=' . $this->session->data['user_token'], true) : 
			$this->url->link('blog/posts/edit', 'user_token=' . $this->session->data['user_token'] . '&post_id=' . $this->request->get['post_id'], true);
		
		$data['cancel'] = $this->url->link('blog/posts', 'user_token=' . $this->session->data['user_token'], true);

		$data['header'] = $this->load->controller('common/header');
		$data['column_left'] = $this->load->controller('common/column_left');
		$data['footer'] = $this->load->controller('common/footer');

		$this->response->setOutput($this->load->view('blog/posts_form', $data));
	}

	protected function validateForm() {
		if (!$this->user->hasPermission('modify', 'blog/posts')) {
			$this->error['warning'] = $this->language->get('error_permission');
		}
		return !$this->error;
	}

	protected function validateDelete() {
		if (!$this->user->hasPermission('modify', 'blog/posts')) {
			$this->error['warning'] = $this->language->get('error_permission');
		}
		return !$this->error;
	}
}