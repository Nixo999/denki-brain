/* contrari-scorrevoli — da Mikuma giro 7, commit 38bb1bb (index.html, «3. I contrari si scambiano di lato»).
   Righe alterne in direzione opposta, in scrub legato allo scroll senza smorzamento (scrub: true, direttiva 20/10).
   Da 900 px lo scambio e' del 22% della riga; sotto, del 3%, perche' le coppie stanno intere nella larghezza.
   Esce subito con ?cattura, con reduced-motion o senza GSAP: le coppie restano ferme al centro. */
(function(){
  var doc = document.documentElement;
  if (doc.classList.contains('cattura') || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!window.gsap || !window.ScrollTrigger || !document.querySelector('[data-contrari]')) return;
  gsap.registerPlugin(ScrollTrigger);
  var mm = gsap.matchMedia();
  function scorri(amp){
    gsap.utils.toArray('[data-contrari] .contro__traccia').forEach(function(tr, i){
      var verso = i % 2 ? 1 : -1;
      gsap.fromTo(tr, { xPercent: amp * verso }, {
        xPercent: -amp * verso, ease: 'none',
        scrollTrigger: { trigger: tr.parentNode, start: 'top bottom', end: 'bottom top', scrub: true }
      });
    });
  }
  mm.add('(min-width: 901px)', function(){ scorri(22); });
  mm.add('(max-width: 900px)', function(){ scorri(3); });
})();
