<?
if(!function_exists('get_field')) {
	require_once $_SERVER['DOCUMENT_ROOT'] . '/wp-load.php';?>
	<link rel='stylesheet' id='iseoblog-style-css' href='/wp-content/themes/iseoblog/style.css' media='all' />
	<script id="iseoblog-jquery-js" src="/libs/jquery/jquery-3.7.1.min.js?ver=1750871516"></script>
<?}
$calc_id = 1734;
$tariffs = "[";
foreach(get_field('tariffs', $calc_id) as $i => $item) {
	$tariffs .= ($i ? ', ' : '') . '{ title: "' . $item['title'] . '", cost: "' . $item['cost'] . '", seo: "' . $item['limit_seo'] . '", dev: "' . $item['limit_dev'] . '", links: "' . $item['limit_links'] . '", content: "' . $item['limit_content'] . '", hits: 0, growth: "' . $item['growth_factor'] . '" }';
}
$tariffs .= "]";
$dots = '[{ month: "0", basic_grow: "0", full_grow: "0", traffic: "", leads: "", sales: "", income:"", roi:"", calc_cost:"" }, ';
foreach(get_field('effect', $calc_id) as $i => $item) {
	$dots .= ($i ? ', ' : '') . '{ month: "' . ($i+1) . '", pess: "' . $item['koeff_pess'] . '", base: "' . $item['koeff_base'] . '", opti: "' . $item['koeff_opti'] . '" }';
}
$dots .= "]";
?>
<div class="tariff-calc-wrap">
	<div class="tariff-calc-lead">
		<p>Рассчитайте ориентировочный бюджет SEO-продвижения и прогноз результата для вашего проекта.</p>
	</div>

	<div class="tariff-calc-box tariff-calc-card">
		<div class="tariff-calc-item">
			<label>Ниша</label>
			<select id="k_niche" name="k_niche">
				<?foreach(get_field('k_niche', $calc_id) as $i => $option) { ?>
				<option value="<?=$option['value']?>"<?=$i ? '' : ' selected=""'?>><?=$option['name']?></option>
				<? } ?>
			</select>
		</div>

		<div class="tariff-calc-item">
			<label>Тип сайта</label>
			<select id="k_site" name="k_site">
				<?foreach(get_field('k_site', $calc_id) as $i => $option) { ?>
				<option value="<?=$option['value']?>" data-override="<?=$option['override'] ? 1 : 0?>" data-conv="<?=$option['conv']?>" data-close="<?=$option['close_rate']?>"<?=$i ? '' : ' selected=""'?>><?=$option['name']?></option>
				<? } ?>
			</select>
		</div>

		<div class="tariff-calc-item">
			<label>Регион / город</label>
			<select id="k_city" name="k_city">
				<?foreach(get_field('k_city', $calc_id) as $i => $option) { ?>
				<option value="<?=$option['value']?>"<?=$i ? '' : ' selected=""'?>><?=$option['name']?></option>
				<? } ?>
			</select>
		</div>

		<div class="tariff-calc-item">
			<label>Конкуренция</label>
			<select id="k_comp" name="k_comp">
				<?foreach(get_field('k_comp', $calc_id) as $i => $option) { ?>
				<option value="<?=$option['value']?>" data-growth="<?=$option['growth']?>" data-override="<?=$option['override'] ? 1 : 0?>"<?=$i ? '' : ' selected=""'?>><?=$option['name']?></option>
				<? } ?>
			</select>
		</div>

		<div class="tariff-calc-item">
			<label>Текущий органический трафик</label>
			<input type="text" id="traffic" name="traffic" value="2000">
		</div>

		<div class="tariff-calc-item">
			<label>Конверсия (%)</label>
			<input type="text" id="cvr" name="cvr" value="<?=str_replace('.', ',', get_field('k_site', $calc_id)[0]['conv'])?>">
		</div>

		<div class="tariff-calc-item">
			<label>Средний чек (₽)<span>средняя сумма одной продажи с сайта</span></label>
			<input type="text" id="avg_check" name="avg_check" value="15000">
		</div>

		<div class="tariff-calc-item">
			<label>Возраст домена (лет)</label>
			<input type="text" id="domain_age" name="domain_age" value="4">
		</div>

		<div class="tariff-calc-item">
			<label>Часы SEO-специалиста в месяц</label>
			<input type="text" id="seo_hours" name="seo_hours" value="30">
		</div>

		<div class="tariff-calc-item">
			<label>Часы программиста в месяц</label>
			<input type="text" id="dev_hours" name="dev_hours" value="10">
		</div>

		<div class="tariff-calc-item">
			<label>Бюджет на ссылки (₽/мес)</label>
			<input type="text" id="links_budget" name="links_budget" value="7000">
		</div>

		<div class="tariff-calc-item">
			<label>Объём контента (тысяч символов в месяц)</label>
			<input type="text" id="content_chars" name="content_chars" value="40">
		</div>

		<div class="tariff-calc-item tariff-calc-item--scenario">
			<label>Сценарий прогноза</label>
			<select id="scenario" name="scenario">
				<option value="pess" selected data-word="пессимистичного">Пессимистичный</option>
				<option value="base" data-word="базового">Базовый</option>
				<option value="opti" data-word="оптимистичного">Оптимистичный</option>
			</select>
		</div>

		<div class="tariff-calc-bottom">
			<div class="tariff-calc-submit btn">Рассчитать</div>

			<div class="tariff-calc-result hidden">
				<div class="tariff-calc-result__badge">Рекомендуемый тариф</div>
				<p class="tariff-calc-result__tariff">
					<span class="tariff-calc-final-tarif"></span>
				</p>
				<p class="tariff-calc-result__price">
					<span class="tariff-calc-final-cost"></span> ₽/мес
				</p>
			</div>
		</div>
	</div>

	<div class="tariff-calc-output">
		<div class="tariff-calc-output__main">
			<div class="tariff-calc-forecast"></div>

			<div class="tariff-calc-includes">
				<div class="tariff-calc-includes__title">Что входит в расчёт</div>
				<div class="tariff-calc-includes__grid">
					<div>SEO-специалист</div>
					<div>Разработка</div>
					<div>Ссылочное продвижение</div>
					<div>Контент</div>
				</div>
			</div>
		</div>

		<div class="tariff-calc-output__request">
			<form class="tariff-calc-request" id="callback__FORM_tariff_calc" name="callback__FORM_tariff_calc" action="#" method="post">
				<div class="tariff-calc-request__title">Получите персональный план продвижения</div>
				<div class="tariff-calc-request__text">
					Оставьте контакты — разберём расчёт, проверим нишу и предложим план SEO-продвижения.
				</div>

				<div class="tariff-calc-request__fields">
					<input type="text" id="tariff_calc_cf_name" name="cf_name" placeholder="Ваше имя" required>
					<input type="tel" id="tariff_calc_cf_phone" name="cf_phone" placeholder="Телефон" required>
				</div>
				<input type="hidden" name="cf_contact" value="Телефон">
				<input type="hidden" name="cf_site" value="не указан">

				<div class="tariff-calc-request__agree personal-data-consent-wrap">
					<div class="checkbox-border">
						<input type="checkbox" class="required-checkbox personal-data-consent" id="personal_data_consent_callback__FORM_tariff_calc" name="personal_data_consent" value="1">
					</div>
					<label for="personal_data_consent_callback__FORM_tariff_calc">Я&nbsp;соглашаюсь с&nbsp;<a href="/privacy-policy.html" target="_blank">политикой конфиденциальности</a> и даю согласие на&nbsp;обработку персональных данных</label>
				</div>

				<button type="button" id="callback__FORM_tariff_calc_send" class="tariff-calc-request__btn" data-root="y">Получить план продвижения</button>
			</form>
		</div>
	</div>

	<div class="tariff-calc-chart tariff-calc-chart-box">
		<div class="tariff-calc-chart__title">Прогноз роста показателей</div>

		<div class="tariff-calc-chart">
			<canvas id="calcChart"></canvas>
		</div>

		<div class="tariff-calc-table"></div>
	</div>
</div>

<script src="<?=get_template_directory_uri() . '/js/chart.js'?>"></script>
<script>
(function ($) {
	$(document).ready(function($) {
		$('#k_site').change(function(){
			var conv = $(this).find('option:selected').attr('data-conv');
			$('#cvr').val(conv.replace(/\./g, ','));
		});

		$('.tariff-calc-submit').click(function(){
			var k_niche = $('#k_niche').val();
			var k_site = $('#k_site').val();
			var k_city = $('#k_city').val();
			var k_comp = $('#k_comp').val();
			var traffic = prepareInput($('#traffic').val());
			var cvr = prepareInput($('#cvr').val());
			if(!cvr) cvr = $('#k_site option:selected').attr('data-conv');
			var close_rate = $('#k_site option:selected').attr('data-close');
			var avg_check = prepareInput($('#avg_check').val());
			var domain_age = prepareInput($('#domain_age').val());
			var seo_hours = prepareInput($('#seo_hours').val());
			var dev_hours = prepareInput($('#dev_hours').val());
			var links_budget = prepareInput($('#links_budget').val());
			var content_chars = prepareInput($('#content_chars').val());
			const seo_rate = <?=get_field('seo_rate', $calc_id)?>;
			const dev_rate = <?=get_field('dev_rate', $calc_id)?>;
			const text_rate = <?=get_field('text_rate', $calc_id)?>;
			const tariffs = <?=$tariffs?>;
			const tarif_uplift_max = <?=get_field('tarif_uplift_max', $calc_id)?>;
			const round_step = <?=get_field('round_step', $calc_id)?>;
			var scenario = $('#scenario').val();
			var comp_growth = prepareInput($('#k_comp option:selected').attr('data-growth'));
			var dots = <?=$dots?>;

			console.log('----- Новый расчет ----');
			var base = (seo_hours * seo_rate) + (dev_hours * dev_rate) + links_budget + ((content_chars / 1000) * text_rate);
			console.log('Базовая стоимость: ', base);
			var k_total = k_niche * k_site * k_city * k_comp;
			console.log('Суммарный коэффициент: ', k_total);
			var rawCost = base * k_total;
			console.log('Сырая стоимость: ', rawCost);
			var tariffPrice = 0;
			var tariffChoice = "только индивидуальное предложение";
			var tariffGrowth = 1;
			for (var i = 0; i < tariffs.length; i++) {
				if(rawCost < (prepareInput(tariffs[i]['cost']) * tarif_uplift_max)) {
					tariffChoice = tariffs[i]['title'];
					tariffGrowth = tariffs[i]['growth'];
					tariffPrice = tariffs[i]['cost'];
					if(i == 0 && ($('#k_site').find('option:selected').attr('data-override') == 1 || $('#k_comp').find('option:selected').attr('data-override') == 1 || traffic > 30000)) {
						console.log('Произошла перезапись младшего тарифа: ', $('#k_site').find('option:selected').text(), $('#k_comp').find('option:selected').text(), traffic);
						tariffChoice = tariffs[1]['title'];
						tariffGrowth = tariffs[1]['growth'];
						tariffPrice = tariffs[1]['cost'];
					}
					break;
				}				
			}

			console.log('Проверяем попадания в диапазоны тарифов:');

			var params = [{key: "seo", value: seo_hours, tarif: 0}, {key: "dev", value: dev_hours, tarif: 0}, {key: "links", value: links_budget, tarif: 0}, {key: "content", value: content_chars, tarif: 0}];
			for(var i = 0; i <params.length; i++ ) {
				var hit = false;
				for (var j = 0; j < tariffs.length; j++) {
					if(params[i]['value'] <= tariffs[j][params[i]['key']] || !tariffs[j][params[i]['key']]) {
						hit = j;
						break;
					}
				}
				if(hit !== false) {
					params[i]['tarif'] = hit;
					console.log('Для параметра ' + params[i]['key'] + ' выбран тариф', tariffs[hit]['title']);
					tariffs[hit]['hits']++;
				} else {
					alert('Ошибка конфигрурации тарифов');
				}
			}
			console.log('Количество попаданий в диапазоны тарифов:');
			var found = false;
			for (var j = 0; j < tariffs.length; j++) {
				console.log(tariffs[j]['title'] + ': ' + tariffs[j]['hits']);
				if (tariffs[j]['hits'] >= 3) {
					found = j;
				}
			}
			if (found === false) {
				console.log('Трех попаданий в один тариф не произошло.');
				console.log('Возвращаемся к сырой стоимости.');
				if (tariffPrice) {
					var minPrice = tariffPrice;
					var maxPrice = tariffPrice * tarif_uplift_max;
					console.log('Выбранный тариф: ', tariffChoice);
					console.log('Стоимость тарифа: ', minPrice);
					console.log('Стоимость тарифа с запасом: ', maxPrice);
					var finalPrice = clamp(rawCost, minPrice, maxPrice);
					finalPrice = Math.round(finalPrice / round_step) * round_step;
					console.log('Финальная стоимость: ', finalPrice);
				} else {
					var finalPrice = Math.round(rawCost / round_step) * round_step;
					tariffChoice = tariffs[tariffs.length-1]['title'];
					tariffGrowth = tariffs[tariffs.length-1]['growth'];
					console.log('Сырая стоиомость больше стоимости максимального тарифа с запасом. Выбираем максимальный тариф. ');
					console.log('Выбранный тариф: ', tariffChoice);
					console.log('Финальная стоимость: ', finalPrice);
				}
			} else {
				tariffChoice = tariffs[found]['title'];
				tariffGrowth = tariffs[found]['growth'];
				console.log('Три попадания для тарифа ' + tariffChoice + '!');
				console.log('Выбранный тариф: ', tariffChoice);
				tariffPrice = tariffs[found]['cost'];
				var maxPrice = tariffPrice * tarif_uplift_max;
				console.log('Стоимость тарифа: ', tariffPrice);
				console.log('Стоимость тарифа с запасом: ', maxPrice);
				var extra = 0;
				var append = 0;
				for(var i = 0; i <params.length; i++ ) {
					if(params[i]['tarif'] > found) {
						if (params[i]['key'] == 'seo') {
							append = (params[i]['value'] - tariffs[found]['seo']) * seo_rate;
							console.log('Добавочная стоимость для ' + params[i]['key'] + ':', append);
							extra += append;
						}
						if (params[i]['key'] == 'dev') {
							append = (params[i]['value'] - tariffs[found]['dev']) * dev_rate;
							console.log('Добавочная стоимость для ' + params[i]['key'] + ':', append);
							extra += append;
						}
						if (params[i]['key'] == 'links') {
							append = params[i]['value'] - tariffs[found]['links'];
							console.log('Добавочная стоимость для ' + params[i]['key'] + ':', append);
							extra += append;
						}
						if (params[i]['key'] == 'content') {
							append = (params[i]['value'] - tariffs[found]['content']) * text_rate;
							console.log('Добавочная стоимость для ' + params[i]['key'] + ':', append);
							extra += append;
						}
					}
				}
				if(!extra) {
					console.log('Добавочных стоимостей нет.');
				}			
				var finalPrice = Math.round((parseFloat(tariffPrice) + parseFloat(extra)) / round_step) * round_step;
				console.log('Промежуточная стоимость: ', finalPrice);
				var postPrice = 0;
				for (var j = found; j < tariffs.length; j++) {
					if(j < (tariffs.length-1)) {
						if(finalPrice > maxPrice) {
							postPrice = tariffs[j]['cost'];
							maxPrice = postPrice * tarif_uplift_max;
							tariffChoice = tariffs[j]['title'];
							tariffGrowth = tariffs[j]['growth'];
							console.log('Повышаем до тарифа', tariffChoice);
						} 
					} else {
						if(finalPrice > maxPrice) {
							postPrice = finalPrice;
							tariffChoice = tariffs[j]['title'];
							tariffGrowth = tariffs[j]['growth'];
							console.log('Повышаем до тарифа', tariffChoice);
						}
					}
				}
				if(postPrice) {
					finalPrice = Math.round(postPrice / round_step) * round_step;
					console.log('Финальная стоимость: ', finalPrice);
				} else {
					console.log('Повышения тарифа не требуются.');
					console.log('Финальная стоимость: ', finalPrice);
	
				}
			}


			dots[0]['traffic'] = traffic;
			dots[0]['leads'] = dots[0]['traffic'] * (cvr / 100);
			dots[0]['sales'] = dots[0]['leads'] * (close_rate / 100);
			dots[0]['income'] = dots[0]['sales'] * avg_check;
			dots[0]['roi'] = finalPrice ? ((dots[0]['income'] - finalPrice) / finalPrice) : 0;
			dots[0]['calc_cost'] = dots[0]['income'];

			
			var domain_growth = 0.8;
			if(domain_age > 1) domain_growth = 0.9;
			if(domain_age > 3) domain_growth = 1;
			if(domain_age > 7) domain_growth = 1.05;
			var traffic_growth = 1.15;
			if(traffic > 1000) traffic_growth = 1;
			if(traffic > 5000) traffic_growth = 0.85;
			if(traffic > 30000) traffic_growth = 0.7;
			var growth_factor_total = Math.min(1.2, (tariffGrowth * comp_growth * domain_growth * traffic_growth)); 

			var trafficData = [ traffic ];
			var leadsData = [ dots[0]['leads'] ];
			var incomeData = [ dots[0]['income'] ];
			var roiData = [ dots[0]['roi']*100 ];
			var cumulativeData = [ dots[0]['income'] ];
			var volatility = 0.5;
			for(var i=1; i<=12; i++) {
//				if(i == 2) volatility = 0.2;
//				if(i == 3) volatility = 0.5;
				dots[i]['month'] = i;
				dots[i]['basic_grow'] = dots[i][scenario] / 100;
				dots[i]['full_grow'] = Math.min(0.12, Math.max(0.001, dots[i]['basic_grow'] * growth_factor_total));
				dots[i]['traffic'] = dots[i-1]['traffic'] * (1 + dots[i]['full_grow']);
//				dots[i]['traffic'] = dots[i]['traffic'] + ((dots[i]['traffic'] - dots[i-1]['traffic']) * 0.4 * (Math.random() - volatility));
				dots[i]['leads'] = dots[i]['traffic'] * (cvr / 100);
				dots[i]['sales'] = dots[i]['leads'] * (close_rate / 100);
				dots[i]['income'] = dots[i]['sales'] * avg_check;
				dots[i]['roi'] = finalPrice ? ((dots[i]['income'] - finalPrice) / finalPrice) : 0;
				dots[i]['calc_cost'] = dots[i]['income'] + dots[i-1]['calc_cost'];
				trafficData.push(Math.round(dots[i]['traffic']));
				leadsData.push(Math.round(dots[i]['leads']));
				incomeData.push(Math.round(dots[i]['income']));
				roiData.push(digits(dots[i]['roi']*100, 10));
				cumulativeData.push(Math.round(dots[i]['calc_cost']));
			}

			var table =	`<table><thead><tr>
				<td>Месяц</td>
				<td>Базовый рост</td>
				<td>Итоговый рост</td>
				<td>Трафик</td>
				<td>Лиды</td>
				<td>Продажи</td>
				<td>Выручка</td>
				<td>ROI</td>
				<td>Накопленная выручка</td>
			</tr></thead><tbody>`;

			for(var i=0; i<=12; i++) {
			table += `<tr>
				<td>`+dots[i]['month']+`</td>
				<td>`+digits(dots[i]['basic_grow']*100, 10)+`</td>
				<td>`+digits(dots[i]['full_grow']*100, 10)+`</td>
				<td>`+Math.round(dots[i]['traffic'])+`</td>
				<td>`+Math.round(dots[i]['leads'])+`</td>
				<td>`+Math.round(dots[i]['sales'])+`</td>
				<td>`+Math.round(dots[i]['income'])+`</td>
				<td>`+digits(dots[i]['roi']*100, 10)+`</td>
				<td>`+Math.round(dots[i]['calc_cost'])+`</td>
			</tr>`;
			}
			
			table += '</tbody></table>';

			forecast = "<p>Накопленная выручка за 12 месяцев: <span>" + Math.round(dots[12]['calc_cost']).toLocaleString('ru-RU').replace(/\s/g, '\xA0') + "</span>&nbsp;₽ (для " + $('#scenario option:selected').attr('data-word') + " сценария)</p>";

			$('.tariff-calc-final-cost').text(finalPrice.toLocaleString('ru-RU').replace(/\s/g, '\xA0'));			
			$('.tariff-calc-final-tarif').text(tariffChoice);			
			$('.tariff-calc-result').removeClass('hidden');
			$('.tariff-calc-forecast').html(forecast);
			$('.tariff-calc-table').html(table);

			const ctx = document.getElementById('calcChart').getContext('2d');
			if (typeof myChart !== 'undefined' && myChart !== null) {
				myChart.destroy();
			}
			myChart = new Chart(ctx, {
				type: 'line',
				data: {
					labels: ['1 месяц', '2 месяц', '3 месяц', '4 месяц', '5 месяц', '6 месяц', '7 месяц', '8 месяц', '9 месяц', '10 месяц', '11 месяц', '12 месяц'],
					datasets: [
						{
							label: 'Условный рост SEO-трафика',
							data: trafficData,
							backgroundColor: '#fa4b15',
							borderColor: '#fa4b15',
							borderWidth: 2,
							yAxisID: 'y1',
							tension: 0.5 
					    },
						{
							label: 'Прогноз лидов',
							data: leadsData,
							backgroundColor: '#fa1582',
							borderColor: '#fa1582',
							borderWidth: 2,
							yAxisID: 'y2',
							tension: 0.5 
					    },
						{
							label: 'Условная выручка',
							data: incomeData,
							backgroundColor: '#15e6fa',
							borderColor: '#15e6fa',
							borderWidth: 2,
							yAxisID: 'y3',
							tension: 0.5 
					    },
						{
							label: 'ROI',
							data: roiData,
							backgroundColor: '#a815fa',
							borderColor: '#a815fa',
							borderWidth: 2,
							yAxisID: 'y4',
							tension: 0.5 
					    },
						{
							label: 'Накопленная выручка',
							data: cumulativeData,
							backgroundColor: '#facc15',
							borderColor: '#facc15',
							borderWidth: 4,
							yAxisID: 'y5',
							tension: 0.5 
					    },
				  	],
				},
				options: {
					responsive: true,
					maintainAspectRatio: false,
					scales: {
						x: {
							border: {
								color: '#ffffff',
							},
							grid: {
			                    display: false
							}
						},
			            y1: {
			                type: 'linear',
							beginAtZero: true,
			                grid: {
			                    display: false
			                },
							border: {
								color: '#ffffff',
							},
							ticks: {
								display: false
							},
			            },
			            y2: {
			                type: 'linear',
							beginAtZero: true,
			                grid: {
			                    display: false
			                },
							border: {
								display: false
							},
							ticks: {
								display: false
							},
			            },
			            y3: {
			                type: 'linear',
							beginAtZero: true,
			                grid: {
			                    display: false
			                },
							border: {
								display: false
							},
							ticks: {
								display: false
							},
			            },
			            y4: {
			                type: 'linear',
							beginAtZero: true,
			                grid: {
			                    display: false
			                },
							border: {
								display: false
							},
							ticks: {
								display: false
							},
			            },
			            y5: {
			                type: 'linear',
							beginAtZero: true,
			                grid: {
			                    display: false
			                },
							border: {
								display: false
							},
							ticks: {
								display: false
							},
			            },
					},
					plugins: {
			            legend: {
			                labels: {
			                    color: 'white',
								font: {
									size: 16
								},
								padding: 40
			                }
			            }
		            }
				},
			});
		});	
	});	

	function prepareInput (val) {
		var result = parseFloat(val.replace(/,/g, '.'));
		if (Number.isNaN(result)) {
			result = 0;
		}
		if (result < 0) {
			result = 0;
		}
		return result;
	}

	function digits (val, treshold) {   	
		return Math.round(val * treshold) / treshold;
	}

	const clamp = (num, min, max) => Math.min(max, Math.max(min, num));

})(jQuery);
</script>
<style>
#scenario {
	font-weight:bold;
}
</style>
