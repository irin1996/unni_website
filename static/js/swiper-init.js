// Initialize Swiper.js
const swiper = new Swiper('.swiper-container', {
  slidesPerView: 3, // Show 3 items at a time
  spaceBetween: 30, // Space between slides
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  loop: true, // Enable infinite scrolling
  autoplay: {
    delay: 3000, // Time between slides (in milliseconds)
    disableOnInteraction: false, // Continue autoplay after user interaction
  },
});

const swiperContainer = document.querySelector('.swiper-container');

// Pause autoplay on hover
swiperContainer.addEventListener('mouseenter', () => {
  swiper.autoplay.stop();
});

// Resume autoplay when hover ends
swiperContainer.addEventListener('mouseleave', () => {
  swiper.autoplay.start();
});