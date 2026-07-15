<?php
class ControllerCheckoutAnketa extends Controller {
	public function index() {
		$received_token = $this->request->post['csrf_token'] ?? '';

		if (empty($received_token) || $received_token !== $this->session->data['csrf_token']) {
			http_response_code(403);
			echo json_encode(array(
				'ok' => false,
				'message' => 'Ошибка безопасности: неверный CSRF токен. Пожалуйста, обновите страницу.'
			));
			exit;
		}

		$token = $this->request->post['g-recaptcha-response'] ?? '';

		if (empty($token)) {
			http_response_code(400);
			echo json_encode(array('ok' => false, 'message' => 'Ошибка безопасности: токен отсутствует'));
			exit;
		}

		$response = file_get_contents("https://www.google.com/recaptcha/api/siteverify", false, stream_context_create(array(
			'http' => array(
				'method' => 'POST',
				'header' => "Content-type: application/x-www-form-urlencoded\r\n",
				'content' => http_build_query(array(
					'secret' => reCAPTCHA_secret,
					'response' => $token
				))
			)
		)));

		$resp_data = json_decode($response, true);

		if (!$resp_data || !$resp_data['success']) {
			http_response_code(400);
			echo json_encode(array('ok' => false, 'message' => 'Ошибка проверки безопасности (reCaptcha)'));
			exit;
		}

		$dialog = 0;
		if (isset($this->request->post['dialog'])) {
			$dialog = intval($this->request->post['dialog']);
		}

		$data = array();
		$data['date_added'] = date('Y-m-d H:i:s');
		$data['type'] = 0;
		$data['status'] = 0;
		$data['author'] = '';
		$data['company'] = '';
		$data['email'] = '';
		$data['phone'] = '';
		$data['text'] = '';

		if (isset($this->request->post['name'])) {
			$data['author'] = $this->request->post['name'];
		} elseif (isset($this->request->post['contact'])) {
			$data['author'] = $this->request->post['contact'];
		}
		if (isset($this->request->post['company'])) {
			$data['company'] = $this->request->post['company'];
		}
		if (isset($this->request->post['phone'])) {
			$data['phone'] = $this->request->post['phone'];
		}
		if (isset($this->request->post['email'])) {
			$data['email'] = $this->request->post['email'];
		}
		if (isset($this->request->post['message'])) {
			$data['text'] = $this->request->post['message'];
		}

		// Reject leads with no user content (prevents admin mail of service-only empty submissions).
		// Audit: SITE-002-PROD-1C-LOGS-AND-FORM-MAIL-AUDIT-01 / OCPilot Run 4.264
		$has_user_field = false;
		foreach (array('name', 'contact', 'phone', 'email', 'company', 'message', 'comment', 'text', 'project_description', 'subject') as $zpm_user_key) {
			if (isset($this->request->post[$zpm_user_key]) && trim((string)$this->request->post[$zpm_user_key]) !== '') {
				$has_user_field = true;
				break;
			}
		}
		if (!$has_user_field) {
			http_response_code(400);
			echo json_encode(array(
				'ok' => false,
				'message' => 'Заполните имя, телефон или e-mail'
			));
			exit;
		}

		$text = '';
		$dialog_label = $this->zpmDialogLabel($dialog);
		$product_name = '';

		if ($dialog == 1) {
			$text = "Вопрос по товару " . chr(10) . chr(13);
			if (isset($this->request->post['tovar'])) {
				$product_name = $this->request->post['tovar'];
				$text .= $product_name . " " . chr(10) . chr(13);
			}
		} elseif ($dialog == 2) {
			$text = "Запрос на обратный звонок " . chr(10) . chr(13);
		} elseif ($dialog == 3) {
			$text = "Вопрос по цене товара " . chr(10) . chr(13);
			if (isset($this->request->post['tovar'])) {
				$product_name = $this->request->post['tovar'];
				$text .= $product_name . " " . chr(10) . chr(13);
			}
			$data['type'] = 1;
		} elseif ($dialog == 5) {
			$text = "Новый отзыв" . chr(10) . chr(13);
		} elseif ($dialog == 7) {
			$text = "Форма диллерам и оптовикам" . chr(10) . chr(13);
		} elseif ($dialog == 8) {
			$text = "Вопрос по доставке" . chr(10) . chr(13);
		} elseif ($dialog == 9) {
			$text = "Вопрос по оплате" . chr(10) . chr(13);
		} elseif ($dialog == 10) {
			$text = "Гарантийное обращение" . chr(10) . chr(13);
		} elseif ($dialog == 11) {
			$text = "Оборудование на заказ" . chr(10) . chr(13);
		}

		if (isset($this->request->post['subject'])) {
			$text .= "Тема: " . $this->request->post['subject'] . chr(10) . chr(13);
		}
		if (isset($this->request->post['text'])) {
			$text .= '   ' . $this->request->post['text'];
		}
		if (isset($this->request->post['comment'])) {
			$text .= $this->request->post['comment'];
		}

		$data['text'] = $text . chr(10) . chr(13) . $data['text'];

		$visitor_message = '';
		if (isset($this->request->post['message']) && $this->request->post['message'] !== '') {
			$visitor_message = $this->request->post['message'];
		} elseif (isset($this->request->post['comment']) && $this->request->post['comment'] !== '') {
			$visitor_message = $this->request->post['comment'];
		} elseif (isset($this->request->post['project_description']) && $this->request->post['project_description'] !== '') {
			$visitor_message = $this->request->post['project_description'];
		} elseif (isset($this->request->post['text']) && $this->request->post['text'] !== '') {
			$visitor_message = $this->request->post['text'];
		} else {
			$visitor_message = trim($data['text']);
		}

		$subject = 'ЗПМ: новая заявка — ' . $dialog_label;
		$submitted_at = date('Y-m-d H:i:s');
		$page_url = $this->zpmResolvePageUrl();
		$service_info = $this->zpmBuildServiceInfo($dialog, $submitted_at);
		$extra_fields = $this->zpmCollectExtraFields();

		$mail_html = '';
		$mail_text = '';
		$renderer = null;

		$renderer_path = DIR_SYSTEM . 'library/zpm/mail_renderer.php';
		if (is_file($renderer_path)) {
			require_once($renderer_path);
			if (class_exists('ZpmMailRenderer')) {
				$renderer = new ZpmMailRenderer();
				$rendered = $renderer->renderAdminForm(array(
					'subject' => $subject,
					'dialog' => $dialog,
					'dialog_label' => $dialog_label,
					'author' => $data['author'],
					'company' => $data['company'],
					'phone' => $data['phone'],
					'email' => $data['email'],
					'message' => $visitor_message,
					'product' => $product_name,
					'page_url' => $page_url,
					'submitted_at' => $submitted_at,
					'extra_fields' => $extra_fields,
					'service_info' => $service_info,
				));
				if (is_array($rendered)) {
					$mail_html = isset($rendered['html']) ? $rendered['html'] : '';
					$mail_text = isset($rendered['text']) ? $rendered['text'] : '';
				}
			}
		}

		if ($mail_html === '') {
			$mail_html = '<p>' . htmlspecialchars($data['text'], ENT_QUOTES, 'UTF-8') . '</p>'
				. '<p>' . htmlspecialchars($data['author'], ENT_QUOTES, 'UTF-8') . '</p>'
				. '<p>' . htmlspecialchars($data['phone'], ENT_QUOTES, 'UTF-8') . '</p>'
				. '<p>' . htmlspecialchars($data['email'], ENT_QUOTES, 'UTF-8') . '</p>';
			$mail_text = strip_tags(html_entity_decode($mail_html, ENT_QUOTES, 'UTF-8'));
		}

		$this->load->model('checkout/anketa');
		$this->model_checkout_anketa->addanketa($data);

		$mail = new Mail($this->config->get('config_mail_engine'));
		$mail->parameter = $this->config->get('config_mail_parameter');
		$mail->smtp_hostname = $this->config->get('config_mail_smtp_hostname');
		$mail->smtp_username = $this->config->get('config_mail_smtp_username');
		$mail->smtp_password = html_entity_decode($this->config->get('config_mail_smtp_password'), ENT_QUOTES, 'UTF-8');
		$mail->smtp_port = $this->config->get('config_mail_smtp_port');
		$mail->smtp_timeout = $this->config->get('config_mail_smtp_timeout');
		$mail->setFrom($this->config->get('config_email'));
		$mail->setSender(html_entity_decode($this->config->get('config_name'), ENT_QUOTES, 'UTF-8'));
		$mail->setSubject($subject);
		$mail->setText($mail_text);
		$mail->setHtml($mail_html);

		$emails = explode(',', (string)$this->config->get('config_mail_alert_email'));
		$send_attempted = false;
		$send_ok = false;

		foreach ($emails as $email) {
			$email = trim($email);
			if (utf8_strlen($email) > 0 && filter_var($email, FILTER_VALIDATE_EMAIL)) {
				$send_attempted = true;
				$mail->setTo($email);
				try {
					$mail->send();
					$send_ok = true;
				} catch (Exception $e) {
					// Do not expose transport errors to visitor.
				}
			}
		}

		if ($send_attempted && $send_ok) {
			$this->zpmSendCustomerFormConfirmation(
				$renderer,
				$data,
				$dialog_label,
				$visitor_message,
				$product_name,
				$submitted_at,
				$extra_fields
			);
			echo json_encode(array('ok' => true, 'message' => 'Заявка отправлена'));
		} elseif ($send_attempted) {
			http_response_code(500);
			echo json_encode(array('ok' => false, 'message' => 'Не удалось отправить заявку. Попробуйте позже или свяжитесь с нами по телефону.'));
		} else {
			echo json_encode(array('ok' => true, 'message' => 'Заявка принята'));
		}
	}

	private function zpmResolveCustomerEmail($posted_email) {
		$posted = trim((string)$posted_email);
		if ($posted !== '' && filter_var($posted, FILTER_VALIDATE_EMAIL)) {
			return $posted;
		}

		if ($this->customer->isLogged()) {
			$account_email = trim((string)$this->customer->getEmail());
			if ($account_email !== '' && filter_var($account_email, FILTER_VALIDATE_EMAIL)) {
				return $account_email;
			}
		}

		return '';
	}

	private function zpmSendCustomerFormConfirmation($renderer, $data, $dialog_label, $visitor_message, $product_name, $submitted_at, $extra_fields = array()) {
		$customer_email = $this->zpmResolveCustomerEmail($data['email']);
		if ($customer_email === '') {
			return;
		}

		$customer_subject = 'ЗПМ: заявка получена — ' . $dialog_label;
		$customer_html = '';
		$customer_text = '';

		if ($renderer instanceof ZpmMailRenderer) {
			$rendered = $renderer->renderCustomerFormConfirmation(array(
				'subject' => $customer_subject,
				'dialog_label' => $dialog_label,
				'author' => $data['author'],
				'phone' => $data['phone'],
				'email' => $data['email'],
				'message' => $visitor_message,
				'product' => $product_name,
				'submitted_at' => $submitted_at,
				'extra_fields' => $extra_fields,
				'next_step' => 'Специалист свяжется с вами по указанным контактам.',
			));
			if (is_array($rendered)) {
				$customer_html = isset($rendered['html']) ? $rendered['html'] : '';
				$customer_text = isset($rendered['text']) ? $rendered['text'] : '';
			}
		}

		if ($customer_html === '') {
			$customer_html = '<p>Мы получили вашу заявку на сайте ЗПМ.</p>'
				. '<p>Специалист свяжется с вами по указанным контактам.</p>';
			$customer_text = strip_tags(html_entity_decode($customer_html, ENT_QUOTES, 'UTF-8'));
		}

		try {
			$customer_mail = new Mail($this->config->get('config_mail_engine'));
			$customer_mail->parameter = $this->config->get('config_mail_parameter');
			$customer_mail->smtp_hostname = $this->config->get('config_mail_smtp_hostname');
			$customer_mail->smtp_username = $this->config->get('config_mail_smtp_username');
			$customer_mail->smtp_password = html_entity_decode($this->config->get('config_mail_smtp_password'), ENT_QUOTES, 'UTF-8');
			$customer_mail->smtp_port = $this->config->get('config_mail_smtp_port');
			$customer_mail->smtp_timeout = $this->config->get('config_mail_smtp_timeout');
			$customer_mail->setFrom($this->config->get('config_email'));
			$customer_mail->setSender(html_entity_decode($this->config->get('config_name'), ENT_QUOTES, 'UTF-8'));
			$customer_mail->setTo($customer_email);
			$customer_mail->setSubject($customer_subject);
			$customer_mail->setText($customer_text);
			$customer_mail->setHtml($customer_html);
			$customer_mail->send();
		} catch (Exception $e) {
			// Customer copy failure must not break admin acceptance response.
		}
	}

	private function zpmDialogLabel($dialog) {
		switch ((int)$dialog) {
			case 1:
				return 'Вопрос по товару';
			case 2:
				return 'Запрос на обратный звонок';
			case 3:
				return 'Вопрос по цене товара';
			case 5:
				return 'Новый отзыв';
			case 7:
				return 'Форма дилерам и оптовикам';
			case 8:
				return 'Вопрос по доставке';
			case 9:
				return 'Вопрос по оплате';
			case 10:
				return 'Гарантийное обращение';
			case 11:
				return 'Оборудование на заказ';
			default:
				return 'Заявка с сайта';
		}
	}

	private function zpmResolvePageUrl() {
		if (!empty($this->request->post['page_url'])) {
			return (string)$this->request->post['page_url'];
		}
		if (!empty($this->request->post['source_page'])) {
			return (string)$this->request->post['source_page'];
		}
		if (!empty($this->request->server['HTTP_REFERER'])) {
			return (string)$this->request->server['HTTP_REFERER'];
		}
		if (!empty($this->request->server['REQUEST_URI'])) {
			$scheme = (!empty($this->request->server['HTTPS']) && $this->request->server['HTTPS'] !== 'off') ? 'https' : 'http';
			$host = !empty($this->request->server['HTTP_HOST']) ? $this->request->server['HTTP_HOST'] : 'bzpm.ru';
			return $scheme . '://' . $host . $this->request->server['REQUEST_URI'];
		}
		return 'https://bzpm.ru/';
	}

	private function zpmBuildServiceInfo($dialog, $submitted_at) {
		$ua = !empty($this->request->server['HTTP_USER_AGENT']) ? (string)$this->request->server['HTTP_USER_AGENT'] : '';
		$parsed = $this->zpmParseUserAgent($ua);

		$info = array(
			'ip' => !empty($this->request->server['REMOTE_ADDR']) ? (string)$this->request->server['REMOTE_ADDR'] : 'unknown',
			'remote_addr' => !empty($this->request->server['REMOTE_ADDR']) ? (string)$this->request->server['REMOTE_ADDR'] : '',
			'user_agent' => $ua,
			'browser' => $parsed['browser'],
			'device' => $parsed['device'],
			'os' => $parsed['os'],
			'referrer' => !empty($this->request->server['HTTP_REFERER']) ? (string)$this->request->server['HTTP_REFERER'] : '',
			'utm' => $this->zpmCollectUtm(),
			'city' => 'unknown',
			'dialog' => (string)(int)$dialog,
			'submitted_at' => $submitted_at,
		);

		if (!empty($this->request->server['HTTP_X_FORWARDED_FOR'])) {
			$info['x_forwarded_for'] = (string)$this->request->server['HTTP_X_FORWARDED_FOR'];
		}
		if (!empty($this->request->server['HTTP_X_REAL_IP'])) {
			$info['x_real_ip'] = (string)$this->request->server['HTTP_X_REAL_IP'];
		}
		if (!empty($this->request->server['HTTP_CF_CONNECTING_IP'])) {
			$info['cf_connecting_ip'] = (string)$this->request->server['HTTP_CF_CONNECTING_IP'];
		}

		return $info;
	}

	private function zpmCollectUtm() {
		$keys = array('utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content');
		$parts = array();

		foreach ($keys as $key) {
			if (!empty($this->request->post[$key])) {
				$parts[] = $key . '=' . $this->request->post[$key];
			}
		}

		if (!$parts && !empty($this->request->server['HTTP_REFERER'])) {
			$ref = (string)$this->request->server['HTTP_REFERER'];
			$query = parse_url($ref, PHP_URL_QUERY);
			if ($query) {
				parse_str($query, $params);
				foreach ($keys as $key) {
					if (!empty($params[$key])) {
						$parts[] = $key . '=' . $params[$key];
					}
				}
			}
		}

		return $parts ? implode('&', $parts) : '';
	}

	private function zpmParseUserAgent($ua) {
		$ua_l = strtolower((string)$ua);
		$result = array(
			'browser' => 'Unknown',
			'device' => 'unknown',
			'os' => 'Unknown',
		);

		if ($ua_l === '') {
			return $result;
		}

		if (strpos($ua_l, 'bot') !== false || strpos($ua_l, 'crawl') !== false || strpos($ua_l, 'spider') !== false) {
			$result['browser'] = 'Bot';
			$result['device'] = 'bot';
		} elseif (strpos($ua_l, 'edg/') !== false || strpos($ua_l, 'edge/') !== false) {
			$result['browser'] = 'Edge';
		} elseif (strpos($ua_l, 'yabrowser') !== false) {
			$result['browser'] = 'Yandex Browser';
		} elseif (strpos($ua_l, 'opr/') !== false || strpos($ua_l, 'opera') !== false) {
			$result['browser'] = 'Opera';
		} elseif (strpos($ua_l, 'firefox/') !== false) {
			$result['browser'] = 'Firefox';
		} elseif (strpos($ua_l, 'chrome/') !== false && strpos($ua_l, 'chromium') === false) {
			$result['browser'] = 'Chrome';
		} elseif (strpos($ua_l, 'safari/') !== false && strpos($ua_l, 'chrome/') === false) {
			$result['browser'] = 'Safari';
		}

		if (strpos($ua_l, 'ipad') !== false || (strpos($ua_l, 'tablet') !== false && strpos($ua_l, 'android') !== false)) {
			$result['device'] = 'tablet';
		} elseif (strpos($ua_l, 'mobile') !== false || strpos($ua_l, 'iphone') !== false || strpos($ua_l, 'android') !== false) {
			$result['device'] = 'mobile';
		} elseif ($result['device'] !== 'bot') {
			$result['device'] = 'desktop';
		}

		if (strpos($ua_l, 'windows') !== false) {
			$result['os'] = 'Windows';
		} elseif (strpos($ua_l, 'iphone') !== false || strpos($ua_l, 'ipad') !== false || strpos($ua_l, 'mac os') !== false) {
			$result['os'] = (strpos($ua_l, 'iphone') !== false || strpos($ua_l, 'ipad') !== false) ? 'iOS' : 'macOS';
		} elseif (strpos($ua_l, 'android') !== false) {
			$result['os'] = 'Android';
		} elseif (strpos($ua_l, 'linux') !== false) {
			$result['os'] = 'Linux';
		}

		return $result;
	}

	private function zpmCollectExtraFields() {
		$map = array(
			'city' => 'Город',
			'region' => 'Регион доставки',
			'delivery_method' => 'Способ получения',
			'order_details' => 'Состав заказа',
			'project_description' => 'Описание задачи',
			'drawings' => 'Чертежи / эскиз',
			'notes' => 'Примечания',
			'equipment_model' => 'Модель оборудования',
			'purchase_date' => 'Дата покупки',
		);
		$extra = array();

		foreach ($map as $key => $label) {
			if (!empty($this->request->post[$key])) {
				$extra[] = array(
					'label' => $label,
					'value' => (string)$this->request->post[$key],
				);
			}
		}

		return $extra;
	}
}
