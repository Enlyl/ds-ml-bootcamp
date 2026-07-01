self.addEventListener('install',()=>self.skipWaiting());

self.addEventListener('activate',e=>e.waitUntil(clients.claim()));

self.addEventListener('fetch',e=>{
  e.respondWith(
    caches.open('dsml-v1').then(c=>c.match(e.request).then(r=>r||fetch(e.request).then(res=>{
      if(res.ok&&res.type==='basic')c.put(e.request,res.clone());
      return res;
    }).catch(()=>new Response('Offline',{status:503}))))
  );
});
