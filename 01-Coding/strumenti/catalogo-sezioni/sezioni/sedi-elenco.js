/* sedi-elenco — da NG Barber, commit 648187b (lightUp delle sedi), senza pin e senza GSAP.
   Da 900 px: la sede che attraversa la meta' dello schermo si accende, le altre si spengono, e nella cornice ferma
   entra la sua foto con una dissolvenza (solo opacita'). Sotto 900 px, con ?cattura o senza IntersectionObserver
   non fa niente: tutte le sedi restano accese, come NG Barber le teneva sul telefono. */
(function(){
  var doc = document.documentElement;
  if (doc.classList.contains('cattura') || !('IntersectionObserver' in window)) return;
  var largo = matchMedia('(min-width: 900px)');
  document.querySelectorAll('[data-sedi]').forEach(function(sezione){
    var sedi = Array.prototype.slice.call(sezione.querySelectorAll('[data-sede]'));
    var foto = Array.prototype.slice.call(sezione.querySelectorAll('[data-sede-foto]'));
    if (!sedi.length) return;
    function accendi(i){
      sedi.forEach(function(s, j){ s.toggleAttribute('data-attiva', j === i); });
      foto.forEach(function(f, j){ f.toggleAttribute('data-visibile', j === i); });
    }
    var oss = new IntersectionObserver(function(voci){
      voci.forEach(function(v){ if (v.isIntersecting) accendi(sedi.indexOf(v.target)); });
    }, { rootMargin: '-50% 0px -50% 0px' });
    function monta(){
      if (largo.matches) { sezione.classList.add('sedi--viva'); accendi(0); sedi.forEach(function(s){ oss.observe(s); }); }
      else { oss.disconnect(); sezione.classList.remove('sedi--viva'); }
    }
    monta();
    largo.addEventListener('change', monta);
  });
})();
