(()=>{
const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
// header
const top=$('.top'),hero=$('.hero,.phero');
const onS=()=>{top&&top.classList.toggle('solid',!hero||scrollY>(hero.offsetHeight-90))};onS();addEventListener('scroll',onS,{passive:true});
const mb=$('.menu'),nav=$('#nav');mb&&mb.addEventListener('click',()=>{const o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o);top.classList.add('solid')});
$$('#nav a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');mb&&mb.setAttribute('aria-expanded','false')}));
// hero slides
const sl=$$('.slide'),bars=$$('.bars i'),cap=$('.cap-t');let si=0;
const show=i=>{sl.forEach((s,k)=>s.classList.toggle('on',k===i));bars.forEach((b,k)=>{b.classList.toggle('on',k===i);b.classList.toggle('done',k<i)});if(cap)cap.textContent=sl[i].dataset.cap||''};
if(sl.length){show(0);if(!reduce)setInterval(()=>{si=(si+1)%sl.length;show(si)},6500)}
// reveal
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.18,rootMargin:'0px 0px -6% 0px'});
$$('.r,.rw,.mapbox').forEach(el=>io.observe(el));
// map route lengths
$$('.draw').forEach(p=>{try{p.style.setProperty('--len',Math.ceil(p.getTotalLength()))}catch(_){}});
// lens merge on scroll
const lv=$('.lens-vis');
if(lv&&!reduce){const cl=$('.cl',lv),cr=$('.cr',lv),mid=$('.lens-mid',lv);
 const f=()=>{const r=lv.getBoundingClientRect(),vh=innerHeight;let p=1-(r.top+r.height/2-vh*.35)/(vh*.75);p=Math.max(0,Math.min(1,p));
  const d=(1-p)*lv.offsetWidth*.16;cl.style.transform=`translateX(${-d}px)`;cr.style.transform=`translateX(${d}px)`;if(mid)mid.style.opacity=Math.max(0,(p-.55)/.45)};
 f();addEventListener('scroll',f,{passive:true});addEventListener('resize',f)}
// sticky steps
const steps=$$('.steps li'),imgs=$$('.stick img'),cnt=$('.stick .count');
if(steps.length){const so=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){const i=steps.indexOf(e.target);steps.forEach((s,k)=>s.classList.toggle('on',k===i));imgs.forEach((m,k)=>m.classList.toggle('on',k===i));if(cnt)cnt.textContent=(i+1)+' / '+steps.length}}),{rootMargin:'-45% 0px -45% 0px'});steps.forEach(s=>so.observe(s))}
// tabs
$$('.tabs button').forEach(b=>b.addEventListener('click',()=>{$$('.tabs button').forEach(x=>x.setAttribute('aria-selected',x===b));$$('.pgrid').forEach(g=>g.hidden=g.id!==b.getAttribute('aria-controls'))}));
// logistics accordion
$$('.mode').forEach(m=>{const act=()=>{$$('.mode').forEach(x=>{x.classList.toggle('on',x===m);x.setAttribute('aria-expanded',x===m)})};m.addEventListener('mouseenter',act);m.addEventListener('click',act);m.addEventListener('focus',act)});
// rail drag
const rail=$('.rail');if(rail){let down=false,sx=0,sl0=0,moved=false;
 rail.addEventListener('pointerdown',e=>{if(e.pointerType!=='mouse')return;down=true;moved=false;sx=e.clientX;sl0=rail.scrollLeft;rail.classList.add('drag')});
 addEventListener('pointermove',e=>{if(!down)return;const dx=e.clientX-sx;if(Math.abs(dx)>4)moved=true;rail.scrollLeft=sl0-dx});
 addEventListener('pointerup',()=>{down=false;rail.classList.remove('drag')});
 $$('.rail-nav button').forEach(b=>b.addEventListener('click',()=>rail.scrollBy({left:(b.dataset.d==='1'?1:-1)*rail.clientWidth*.8,behavior:'smooth'})))}
// bank parallax
const bp=$('.bank .ph img');if(bp&&!reduce){const f=()=>{const r=bp.parentElement.getBoundingClientRect();bp.style.transform=`translateY(${(r.top/innerHeight)*-8}%)`};f();addEventListener('scroll',f,{passive:true})}
// form
$$('form.enq').forEach(f=>f.addEventListener('submit',async e=>{e.preventDefault();const m=$('.form-msg',f),b=$('button[type=submit]',f),l=b.textContent;b.disabled=true;b.textContent=f.dataset.sending;m.className='form-msg';
 try{const r=await fetch(f.action,{method:'POST',body:new FormData(f),headers:{Accept:'application/json'}});if(!r.ok)throw 0;m.textContent=f.dataset.ok;m.className='form-msg ok';f.reset()}catch(_){m.textContent=f.dataset.err;m.className='form-msg err'}
 b.disabled=false;b.textContent=l}));
})();
