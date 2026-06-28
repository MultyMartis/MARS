<?php
class ControllerInformationDealers extends Controller {

	public function index() {
		$this->load->language('information/contact');

		$this->document->setTitle('Дилерам и оптовым партнёрам — ЗПМ');
		$this->document->setDescription('Партнёрская программа завода пищевого машиностроения ЗПМ: сотрудничество с дилерами, оптовыми компаниями и проектными партнёрами. Прямые поставки от производителя, поставки по России, понятный порядок начала работы.');
		$this->document->setKeywords('дилеры оборудования для общепита, сотрудничество производитель оборудования, оптовые поставки оборудования для ресторанов, партнёрская программа ЗПМ');
		$this->document->setBodyClass('page--inner');

		$data['breadcrumbs'] = array();

		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_home'),
			'href' => $this->url->link('common/home')
		);

		$data['breadcrumbs'][] = array(
			'text' => 'Дилерам',
			'href' => $this->url->link('information/dealers')
		);

		$breadcrumbs = new Breadcrumbs();
		$breadcrumbs->breadcrumbs = $data['breadcrumbs'];
		$this->document->setBreadcrumbs($breadcrumbs->render());

		$pageintro = new Pageintro();
		$pageintro->title = 'Дилерам и оптовым партнёрам';
		$this->document->setPageintro($pageintro->render());

		$data['page_lead'] = '<p>ООО «Завод пищевого машиностроения» (ЗПМ) — российский производитель нейтрального оборудования из&nbsp;нержавеющей стали для общепита и&nbsp;пищевых производств. Работаем с&nbsp;дилерами, оптовыми и&nbsp;проектными партнёрами <strong>напрямую с&nbsp;завода</strong>.</p>'
			. '<p>Поставки организуются по&nbsp;всей России — с&nbsp;площадки в&nbsp;Барнауле или со&nbsp;склада партнёра в&nbsp;Московской области. Оставьте заявку или свяжитесь с&nbsp;нами: менеджер уточнит профиль компании, направление работы и&nbsp;предложит формат взаимодействия.</p>';

		$data['column_left'] = $this->load->controller('common/column_left');
		$data['column_right'] = $this->load->controller('common/column_right');
		$data['content_top'] = $this->load->controller('common/content_top');
		$data['content_bottom'] = $this->load->controller('common/content_bottom');
		$data['footer'] = $this->load->controller('common/footer');
		$data['header'] = $this->load->controller('common/header');

		$this->response->setOutput($this->load->view('information/dealers', $data));
	}
}
