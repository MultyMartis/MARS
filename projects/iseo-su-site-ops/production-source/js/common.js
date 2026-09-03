
// Все OWL Carousel

$(document).ready(function() {
            $('#recommendations_slider').owlCarousel({
                loop:false, //Зацикливаем слайдер
                margin:20, //Отступ от элемента справа в 50px
                nav:false, //Отключение навигации
                dots:true,
                autoplay:false, //Автозапуск слайдера
                smartSpeed:1000, //Время движения слайда
                autoplayTimeout:5000, //Время смены слайда
        responsive:{
            0:{
                items:1
            },
            630:{
                items:2
            },
            1024:{
                items:3
            },
            1440:{
                items:4
            }
        }
    });
});



$(document).ready(function() {
            $('#partners_slider_btn').owlCarousel({
                loop:false, //Зацикливаем слайдер
                margin:20, //Отступ от элемента справа в 50px
                nav:false, //Отключение навигации
                dots:true,
                autoplay:false, //Автозапуск слайдера
                smartSpeed:1000, //Время движения слайда
                autoplayTimeout:5000, //Время смены слайда
        responsive:{
            0:{
                items:1
            },
            630:{
                items:2
            },
            1024:{
                items:3
            }
        }
    });
});



$(document).ready(function() {
            $('#about_team_carousel').owlCarousel({
                loop:true, //Зацикливаем слайдер
                margin:20, //Отступ от элемента справа в 50px
                nav:false, //Отключение навигации
                dots:true,
                autoplay:false, //Автозапуск слайдера
                smartSpeed:1000, //Время движения слайда
                autoplayTimeout:5000, //Время смены слайда
        responsive:{
            0:{
                items:2
            },
            1024:{
                items:3
            }
        }
    });
});



$(document).ready(function() {
            $('#achievement_slider').owlCarousel({
                loop:false,
                margin:20,
                nav:false,
                dots:true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
        responsive:{
            0:{
                items:1
            },
            1309:{
                items:2
            },
            1439:{
                items:4
            }
        }
    });
            $('#project_achievement_slider').owlCarousel({
                loop:false,
                margin:20,
                nav:false,
                dots:true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
        responsive:{
            0:{
                items:1
            },
            860:{
                items:2
            }
        }
    });
});


$(document).ready(function() {
            $('#project_team_slider').owlCarousel({
                loop:false,
                margin:20,
				autoHeight:true,
                nav:false,
                dots:true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
        responsive:{
            0:{
                items:1
            },
            680:{
                items:2
            },
            1199:{
                items:3
            },
            1439:{
                items:4
            }
        }
    });
});



$(document).ready(function() {
            $('#blog_autors_articles').owlCarousel({
                loop:false,
                margin:20,
                nav:false,
                dots:true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
        responsive:{
            0:{
                items:1
            },
            490:{
                items:2
            },
            1199:{
                items:3
            },
            1439:{
                items:4
            }
        }
    });
});



$(document).ready(function() {
            $('#cases_stats_slider').owlCarousel({
                loop:false,
                margin:20,
                nav:false,
                dots:true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
        responsive:{
            0:{
                items:1
            },
            1309:{
                items:2
            },
            1439:{
                items:4
            }
        }
    });
});



$(document).ready(function() {
            $('#cases_stats_slider_after').owlCarousel({
                loop:false,
                margin:20,
                nav:false,
                dots:true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
        responsive:{
            0:{
                items:1
            },
            1309:{
                items:2
            },
            1439:{
                items:4
            }
        }
    });
});



$(document).ready(function() {
            $('#case_short__stat').owlCarousel({
                loop:false,
                margin:20,
                nav:false,
                dots:true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
        responsive:{
            0:{
                items:1
            },
            380:{
                items:2
            },
            560:{
                items:3
            },
            1439:{
                items:3
            }
        }
    });
});



$(document).ready(function() {
            $('#case_catalog_slider').owlCarousel({
                loop:false,
                margin:20,
                nav:false,
                dots:true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
        responsive:{
            0:{
                items:1
            },
            1309:{
                items:1
            },
            1439:{
                items:2
            }
        }
    });
});



$(document).ready(function() {
            $('#career_info__slider_img').owlCarousel({
                loop:false,
                margin:20,
                nav:false,
                dots:true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
        responsive:{
            0:{
                items:1
            }
        }
    });
});



$(document).ready(function() {
            $('#tariffs_slider').owlCarousel({
                loop:false,
                margin:20,
                nav:false,
                dots:true,
                autoHeight: true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
        responsive:{
            0:{
                items:1
            },
            630:{
                items:2
            },
            1024:{
                items:3
            },
            1440:{
                items:4
            }
        }
    });
});



$(document).ready(function() {
            $('#reviews_slider').owlCarousel({
                loop:true,
                margin:20,
                nav:false,
                dots:true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:7000,
        responsive:{
            0:{
                items:1
            },
            1309:{
                items:2
            },
            1439:{
                items:4
            }
        }
    });
});



$('.team_sl__btns > a').click(function(){
    $('.team_sl__btns > a').removeClass('active');
    $(this).addClass('active');
});

$(document).ready(function() {
            $('#about_team_slider').owlCarousel({
                loop:true,
                margin:20,
                nav:true,
                dots:false,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
                items: 1,
                navText:["<div class='case_stat_info__prev'></div>","<div class='case_stat_info__next'></div>"]
    });
});



$(document).ready(function() {
            $('#about_team_slider__btn').owlCarousel({
                loop:false, //Зацикливаем слайдер
                margin:20, //Отступ от элемента справа в 50px
                nav:false, //Отключение навигации
                dots:true,
                autoplay:false, //Автозапуск слайдера
                smartSpeed:1000, //Время движения слайда
                autoplayTimeout:5000, //Время смены слайда
        responsive:{
            0:{
                items:3
            },
            767:{
                items:4
            },
            1309:{
                items:5
            },
            1439:{
                items:6
            }
        }
    });
});


$(document).ready(function() {
            $('#team_slider').owlCarousel({
                loop:false, //Зацикливаем слайдер
                margin:20, //Отступ от элемента справа в 50px
                nav:false, //Отключение навигации
                dots:true,
                autoplay:false, //Автозапуск слайдера
                smartSpeed:1000, //Время движения слайда
                autoplayTimeout:5000, //Время смены слайда
        responsive:{
            0:{
                items:3
            },
            767:{
                items:4
            },
            1309:{
                items:5
            },
            1439:{
                items:6
            }
        }
    });
});











$(document).ready(function() {
    $('#time_slider').owlCarousel({
        loop:false,
        margin:20,
        mouseDrag:false,
        touchDrag:true,
        nav:false,
        dots:false,
        autoHeight:true,
        autoplay:false,
        smartSpeed:1000,
        URLhashListener:true,
        autoplayHoverPause:true,
        startPosition: 'URLHash',
        autoplayTimeout:3000,
        responsive:{
            0:{
                items:1
            }
        }
    });
});



$(document).ready(function() {
            $('#case_design_carousel').owlCarousel({
                loop:false, //Зацикливаем слайдер
                margin:20, //Отступ от элемента справа в 50px
                nav:false, //Отключение навигации
                dots:true,
                autoplay:false, //Автозапуск слайдера
                smartSpeed:1000, //Время движения слайда
                autoplayTimeout:5000, //Время смены слайда
        responsive:{
            0:{
                items:2
            },
            1024:{
                items:3
            }
        }
    });
});



$(document).ready(function () {

    $('#case_SEO_AI_carousel').owlCarousel({
        loop:false, //Зацикливаем слайдер
        margin:20, //Отступ от элемента справа в 50px
        nav:false, //Отключение навигации
        dots:true,
        autoplay:false, //Автозапуск слайдера
        smartSpeed:1000, //Время движения слайда
        autoplayTimeout:5000, //Время смены слайда
        responsive:{
            0:{
                items:2
            },
            1024:{
                items:3
            }
        },
        navText:["<div class='case_stat_info__prev'></div>","<div class='case_stat_info__next'></div>"]
    });

    const selector = $(".case_stat__gallery .owl-item:not(.cloned) [data-fancybox]");
    $(selector).fancybox({
        loop: true,
        buttons: ["close"],
        autoFocus: false,
        backFocus: false,
        trapFocus: false,
        hash: false,
        btnTpl: {
            arrowLeft:
                '<div data-fancybox-prev class="fancybox-button case_stat_info__left" title="Назад">' +
                "</div>",
            arrowRight:
                '<div data-fancybox-next class="fancybox-button case_stat_info__right" title="Далее">' +
                "</div>"
        },
        animationDuration: 0,
        transitionDuration: 0,
        touch: {
            momentum: false
        },
        animationEffect: false,
        afterShow: function (instance) {
            instance.scaleToActual(0, 0);
        },
        beforeClose: function (instance, slide) {
            const index = instance.currIndex;
            const elementClicked = $(slide.opts.$orig);
            elementClicked
                .closest(".owl-carousel")
                .trigger("to.owl.carousel", [index, 0, true]);
        }
    });

    $(document).on(
        "click.fb",
        ".case_stat__gallery .owl-item.cloned .case_stat__gallery__item",
        function () {
            $.fancybox.destroy();
            const $slides = $(this).parent().siblings(".owl-item:not(.cloned)");

            $slides
                .eq(($(this).attr("data-index") || 0) % $slides.length)
                .find("[data-fancybox]")
                .trigger("click.fb-start", { $trigger: $(this) });

            return false;
        }
    );
});















$(document).ready(function() {
            $('#case_AI_carousel').owlCarousel({
                loop:false, //Зацикливаем слайдер
                margin:20, //Отступ от элемента справа в 50px
                nav:false, //Отключение навигации
                dots:true,
                autoplay:false, //Автозапуск слайдера
                smartSpeed:1000, //Время движения слайда
                autoplayTimeout:5000, //Время смены слайда
        responsive:{
            0:{
                items:2
            },
            1024:{
                items:3
            }
        }
    });
});



$(document).ready(function() {
            $('#promotion_slider').owlCarousel({
                loop:false,
                margin:20,
                nav:false,
                dots:true,
                autoplay:false,
                smartSpeed:1000,
                autoplayTimeout:5000,
        responsive:{
            0:{
                items:1
            },
            767:{
                items:2
            },
            1439:{
                items:4
            }
        }
    });
});










// Оffcanvas Menu Desktop (Мега меню)

jQuery(document).ready(function() {
    jQuery(".see_more_btn").click(function () {
    elementClick = jQuery(this).attr("href")
    destination = jQuery(elementClick).offset().top - 0;
    jQuery("html:not(:animated),body:not(:animated)").animate({scrollTop: destination}, 1000);
    return false;
    });
});

$('.offcanvas_menu__btn').click(function(event) {
    if($('#offcanvas-MENU').hasClass('open'))
        {
        $('#offcanvas-MENU').fadeOut(300, function() {
           $('#offcanvas-MENU').removeClass('open');
           $('body').removeClass('full_scroll'); // ← добавлено
        });
    } else {
        $('#offcanvas-MENU').fadeIn(500, function() {
            $('#offcanvas-MENU').addClass('open');
            $('body').addClass('full_scroll'); // ← добавлено
        });
    }    
});

$('.offcanvas_menu__close').click(function(event) {
    if($('#offcanvas-MENU').hasClass('open'))
        {
        $('#offcanvas-MENU').fadeOut(300, function() {
           $('#offcanvas-MENU').removeClass('open');
           $('body').removeClass('full_scroll'); // ← добавлено
        });
    } else {
        $('#offcanvas-MENU').fadeIn(500, function() {
            $('#offcanvas-MENU').addClass('open');
            $('body').addClass('full_scroll'); // ← добавлено
        });
    }    
});

$('#001').hover(function(event) {
    $('#offcanvas-MENU').removeClass('open');
    $('#offcanvas-MENU').fadeOut(500).hide('');
    $('#002 .sub_menu').removeClass('open');
    $('#002 .sub_menu').fadeOut(500).hide('');
    if($('#001 .sub_menu').hasClass('open'))
        {
        $('#001 .sub_menu').fadeOut(500, function() {
           $('#001 .sub_menu').removeClass('open');
        });
    } else {
        $('#001 .sub_menu').fadeIn(500, function() {
            $('#001 .sub_menu').addClass('open');
        });
    }
});

$('#002').hover(function(event) {
    $('#offcanvas-MENU').removeClass('open');
    $('#offcanvas-MENU').fadeOut(500).hide('');
    $('#001 .sub_menu').removeClass('open');
    $('#001 .sub_menu').fadeOut(500).hide('');
    if($('#002 .sub_menu').hasClass('open'))
        {
        $('#002 .sub_menu').fadeOut(500, function() {
           $('#002 .sub_menu').removeClass('open');
        });
    } else {
        $('#002 .sub_menu').fadeIn(500, function() {
            $('#002 .sub_menu').addClass('open');
        });
    }
});





// Мобильное Мега меню

$('#m001').click(function(event) {
    $('#m002 .sub_navigations__wrap').fadeOut(500).removeClass('open');
    if($('#m001 .sub_navigations__wrap').hasClass('open'))
        {
        $('#m001 .sub_navigations__wrap').fadeOut(500, function() {
           $('#m001 .sub_navigations__wrap').removeClass('open');
        });
    } else {
        $('#m001 .sub_navigations__wrap').fadeIn(500, function() {
            $('#m001 .sub_navigations__wrap').addClass('open');
        });
    }
});

$('#m002').click(function(event) {
    $('#m001 .sub_navigations__wrap').fadeOut(500).removeClass('open');
    if($('#m002 .sub_navigations__wrap').hasClass('open'))
        {
        $('#m002 .sub_navigations__wrap').fadeOut(500, function() {
           $('#m002 .sub_navigations__wrap').removeClass('open');
        });
    } else {
        $('#m002 .sub_navigations__wrap').fadeIn(500, function() {
            $('#m002 .sub_navigations__wrap').addClass('open');
        });
    }
});





// Блок ВОПРОС ОТВЕТ

$('#tab01').click(function(event) {
    var wasActive = $('#tab01.uni_faq_block').hasClass('active');
    $('.uni_faq_block').removeClass('active');

    if (!wasActive) {
        $('#tab01.uni_faq_block').addClass('active');

        $('html, body').animate({
            scrollTop: $('#tab01').offset().top
        }, 500);
    } else {
        $('html, body').animate({
            scrollTop: $('.uni_faq').offset().top
        }, 500);
    }
});

$('#tab02').click(function(event) {
    var wasActive = $('#tab02.uni_faq_block').hasClass('active');
    $('.uni_faq_block').removeClass('active');

    if (!wasActive) {
        $('#tab02.uni_faq_block').addClass('active');

        $('html, body').animate({
            scrollTop: $('#tab02').offset().top
        }, 500);
    } else {
        $('html, body').animate({
            scrollTop: $('.uni_faq').offset().top
        }, 500);
    }
});

$('#tab03').click(function(event) {
    var wasActive = $('#tab03.uni_faq_block').hasClass('active');
    $('.uni_faq_block').removeClass('active');

    if (!wasActive) {
        $('#tab03.uni_faq_block').addClass('active');

        $('html, body').animate({
            scrollTop: $('#tab03').offset().top
        }, 500);
    } else {
        $('html, body').animate({
            scrollTop: $('.uni_faq').offset().top
        }, 500);
    }
});

$('#tab04').click(function(event) {
    var wasActive = $('#tab04.uni_faq_block').hasClass('active');
    $('.uni_faq_block').removeClass('active');

    if (!wasActive) {
        $('#tab04.uni_faq_block').addClass('active');

        $('html, body').animate({
            scrollTop: $('#tab04').offset().top
        }, 500);
    } else {
        $('html, body').animate({
            scrollTop: $('.uni_faq').offset().top
        }, 500);
    }
});












// Кнопка ЗАГРУЗИТЬ ЕЩЕ

var more = document.querySelectorAll('.load_more');

for (var i = 0; i < more.length; i++) {
  more[i].addEventListener('click', function() {
    var showPerClick = 4;
	var currentFilter = $('.sub_filter_btn.current').data('filter');
	if(!currentFilter) {
		if($('.services_prices').length) {
			currentFilter = '.services_prices .uni_grid_blocks > div';
		} else {
			currentFilter = '.reviews_block';
		}
	}
    var hidden = this.parentNode.querySelectorAll(currentFilter+'.hidden');
    for (var i = 0; i < showPerClick; i++) {
      if (!hidden[i]) return this.style.display = 'none';
      hidden[i].classList.remove('hidden');
    }
   if (!hidden[i+1]) return this.style.display = 'none';
  });
}


var more = document.querySelectorAll('.see_more');

for (var i = 0; i < more.length; i++) {
  more[i].addEventListener('click', function() {
    var showPerClick = 4;
    var currentFilter = $('.blog_filter__navigations.current').data('filter');
    if(!currentFilter) {
        currentFilter = '.blog_teaser_block';
    }
    var hidden = this.parentNode.querySelectorAll(currentFilter+'.hidden');
    for (var i = 0; i < showPerClick; i++) {
      if (!hidden[i]) return this.style.display = 'none';
      hidden[i].classList.remove('hidden');
    }
   if (!hidden[i]) return this.style.display = 'none';
  });
}








// Фильтр БОНУСОВ И АКЦИИ

$(document).ready(function() {
	$('.sub_filter_item > a').each(function(){
		var filterCount = $('.case_catalog__wrap > ' + $(this).data('filter')).length;
		$(this).find('span').text('('+filterCount+')');
		if(!filterCount) {
			$(this).parent().hide();
		}
	});
	$('.bonus__navigations > a').each(function(){
		var filterCount = $('.case_catalog__wrap > ' + $(this).data('filter')).length;
		$(this).find('span').text('('+filterCount+')');
		if(!filterCount) {
			$(this).parent().hide();
		}
	});
});


// Обработчик кнопок калькулятора


$(document).ready(function() {
	$('.calculator_stage__btns .next, .calculator_stage__btns .back').click(function(){
		var stage = $(this).attr('data-target');
		handleCalcStage(Number(stage));
		return false;
	});
	$('.calculator_stage__options input').click(function(){
		$('.calculator_stage__errors').text('');
	});
	$('.calculator_stage__btns .submit').click(function(e){
		e.preventDefault;		
		var isSelected = $('.calculator_stage:visible input[type="radio"]:checked').length;
		var numSelect = $('.calculator_stage:visible input[type="radio"]').length;
		if(!isSelected && numSelect) {
			$('.calculator_stage__errors').text('Пожалуйста, выберите один из вариантов');
		}
		if (checkEmptyFields($(this).closest('form')) === '0') {
			if(!isSelected && numSelect) {
				return;
			}
			
            $(this).replaceWith("<em>отправка...</em>");
            
            $.ajax({
                type: 'POST',
                url: 'calc__FORM.php',
                data: $('[id^="calculator__FORM"]').serialize() + getPageAttrs(),
                success: function(data) {
                    if(data == "true") {
                        $('[id^="calculator__FORM"]').fadeOut("fast", function(){
                            $(this).before("<p>Успешно! Сообщение отправлено</p>");
                            ym(54287016, 'reachGoal', 'form_home');
                        });
                    }
                }
            });
		}
		return false;
	});
});




// Фильтр Каталога Кейсов

$('.case_catalog__navigations a').click(function(){
    $('.case_catalog__navigations a').removeClass('current');
    $(this).addClass('current');
	$('.case_catalog__sub_navigations > div').addClass('hidden');
	$('.case_catalog__sub_navigations > ' + $(this).data('filter')).removeClass('hidden');
	$('.case_catalog__wrap > div').addClass('hidden');
	$('.case_catalog__wrap > div').each(function(index){
		if(index > 3){
			$('.case_catalog__wrap > .load_more').show();
			return false;
		} else {
			$(this).removeClass('hidden');
		}
	});
    $('.sub_filter_btn').removeClass('current');
    $('.sub_filter_btn').eq(0).addClass('current');
});

$('.sub_filter_btn').click(function(){
    $('.sub_filter_btn').removeClass('current');
    $(this).addClass('current');
	$('.case_catalog__wrap > div').addClass('hidden');
	var filterClass = '.case_catalog__wrap > ' + $(this).data('filter');
	var filterCount = $(filterClass).length;
	$(this).find('span').text('('+filterCount+')');
	$('.case_catalog__wrap > .load_more').hide();
	$(filterClass).each(function(index){
		if(index > 3){
			$('.case_catalog__wrap > .load_more').show();
			return false;
		} else {
			$(this).removeClass('hidden');
		}
	});
});

$('.our_history__btns > a').click(function(){
    $('.our_history__btns > a').removeClass('active');
    $(this).addClass('active');
});







// Просмотр видео в FANCYBOX

$(".video_shorts_modalbox").fancybox({
    maxWidth    : 406,
    maxHeight   : 720,
    fitToView   : false,
    width       : 406,
    height      : 720,
    autoSize    : false,
    closeClick  : false,
    openEffect  : 'none',
    closeEffect : 'none'
});

$(".video_modalbox").fancybox({
    maxWidth    : 1200,
    maxHeight   : 900,
    fitToView   : false,
    width       : '70%',
    height      : '70%',
    autoSize    : false,
    closeClick  : false,
    openEffect  : 'none',
    closeEffect : 'none'
});




$(document).ready(function() {
	$('.contact_select').change(function(){
		var ph = "Укажите ";
		if($(this).val() == "Телефон"){
			ph += "номер телефона:"
		} else {
			ph += "номер в " + $(this).val() + ":";
		}
		$(this).closest('form').find('input[type="tel"]').attr('placeholder', ph);
	});
});



// Формы обратной связи и МОДАЛЬНЫЕ ОКНА с формами

$(".modalbox").fancybox();



// Формы на ГЛАВНОЙ

            // $("#callback__FORM_popup").submit(function() { return false; });        
            $("#callback__FORM_send").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#callback__FORM_send").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'callback__FORM.php',
                        data: $("#callback__FORM").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#callback__FORM").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_home');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
				}
            });



            // $("#audit__FORM_popup").submit(function() { return false; });
            $("#audit__FORM_send").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#audit__FORM_send").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'audit__FORM.php',
                        data: $("#audit__FORM").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#audit__FORM").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_home');
                                    setTimeout("$.fancybox.close()", 3000);                                    
                                });
                            }
                        }
                    });
				}
            });



            $("#page__FORM_send").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#page__FORM_send").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'page__FORM.php',
                        data: $("#page__FORM").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#page__FORM").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
									ym(54287016, 'reachGoal', 'form_home');
                                });
                            }
                        }
                    });
				}
            });



// Формы на страницах ИНФО




$("#callback__FORM_send_info").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#callback__FORM_send_info").replaceWith("<em>отправка...</em>");

		var root = false;
		if($(this).attr('data-root')) root = true;
        $.ajax({
            type: 'POST',
            url: root ? '/callback__FORM.php' : 'callback__FORM.php',
            data: $("#callback__FORM_info").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#callback__FORM_info").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_info');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

// WAVE 01A — SEO/tariff calculator result lead form (after "Рассчитать")
$(document).on("click", "#callback__FORM_tariff_calc_send", function(e){
    e.preventDefault();
    var $form = $("#callback__FORM_tariff_calc");
    if (!$form.length) return;
    if (checkEmptyFields($form) !== '0') return;
    var $btn = $(this);
    if ($btn.data("busy")) return;
    $btn.data("busy", true);
    var btnHtml = $btn.html();
    $btn.prop("disabled", true).html("отправка...");
    $.ajax({
        type: 'POST',
        url: '/callback__FORM.php',
        data: $form.serialize() + getPageAttrs(),
        success: function(data) {
            if (data == "true") {
                $form.fadeOut("fast", function(){
                    $(this).before("<p class=\"tariff-calc-request__success\">Успешно! Сообщение отправлено</p>");
                    if (typeof ym === "function") {
                        ym(54287016, 'reachGoal', 'form_info');
                    }
                });
            } else {
                $btn.prop("disabled", false).html(btnHtml).data("busy", false);
            }
        },
        error: function() {
            $btn.prop("disabled", false).html(btnHtml).data("busy", false);
        }
    });
});

$("#audit__FORM_send_info").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#audit__FORM_send_info").replaceWith("<em>отправка...</em>");
            
        $.ajax({
            type: 'POST',
            url: 'audit__FORM.php',
            data: $("#audit__FORM_info").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#audit__FORM_info").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_info');
                        setTimeout("$.fancybox.close()", 3000);                                    
                    });
                }
            }
        });
    }
});

$("#page__FORM_send_info").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
    $("#page__FORM_send_info").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: '/page__FORM.php',
            data: $("#page__FORM_info").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#page__FORM_info").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_info');
                    });
                }
            }
        });
    }
});



            // $("#bonus__FORM_popup").submit(function() { return false; });
            $("#bonus__FORM_send").on("click", function(){
                if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#bonus__FORM_send").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'bonus__FORM.php',
                        data: $("#bonus__FORM").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#bonus__FORM").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
                }
            });

            $("#bonus__FORM_send_seo").on("click", function(){
                if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#bonus__FORM_seo").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'bonus__FORM.php',
                        data: $("#bonus__FORM_seo").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#bonus__FORM_seo").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
                }
            });



            // $("#bonus__FORM_popup_1").submit(function() { return false; });
            $("#bonus__FORM_send_1").on("click", function(){
                if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#bonus__FORM_send_1").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'bonus__FORM.php',
                        data: $("#bonus__FORM_1").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#bonus__FORM_1").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
                }
            });



            // $("#bonus__FORM_popup_2").submit(function() { return false; });
            $("#bonus__FORM_send_2").on("click", function(){
                if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#bonus__FORM_send_2").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'bonus__FORM.php',
                        data: $("#bonus__FORM_2").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#bonus__FORM_2").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
                }
            });



            // $("#bonus__FORM_popup_3").submit(function() { return false; });
            $("#bonus__FORM_send_3").on("click", function(){
                if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#bonus__FORM_send_3").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'bonus__FORM.php',
                        data: $("#bonus__FORM_3").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#bonus__FORM_3").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
                }
            });



            // $("#bonus__FORM_popup_4").submit(function() { return false; });
            $("#bonus__FORM_send_4").on("click", function(){
                if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#bonus__FORM_send_4").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'bonus__FORM.php',
                        data: $("#bonus__FORM_4").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#bonus__FORM_4").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
                }
            });



            // $("#bonus__FORM_popup_5").submit(function() { return false; });
            $("#bonus__FORM_send_5").on("click", function(){
                if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#bonus__FORM_send_5").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'bonus__FORM.php',
                        data: $("#bonus__FORM_5").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#bonus__FORM_5").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
                }
            });



            // $("#bonus__FORM_popup_6").submit(function() { return false; });
            $("#bonus__FORM_send_6").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#bonus__FORM_send_6").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'bonus__FORM.php',
                        data: $("#bonus__FORM_6").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#bonus__FORM_6").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
				}
            });


            // $("#career__FORM_popup").submit(function() { return false; });
            $("#career__FORM_send").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#career__FORM_send").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'career__FORM.php',
                        data: $("#career__FORM").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#career__FORM").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
				}
            });

            $("#review_page__FORM_send").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#review_page__FORM_send").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'review__FORM.php',
                        data: $("#review_page__FORM").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#review_page__FORM").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
				}
            });

            $("#review_page__FORM_send_info").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#review_page__FORM_send_info").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'review__FORM.php',
                        data: $("#review_page__FORM_info").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#review_page__FORM_info").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
				}
            });

            // $("#review__FORM_popup").submit(function() { return false; });
            $("#review__FORM_send").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#review__FORM_send").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'review__FORM.php',
                        data: $("#review__FORM").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#review__FORM").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
				}
            });



            $("#partners_page__FORM_send").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#partners_page__FORM_send").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'partners__FORM.php',
                        data: $("#partners_page__FORM").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#partners_page__FORM").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
				}
            });

            // $("#partners__FORM_popup").submit(function() { return false; });
            $("#partners__FORM_send").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#partners__FORM_send").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'partners__FORM.php',
                        data: $("#partners__FORM").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#partners__FORM").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
				}
            });

            $("#partners__FORM_send_info").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#partners__FORM_send_info").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'partners__FORM.php',
                        data: $("#partners__FORM_info").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#partners__FORM_info").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
				}
            });


            $("#partners_page__FORM_send_info").on("click", function(){
				if (checkEmptyFields($(this).closest('form')) === '0') {
                    $("#partners_page__FORM_send_info").replaceWith("<em>отправка...</em>");
                    
                    $.ajax({
                        type: 'POST',
                        url: 'partners__FORM.php',
                        data: $("#partners_page__FORM_info").serialize() + getPageAttrs(),
                        success: function(data) {
                            if(data == "true") {
                                $("#partners_page__FORM_info").fadeOut("fast", function(){
                                    $(this).before("<p>Успешно! Сообщение отправлено</p>");
                                    ym(54287016, 'reachGoal', 'form_info');
                                    setTimeout("$.fancybox.close()", 3000);
                                });
                            }
                        }
                    });
				}
            });


// Формы на страницах КЕЙСЫ

$("#callback__FORM_send_cases").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#callback__FORM_send_cases").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'callback__FORM.php',
            data: $("#callback__FORM_cases").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#callback__FORM_cases").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_cases');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#audit__FORM_send_cases").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#audit__FORM_send_cases").replaceWith("<em>отправка...</em>");
            
        $.ajax({
            type: 'POST',
            url: 'audit__FORM.php',
            data: $("#audit__FORM_cases").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#audit__FORM_cases").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_cases');
                        setTimeout("$.fancybox.close()", 3000);                                    
                    });
                }
            }
        });
    }
});

$("#page__FORM_send_cases").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
    $("#page__FORM_send_cases").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: 'page__FORM.php',
            data: $("#page__FORM_cases").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#page__FORM_cases").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_cases');
                    });
                }
            }
        });
    }
});



// Формы на странице УСЛУГИ

$("#callback__FORM_send_services").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#callback__FORM_send_services").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'callback__FORM.php',
            data: $("#callback__FORM_services").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#callback__FORM_services").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#audit__FORM_send_services").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#audit__FORM_send_services").replaceWith("<em>отправка...</em>");
            
        $.ajax({
            type: 'POST',
            url: 'audit__FORM.php',
            data: $("#audit__FORM_services").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#audit__FORM_services").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services');
                        setTimeout("$.fancybox.close()", 3000);                                    
                    });
                }
            }
        });
    }
});

$("#page__FORM_send_services").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
    $("#page__FORM_send_services").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: 'page__FORM.php',
            data: $("#page__FORM_services").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#page__FORM_services").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services');
                    });
                }
            }
        });
    }
});


















// Формы на страницах СЕО

$("#callback__FORM_send_seo").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#callback__FORM_send_seo").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'callback__FORM.php',
            data: $("#callback__FORM_seo").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#callback__FORM_seo").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___seo');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    } else {
		return false;
	}
});

$("#audit__FORM_send_seo").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#audit__FORM_send_seo").replaceWith("<em>отправка...</em>");
		var root = false;
		if($(this).attr('data-root')) root = true;

        $.ajax({
            type: 'POST',
            url: root ? '/audit__FORM.php' : 'audit__FORM.php',
            data: $("#audit__FORM_seo").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#audit__FORM_seo").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___seo');
                        setTimeout("$.fancybox.close()", 3000);                                    
                    });
                }
            }
        });
    } else {
		return false;
	}
});

$("#page__FORM_send_seo").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
    $("#page__FORM_send_seo").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: 'page__FORM.php',
            data: $("#page__FORM_seo").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#page__FORM_seo").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___seo');
                    });
                }
            }
        });
    } else {
		return false;
	}
});

$("#tariff_1__FORM_send_seo").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_1__FORM_send_seo").replaceWith("<em>отправка...</em>");
                
		var root = false;
		if($(this).attr('data-root')) root = true;
        $.ajax({
            type: 'POST',
            url: root ? '/tariff_1__FORM.php' : 'tariff_1__FORM.php',
            data: $("#tariff_1__FORM_seo").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_1__FORM_seo").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___seo');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    } else {
		return false;
	}
});

$("#tariff_2__FORM_send_seo").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_2__FORM_send_seo").replaceWith("<em>отправка...</em>");
                    
		var root = false;
		if($(this).attr('data-root')) root = true;
        $.ajax({
            type: 'POST',
            url: root ? '/tariff_2__FORM.php' : 'tariff_2__FORM.php',
            data: $("#tariff_2__FORM_seo").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_2__FORM_seo").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___seo');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    } else {
		return false;
	}
});

$("#tariff_3__FORM_send_seo").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_3__FORM_send_seo").replaceWith("<em>отправка...</em>");
            
		var root = false;
		if($(this).attr('data-root')) root = true;
        $.ajax({
            type: 'POST',
            url: root ? '/tariff_3__FORM.php' : 'tariff_3__FORM.php',
            data: $("#tariff_3__FORM_seo").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_3__FORM_seo").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___seo');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    } else {
		return false;
	}
});

$("#tariff_4__FORM_send_seo").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_4__FORM_send_seo").replaceWith("<em>отправка...</em>");
                
		var root = false;
		if($(this).attr('data-root')) root = true;
        $.ajax({
            type: 'POST',
            url: root ? '/tariff_4__FORM.php' : 'tariff_4__FORM.php',
            data: $("#tariff_4__FORM_seo").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_4__FORM_seo").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___seo');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    } else {
		return false;
	}
});
























// Формы на страницах РЕКЛАМА

$("#callback__FORM_send_adv").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#callback__FORM_send_adv").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'callback__FORM.php',
            data: $("#callback__FORM_adv").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#callback__FORM_adv").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___adv');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#audit__FORM_send_adv").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#audit__FORM_send_adv").replaceWith("<em>отправка...</em>");
            
        $.ajax({
            type: 'POST',
            url: 'audit__FORM.php',
            data: $("#audit__FORM_adv").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#audit__FORM_adv").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___adv');
                        setTimeout("$.fancybox.close()", 3000);                                    
                    });
                }
            }
        });
    }
});

$("#page__FORM_send_adv").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
    $("#page__FORM_send_adv").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: 'page__FORM.php',
            data: $("#page__FORM_adv").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#page__FORM_adv").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___adv');
                    });
                }
            }
        });
    }
});

$("#tariff_1__FORM_send_adv").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_1__FORM_send_adv").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'tariff_1__FORM.php',
            data: $("#tariff_1__FORM_adv").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_1__FORM_adv").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___adv');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_2__FORM_send_adv").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_2__FORM_send_adv").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: 'tariff_2__FORM.php',
            data: $("#tariff_2__FORM_adv").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_2__FORM_adv").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___adv');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_3__FORM_send_adv").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_3__FORM_send_adv").replaceWith("<em>отправка...</em>");
            
        $.ajax({
            type: 'POST',
            url: 'tariff_3__FORM.php',
            data: $("#tariff_3__FORM_adv").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_3__FORM_adv").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___adv');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_4__FORM_send_adv").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_4__FORM_send_adv").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'tariff_4__FORM.php',
            data: $("#tariff_4__FORM_adv").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_4__FORM_adv").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___adv');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

















// Формы на страницах АУДИТ

$("#callback__FORM_send_audit").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#callback__FORM_send_audit").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'callback__FORM.php',
            data: $("#callback__FORM_audit").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#callback__FORM_audit").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___audit');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#audit__FORM_send_audit").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#audit__FORM_send_audit").replaceWith("<em>отправка...</em>");
            
        $.ajax({
            type: 'POST',
            url: 'audit__FORM.php',
            data: $("#audit__FORM_audit").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#audit__FORM_audit").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___audit');
                        setTimeout("$.fancybox.close()", 3000);                                    
                    });
                }
            }
        });
    }
});

$("#page__FORM_send_audit").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
    $("#page__FORM_send_audit").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: 'page__FORM.php',
            data: $("#page__FORM_audit").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#page__FORM_audit").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___audit');
                    });
                }
            }
        });
    }
});

$("#tariff_1__FORM_send_audit").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_1__FORM_send_audit").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'tariff_1__FORM.php',
            data: $("#tariff_1__FORM_audit").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_1__FORM_audit").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___audit');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_2__FORM_send_audit").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_2__FORM_send_audit").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: 'tariff_2__FORM.php',
            data: $("#tariff_2__FORM_audit").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_2__FORM_audit").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___audit');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_3__FORM_send_audit").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_3__FORM_send_audit").replaceWith("<em>отправка...</em>");
            
        $.ajax({
            type: 'POST',
            url: 'tariff_3__FORM.php',
            data: $("#tariff_3__FORM_audit").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_3__FORM_audit").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___audit');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_4__FORM_send_audit").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_4__FORM_send_audit").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'tariff_4__FORM.php',
            data: $("#tariff_4__FORM_audit").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_4__FORM_audit").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___audit');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});


















// Формы на страницах РАЗРАБОТКА

$("#callback__FORM_send_develop").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#callback__FORM_send_develop").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'callback__FORM.php',
            data: $("#callback__FORM_develop").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#callback__FORM_develop").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___dev');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#audit__FORM_send_develop").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#audit__FORM_send_develop").replaceWith("<em>отправка...</em>");
            
        $.ajax({
            type: 'POST',
            url: 'audit__FORM.php',
            data: $("#audit__FORM_develop").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#audit__FORM_develop").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___dev');
                        setTimeout("$.fancybox.close()", 3000);                                    
                    });
                }
            }
        });
    }
});

$("#page__FORM_send_develop").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
    $("#page__FORM_send_develop").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: 'page__FORM.php',
            data: $("#page__FORM_develop").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#page__FORM_develop").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___dev');
                    });
                }
            }
        });
    }
});

$("#tariff_1__FORM_send_develop").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_1__FORM_send_develop").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'tariff_1__FORM.php',
            data: $("#tariff_1__FORM_develop").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_1__FORM_develop").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___dev');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_2__FORM_send_develop").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_2__FORM_send_develop").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: 'tariff_2__FORM.php',
            data: $("#tariff_2__FORM_develop").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_2__FORM_develop").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___dev');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_3__FORM_send_develop").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_3__FORM_send_develop").replaceWith("<em>отправка...</em>");
            
        $.ajax({
            type: 'POST',
            url: 'tariff_3__FORM.php',
            data: $("#tariff_3__FORM_develop").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_3__FORM_develop").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___dev');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_4__FORM_send_develop").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_4__FORM_send_develop").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'tariff_4__FORM.php',
            data: $("#tariff_4__FORM_develop").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_4__FORM_develop").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___dev');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});







// Формы на страницах SERM

$("#callback__FORM_send_serm").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#callback__FORM_send_serm").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'callback__FORM.php',
            data: $("#callback__FORM_serm").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#callback__FORM_serm").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___serm');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#audit__FORM_send_serm").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#audit__FORM_send_serm").replaceWith("<em>отправка...</em>");
            
        $.ajax({
            type: 'POST',
            url: 'audit__FORM.php',
            data: $("#audit__FORM_serm").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#audit__FORM_serm").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___serm');
                        setTimeout("$.fancybox.close()", 3000);                                    
                    });
                }
            }
        });
    }
});

$("#page__FORM_send_serm").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
    $("#page__FORM_send_serm").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: 'page__FORM.php',
            data: $("#page__FORM_serm").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#page__FORM_serm").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___serm');
                    });
                }
            }
        });
    }
});

$("#tariff_1__FORM_send_serm").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_1__FORM_send_serm").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'tariff_1__FORM.php',
            data: $("#tariff_1__FORM_serm").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_1__FORM_serm").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___serm');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_2__FORM_send_serm").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_2__FORM_send_serm").replaceWith("<em>отправка...</em>");
                    
        $.ajax({
            type: 'POST',
            url: 'tariff_2__FORM.php',
            data: $("#tariff_2__FORM_serm").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_2__FORM_serm").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___serm');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_3__FORM_send_serm").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_3__FORM_send_serm").replaceWith("<em>отправка...</em>");
            
        $.ajax({
            type: 'POST',
            url: 'tariff_3__FORM.php',
            data: $("#tariff_3__FORM_serm").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_3__FORM_serm").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___serm');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

$("#tariff_4__FORM_send_serm").on("click", function(){
    if (checkEmptyFields($(this).closest('form')) === '0') {
        $("#tariff_4__FORM_send_serm").replaceWith("<em>отправка...</em>");
                
        $.ajax({
            type: 'POST',
            url: 'tariff_4__FORM.php',
            data: $("#tariff_4__FORM_serm").serialize() + getPageAttrs(),
            success: function(data) {
                if(data == "true") {
                    $("#tariff_4__FORM_serm").fadeOut("fast", function(){
                        $(this).before("<p>Успешно! Сообщение отправлено</p>");
                        ym(54287016, 'reachGoal', 'form_services___serm');
                        setTimeout("$.fancybox.close()", 3000);
                    });
                }
            }
        });
    }
});

















var scrollToTopBtn = document.querySelector(".scroll_to_top");
var rootElement = document.documentElement;

function handleScroll() {
  // Do something on scroll
  var scrollTotal = rootElement.scrollHeight - rootElement.clientHeight;
  if (rootElement.scrollTop / scrollTotal > 0.1) {
    // Show button
    scrollToTopBtn.classList.add("showBtn");
  } else {
    // Hide button
    scrollToTopBtn.classList.remove("showBtn");
  }
}

function scrollToTop() {
  // Scroll to top logic
  rootElement.scrollTo({
    top: 0,
    behavior: "smooth"
  });
}
scrollToTopBtn.addEventListener("click", scrollToTop);
document.addEventListener("scroll", handleScroll);





$(('input[name$="_site_no"]')).click(function(){
	$(this).closest('form').find('input[name$="_site"]').removeClass('error');
});

// Проверка форм обратной связи на валидность

$('input[type="text"], input[type="email"], input[type="tel"], textarea, select').change(function(){
	$(this).removeClass('error');
});

function checkEmptyFields(form) {
	form.attr('data-errors','0');
	form.find('input[type="text"], input[type="email"], input[type="tel"], textarea').each(function(){
		$(this).removeClass('error');
		if($(this).val().length === 0 && $(this).prop('required')){
			$(this).addClass('error');
			$(this).closest('form').attr('data-errors','1');
		}
	});
	form.find('select').each(function(){
		$(this).removeClass('error');
		if(!$(this).val() && $(this).prop('required')){
			$(this).addClass('error');
			$(this).closest('form').attr('data-errors','1');
		}
	});
	var noSite = form.find('input[name$="_site_no"]').is(':checked');
	form.find('input[name$="_site"]').each(function(){
		$(this).removeClass('error');
		if($(this).val().length === 0 && !noSite){
			$(this).addClass('error');
			$(this).closest('form').attr('data-errors','1');
		}
	});
	form.find('.required-checkbox').each(function(){
		$(this).parent().removeClass('error');
		if(!$(this).prop('checked')){
			$(this).parent().addClass('error');
			$(this).closest('form').attr('data-errors','1');
		}
	});
	// Explicit personal-data consent (WAVE 1): must be present, checked, value exactly "1".
	var consentInputs = form.find('input[name="personal_data_consent"]');
	if (consentInputs.length === 0) {
		form.attr('data-errors','1');
	} else {
		consentInputs.each(function(){
			$(this).parent().removeClass('error');
			if (!$(this).prop('checked') || String($(this).val()) !== '1') {
				$(this).parent().addClass('error');
				form.attr('data-errors','1');
			}
		});
	}
//	console.log(form.attr('data-errors'));
	return form.attr('data-errors');
}

function getPageAttrs() {
	return '&pf_page_title=' + $('title').eq(0).text() + '&pf_page_link=' + window.location.href;
}

function handleCalcStage(step){
	if(step < 1 || step > 5) return;
	var isSelected = $('.calculator_stage:visible input[type="radio"]:checked').length;
	var numSelect = $('.calculator_stage:visible input[type="radio"]').length;
	if(!isSelected && numSelect) {
		$('.calculator_stage__errors').text('Пожалуйста, выберите один из вариантов');
		return;
	}
	if(step == 1) {
		$('.calculator_stage__btns .back').hide();
	} else {
		$('.calculator_stage__btns .back').show();
	}
	if(step == 5) {
		$('.calculator_stage__btns .next').hide();
		$('.calculator_stage__btns .submit').show();
	} else {
		$('.calculator_stage__btns .next').show();
		$('.calculator_stage__btns .submit').hide();
	}
	$('.calculator_stage__btns .next').attr('data-target', step+1);
	$('.calculator_stage__btns .back').attr('data-target', step-1);

	
	$('.calculator_stage').hide();	
	$('.calculator_stage[data-stage="'+step+'"]').fadeIn();	
}






// Галерея скринкастов для кейсов (owl + fancybox)

$(document).ready(function () {

    $('#case_stat_info__carousel').owlCarousel({
        loop:true, //Зацикливаем слайдер
        margin:20, //Отступ от элемента справа в 50px
        nav:true, //Отключение навигации
        dots:false,
        items: 1,
        autoplay:false, //Автозапуск слайдера
        smartSpeed:1000, //Время движения слайда
        autoplayTimeout:5000, //Время смены слайда
        navText:["<div class='case_stat_info__prev'></div>","<div class='case_stat_info__next'></div>"]
    });

    const selector = $(".case_stat__gallery .owl-item:not(.cloned) [data-fancybox]");
    $(selector).fancybox({
        loop: true,
        buttons: ["close"],
        autoFocus: false,
        backFocus: false,
        trapFocus: false,
        hash: false,
        btnTpl: {
            arrowLeft:
                '<div data-fancybox-prev class="fancybox-button case_stat_info__left" title="Назад">' +
                "</div>",
            arrowRight:
                '<div data-fancybox-next class="fancybox-button case_stat_info__right" title="Далее">' +
                "</div>"
        },
        animationDuration: 0,
        transitionDuration: 0,
        touch: {
            momentum: false
        },
        animationEffect: false,
        afterShow: function (instance) {
            instance.scaleToActual(0, 0);
        },
        beforeClose: function (instance, slide) {
            const index = instance.currIndex;
            const elementClicked = $(slide.opts.$orig);
            elementClicked
                .closest(".owl-carousel")
                .trigger("to.owl.carousel", [index, 0, true]);
        }
    });

    $(document).on(
        "click.fb",
        ".case_stat__gallery .owl-item.cloned .case_stat__gallery__item",
        function () {
            $.fancybox.destroy();
            const $slides = $(this).parent().siblings(".owl-item:not(.cloned)");

            $slides
                .eq(($(this).attr("data-index") || 0) % $slides.length)
                .find("[data-fancybox]")
                .trigger("click.fb-start", { $trigger: $(this) });

            return false;
        }
    );
});


$(document).ready(function () {
	$('.language-toggle').click(function(){
		if(window.location.hostname == "i-seo.su") {
			window.location.href = window.location.protocol + "//en.i-seo.su" + window.location.pathname;
		} else if(window.location.hostname == "en.i-seo.su") {
			window.location.href = window.location.protocol + "//i-seo.su" + window.location.pathname;
		}
	});
	if ($('#stories-video').length) {
		const video = document.getElementById('stories-video');
		video.addEventListener('loadeddata', () => {
			$('.stories-video').css('opacity','1');
			setTimeout(() => {
				video.muted = true; 
				video.play();
			}, 300);
			$('.stories-video').click((event) => {
				var clickedElement = $(event.target);
				if (!clickedElement.hasClass('stories-video__button')) {
					if($('.stories-video').hasClass('active')){
						$('.stories-video').removeClass('active');
						video.muted = true; 
					} else {
						video.muted = false; 
						video.currentTime = 0;
						video.play();
						$('.stories-video').addClass('active');
						if(!$('.stories-video .stories-video__button').hasClass('active')) {
							setTimeout(() => {
								$('.stories-video .stories-video__button').addClass('active');
							}, 30000);
						}
					}
				}
			});
			$('.stories-video__close').click(() => {
				video.pause();
				$('.stories-video').remove();
			});
		});
		
	}

});





// Скопировать ссылку на бонусы и акции

function copyLink(e) {
   let link = e.target.dataset.link;
   let tmp   = document.createElement('INPUT');
   tmp.value = link;
   document.body.appendChild(tmp); 
   tmp.select(); 
   document.execCommand('copy'); 
   document.body.removeChild(tmp);
   alert('Ссылка скопирована');
}


$(document).ready(function () {

    $('input[type="tel"]').mask('+7 (000) 000-00-00');

    $('input[type="tel"]').on('focus', function () {
        if (!this.value) {
            this.value = '+7 ';
        }
    });

});


/* ISEO_FORM_SECURITY_V1 */
(function ($) {
  if (!$ || !$.ajax) return;
  var HP = "contact_company_url";
  var tokenCache = null;

  function ensureSecurityFields($form) {
    if (!$form || !$form.length) return;
    if (!$form.find('input[name="' + HP + '"]').length) {
      var wrap = document.createElement("div");
      wrap.className = "iseo-hp";
      wrap.setAttribute("aria-hidden", "true");
      wrap.style.cssText = "position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden;";
      wrap.innerHTML = '<label>Company URL<input type="text" name="' + HP + '" value="" tabindex="-1" autocomplete="off"></label>';
      $form.append(wrap);
    }
    if (tokenCache) {
      if (!$form.find('input[name="iseo_ft"]').length) {
        $form.append('<input type="hidden" name="iseo_ft" value="">');
        $form.append('<input type="hidden" name="iseo_fs" value="">');
        $form.append('<input type="hidden" name="iseo_fid" value="">');
      }
      $form.find('input[name="iseo_ft"]').val(tokenCache.t);
      $form.find('input[name="iseo_fs"]').val(tokenCache.s);
      $form.find('input[name="iseo_fid"]').val(tokenCache.id);
    }
  }

  function refreshToken() {
    $.ajax({
      url: "/iseo-form-token.php",
      dataType: "json",
      cache: false,
      success: function (d) {
        if (d && d.t && d.s && d.id) {
          tokenCache = d;
          $('form[id*="FORM"]').each(function () {
            ensureSecurityFields($(this));
          });
        }
      }
    });
  }

  $(function () {
    refreshToken();
    setInterval(refreshToken, 240000);
    $('form[id*="FORM"]').each(function () {
      ensureSecurityFields($(this));
    });
    $(document).on("click", '[id*="FORM_send"], [id*="_send"]', function () {
      ensureSecurityFields($(this).closest("form"));
    });
  });

  $.ajaxPrefilter(function (options) {
    if (!options || !options.url || !/__FORM\.php/i.test(options.url)) return;
    if (!tokenCache) return;
    var extra =
      "&iseo_ft=" +
      encodeURIComponent(tokenCache.t) +
      "&iseo_fs=" +
      encodeURIComponent(tokenCache.s) +
      "&iseo_fid=" +
      encodeURIComponent(tokenCache.id);
    if (typeof options.data === "string") {
      if (options.data.indexOf("iseo_ft=") === -1) options.data += extra;
      if (options.data.indexOf(HP + "=") === -1) {
        options.data += "&" + encodeURIComponent(HP) + "=";
      }
    }
  });

  $(document).ajaxComplete(function (_e, xhr, settings) {
    if (!settings || !settings.url || !/__FORM\.php/i.test(settings.url)) return;
    if (xhr && typeof xhr.responseText === "string" && xhr.responseText.trim() !== "true") {
      var $busy = $("em")
        .filter(function () {
          var t = $(this).text();
          return t.indexOf("Отправ") !== -1 || t.indexOf("отправ") !== -1;
        })
        .last();
      if ($busy.length) {
        $busy.replaceWith(
          '<p class="iseo-form-error">Не удалось отправить заявку. Проверьте заполнение формы и попробуйте ещё раз.</p>'
        );
      }
    }
  });
})(jQuery);

/* ISEO-SU Metrika visitor IP param loader — fail-open; kill switch is server config */
(function () {
  try {
    if (window.__ISEO_METRIKA_VISITOR_IP_LOADER) return;
    window.__ISEO_METRIKA_VISITOR_IP_LOADER = true;
    var s = document.createElement("script");
    s.src = "/js/metrika-visitor-ip.js";
    s.async = true;
    (document.head || document.documentElement).appendChild(s);
  } catch (_e) {}
})();


