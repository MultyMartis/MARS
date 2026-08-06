<?php
/**
 * SITE-002 OpenCart admin — Обмен с 1С (Phase 1B-D6G).
 * Manual async launch of canonical MARS 1C import runner.
 */
class ControllerToolMars1cExchange extends Controller {
    private $error = array();

    public function index() {
        $this->load->language('tool/mars_1c_exchange');
        $this->document->setTitle($this->language->get('heading_title'));
        $this->load->model('tool/mars_1c_exchange');

        if (!$this->user->hasPermission('access', 'tool/mars_1c_exchange')) {
            $this->response->redirect($this->url->link('error/permission', 'user_token=' . $this->session->data['user_token'], true));
            return;
        }

        $data['heading_title'] = $this->language->get('heading_title');
        $data['text_confirm'] = $this->language->get('text_confirm');
        $data['button_run'] = $this->language->get('button_run');
        $data['button_refresh'] = $this->language->get('button_refresh');
        $data['user_token'] = $this->session->data['user_token'];
        $data['can_modify'] = $this->user->hasPermission('modify', 'tool/mars_1c_exchange');
        $data['status_url'] = $this->url->link('tool/mars_1c_exchange/status', 'user_token=' . $this->session->data['user_token'], true);
        $data['run_url'] = $this->url->link('tool/mars_1c_exchange/run', 'user_token=' . $this->session->data['user_token'], true);
        $data['breadcrumbs'] = array();
        $data['breadcrumbs'][] = array(
            'text' => $this->language->get('text_home'),
            'href' => $this->url->link('common/dashboard', 'user_token=' . $this->session->data['user_token'], true)
        );
        $data['breadcrumbs'][] = array(
            'text' => $this->language->get('heading_title'),
            'href' => $this->url->link('tool/mars_1c_exchange', 'user_token=' . $this->session->data['user_token'], true)
        );
        $data['header'] = $this->load->controller('common/header');
        $data['column_left'] = $this->load->controller('common/column_left');
        $data['footer'] = $this->load->controller('common/footer');
        $data['initial'] = $this->model_tool_mars_1c_exchange->getPublicStatus();
        $this->response->setOutput($this->load->view('tool/mars_1c_exchange', $data));
    }

    public function status() {
        $this->load->language('tool/mars_1c_exchange');
        $this->response->addHeader('Content-Type: application/json; charset=utf-8');
        if (!$this->user->hasPermission('access', 'tool/mars_1c_exchange')) {
            $this->response->setOutput(json_encode(array('ok' => false, 'error' => 'permission'), JSON_UNESCAPED_UNICODE));
            return;
        }
        $this->load->model('tool/mars_1c_exchange');
        $this->response->setOutput(json_encode($this->model_tool_mars_1c_exchange->getPublicStatus(), JSON_UNESCAPED_UNICODE));
    }

    public function run() {
        $this->load->language('tool/mars_1c_exchange');
        $this->response->addHeader('Content-Type: application/json; charset=utf-8');

        if ($this->request->server['REQUEST_METHOD'] !== 'POST') {
            $this->response->setOutput(json_encode(array('ok' => false, 'error' => 'POST required'), JSON_UNESCAPED_UNICODE));
            return;
        }
        if (!$this->user->hasPermission('modify', 'tool/mars_1c_exchange')) {
            $this->response->setOutput(json_encode(array('ok' => false, 'error' => 'Нет права на изменение'), JSON_UNESCAPED_UNICODE));
            return;
        }
        $token = isset($this->session->data['user_token']) ? $this->session->data['user_token'] : '';
        $reqToken = isset($this->request->post['user_token']) ? $this->request->post['user_token'] : (isset($this->request->get['user_token']) ? $this->request->get['user_token'] : '');
        if ($token === '' || $reqToken === '' || !hash_equals($token, $reqToken)) {
            $this->response->setOutput(json_encode(array('ok' => false, 'error' => 'Неверный токен'), JSON_UNESCAPED_UNICODE));
            return;
        }

        $this->load->model('tool/mars_1c_exchange');
        $result = $this->model_tool_mars_1c_exchange->enqueueManualImport();
        $this->response->setOutput(json_encode($result, JSON_UNESCAPED_UNICODE));
    }
}
