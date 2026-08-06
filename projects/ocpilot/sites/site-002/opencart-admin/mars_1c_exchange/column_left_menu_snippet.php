<?php
// Insert inside admin/controller/common/column_left.php system menu children, near tools:
// Requires access permission tool/mars_1c_exchange.
if ($this->user->hasPermission('access', 'tool/mars_1c_exchange')) {
    $system[] = array(
        'name'     => 'Обмен с 1С',
        'href'     => $this->url->link('tool/mars_1c_exchange', 'user_token=' . $this->session->data['user_token'], true),
        'children' => array()
    );
}
