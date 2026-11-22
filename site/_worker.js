const J=(b,s=200)=>new Response(JSON.stringify(b),{status:s,headers:{'content-type':'application/json'}});
const esc=s=>String(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const IMG={"cn_market": "photo-1748406144100-e2f1c470e1ae", "cn_line": "photo-1700727448686-b314cb5f9948", "hero_port": "photo-1590496793907-4d66e2994b4d", "ship_aerial": "photo-1699588999949-e25959a59550", "mog_port": "photo-1763454319156-a36c4761e794", "tz_containers": "photo-1678182451047-196f22a4143e", "dar_port": "photo-1561702469-c4239ced3f47", "nbo_skyline": "photo-1611348524140-53c9a25263d6", "cn_wholesale": "photo-1787013847671-8a24b4b1e0ff", "cn_inspector": "photo-1700727448575-6f1680cd7d75", "ship_aerial2": "photo-1613690399151-65ea69478674", "handshake": "photo-1521791136064-7986c2920216", "trader_phone": "photo-1687422809654-579d81c29d32", "cn_factorywoman": "photo-1572081608077-1af152703136", "ship_loading": "photo-1769144256181-698b8f807066", "phone_acc": "photo-1624823183493-ed5832f48f18", "solar": "photo-1679046410011-b6bf7ce71f22", "fabric_rolls": "photo-1705250466297-90035b3a2b26", "furniture": "photo-1687180498602-5a1046defaa4", "engine": "photo-1486262715619-67b85e0b08d3", "steel": "photo-1697698532634-ea59b636ccea", "ceramics_colour": "photo-1524259493079-d51c2c78adfe", "coffee_harvest": "photo-1775434657007-549ae5d21bd4", "sesame": "photo-1776669236271-5cfe72d74755", "resin": "photo-1790821074454-7bd7570c53d9", "goats": "photo-1713884985824-808512e41eb4", "fruit_stall": "photo-1781684025382-fb7e6dff59c4", "green_coffee": "photo-1508061110522-9ee0a799e290", "market_greens": "photo-1572861875689-0d8553d82f60", "coffee_sack": "photo-1524350876685-274059332603", "containers_aerial": "photo-1562892302-97faedd66f1c", "mog_aerial": "photo-1723151684036-d014403c33b2", "dar_skyline": "photo-1766730251071-fe1a835875db", "add_street": "photo-1771495562804-373fb516114c", "kla_skyline": "photo-1763220207281-c4d0febb61a8", "dji_aerial": "photo-1558389875-904e76f96b9c", "nansha_view": "photo-1764520681019-bd5a61491e76", "shenzhen_sunset": "photo-1759970729294-99c7eebeaf54", "shanghai_night": "photo-1474181487882-5abf3f0ba6c2", "cargo_plane": "photo-1571086291540-b137111fa1c7", "truck_road": "photo-1611746351408-c0a1346be8e8", "warehouse": "photo-1553413077-190dd305871c", "djibouti_port": "photo-1555686367-56d5186965d5", "dji_boats": "photo-1691499331978-a941b29cec88", "warehouse_yellow": "photo-1586528116311-ad8dd3c8310d", "containers_aerial2": "photo-1769144256227-5185141c3aca", "mog_coast": "photo-1661135401065-36dee543c72b"};
async function img(req,env,ctx,path){
 const m=path.match(/^\/img\/([a-z0-9_]+)-(800|1600)\.jpg$/);if(!m||!IMG[m[1]])return null;
 const a=await env.ASSETS.fetch(req);if(a.ok)return a;
 const cache=caches.default;const key=new Request(new URL(path,'https://saweli.com').toString());let r=await cache.match(key);if(r)return r;
 const up=await fetch(`https://images.unsplash.com/${IMG[m[1]]}?auto=format&fm=jpg&fit=crop&w=${m[2]}&q=${m[2]==='800'?72:70}`,{cf:{cacheEverything:true,cacheTtl:31536000}});
 if(!up.ok)return new Response('not found',{status:404});
 r=new Response(up.body,{headers:{'content-type':'image/jpeg','cache-control':'public, max-age=31536000, immutable','access-control-allow-origin':'*'}});
 ctx.waitUntil(cache.put(key,r.clone()));return r;
}
export default {
 async fetch(req,env,ctx){
  const url=new URL(req.url);
  if(url.pathname.startsWith('/img/')){const r=await img(req,env,ctx,url.pathname);if(r)return r}
  if(url.hostname==='www.saweli.com'){url.hostname='saweli.com';return Response.redirect(url.toString(),301);}
  if(url.pathname==='/api/enquiry'||url.pathname==='/api/subscribe'){
   if(req.method!=='POST')return J({error:'method'},405);
   let f;try{f=await req.formData();}catch(e){return J({error:'bad form'},400);}
   if(f.get('website'))return J({ok:true});
   const g=k=>String(f.get(k)||'').trim().slice(0,4000);
   const at=new Date().toISOString(),ipc=(req.cf&&req.cf.country)||'';
   if(url.pathname==='/api/subscribe'){const em=g('email').toLowerCase();if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em))return J({error:'email'},422);if(env.ENQUIRIES)await env.ENQUIRIES.put('sub:'+em,JSON.stringify({email:em,at,ip_country:ipc}));return J({ok:true});}
   const e={name:g('name'),company:g('company'),email:g('email'),phone:g('phone'),country:g('country'),role:g('role'),message:g('message'),lang:g('lang'),at,ip_country:ipc};
   if(!e.name||!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(e.email)||!e.message)return J({error:'missing fields'},422);
   const id=at+'-'+crypto.randomUUID().slice(0,8);
   if(env.ENQUIRIES)await env.ENQUIRIES.put('enq:'+id,JSON.stringify(e));
   return J({ok:true,id});
  }
  if(url.pathname==='/admin/enquiries'){
   const a=req.headers.get('authorization')||'';
   if(!(env.ADMIN_PASS&&a==='Basic '+btoa('saweli:'+env.ADMIN_PASS)))return new Response('Sign in required',{status:401,headers:{'www-authenticate':'Basic realm="Saweli enquiries"'}});
   const load=async pre=>{const l=await env.ENQUIRIES.list({prefix:pre,limit:1000});const out=[];for(const k of l.keys.reverse()){const v=await env.ENQUIRIES.get(k.name,'json');if(v)out.push(v)}return out};
   const rows=await load('enq:'),subs=await load('sub:');
   if(url.searchParams.get('format')==='json')return J({enquiries:rows,subscribers:subs});
   const cols=['at','role','name','company','email','phone','country','lang','message'];
   const tb=(c,r)=>'<table><tr>'+c.map(x=>'<th>'+x+'</th>').join('')+'</tr>'+r.map(o=>'<tr>'+c.map(x=>'<td>'+esc(o[x])+'</td>').join('')+'</tr>').join('')+'</table>';
   const html='<!doctype html><meta charset=utf-8><meta name=robots content=noindex><title>Saweli enquiries</title><style>body{font:14px system-ui;margin:24px;color:#2a1d14}table{border-collapse:collapse;width:100%;margin-bottom:40px}td,th{border-bottom:1px solid #e7dccf;padding:8px;text-align:left;vertical-align:top}th{background:#f6efe6}</style><h1>Enquiries ('+rows.length+')</h1><p><a href="?format=json">JSON</a></p>'+tb(cols,rows)+'<h2>Subscribers ('+subs.length+')</h2>'+tb(['at','email','ip_country'],subs);
   return new Response(html,{headers:{'content-type':'text/html; charset=utf-8','cache-control':'no-store'}});
  }
  return env.ASSETS.fetch(req);
 }
};
