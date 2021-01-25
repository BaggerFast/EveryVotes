document.addEventListener('scroll', function (e) {
  if (window.scrollY > 100) {
    ttt.classList.remove("hidden-ttt");
    ttt.classList.add("visible-ttt");
  }
  else {
    ttt.classList.remove("visible-ttt");
    ttt.classList.add("hidden-ttt");
  }
});

ttt.addEventListener('click', function (e) {
  window.scroll({
    top: 0,
    behavior: 'smooth'
  });
});
