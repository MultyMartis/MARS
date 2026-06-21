<?php

//$offers_directory = DIR_ROOT . '1c_exchange/';

$offers_directory = DIR_ROOT . '1c_incoming/webdata/'; 
$files = glob($offers_directory . 'offers0_*.xml');

if (empty($files)) {
    echo "Файлы предложений (цены/остатки) не найдены.";
    return false;
}

sort($files); 

$existing_products = [];
$query = $this->db->query("SELECT product_id, xml_id FROM " . DB_PREFIX . "product WHERE xml_id IS NOT NULL AND xml_id <> ''");
foreach ($query->rows as $row) {
    $existing_products[$row['xml_id']] = $row['product_id'];
}

foreach ($files as $file) {
    echo "<b>Обработка цен и остатков из файла: " . basename($file) . "</b><br>";

    $xml = simplexml_load_file($file);
    if (!$xml) continue;


    if (isset($xml->ПакетПредложений->Предложения->Предложение)) {
        
        foreach ($xml->ПакетПредложений->Предложения->Предложение as $offer) {
            $xml_id = (string)$offer->Ид;

          
            if (!isset($existing_products[$xml_id])) {
                continue;
            }

            $product_id = $existing_products[$xml_id];        
            $quantity = isset($offer->Количество) ? (int)$offer->Количество : 0;          
            $price = 0;
            if (isset($offer->Цены->Цена)) {
     
                $price = (float)$offer->Цены->Цена[0]->ЦенаЗаЕдиницу;
            }


            $this->db->query("UPDATE " . DB_PREFIX . "product SET 
                quantity = '" . (int)$quantity . "', 
                price = '" . (float)$price . "' 
                WHERE product_id = '" . (int)$product_id . "'");

            echo "Товар ID {$product_id}: обновлена цена ({$price} руб.) и остаток ({$quantity} шт.)<br>";
        }
    }


    unset($xml);
    gc_collect_cycles();
    
    echo "<b>Файл " . basename($file) . " обработан.</b><br><br>";
    // rename($file, $file . '.bak'); 
}


$itsOK = true;