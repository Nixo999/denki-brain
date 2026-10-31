/* barra-fissa — da Groavel, commit a6a1751 (Barra.astro). Senza questo file la barra funziona lo stesso.
   «scesa» dopo 80 px con una sentinella e un IntersectionObserver: niente ascolto dello scroll.
   Il menu del telefono e' un <details>: qui si aggiungono Esc, il clic fuori e la chiusura quando si sceglie una voce. */
(function(){
  var barra = document.querySelector('[data-barra]');
  var sentinella = document.querySelector('[data-sentinella]');
  if (barra && sentinella && 'IntersectionObserver' in window) {
    new IntersectionObserver(function(voci){ barra.classList.toggle('scesa', !voci[0].isIntersecting); }).observe(sentinella);
  }
  var menu = document.querySelector('[data-menu]');
  if (!menu) return;
  function chiudi(){ if (menu.open) menu.open = false; }
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && menu.open) { chiudi(); menu.querySelector('summary').focus(); }
  });
  document.addEventListener('click', function(e){ if (!menu.contains(e.target)) chiudi(); });
  menu.querySelectorAll('.barra__foglio a').forEach(function(a){ a.addEventListener('click', chiudi); });
})();
