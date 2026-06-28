<?php
class ControllerInformationPayment extends Controller {

	public function index() {
		$this->load->language('information/contact');

		$this->document->setTitle('Оплата оборудования — ЗПМ');
		$this->document->setDescription('Как оплатить оборудование ЗПМ для юридических лиц: безналичный расчёт по счёту, порядок выставления документов, этапы после оплаты. Работа с предприятиями и закупщиками по всей России.');
		$this->document->setKeywords('оплата оборудования ЗПМ, безналичный расчёт, счёт на оплату, B2B закупка');
		$this->document->setBodyClass('page--inner');

		$data['breadcrumbs'] = array();

		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_home'),
			'href' => $this->url->link('common/home')
		);

		$data['breadcrumbs'][] = array(
			'text' => 'Оплата',
			'href' => $this->url->link('information/payment')
		);

		$breadcrumbs = new Breadcrumbs();
		$breadcrumbs->breadcrumbs = $data['breadcrumbs'];
		$this->document->setBreadcrumbs($breadcrumbs->render());

		$pageintro = new Pageintro();
		$pageintro->title = 'Оплата';
		$this->document->setPageintro($pageintro->render());

		$data['page_lead'] = '<p>ООО «Завод пищевого машиностроения» (ЗПМ) работает с&nbsp;юридическими лицами и&nbsp;индивидуальными предпринимателями по&nbsp;безналичному расчёту. Оплата проходит по&nbsp;выставленному счёту — после согласования состава заказа и&nbsp;коммерческих условий с&nbsp;менеджером.</p>'
			. '<p>Порядок понятен на&nbsp;каждом этапе: заявка → коммерческое предложение → счёт → оплата → подтверждение → производство или отгрузка. Закрывающие документы передаются по&nbsp;факту отгрузки. Менеджер сопровождает процесс от&nbsp;первого запроса до&nbsp;подтверждения оплаты и&nbsp;передачи заказа на&nbsp;комплектацию или в&nbsp;производство.</p>'
			. '<p>Юридические реквизиты организации для проверки контрагента — на&nbsp;странице <a href="/contact/">Контакты</a>. Способ и&nbsp;срок получения оборудования после оплаты — на&nbsp;странице <a href="/delivery">Доставка</a>.</p>';

		$data['column_left'] = $this->load->controller('common/column_left');
		$data['column_right'] = $this->load->controller('common/column_right');
		$data['content_top'] = $this->load->controller('common/content_top');
		$data['content_bottom'] = $this->load->controller('common/content_bottom');
		$data['footer'] = $this->load->controller('common/footer');
		$data['header'] = $this->load->controller('common/header');

		$this->response->setOutput($this->load->view('information/payment', $data));
	}
}
