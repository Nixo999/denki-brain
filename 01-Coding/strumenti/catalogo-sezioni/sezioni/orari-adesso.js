/* orari-adesso — da Fiftynine, commit 16b3492 (index.html, «la linea del giorno»), generalizzato a piu' fasce.
   Legge gli orari dalla lista (unico posto dove sono scritti), calcola l'ora di Roma e accende l'indicatore e il
   binario. Si aggiorna ogni minuto. Funziona anche in ?cattura: e' un dato, non un'animazione. */
(function(){
  var GIORNI = ['domenica','lunedì','martedì','mercoledì','giovedì','venerdì','sabato'];
  function minuti(hhmm){ var p = hhmm.split(':'); return (+p[0]) * 60 + (+p[1]); }
  function ore(min){ return Math.floor(min / 60) + ':' + ('0' + (min % 60)).slice(-2); }
  function adessoRoma(){
    try {
      var p = new Intl.DateTimeFormat('en-US', { timeZone: 'Europe/Rome', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
      var trova = function(t){ return p.find(function(x){ return x.type === t; }).value; };
      return { g: { Sun:0, Mon:1, Tue:2, Wed:3, Thu:4, Fri:5, Sat:6 }[trova('weekday')], min: (+trova('hour') % 24) * 60 + (+trova('minute')) };
    } catch (e) { var d = new Date(); return { g: d.getDay(), min: d.getHours() * 60 + d.getMinutes() }; }
  }

  document.querySelectorAll('[data-orari]').forEach(function(sezione){
    var lista = sezione.querySelector('[data-orari-lista]');
    var adesso = sezione.querySelector('[data-orari-adesso]');
    var binario = sezione.querySelector('[data-orari-binario]');
    if (!lista || !adesso) return;
    // ORARI[g] = [[apre, chiude], ...] oppure un array vuoto se quel giorno e' chiuso
    var ORARI = [], righe = [];
    lista.querySelectorAll('li').forEach(function(li){
      var t = li.querySelectorAll('time'), fasce = [];
      for (var k = 0; k + 1 < t.length; k += 2) fasce.push([minuti(t[k].getAttribute('datetime')), minuti(t[k + 1].getAttribute('datetime'))]);
      (li.getAttribute('data-giorni') || '').split(',').forEach(function(g){ if (g !== '') { ORARI[+g] = fasce; righe[+g] = li; } });
    });
    if (!ORARI.some(function(f){ return f && f.length; })) return;   // nessun orario scritto: resta la lista com'e'

    var testo = adesso.querySelector('span');
    var pieno = sezione.querySelector('[data-orari-pieno]'), cursore = sezione.querySelector('[data-orari-cursore]');
    var apre = sezione.querySelector('[data-orari-apre]'), chiude = sezione.querySelector('[data-orari-chiude]');

    function aggiorna(){
      var ora = adessoRoma(), min = ora.min, oggi = ORARI[ora.g] || [];
      lista.querySelectorAll('li').forEach(function(li){ li.toggleAttribute('data-oggi', li === righe[ora.g]); });
      var dentro = oggi.find(function(f){ return min >= f[0] && min < f[1]; });
      if (dentro) {
        adesso.classList.remove('chiuso');
        testo.textContent = 'Aperto adesso · chiude alle ' + ore(dentro[1]);
      } else {
        // la prossima apertura: piu' tardi oggi, se no il primo giorno che apre
        var prossima = oggi.find(function(f){ return f[0] > min; }), quando = '';
        if (prossima) prossima = prossima[0];
        for (var k = 1; k <= 7 && prossima == null; k++) {
          var d = ORARI[(ora.g + k) % 7];
          if (d && d.length) { prossima = d[0][0]; quando = k === 1 ? ' domani' : ' ' + GIORNI[(ora.g + k) % 7]; }
        }
        adesso.classList.add('chiuso');
        testo.textContent = prossima == null ? 'Chiuso' : 'Chiuso adesso · riapre' + quando + ' alle ' + ore(prossima);
      }
      adesso.hidden = false;
      if (!binario) return;
      if (!oggi.length) { binario.hidden = true; return; }
      var inizio = oggi[0][0], fine = oggi[oggi.length - 1][1];
      var q = Math.max(0, Math.min(1, (min - inizio) / (fine - inizio)));
      binario.hidden = false;
      apre.textContent = ore(inizio); chiude.textContent = ore(fine);
      pieno.style.width = (q * 100).toFixed(1) + '%';
      cursore.style.left = (q * 100).toFixed(1) + '%';
      cursore.classList.toggle('visibile', min >= inizio && min < fine);
    }
    aggiorna();
    setInterval(aggiorna, 60000);
  });
})();
