<?php
// 1. Включаем отображение всех ошибок
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Увеличиваем лимиты
set_time_limit(0);
ini_set('memory_limit', '512M');

require_once('config.php');
require_once(DIR_SYSTEM . 'startup.php');

$registry = new Registry();
$db = new DB(DB_DRIVER, DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_PORT);
$registry->set('db', $db);

// Инициализируем конфиг (обязательно для DB_PREFIX)
$config = new Config();
$registry->set('config', $config);

require_once(DIR_SYSTEM . 'engine/model.php');

// Пробуем подключить модель из админки (так как мы туда писали метод refreshPriceIndex)
// В OpenCart DIR_STORAGE или DIR_APPLICATION могут запутать, поэтому укажем от корня:
$admin_model_path = __DIR__ . '/admin/model/catalog/product.php';

if (file_exists($admin_model_path)) {
    require_once($admin_model_path);
} else {
    // Если вдруг файла нет в админке, пробуем в каталоге
    $catalog_model_path = __DIR__ . '/catalog/model/catalog/product.php';
    if (file_exists($catalog_model_path)) {
        require_once($catalog_model_path);
    } else {
        die("Error: Could not find product model in admin or catalog folder.\n");
    }
}

$model = new ModelCatalogProduct($registry);

if (!method_exists($model, 'refreshPriceIndex')) {
    die("Error: Method refreshPriceIndex not found in ModelCatalogProduct. Check admin/model/catalog/product.php\n");
}

$products = $db->query("SELECT product_id FROM " . DB_PREFIX . "product")->rows;
echo "Total products found: " . count($products) . "\n";

foreach ($products as $product) {
    echo "Processing ID: " . $product['product_id'] . "... ";
    
    // Вызываем метод
    $model->refreshPriceIndex($product['product_id']);
    
    echo "OK\n";
    
    // Чтобы не вешать сервер при выводе в браузер
    flush(); 
}

echo "--- All Done ---";