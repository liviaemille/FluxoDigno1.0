/**
* Template Name: Impact - v1.1.1
* Template URL: https://bootstrapmade.com/impact-bootstrap-business-website-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
document.addEventListener('DOMContentLoaded', () => {
  "use strict";

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Sticky Header on Scroll
   */
  const selectHeader = document.querySelector('#header');
  if (selectHeader) {
    let headerOffset = selectHeader.offsetTop;
    let nextElement = selectHeader.nextElementSibling;

    const headerFixed = () => {
      if ((headerOffset - window.scrollY) <= 0) {
        selectHeader.classList.add('sticked');
        if (nextElement) nextElement.classList.add('sticked-header-offset');
      } else {
        selectHeader.classList.remove('sticked');
        if (nextElement) nextElement.classList.remove('sticked-header-offset');
      }
    }
    window.addEventListener('load', headerFixed);
    document.addEventListener('scroll', headerFixed);
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = document.querySelectorAll('#navbar a');

  function navbarlinksActive() {
    navbarlinks.forEach(navbarlink => {

      if (!navbarlink.hash) return;

      let section = document.querySelector(navbarlink.hash);
      if (!section) return;

      let position = window.scrollY + 200;

      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active');
      } else {
        navbarlink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navbarlinksActive);
  document.addEventListener('scroll', navbarlinksActive);

  /**
   * Mobile nav toggle
   */
  const mobileNavShow = document.querySelector('.mobile-nav-show');
  const mobileNavHide = document.querySelector('.mobile-nav-hide');

  document.querySelectorAll('.mobile-nav-toggle').forEach(el => {
<<<<<<< HEAD:FluxoDigno/templates/sistema/assets/js/main.js
    el.addEventListener('click', function(event) {
=======
    el.addEventListener('click', function (event) {
>>>>>>> eaa63c1fd0463413ba9910df95e52e639e4775d6:FluxoDigno/sistema/templates/assets/js/main.js
      event.preventDefault();
      mobileNavToogle();
    })
  });

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavShow.classList.toggle('d-none');
    mobileNavHide.classList.toggle('d-none');
  }

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navbar a').forEach(navbarlink => {

    if (!navbarlink.hash) return;

    let section = document.querySelector(navbarlink.hash);
    if (!section) return;

    navbarlink.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  const navDropdowns = document.querySelectorAll('.navbar .dropdown > a');

  navDropdowns.forEach(el => {
<<<<<<< HEAD:FluxoDigno/templates/sistema/assets/js/main.js
    el.addEventListener('click', function(event) {
=======
    el.addEventListener('click', function (event) {
>>>>>>> eaa63c1fd0463413ba9910df95e52e639e4775d6:FluxoDigno/sistema/templates/assets/js/main.js
      if (document.querySelector('.mobile-nav-active')) {
        event.preventDefault();
        this.classList.toggle('active');
        this.nextElementSibling.classList.toggle('dropdown-active');

        let dropDownIndicator = this.querySelector('.dropdown-indicator');
        dropDownIndicator.classList.toggle('bi-chevron-up');
        dropDownIndicator.classList.toggle('bi-chevron-down');
      }
    })
  });

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Scroll top button
   */
  const scrollTop = document.querySelector('.scroll-top');
  if (scrollTop) {
<<<<<<< HEAD:FluxoDigno/templates/sistema/assets/js/main.js
    const togglescrollTop = function() {
=======
    const togglescrollTop = function () {
>>>>>>> eaa63c1fd0463413ba9910df95e52e639e4775d6:FluxoDigno/sistema/templates/assets/js/main.js
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
    window.addEventListener('load', togglescrollTop);
    document.addEventListener('scroll', togglescrollTop);
    scrollTop.addEventListener('click', window.scrollTo({
      top: 0,
      behavior: 'smooth'
    }));
  }

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Clients Slider
   */
  new Swiper('.clients-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 2,
        spaceBetween: 40
      },
      480: {
        slidesPerView: 3,
        spaceBetween: 60
      },
      640: {
        slidesPerView: 4,
        spaceBetween: 80
      },
      992: {
        slidesPerView: 6,
        spaceBetween: 120
      }
    }
  });

  /**
   * Init swiper slider with 1 slide at once in desktop view
   */
  new Swiper('.slides-1', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    }
  });

  /**
   * Init swiper slider with 3 slides at once in desktop view
   */
  new Swiper('.slides-3', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 40
      },

      1200: {
        slidesPerView: 3,
      }
    }
  });

  /**
   * Porfolio isotope and filter
   */
  let portfolionIsotope = document.querySelector('.portfolio-isotope');

  if (portfolionIsotope) {

    let portfolioFilter = portfolionIsotope.getAttribute('data-portfolio-filter') ? portfolionIsotope.getAttribute('data-portfolio-filter') : '*';
    let portfolioLayout = portfolionIsotope.getAttribute('data-portfolio-layout') ? portfolionIsotope.getAttribute('data-portfolio-layout') : 'masonry';
    let portfolioSort = portfolionIsotope.getAttribute('data-portfolio-sort') ? portfolionIsotope.getAttribute('data-portfolio-sort') : 'original-order';

    window.addEventListener('load', () => {
      let portfolioIsotope = new Isotope(document.querySelector('.portfolio-container'), {
        itemSelector: '.portfolio-item',
        layoutMode: portfolioLayout,
        filter: portfolioFilter,
        sortBy: portfolioSort
      });

      let menuFilters = document.querySelectorAll('.portfolio-isotope .portfolio-flters li');
<<<<<<< HEAD:FluxoDigno/templates/sistema/assets/js/main.js
      menuFilters.forEach(function(el) {
        el.addEventListener('click', function() {
=======
      menuFilters.forEach(function (el) {
        el.addEventListener('click', function () {
>>>>>>> eaa63c1fd0463413ba9910df95e52e639e4775d6:FluxoDigno/sistema/templates/assets/js/main.js
          document.querySelector('.portfolio-isotope .portfolio-flters .filter-active').classList.remove('filter-active');
          this.classList.add('filter-active');
          portfolioIsotope.arrange({
            filter: this.getAttribute('data-filter')
          });
          if (typeof aos_init === 'function') {
            aos_init();
          }
        }, false);
      });

    });

  }

  /**
   * Animation on scroll function and init
   */
  function aos_init() {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', () => {
    aos_init();
  });

<<<<<<< HEAD:FluxoDigno/templates/sistema/assets/js/main.js
});
=======
});


/* 
* Proximo formulário Cadastro de Ponto de Coleta
*/
const nomePosto = document.getElementById('exampleInputNomePosto');
const bairro = document.getElementById('exampleInputBairro');
const rua = document.getElementById('exampleInputRua');
const numero = document.getElementById('exampleInputNumero');
const pix = document.getElementById('exampleInputPix');
const horaAbrir = document.getElementById('exampleInputHorarioAbrir');
const horaFechar= document.getElementById('exampleInputHorarioFechar');
const telefone = document.getElementById('exampleInputTelefone');
const form1 = document.getElementById('formPontoColeta1');
const form2 = document.getElementById('formPontoColeta2');
form2.style.display = 'none';
const buttonNext1 = document.getElementById('button-next-1');

form1.addEventListener('submit', (e) => {
  e.preventDefault()
  checkInputsForm1();
})

form2.addEventListener('submit', (e) => {
  e.preventDefault()
  checkInputsForm2();
})

function checkInputsForm1() {
  const nomePostoValue = nomePosto.value.trim();
  const bairroValue = bairro.value.trim();
  const ruaValue = rua.value.trim();
  const numeroValue = numero.value.trim();
  const pixValue = pix.value.trim();

  const valideNomePosto = validateInput(nomePosto, nomePostoValue);
  const valideBairro = validateInput(bairro, bairroValue);
  const valideRua = validateInput(rua, ruaValue);
  const valideNumero = validateInput(numero, numeroValue);
  const validePix = validateInput(pix, pixValue);

  if (
    valideNomePosto &&
    valideBairro &&
    valideRua &&
    valideNumero &&
    validePix
  ) {
    form1.style.display = 'none';
    form2.style.display = 'block';
  }

}
function checkInputsForm2() {
  const horaAbrirValue = horaAbrir.value.trim();
  const horaFecharValue = horaFechar.value.trim();
  const telefoneValue = telefone.value.trim();

  const valideHoraAbrir = validateInput(horaAbrir, horaAbrirValue);
  const valideHoraFechar = validateInput(horaFechar, horaFecharValue);
  const valideTelefone = validateInput(telefone, telefoneValue);

  if(
    valideHoraAbrir &&
    valideHoraFechar &&
    valideTelefone
  ) {
    window.location.replace("./sucessoCadastro.html");
  }
}


function validateInput(input, value) {
  if (value === "") {
    errorValidation(input, "Preencha esse campo")
    return false;
  }
  successValidation(input)
  return true;
}

function successValidation(input) {
  input.classList.remove('error');
  input.classList.add('success');
}

function errorValidation(input, message) {
  const formControl = input.parentElement;
  formControl.querySelector("small").innerText = message;
  input.classList.remove('success');
  input.classList.add('error');
}
>>>>>>> eaa63c1fd0463413ba9910df95e52e639e4775d6:FluxoDigno/sistema/templates/assets/js/main.js
