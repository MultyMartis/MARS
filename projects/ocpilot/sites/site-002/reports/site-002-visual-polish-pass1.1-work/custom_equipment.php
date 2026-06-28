<?php
class ControllerInformationCustomEquipment extends Controller {

	public function index() {
		$this->load->language('information/contact');

		$this->document->setTitle('Оборудование на заказ — изготовление по вашим требованиям | ООО «ЗПМ»');
		$this->document->setDescription('Завод пищевого машиностроения ЗПМ изготавливает нейтральное оборудование из нержавеющей стали на заказ: нестандартные размеры, комплектация и конструкция под ваше помещение и технологию. Производство в Барнауле, поставки по России.');
		$this->document->setKeywords('оборудование на заказ, изготовление нержавеющей стали, нестандартное оборудование общепит, ЗПМ на заказ, производство Барнаул');
		$this->document->setBodyClass('page--inner');

		$data['breadcrumbs'] = array();

		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_home'),
			'href' => $this->url->link('common/home')
		);

		$data['breadcrumbs'][] = array(
			'text' => 'Оборудование на заказ',
			'href' => $this->url->link('information/custom_equipment')
		);

		$breadcrumbs = new Breadcrumbs();
		$breadcrumbs->breadcrumbs = $data['breadcrumbs'];
		$this->document->setBreadcrumbs($breadcrumbs->render());

		$pageintro = new Pageintro();
		$pageintro->title = 'Оборудование на заказ';
		$this->document->setPageintro($pageintro->render());

		$data['page_lead'] = '<p>ООО «Завод пищевого машиностроения» (ЗПМ) изготавливает нейтральное оборудование из&nbsp;нержавеющей стали по&nbsp;техническому заданию заказчика — когда серийная модель из&nbsp;каталога не&nbsp;подходит по&nbsp;размеру, комплектации или условиям установки. Производство выполняется на&nbsp;собственной площадке в&nbsp;Барнауле; отгрузка — по&nbsp;всей России.</p>'
			. '<p>На&nbsp;этой странице — что можно заказать, как устроена работа над проектом, какие данные нужны для расчёта и&nbsp;что вы&nbsp;получаете на&nbsp;выходе. Если нужна конкретная конфигурация — опишите задачу в&nbsp;форме внизу страницы или свяжитесь с&nbsp;менеджером.</p>';

		$data['column_left'] = $this->load->controller('common/column_left');
		$data['column_right'] = $this->load->controller('common/column_right');
		$data['content_top'] = $this->load->controller('common/content_top');
		$data['content_bottom'] = $this->load->controller('common/content_bottom');
		$data['footer'] = $this->load->controller('common/footer');
		$data['header'] = $this->load->controller('common/header');

		$this->response->setOutput($this->load->view('information/custom_equipment', $data));
	}
}
