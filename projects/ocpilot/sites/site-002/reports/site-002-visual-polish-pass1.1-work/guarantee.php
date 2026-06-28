<?php
class ControllerInformationGuarantee extends Controller {

	public function index() {
		$this->load->language('information/contact');

		$this->document->setTitle('Гарантия на оборудование — ЗПМ');
		$this->document->setDescription('Гарантийная поддержка оборудования ЗПМ: как обратиться при неисправности, какие документы подготовить и как проходит рассмотрение обращения. Производитель — ООО «Завод пищевого машиностроения».');
		$this->document->setKeywords('гарантия ЗПМ, гарантийное обслуживание, обращение по гарантии, заводской дефект');
		$this->document->setBodyClass('page--inner');

		$data['breadcrumbs'] = array();

		$data['breadcrumbs'][] = array(
			'text' => $this->language->get('text_home'),
			'href' => $this->url->link('common/home')
		);

		$data['breadcrumbs'][] = array(
			'text' => 'Гарантия',
			'href' => $this->url->link('information/guarantee')
		);

		$breadcrumbs = new Breadcrumbs();
		$breadcrumbs->breadcrumbs = $data['breadcrumbs'];
		$this->document->setBreadcrumbs($breadcrumbs->render());

		$pageintro = new Pageintro();
		$pageintro->title = 'Гарантия на оборудование';
		$this->document->setPageintro($pageintro->render());

		$data['page_lead'] = '<p>ООО «Завод пищевого машиностроения» (ЗПМ) выпускает нейтральное оборудование из&nbsp;нержавеющей стали для общепита и&nbsp;пищевых производств и&nbsp;сопровождает его после покупки. Если в&nbsp;работе оборудования возникла неисправность, вы&nbsp;можете обратиться к&nbsp;заводу: менеджер примет обращение, уточнит обстоятельства и&nbsp;подскажет, какие документы и&nbsp;сведения понадобятся для рассмотрения.</p>'
			. '<p>Гарантийная поддержка распространяется на&nbsp;оборудование при соблюдении правил эксплуатации, транспортировки и&nbsp;хранения, указанных в&nbsp;документации производителя. Конкретные условия — срок, объём покрытия и&nbsp;порядок урегулирования — зависят от&nbsp;модели и&nbsp;условий поставки; их&nbsp;уточняет менеджер по&nbsp;вашему обращению и&nbsp;комплекту документов. Производственный контроль и&nbsp;документы соответствия на&nbsp;продукцию — на&nbsp;странице <a href="/about">О&nbsp;компании</a>; порядок получения оборудования — на&nbsp;странице <a href="/delivery">Доставка</a>.</p>';

		$data['column_left'] = $this->load->controller('common/column_left');
		$data['column_right'] = $this->load->controller('common/column_right');
		$data['content_top'] = $this->load->controller('common/content_top');
		$data['content_bottom'] = $this->load->controller('common/content_bottom');
		$data['footer'] = $this->load->controller('common/footer');
		$data['header'] = $this->load->controller('common/header');

		$this->response->setOutput($this->load->view('information/guarantee', $data));
	}
}
