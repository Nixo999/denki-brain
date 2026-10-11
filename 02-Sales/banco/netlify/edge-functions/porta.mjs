// La porta del banco: senza una sessione buona la pagina manda al login e le
// liste rispondono 401. Sta davanti a tutto tranne login, API (le funzioni
// controllano da sole), icone e manifest: cosi' anche /Index.html, /index o
// un percorso inventato passano di qui.
import { chi } from '../sessione.mjs';

export default async (req) => {
  if (await chi(req)) return; // prosegue verso il file statico
  if (new URL(req.url).pathname.toLowerCase().startsWith('/dati/')) {
    return new Response('', { status: 401, headers: { 'cache-control': 'no-store' } });
  }
  return new Response('', { status: 302, headers: { location: '/login', 'cache-control': 'no-store' } });
};

export const config = {
  path: '/*',
  excludedPath: ['/login*', '/api/*', '/icone/*', '/manifest.webmanifest'],
};
