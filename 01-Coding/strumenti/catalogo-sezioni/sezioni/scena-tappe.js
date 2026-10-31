/* scena-tappe — da Groavel, commit a6a1751 (src/scripts/spina.js, funzione scena), riscritta senza GSAP.
   Da 1024 px: una tappa attiva alla volta, quella che passa la meta' dello schermo. La foto della cornice cambia con
   opacita' e transform (lavoro del compositore, nessuna ridipintura), il dato e il nome si aggiornano.
   Sotto 1024 px, con ?cattura o senza IntersectionObserver non fa niente: la pagina e' gia' completa.
   Con reduced-motion la foto cambia lo stesso, senza transizione (base.css accorcia le durate). */
(function(){
  var doc = document.documentElement;
  if (doc.classList.contains('cattura') || !('IntersectionObserver' in window)) return;
  var largo = matchMedia('(min-width: 1024px)');
  document.querySelectorAll('[data-scena]').forEach(function(sezione){
    var tappe = Array.prototype.slice.call(sezione.querySelectorAll('[data-tappa]'));
    var foto = Array.prototype.slice.call(sezione.querySelectorAll('[data-scena-foto]'));
    var dato = sezione.querySelector('[data-scena-dato]');
    var nome = sezione.querySelector('[data-scena-nome]');
    if (!tappe.length || !foto.length) return;
    var corrente = -1;

    function attiva(i){
      if (i === corrente) return;
      corrente = i;
      tappe.forEach(function(t, j){ t.toggleAttribute('data-attivo', j === i); });
      if (dato) dato.textContent = tappe[i].dataset.dato || '';
      if (nome) nome.textContent = tappe[i].dataset.nome || '';
      var arriva = foto[i];
      if (!arriva || arriva.hasAttribute('data-visibile')) return;
      foto.forEach(function(f){
        f.removeAttribute('data-uscente');
        if (f.hasAttribute('data-visibile')) { f.removeAttribute('data-visibile'); f.setAttribute('data-uscente', ''); }
      });
      arriva.setAttribute('data-visibile', '');
    }

    // la riga di scatto e' la meta' dello schermo: una tappa e' attiva finche' la attraversa
    var oss = new IntersectionObserver(function(voci){
      voci.forEach(function(v){ if (v.isIntersecting) attiva(tappe.indexOf(v.target)); });
    }, { rootMargin: '-50% 0px -50% 0px' });

    function monta(){
      if (largo.matches) { sezione.classList.add('scena--viva'); tappe.forEach(function(t){ oss.observe(t); }); }
      else { oss.disconnect(); sezione.classList.remove('scena--viva'); }
    }
    monta();
    largo.addEventListener('change', monta);
  });
})();
