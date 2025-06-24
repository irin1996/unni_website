const toTopBtn = document.getElementById('toTopBtn');
const footer = document.querySelector('footer'); // Select the footer element

window.addEventListener('scroll', () => {
  const scrollPosition = document.documentElement.scrollTop || document.body.scrollTop;
  const windowHeight = window.innerHeight;
  const footerTop = footer.offsetTop; // Get the top position of the footer

  // Show button only when scrolled down but hide it when reaching the footer
  if (scrollPosition + windowHeight < footerTop) {
    toTopBtn.style.opacity = "1"; // Show button
    toTopBtn.style.pointerEvents = "auto"; // Enable button interaction
  } else {
    toTopBtn.style.opacity = "0"; // Hide button
    toTopBtn.style.pointerEvents = "none"; // Disable button interaction
  }
});

// Smooth scroll to the top when the button is clicked
toTopBtn.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
