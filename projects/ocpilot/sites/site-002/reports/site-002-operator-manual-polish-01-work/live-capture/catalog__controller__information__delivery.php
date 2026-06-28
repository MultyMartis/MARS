<?php
class ControllerInformationDelivery extends Controller {

	public function index() {
		$this->load->language('information/contact');

		$this->document->setTitle('Доставка оборудования — ЗПМ');
		$this->document->setDescription('Как получить оборудование ЗПМ: отгрузка из Барнаула и со склада партнёра в Московской области, доставка транспортными компаниями по России, самовывоз. Порядок отгрузки после оплаты.');
		$this->document->setKeywords('доставка оборудования ЗПМ, доставка по России, самовывоз Барнаул, транспортная компания');
		$this->document->setBodyClass('page--inner');

		$data['breadcrumbs'] = array();

		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_home'),
			'href' => $this->url->link('common/home')
		);

		$data['breadcrumbs'][] = array(
			'text' => 'Доставка',
			'href' => $this->url->link('information/delivery')
		);

		$breadcrumbs = new Breadcrumbs();
		$breadcrumbs->breadcrumbs = $data['breadcrumbs'];
		$this->document->setBreadcrumbs($breadcrumbs->render());

		$pageintro = new Pageintro();
		$pageintro->title = 'Доставка';
		$this->document->setPageintro($pageintro->render());

		$data['page_lead'] = '<p>ООО «Завод пищевого машиностроения» (ЗПМ) поставляет нейтральное оборудование из нержавеющей стали предприятиям общепита и пищевых производств по всей России. Отгрузка выполняется с производственной площадки в Барнауле или со склада партнёра в Московской области — в зависимости от состава заказа и согласованного способа получения.</p>'
			. '<p>Вы выбираете, как забрать оборудование: самовывоз или доставка транспортной компанией. Менеджер сопровождает заказ от готовности к отгрузке до передачи груза — с понятными этапами, адресами точек выдачи и комплектом документов. Условия оплаты и момент запуска производства или отгрузки — на странице <a href="/payment-methods">Оплата</a>.</p>';

		$data['column_left'] = $this->load->controller('common/column_left');
		$data['column_right'] = $this->load->controller('common/column_right');
		$data['content_top'] = $this->load->controller('common/content_top');
		$data['content_bottom'] = $this->load->controller('common/content_bottom');
		$data['footer'] = $this->load->controller('common/footer');
		$data['header'] = $this->load->controller('common/header');

		$this->response->setOutput($this->load->view('information/delivery', $data));
	}
}
