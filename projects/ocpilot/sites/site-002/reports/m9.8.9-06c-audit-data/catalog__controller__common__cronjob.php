<?php

ini_set('error_reporting', E_ALL);
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
ini_set('max_execution_time', '300');
ini_set('memory_limit', '512M');

class ControllerCommonCronjob extends Controller
{
    
	private $importsrc=0; //Источник импорта

	private $xml_ids = array();


	
	
	protected $time_start;


    public function index()
    {
		$this->time_start = microtime(true);
		$date = new DateTimeImmutable();
		echo $date->format(DateTimeInterface::RFC2822), "\n";


		
		$this->load->model('catalog/cronjob');

		$nextTasks = $this->model_catalog_cronjob->getTasks();

		if (!empty($nextTasks))
		{
			foreach ($nextTasks as $currentTask)
			{
				$itsOK = false;
				switch ($currentTask['command'])
				{
					case '1c':
						$this->importsrc=1; //Импорт из 1С
						echo $currentTask['name']."<br>";
						$itsOK = $this->parse1C();
						break;

					case '1c_offers':
						$this->importsrc=2; //Импорт из 1С
						echo $currentTask['name']."<br>";
						$itsOK = $this->parse1COffers();
						break;	
					
				};
				if ($itsOK)	
					{
						$this->model_catalog_cronjob->setDone($currentTask['id']);
						break;
					}

			}
		}
				

    }


	protected function parse1C()
	{
		include('import_1C.php');
		return $itsOK;

	}

	protected function parse1COffers()
	{
		include('import_1C_offers.php');
		return $itsOK;
	}


	

  protected function processProduct1C($product_id, $xml_item, $mode = 'insert') {	

    $special_attributes = [
        'a5502310-40de-11ee-8007-a85e4515c4f4' => 'weight', 
        '160c111b-7571-11ef-ae97-581122cf362c' => 'width',  
        '382aa5f0-7571-11ef-ae97-581122cf362c' => 'height', 
        '4aa05001-7571-11ef-ae97-581122cf362c' => 'length', 
        '8cdc00f1-e264-11e8-977e-60a44cac3e7c' => 'status', 
    ];
    
    include('import_1C_process.php');
		return $product_id;

	}

	
protected function translit($string) {
    $replace = [
        'а'=>'a','б'=>'b','в'=>'v','г'=>'g','д'=>'d','е'=>'e','ё'=>'e','ж'=>'zh','з'=>'z','и'=>'i','й'=>'y','к'=>'k','л'=>'l','м'=>'m','н'=>'n','о'=>'o','п'=>'p','р'=>'r','с'=>'s','т'=>'t','у'=>'u','ф'=>'f','х'=>'h','ц'=>'c','ч'=>'ch','ш'=>'sh','щ'=>'sch','ь'=>'','ы'=>'y','ъ'=>'','э'=>'e','ю'=>'yu','я'=>'ya'
    ];
    $str = mb_strtolower($string);
    $str = strtr($str, $replace);
    $str = preg_replace('/[^a-z0-9]/', '-', $str); // заменяем всё лишнее на дефис
    $str = preg_replace('/-+/', '-', $str);        // удаляем двойные дефисы
    return trim($str, '-');
  }



	

	protected function l($m, $die = false)
	{
		$this->log->write("Import: ".$m); 
		if ($die) die($m);
		else echo $m."<br>";
		
	}


	/**
 * Обрабатывает изображение (конвертация TIFF/CMYK, очистка метаданных)
 * * @param string $src_path Относительный путь к картинке из XML
 * @return string Относительный путь к сохраненному файлу для БД OpenCart или пустая строка
 */
protected function processImage1C($src_path) {
    $src = preg_replace('/\s+/', '', (string)$src_path);
    if (!$src) {
        return '';
    }

    $dest = 'catalog/1c_import/' . basename($src);
	
	// Меняем расширение на .jpg в целевом пути, так как Imagick всё равно конвертирует в jpeg
	$dest = preg_replace('/\.(tiff|tif|png|bmp|webp)$/i', '.jpg', $dest);
    $source_file = DIR_ROOT . '1c_incoming/webdata/' . $src;
	$final_file = DIR_IMAGE . $dest;

	if (file_exists($final_file)) {
        return $dest;
    }

    if (!file_exists($source_file)) {
        return '';
    }

    if (!is_dir(DIR_IMAGE . 'catalog/1c_import/')) {
        mkdir(DIR_IMAGE . 'catalog/1c_import/', 0755, true);
    }

    if (extension_loaded('imagick')) {
        try {
            $im = new Imagick();
            // [0] — берем только первую страницу/слой, если это многослойный TIFF
            $im->readImage($source_file . '[0]'); 

            // 1. Убираем альфа-канал и заменяем его белым цветом (исправление черного фона)
            if ($im->getImageAlphaChannel()) {
                $im->setImageBackgroundColor('white');
                $im->setImageAlphaChannel(Imagick::ALPHACHANNEL_REMOVE);
                $im->mergeImageLayers(Imagick::LAYERMETHOD_FLATTEN);
            }

            // 2. Принудительно переводим в sRGB (если был CMYK)
            if ($im->getImageColorspace() == Imagick::COLORSPACE_CMYK) {
                $im->transformImageColorspace(Imagick::COLORSPACE_SRGB);
            }

            // 3. Устанавливаем формат и качество
            $im->setImageFormat('jpeg');
            $im->setImageCompressionQuality(80);
            $im->stripImage(); // Удаляем профили и XML-мусор

            // 4. Записываем файл
            $im->writeImage(DIR_IMAGE . $dest);
            
            $im->clear();
            $im->destroy();
            
            chmod(DIR_IMAGE . $dest, 0644);
            return $dest;
            
        } catch (Exception $e) {
            // Если Imagick упал, пытаемся просто скопировать файл как есть
            if (copy($source_file, DIR_IMAGE . $dest)) {
                chmod(DIR_IMAGE . $dest, 0644);
                return $dest;
            }
        }
    } else {
        // Если Imagick не установлен, просто копируем
        if (copy($source_file, DIR_IMAGE . $dest)) {
            chmod(DIR_IMAGE . $dest, 0644);
            return $dest;
        }
    }

    return '';
}













}
