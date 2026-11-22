// Runs inside the Cloudflare dashboard tab. Pulls the site from GitHub, self-hosts photos, deploys to Pages.
window.__sawDeploy = async function (BASE, log = console.log) {
  const A = 'f805f3d6181f854be25e71ff3bf28450', X = { 'x-atok': window.__H['x-atok'] };
  const man = await (await fetch(BASE + 'manifest.json', { cache: 'no-store' })).json();
  const TYPES = { html: 'text/html', css: 'text/css', js: 'application/javascript', svg: 'image/svg+xml', xml: 'application/xml', txt: 'text/plain', json: 'application/json',
    woff2: 'font/woff2', mp4: 'video/mp4', m4a: 'audio/mp4', jpg: 'image/jpeg', png: 'image/png' };
  const b64 = buf => { const b = new Uint8Array(buf); let r = ''; for (let i = 0; i < b.length; i += 0x8000) r += String.fromCharCode.apply(null, b.subarray(i, i + 0x8000)); return btoa(r); };
  const hash = async (v, ext) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(v + ext)))].map(b => b.toString(16).padStart(2, '0')).join('').slice(0, 32);
  const files = {}; let special = {};
  const pool = async (list, n, fn) => { let i = 0; await Promise.all(Array.from({ length: n }, async () => { while (i < list.length) { const k = list[i++]; await fn(k); } })); };
  await pool(man.files, 8, async p => {
    const r = await fetch(BASE + 'site' + p, { cache: 'no-store' }); if (!r.ok) throw new Error('missing ' + p);
    const buf = await r.arrayBuffer();
    if (p === '/_headers' || p === '/_redirects' || p === '/_worker.js') { special[p] = new TextDecoder().decode(buf); return; }
    files[p] = [b64(buf), TYPES[p.split('.').pop()] || 'application/octet-stream'];
  });
  log('site files ' + Object.keys(files).length);
  // photos: use copies committed under site/img when present; otherwise the worker serves them from Unsplash through the Cloudflare cache
  log('images from repo ' + Object.keys(files).filter(p => p.startsWith('/img/')).length);
  if (window.__BIN) for (const [p, [v, t]] of Object.entries(window.__BIN)) if (!files[p]) files[p] = [v, t];
  const mf = {}, items = [];
  for (const [p, [v, t]] of Object.entries(files)) { const h = await hash(v, p.split('.').pop()); mf[p] = h; items.push({ key: h, value: v, metadata: { contentType: t }, base64: true }); }
  const tok = await (await fetch(`/api/v4/accounts/${A}/pages/projects/saweli/upload-token`, { credentials: 'include', headers: X })).json();
  const auth = { ...X, Authorization: 'Bearer ' + tok.result.jwt, 'content-type': 'application/json' };
  const cm = await (await fetch('/api/v4/pages/assets/check-missing', { method: 'POST', credentials: 'include', headers: auth, body: JSON.stringify({ hashes: Object.values(mf) }) })).json();
  const miss = new Set(cm.result); const todo = items.filter(i => miss.has(i.key));
  let batch = [], size = 0;
  const flush = async () => { if (!batch.length) return; const r = await (await fetch('/api/v4/pages/assets/upload', { method: 'POST', credentials: 'include', headers: auth, body: JSON.stringify(batch) })).json(); if (!r.success) throw new Error('upload ' + JSON.stringify(r.errors)); batch = []; size = 0; };
  for (const it of todo) { batch.push(it); size += it.value.length; if (size > 8e6 || batch.length >= 40) await flush(); }
  await flush();
  await fetch('/api/v4/pages/assets/upsert-hashes', { method: 'POST', credentials: 'include', headers: auth, body: JSON.stringify({ hashes: Object.values(mf) }) });
  log('uploaded ' + todo.length + ' of ' + items.length);
  const fd = new FormData(); fd.append('manifest', JSON.stringify(mf)); fd.append('branch', 'main');
  for (const n of ['_headers', '_redirects']) if (special['/' + n]) fd.append(n, new File([special['/' + n]], n));
  fd.append('_worker.js', new File([special['/_worker.js']], '_worker.js', { type: 'application/javascript+module' }));
  const d = await (await fetch(`/api/v4/accounts/${A}/pages/projects/saweli/deployments`, { method: 'POST', credentials: 'include', headers: X, body: fd })).json();
  return JSON.stringify({ ok: d.success, id: d.result && d.result.id, err: d.errors, files: items.length });
};
