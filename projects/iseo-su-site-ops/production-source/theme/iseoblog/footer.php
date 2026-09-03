<?php
/**
 * The template for displaying the footer
 *
 * Contains the closing of the #content div and all content after.
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package iseoblog
 */

?>

				<!-- --- -->

				<div class="content_block">
					<div class="content_block__title">
						<h3>Наш Telegram-канал</h3>
					</div>

					<div class="two_common_col">
						<div class="two_common_col__personal">
							<div class="two_common_col__personal_wrap">
								<img src="/img/ico_tg.svg" alt="Telegram">
							</div>
						</div>
						<div class="two_common_col__info">
							<div class="two_common_col__title">Присоединяйтесь к&nbsp;нашему Telegram-каналу. Теперь вы&nbsp;можете читать последние новости из&nbsp;мира интернет-маркетинга прямо в&nbsp;мессенджере</div>
							<a href="https://t.me/DMarketingIseo" target="_blank">Подписаться</a>
						</div>
					</div>

				</div>

				<!-- --- -->


				<!-- --- -->

				<div class="content_block">
					<div class="content_block__title">
						<h3>Бесплатный аудит</h3>
					</div>

					<div class="free_audit">
						
						<div class="free_audit__personal">
							<div class="free_audit__personal_wrap">
								<img src="/img/team_01.png" alt="Никита Шваков">
								<div class="free_audit__personal_name">
									<div>Никита Шваков</div>
									<span>Основатель INTLSEO</span>
								</div>
							</div>
							<div class="free_audit__personal_btns">
								<a href="https://t.me/niki1man">Telegram</a>
								<a href="https://api.whatsapp.com/send/?phone=79523014663">WhatsApp</a>
							</div>
						</div>

						<div class="free_audit__FORM_info">
							<div class="free_audit__form__title">Заполните форму или напишите в&nbsp;удобный мессенджер</div>
							<form id="page__FORM_info" name="page__FORM_info" action="#" method="post">
								<div>									
									<input type="text" id="pf_name" name="pf_name" placeholder="Ваше имя" required>
									<!-- <label for="name">Ваше имя</label> -->
								</div>
			<div>									
				<select id="pf_contact" class="contact_select" name="pf_contact" required>
					<option selected disabled>Выберите способ связи:</option>
					<option value="Телефон">Телефон</option>
					<option value="Telegram">Telegram</option>
					<option value="WhatsApp">WhatsApp</option>
				</select>
			</div>
								<div>									
									<input type="tel" id="pf_phone" name="pf_phone" placeholder="Телефон" required>
									<!-- <label for="contact">WhatsApp / Telegram</label> -->
								</div>
								<div>									
									<input type="text" id="pf_site" name="pf_site" placeholder="Адрес сайта">
									<!-- <label for="site">Адрес сайта</label> -->
								</div>
								<div>	
									<textarea id="pf_comment" name="pf_comment" placeholder="Комментарий"></textarea>
									<!-- <label for="comment">Комментарий</label> -->
								</div>
								<div class="form_agree__wrap personal-data-consent-wrap">
				<div class="checkbox-border">
	              <input type="checkbox" class="required-checkbox personal-data-consent" id="personal_data_consent_page__FORM_info" name="personal_data_consent" value="1" required>
				</div>
              <label for="personal_data_consent_page__FORM_info">Я&nbsp;соглашаюсь с&nbsp;<a href="/privacy-policy.html" target="_blank">политикой конфиденциальности</a> и даю согласие на&nbsp;обработку персональных данных</label>
            </div>
								<button id="page__FORM_send_info" type="submit">Отправить</button>
							</form>
						</div>
					</div>

				</div>

				<!-- --- -->

			</div>
		</div>
	</main>

<?include_once get_template_directory() . "/template-parts/content-footer.php";?>

	<div class="page_overlay"></div>

	<div id="callback__FORM_popup" class="popup__FORM_wrap">
		<div class="callback_form__title">Мы перезвоним вам</div>
		<div class="callback_form__description">Заполните форму обратной связи и&nbsp;мы&nbsp;свяжемся с&nbsp;вами</div>
		<form id="callback__FORM_info" name="callback__FORM_info" action="#" method="post">
			<div>									
				<input type="text" id="cf_name" name="cf_name" placeholder="Ваше имя" required>
				<!-- <label for="name">Ваше имя</label> -->
			</div>
			<div>									
				<select id="сf_contact" class="contact_select" name="сf_contact" required>
					<option selected disabled>Выберите способ связи:</option>
					<option value="Телефон">Телефон</option>
					<option value="Telegram">Telegram</option>
					<option value="WhatsApp">WhatsApp</option>
				</select>
			</div>
			<div>									
				<input type="tel" id="cf_phone" name="cf_phone" placeholder="Телефон" required>
				<!-- <label for="contact">Телефон</label> -->
			</div>
			<div>									
				<input type="text" id="cf_site" name="cf_site" placeholder="Адрес сайта">
				<!-- <label for="site">Адрес сайта</label> -->
			</div>
			<div class="callback_form__agree personal-data-consent-wrap">
				<div class="checkbox-border">
	              <input type="checkbox" class="required-checkbox personal-data-consent" id="personal_data_consent_callback__FORM_info" name="personal_data_consent" value="1" required>
				</div>
              <label for="personal_data_consent_callback__FORM_info">Я&nbsp;соглашаюсь с&nbsp;<a href="/privacy-policy.html" target="_blank">политикой конфиденциальности</a> и даю согласие на&nbsp;обработку персональных данных</label>
            </div>
			<button id="callback__FORM_send_info" type="submit" data-root="y">Отправить</button>
		</form>					
	</div>

	<div id="audit__FORM_popup" class="popup__FORM_wrap">
		<div class="callback_form__title">Получить бесплатный аудит вашего сайта</div>
		<div class="callback_form__description">Заполните форму обратной связи и&nbsp;мы&nbsp;сделаем аудит вашего сайта бесплатно</div>
		<form id="audit__FORM_seo" name="audit__FORM_seo" action="#" method="post">
			<div>									
				<input type="text" id="af_name" name="af_name" placeholder="Ваше имя" required>
				<!-- <label for="name">Ваше имя</label> -->
			</div>
			<div>									
				<input type="tel" id="af_phone" name="af_phone" placeholder="Телефон" required>
				<!-- <label for="contact">Телефон</label> -->
			</div>
			<div>									
				<input type="text" id="af_site" name="af_site" placeholder="Адрес сайта">
				<!-- <label for="name">Адрес сайта</label> -->
			</div>
			<div>	
				<textarea id="af_comment" name="af_comment" placeholder="Комментарий"></textarea>
				<!-- <label for="comment">Комментарий</label> -->
			</div>
                <div class="calc_site_no__wrap">                 
				<div class="checkbox-border">
                  <input type="checkbox" class="required-checkbox" id="cf_agree3" name="cf_agree3" value="Да">
				</div>
                  <label for="cf_agree3">Аудит для самостоятельного просмотра предоставляется только после онлайн-созвона.</label>
                </div>
			<div class="callback_form__agree personal-data-consent-wrap">
				<div class="checkbox-border">
	              <input type="checkbox" class="required-checkbox personal-data-consent" id="personal_data_consent_audit__FORM_seo" name="personal_data_consent" value="1" required>
				</div>
              <label for="personal_data_consent_audit__FORM_seo">Я&nbsp;соглашаюсь с&nbsp;<a href="/privacy-policy.html" target="_blank">политикой конфиденциальности</a> и даю согласие на&nbsp;обработку персональных данных</label>
            </div>
			<button id="audit__FORM_send_seo" type="submit" data-root="y">Отправить</button>
		</form>					
	</div>


<?	$need_root = true;
	include_once get_template_directory() . "/template-parts/content-tarifs-popups.php";
?>

	<div class="scroll_to_top"></div>

	<!-- Yandex.Metrika counter -->
	<script type="text/javascript" >
	   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
	   m[i].l=1*new Date();
	   for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
	   k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
	   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

	   ym(54287016, "init", {
	        clickmap:true,
	        trackLinks:true,
	        accurateTrackBounce:true,
	        webvisor:true
	   });
	</script>
	<noscript><div><img src="https://mc.yandex.ru/watch/54287016" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
	<!-- /Yandex.Metrika counter -->

<?php wp_footer(); ?>

</body>
</html>
