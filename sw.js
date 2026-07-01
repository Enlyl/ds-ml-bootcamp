self.addEventListener('install',()=>self.skipWaiting());

self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!=='dsml-v2').map(k=>caches.delete(k)))).then(()=>clients.claim())));

self.addEventListener('fetch',e=>{
  e.respondWith(
    caches.open('dsml-v2').then(c=>c.match(e.request).then(r=>r||fetch(e.request).then(res=>{
      if(res.ok&&res.type==='basic')c.put(e.request,res.clone());
      return res;
    }).catch(()=>new Response('Offline',{status:503}))))
  );
});
