<?php
/**
 * ZPM shared mail renderer — SITE-002 mail design system foundation.
 *
 * Returns HTML/text strings only. No Mail::send(), no DB, no request globals.
 * Load: require_once(DIR_SYSTEM . 'library/zpm/mail_renderer.php');
 */
class ZpmMailRenderer {
	private $brand = 'ЗПМ';
	private $domain = 'bzpm.ru';

	private $palette = array(
		'bg' => '#f5f7fa',
		'container' => '#ffffff',
		'text' => '#1f2933',
		'muted' => '#667085',
		'border' => '#e5e7eb',
		'accent' => '#0f766e',
		'accent_text' => '#ffffff',
	);

	public function render($type, $data = array(), $options = array()) {
		switch ($type) {
			case 'admin_form':
				return $this->renderAdminForm($data, $options);
			case 'customer_form':
				return $this->renderCustomerFormConfirmation($data, $options);
			case 'account':
				return $this->renderAccountMail($data, $options);
			case 'order':
				return $this->renderOrderMail($data, $options);
			default:
				$title = isset($data['title']) ? $data['title'] : 'Уведомление';
				$sections = isset($data['sections']) ? $data['sections'] : array();
				return $this->renderLayout($title, $sections, $options);
		}
	}

	public function renderAdminForm($data, $options = array()) {
		$title = isset($data['subject']) ? $data['subject'] : 'Новая заявка с сайта';
		$dialog = isset($data['dialog_label']) ? $data['dialog_label'] : '';

		$summary = array();
		if ($dialog !== '') {
			$summary[] = array('label' => 'Тип формы', 'value' => $dialog);
		}
		if (!empty($data['product'])) {
			$summary[] = array('label' => 'Товар', 'value' => $data['product']);
		}
		if (!empty($data['submitted_at'])) {
			$summary[] = array('label' => 'Дата', 'value' => $data['submitted_at']);
		}

		$contact_rows = array();
		if (!empty($data['author'])) {
			$contact_rows[] = array('label' => 'Имя', 'value' => $data['author']);
		}
		if (!empty($data['phone'])) {
			$contact_rows[] = array('label' => 'Телефон', 'value' => $data['phone']);
		}
		if (!empty($data['email'])) {
			$contact_rows[] = array('label' => 'E-mail', 'value' => $data['email']);
		}

		$sections = array();
		if ($summary) {
			$sections[] = $this->componentSummaryCard('Кратко', $summary);
		}
		if ($contact_rows) {
			$sections[] = $this->componentKeyValueTable('Контактные данные', $contact_rows);
		}
		if (!empty($data['message'])) {
			$sections[] = $this->componentMessageBlock('Сообщение', $data['message']);
		}
		if (!empty($data['service_info']) && is_array($data['service_info'])) {
			$sections[] = $this->componentServiceInfo($data['service_info'], isset($data['page_url']) ? $data['page_url'] : '');
		}

		return $this->renderLayout($title, $sections, $options);
	}

	public function renderCustomerFormConfirmation($data, $options = array()) {
		$title = isset($data['subject']) ? $data['subject'] : 'Заявка принята';
		$dialog = isset($data['dialog_label']) ? $data['dialog_label'] : 'Обращение с сайта';

		$summary = array(
			array('label' => 'Тип обращения', 'value' => $dialog),
		);
		if (!empty($data['submitted_at'])) {
			$summary[] = array('label' => 'Дата', 'value' => $data['submitted_at']);
		}

		$sections = array(
			$this->componentSummaryCard('Спасибо за обращение', $summary),
			$this->componentMessageBlock(
				'Что дальше',
				isset($data['next_step'])
					? $data['next_step']
					: 'Мы получили вашу заявку и свяжемся с вами в ближайшее рабочее время.'
			),
		);

		if (!empty($data['cta_url']) && !empty($data['cta_label'])) {
			$sections[] = $this->componentButton($data['cta_label'], $data['cta_url']);
		}

		return $this->renderLayout($title, $sections, $options);
	}

	public function renderAccountMail($data, $options = array()) {
		$title = isset($data['title']) ? $data['title'] : 'Регистрация на сайте ' . $this->brand;

		$rows = array();
		if (!empty($data['customer_name'])) {
			$rows[] = array('label' => 'Имя', 'value' => $data['customer_name']);
		}
		if (!empty($data['login_url'])) {
			$rows[] = array('label' => 'Вход', 'value' => $data['login_url']);
		}

		$sections = array(
			$this->componentMessageBlock(
				'Добро пожаловать',
				isset($data['intro'])
					? $data['intro']
					: 'Ваш личный кабинет на сайте ' . $this->brand . ' успешно создан.'
			),
		);

		if ($rows) {
			$sections[] = $this->componentKeyValueTable('Данные аккаунта', $rows);
		}

		if (!empty($data['cta_url']) && !empty($data['cta_label'])) {
			$sections[] = $this->componentButton($data['cta_label'], $data['cta_url']);
		}

		return $this->renderLayout($title, $sections, $options);
	}

	public function renderOrderMail($data, $options = array()) {
		$title = isset($data['title']) ? $data['title'] : 'Заказ №' . (isset($data['order_id']) ? $data['order_id'] : '');

		$summary = array();
		if (!empty($data['order_id'])) {
			$summary[] = array('label' => 'Номер заказа', 'value' => '#' . $data['order_id']);
		}
		if (!empty($data['order_status'])) {
			$summary[] = array('label' => 'Статус', 'value' => $data['order_status']);
		}
		if (!empty($data['order_date'])) {
			$summary[] = array('label' => 'Дата', 'value' => $data['order_date']);
		}

		$sections = array();
		if ($summary) {
			$sections[] = $this->componentSummaryCard('Информация о заказе', $summary);
		}
		if (!empty($data['products']) && is_array($data['products'])) {
			$sections[] = $this->componentOrderTable($data['products'], isset($data['totals']) ? $data['totals'] : array());
		}
		if (!empty($data['message'])) {
			$sections[] = $this->componentMessageBlock('Комментарий', $data['message']);
		}
		if (!empty($data['cta_url']) && !empty($data['cta_label'])) {
			$sections[] = $this->componentButton($data['cta_label'], $data['cta_url']);
		}

		return $this->renderLayout($title, $sections, $options);
	}

	public function renderLayout($title, $sections, $options = array()) {
		$preheader = isset($options['preheader']) ? $options['preheader'] : $title;
		$body = $this->componentHeader();
		$body .= $this->componentTitle($title);
		foreach ($sections as $section) {
			$body .= $section;
		}
		$body .= $this->componentFooter();

		$html = $this->wrapDocument($title, $preheader, $body);
		$text = $this->textFromHtml($html);

		return array(
			'html' => $html,
			'text' => $text,
			'subject' => $title,
		);
	}

	public function textFromHtml($html) {
		$text = html_entity_decode(strip_tags(str_replace(array('<br>', '<br/>', '<br />', '</p>', '</tr>', '</li>'), "\n", $html)), ENT_QUOTES, 'UTF-8');
		$text = preg_replace("/\n{3,}/", "\n\n", $text);
		return trim($text);
	}

	private function escape($value) {
		return htmlspecialchars((string)$value, ENT_QUOTES, 'UTF-8');
	}

	private function wrapDocument($title, $preheader, $body) {
		$p = $this->palette;
		$brand = $this->escape($this->brand);
		$domain = $this->escape($this->domain);
		$safe_title = $this->escape($title);
		$safe_preheader = $this->escape($preheader);

		return '<!DOCTYPE html>'
			. '<html lang="ru">'
			. '<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">'
			. '<title>' . $safe_title . '</title></head>'
			. '<body style="margin:0;padding:0;background-color:' . $p['bg'] . ';font-family:Arial,Helvetica,sans-serif;color:' . $p['text'] . ';">'
			. '<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:transparent;">' . $safe_preheader . '</div>'
			. '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color:' . $p['bg'] . ';padding:24px 12px;">'
			. '<tr><td align="center">'
			. '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="600" style="max-width:600px;width:100%;background-color:' . $p['container'] . ';border:1px solid ' . $p['border'] . ';border-radius:8px;overflow:hidden;">'
			. '<tr><td style="padding:24px 28px;font-size:15px;line-height:1.55;color:' . $p['text'] . ';">'
			. $body
			. '</td></tr></table>'
			. '<p style="margin:16px 0 0;font-size:12px;line-height:1.4;color:' . $p['muted'] . ';text-align:center;">'
			. $brand . ' · ' . $domain . '</p>'
			. '</td></tr></table>'
			. '</body></html>';
	}

	private function componentHeader() {
		$p = $this->palette;
		$brand = $this->escape($this->brand);
		$domain = $this->escape($this->domain);

		return '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 20px;">'
			. '<tr><td style="padding-bottom:16px;border-bottom:2px solid ' . $p['accent'] . ';">'
			. '<div style="font-size:22px;font-weight:700;color:' . $p['accent'] . ';letter-spacing:0.02em;">' . $brand . '</div>'
			. '<div style="margin-top:4px;font-size:13px;color:' . $p['muted'] . ';">' . $domain . '</div>'
			. '</td></tr></table>';
	}

	private function componentTitle($title) {
		$p = $this->palette;
		return '<h1 style="margin:0 0 20px;font-size:20px;line-height:1.35;font-weight:700;color:' . $p['text'] . ';">'
			. $this->escape($title) . '</h1>';
	}

	private function componentSummaryCard($heading, $rows) {
		$p = $this->palette;
		$html = '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 16px;background-color:' . $p['bg'] . ';border:1px solid ' . $p['border'] . ';border-radius:6px;">'
			. '<tr><td style="padding:14px 16px;">'
			. '<div style="margin:0 0 10px;font-size:14px;font-weight:700;color:' . $p['text'] . ';">' . $this->escape($heading) . '</div>';

		foreach ($rows as $row) {
			$html .= '<div style="margin:0 0 6px;font-size:14px;line-height:1.45;">'
				. '<span style="color:' . $p['muted'] . ';">' . $this->escape($row['label']) . ':</span> '
				. '<span style="color:' . $p['text'] . ';font-weight:600;">' . $this->escape($row['value']) . '</span>'
				. '</div>';
		}

		$html .= '</td></tr></table>';
		return $html;
	}

	private function componentKeyValueTable($heading, $rows) {
		$p = $this->palette;
		$html = '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 16px;border-collapse:collapse;">'
			. '<tr><td colspan="2" style="padding:0 0 8px;font-size:14px;font-weight:700;color:' . $p['text'] . ';">' . $this->escape($heading) . '</td></tr>';

		foreach ($rows as $row) {
			$html .= '<tr>'
				. '<td style="padding:8px 10px 8px 0;width:38%;vertical-align:top;font-size:14px;color:' . $p['muted'] . ';border-top:1px solid ' . $p['border'] . ';">' . $this->escape($row['label']) . '</td>'
				. '<td style="padding:8px 0;vertical-align:top;font-size:14px;color:' . $p['text'] . ';font-weight:600;border-top:1px solid ' . $p['border'] . ';">' . $this->escape($row['value']) . '</td>'
				. '</tr>';
		}

		$html .= '</table>';
		return $html;
	}

	private function componentMessageBlock($heading, $message) {
		$p = $this->palette;
		$safe_message = nl2br($this->escape($message));

		return '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 16px;">'
			. '<tr><td style="padding:14px 16px;background-color:' . $p['container'] . ';border:1px solid ' . $p['border'] . ';border-radius:6px;">'
			. '<div style="margin:0 0 8px;font-size:14px;font-weight:700;color:' . $p['text'] . ';">' . $this->escape($heading) . '</div>'
			. '<div style="font-size:14px;line-height:1.55;color:' . $p['text'] . ';">' . $safe_message . '</div>'
			. '</td></tr></table>';
	}

	private function componentServiceInfo($service_info, $page_url = '') {
		$p = $this->palette;
		$rows = array();

		$map = array(
			'ip' => 'IP',
			'user_agent' => 'User-Agent',
			'referrer' => 'Referrer',
			'utm' => 'UTM',
			'city' => 'Город',
			'dialog' => 'Dialog ID',
			'submitted_at' => 'Отправлено',
		);

		foreach ($map as $key => $label) {
			if (!empty($service_info[$key])) {
				$rows[] = array('label' => $label, 'value' => $service_info[$key]);
			}
		}
		if ($page_url !== '') {
			$rows[] = array('label' => 'Страница', 'value' => $page_url);
		}

		if (!$rows) {
			return '';
		}

		$html = '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:16px 0 0;border-collapse:collapse;">'
			. '<tr><td colspan="2" style="padding:12px 0 8px;font-size:12px;font-weight:700;color:' . $p['muted'] . ';text-transform:uppercase;letter-spacing:0.04em;border-top:1px dashed ' . $p['border'] . ';">Служебная информация</td></tr>';

		foreach ($rows as $row) {
			$html .= '<tr>'
				. '<td style="padding:4px 10px 4px 0;width:32%;vertical-align:top;font-size:12px;color:' . $p['muted'] . ';">' . $this->escape($row['label']) . '</td>'
				. '<td style="padding:4px 0;vertical-align:top;font-size:12px;color:' . $p['muted'] . ';word-break:break-word;">' . $this->escape($row['value']) . '</td>'
				. '</tr>';
		}

		$html .= '</table>';
		return $html;
	}

	private function componentOrderTable($products, $totals = array()) {
		$p = $this->palette;
		$html = '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 16px;border-collapse:collapse;">'
			. '<tr>'
			. '<th align="left" style="padding:10px 8px;font-size:13px;color:' . $p['muted'] . ';border-bottom:2px solid ' . $p['border'] . ';">Товар</th>'
			. '<th align="center" style="padding:10px 8px;font-size:13px;color:' . $p['muted'] . ';border-bottom:2px solid ' . $p['border'] . ';">Кол-во</th>'
			. '<th align="right" style="padding:10px 8px;font-size:13px;color:' . $p['muted'] . ';border-bottom:2px solid ' . $p['border'] . ';">Сумма</th>'
			. '</tr>';

		foreach ($products as $product) {
			$name = isset($product['name']) ? $product['name'] : '';
			$qty = isset($product['quantity']) ? $product['quantity'] : '';
			$total = isset($product['total']) ? $product['total'] : '';
			$html .= '<tr>'
				. '<td style="padding:10px 8px;font-size:14px;color:' . $p['text'] . ';border-bottom:1px solid ' . $p['border'] . ';">' . $this->escape($name) . '</td>'
				. '<td align="center" style="padding:10px 8px;font-size:14px;color:' . $p['text'] . ';border-bottom:1px solid ' . $p['border'] . ';">' . $this->escape($qty) . '</td>'
				. '<td align="right" style="padding:10px 8px;font-size:14px;color:' . $p['text'] . ';border-bottom:1px solid ' . $p['border'] . ';">' . $this->escape($total) . '</td>'
				. '</tr>';
		}

		foreach ($totals as $total_row) {
			$label = isset($total_row['label']) ? $total_row['label'] : '';
			$value = isset($total_row['value']) ? $total_row['value'] : '';
			$html .= '<tr>'
				. '<td colspan="2" align="right" style="padding:8px;font-size:14px;color:' . $p['muted'] . ';">' . $this->escape($label) . '</td>'
				. '<td align="right" style="padding:8px;font-size:14px;font-weight:700;color:' . $p['text'] . ';">' . $this->escape($value) . '</td>'
				. '</tr>';
		}

		$html .= '</table>';
		return $html;
	}

	private function componentButton($label, $url) {
		$p = $this->palette;
		$safe_url = $this->escape($url);
		$safe_label = $this->escape($label);

		return '<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:8px 0 16px;">'
			. '<tr><td align="left" style="border-radius:6px;background-color:' . $p['accent'] . ';">'
			. '<a href="' . $safe_url . '" style="display:inline-block;padding:12px 20px;font-size:14px;font-weight:700;color:' . $p['accent_text'] . ';text-decoration:none;">'
			. $safe_label . '</a>'
			. '</td></tr></table>';
	}

	private function componentFooter() {
		$p = $this->palette;
		$year = date('Y');

		return '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top:20px;border-top:1px solid ' . $p['border'] . ';">'
			. '<tr><td style="padding-top:16px;font-size:12px;line-height:1.5;color:' . $p['muted'] . ';">'
			. 'Это автоматическое письмо с сайта ' . $this->escape($this->domain) . '. '
			. 'Если вы получили его по ошибке, просто проигнорируйте.'
			. '<br>© ' . $year . ' ' . $this->escape($this->brand) . '.'
			. '</td></tr></table>';
	}
}
