const J=(b,s=200)=>new Response(JSON.stringify(b),{status:s,headers:{'content-type':'application/json'}});
const esc=s=>String(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
export default {
 async fetch(req,env){
  const url=new URL(req.url);
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
