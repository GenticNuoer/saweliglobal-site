(()=>{
const d=document,w=window,$=(s,c=d)=>c.querySelector(s),$$=(s,c=d)=>[...c.querySelectorAll(s)];
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
const root=d.documentElement;
// loader: first page of a visit only
const ld=$('.loader');
if(ld){let seen=false;try{seen=sessionStorage.getItem('sw-l')}catch(e){}
 if(seen||RM){ld.remove()}else{try{sessionStorage.setItem('sw-l',1)}catch(e){}
  w.addEventListener('load',()=>setTimeout(()=>{ld.classList.add('go');setTimeout(()=>ld.remove(),1300)},900));setTimeout(()=>ld&&ld.classList.add('go'),3200)}}
// split headings into words
$$('[data-split]').forEach(el=>{const walk=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=d.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(p=>{if(!p)return;if(/^\s+$/.test(p)){f.appendChild(d.createTextNode(p));return}const o=d.createElement('span');o.className='w';const i=d.createElement('span');i.textContent=p;o.appendChild(i);f.appendChild(o)});c.replaceWith(f)}else if(c.nodeType===1&&!c.classList.contains('w'))walk(c)})};walk(el);el.classList.add('split');$$('.w>span',el).forEach((s,i)=>s.style.transitionDelay=(i*0.055+(+el.dataset.split||0))+'s')});
// reveal
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px',threshold:.08});
$$('.r,.clip,.split,.mapbox').forEach(el=>io.observe(el));
$$('.hero .split,.phero .split').forEach(el=>setTimeout(()=>el.classList.add('in'),ld&&ld.isConnected?1100:150));
// map path lengths
$$('.draw').forEach(p=>{try{p.style.setProperty('--len',Math.ceil(p.getTotalLength()))}catch(e){}});
// header
const top=$('.top'),hero=$('.hero,.phero');let lastY=0;
const prog=$('.prog'),wa=$('.wa');
let ticking=false;
function onScroll(){const y=w.scrollY,h=hero?hero.offsetHeight-90:40;
 top.classList.toggle('solid',y>h||!hero);
 top.classList.toggle('hide',y>lastY&&y>600&&!root.classList.contains('menu-open'));lastY=y;
 if(prog){const m=d.documentElement.scrollHeight-innerHeight;prog.style.transform=`scaleX(${m>0?y/m:0})`}
 if(wa)wa.classList.toggle('on',y>500);
 par();journey();statement();ticking=false}
w.addEventListener('scroll',()=>{if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});
// menu
const bg=$('.burger');if(bg)bg.addEventListener('click',()=>{const o=root.classList.toggle('menu-open');bg.setAttribute('aria-expanded',o);d.body.style.overflow=o?'hidden':''});
$$('.drawer a').forEach(a=>a.addEventListener('click',()=>{root.classList.remove('menu-open');d.body.style.overflow=''}));
// cursor
const cur=$('.cur');
if(cur&&matchMedia('(hover:hover) and (pointer:fine)').matches&&!RM){let x=0,y=0,cx=0,cy=0;
 w.addEventListener('mousemove',e=>{x=e.clientX;y=e.clientY;cur.classList.add('on')});
 d.addEventListener('mouseleave',()=>cur.classList.remove('on'));
 (function loop(){cx+=(x-cx)*.2;cy+=(y-cy)*.2;cur.style.transform=`translate(${cx}px,${cy}px)`;requestAnimationFrame(loop)})();
 d.addEventListener('mouseover',e=>{const t=e.target.closest('[data-cur],.svc a,.bento article,.rail a,.jcard,.port,.mode');cur.classList.toggle('big',!!t);$('span',cur).textContent=t?(t.dataset.cur||(t.matches('.rail')||t.closest('.rail')?'Drag':'View')):''});
 // magnetic buttons
 $$('.btn').forEach(b=>{b.addEventListener('mousemove',e=>{const r=b.getBoundingClientRect();b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.18}px,${(e.clientY-r.top-r.height/2)*.3}px)`});b.addEventListener('mouseleave',()=>b.style.transform='')})}
// hero slides
const hs=$('.hero');if(hs){const sl=$$('.slide',hs),dots=$$('.dots button',hs),cap=$('.cap .t',hs);let i=0,tm;
 const show=n=>{sl[i].classList.remove('on');dots[i]&&dots[i].classList.remove('on');i=(n+sl.length)%sl.length;sl[i].classList.add('on');if(dots[i]){void dots[i].offsetWidth;dots[i].classList.add('on')}if(cap)cap.textContent=sl[i].dataset.cap;
  const im=$('img',sl[(i+1)%sl.length]);if(im&&im.loading==='lazy')im.loading='eager';clearTimeout(tm);tm=setTimeout(()=>show(i+1),7000)};
 dots.forEach((b,n)=>b.addEventListener('click',()=>show(n)));if(!RM)tm=setTimeout(()=>show(1),7000)}
// parallax
const pars=$$('[data-par]');
function par(){if(RM)return;pars.forEach(el=>{const r=el.parentElement.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;const k=+el.dataset.par||.15;el.style.transform=`translate3d(0,${(r.top)*-k}px,0)`})}
// horizontal journey
const jr=$('.journey');
function journey(){if(!jr||innerWidth<=760)return;const tr=$('.track',jr),r=jr.getBoundingClientRect(),max=jr.offsetHeight-innerHeight;const p=Math.min(1,Math.max(0,-r.top/max));const dist=tr.scrollWidth-innerWidth;tr.style.transform=`translate3d(${-p*dist}px,0,0)`;const pi=$('.jprog i',jr);if(pi)pi.style.transform=`scaleX(${p})`}
// statement scrub
const st=$('.statement');let words=[];
if(st){const walk=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=d.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(p=>{if(!p)return;if(/^\s+$/.test(p)){f.appendChild(d.createTextNode(p));return}const s=d.createElement('span');s.className='wd'+(c.parentElement.tagName==='EM'?' t':'');s.textContent=p;f.appendChild(s)});c.replaceWith(f)}else if(c.nodeType===1)walk(c)})};walk(st);words=$$('.wd',st)}
function statement(){if(!st)return;const r=st.getBoundingClientRect();const p=Math.min(1,Math.max(0,(innerHeight*.85-r.top)/(r.height+innerHeight*.35)));const n=Math.round(p*words.length);words.forEach((x,i)=>x.classList.toggle('on',i<n||RM))}
// counters
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;const el=e.target,to=+el.dataset.count,t0=performance.now();cio.unobserve(el);if(RM){el.textContent=to;return}(function f(t){const k=Math.min(1,(t-t0)/1600),v=Math.round(to*(1-Math.pow(1-k,3)));el.textContent=v;if(k<1)requestAnimationFrame(f)})(t0)}),{threshold:.5});
$$('[data-count]').forEach(el=>cio.observe(el));
// sticky steps
const sx=$('.stepsx');if(sx){const items=$$('ol>li',sx),ims=$$('.stick img',sx),lbl=$('.stick .lbl',sx);
 const so=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){const n=items.indexOf(e.target);items.forEach((x,i)=>x.classList.toggle('on',i===n));ims.forEach((x,i)=>x.classList.toggle('on',i===n));if(lbl)lbl.textContent=(n+1)+' / '+items.length}}),{rootMargin:'-45% 0px -45% 0px'});items.forEach(x=>so.observe(x))}
// tabs
$$('.tabs').forEach(tb=>{const bs=$$('button',tb);bs.forEach(b=>b.addEventListener('click',()=>{bs.forEach(x=>{x.setAttribute('aria-selected',x===b);const p=d.getElementById(x.getAttribute('aria-controls'));if(p)p.hidden=x!==b});const p=d.getElementById(b.getAttribute('aria-controls'));$$('.r,.clip',p).forEach(e=>e.classList.add('in'))}))});
// modes
$$('.modes').forEach(m=>{const ms=$$('.mode',m);ms.forEach(x=>{const on=()=>ms.forEach(y=>{y.classList.toggle('on',y===x);y.setAttribute('aria-expanded',y===x)});x.addEventListener('mouseenter',on);x.addEventListener('click',on);x.addEventListener('focus',on)})});
// rails
$$('.rail').forEach(r=>{let down=false,sx=0,sl=0,moved=false;r.addEventListener('pointerdown',e=>{if(e.pointerType!=='mouse')return;down=true;moved=false;sx=e.clientX;sl=r.scrollLeft;r.classList.add('drag')});
 w.addEventListener('pointermove',e=>{if(!down)return;const dx=e.clientX-sx;if(Math.abs(dx)>4)moved=true;r.scrollLeft=sl-dx});
 w.addEventListener('pointerup',()=>{down=false;r.classList.remove('drag')});r.addEventListener('click',e=>{if(moved){e.preventDefault();moved=false}},true);
 const nav=d.querySelector(`[data-rail="${r.id}"]`);if(nav)$$('button',nav).forEach(b=>b.addEventListener('click',()=>r.scrollBy({left:(+b.dataset.dir)*r.clientWidth*.7,behavior:'smooth'})))});
// forms
async function send(f,url,msg){const m=$(msg,f)||f.nextElementSibling;try{const r=await fetch(url,{method:'POST',body:new FormData(f),headers:{Accept:'application/json'}});if(!r.ok)throw 0;m.textContent=f.dataset.ok;m.className=(m.className.split(' ')[0])+' ok';f.reset()}catch(_){m.textContent=f.dataset.err;m.className=(m.className.split(' ')[0])+' err'}}
$$('form.enq').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();send(f,'/api/enquiry','.form-msg')}));
$$('form.sub').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();send(f,'/api/subscribe','.submsg')}));
// prefill product from query
const q=new URLSearchParams(location.search).get('need');if(q){const t=$('form.enq textarea');if(t)t.value=q}
onScroll();
})();
