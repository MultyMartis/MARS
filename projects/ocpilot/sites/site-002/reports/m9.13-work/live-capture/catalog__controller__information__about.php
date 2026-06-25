<?php
class ControllerInformationAbout extends Controller {


	public function index() {
		$this->load->language('information/contact');

		$this->document->setTitle('О компании');


		$data['breadcrumbs'] = array();

		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_home'),
			'href' => $this->url->link('common/home')
		);

		$data['breadcrumbs'][] = array(
			'text' => 'О компании',
			'href' => $this->url->link('information/contact')
		);

        	$breadcrumbs = new Breadcrumbs();
			$breadcrumbs->breadcrumbs  = $data['breadcrumbs'];
			$this->document->setBreadcrumbs( $breadcrumbs->render() );

			$pageintro = new Pageintro();
			$pageintro->title = 'О компании';
			$pageintro->description = '';
			$this->document->setPageintro( $pageintro->render() );

	
        $data['blockaboutadvanttop'] = $this->load->view('sections/blockaboutadvanttop');
        $data['blockaboutadvantbotom'] = $this->load->view('sections/blockaboutadvantbotom');
        $data['aboutcertificates'] = $this->load->view('sections/aboutcertificates');
        $data['blockdealersform'] = $this->load->view('sections/blockdealersform');

		

		$data['column_left'] = $this->load->controller('common/column_left');
		$data['column_right'] = $this->load->controller('common/column_right');
		$data['content_top'] = $this->load->controller('common/content_top');
		$data['content_bottom'] = $this->load->controller('common/content_bottom');
		$data['footer'] = $this->load->controller('common/footer');
		$data['header'] = $this->load->controller('common/header');

		$this->response->setOutput($this->load->view('information/about', $data));
	}

	
}
