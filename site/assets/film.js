/* Saweli how-it-works film: a scripted SVG animation driven by one clock */
(()=>{
const box=document.querySelector('.film');if(!box)return;
const data=JSON.parse(document.getElementById('film-data').textContent);
const NS='http://www.w3.org/2000/svg';
const T='#FF5A1F',U='#2B211B',U2='#1B1410',SH='#FFF8F1',SUN='#FFC93C',G='#6E625A',LN='#E8DCD2';
const SER="'Fraunces Variable',Fraunces,Georgia,serif",SAN="'Inter Variable',Inter,Arial,sans-serif",ZH="'Noto Serif SC',serif",ZHS="'Noto Sans SC',sans-serif";
const FV=`font-weight="300" style="font-variation-settings:'opsz' 144,'SOFT' 50"`;
const SC=[['intro',5],['order',7.2],['verify',8.2],['inspect',8.2],['ship',9],['pay',8.2],['end',5.6]];
let S=0;const START=SC.map(([n,d])=>{const s=S;S+=d;return s});const TOTAL=S;
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const p=(t,a,b)=>cl((t-a)/(b-a));
const eo=x=>1-Math.pow(1-x,3),eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2,back=x=>{const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const tick='M-9 0 L-3 6 L9 -7',cross='M-7 -7 L7 7 M7 -7 L-7 7';
const txt=(x,y,s,o='')=>`<text x="${x}" y="${y}" ${o}>${s}</text>`;
const title=(k,n,h,dark)=>`<g class="ttl"><text x="120" y="122" font-family="${SAN}" font-weight="600" font-size="21" letter-spacing="1" fill="${dark?SUN:T}">STEP ${n}<tspan font-family="${ZHS}" font-weight="500" dx="14">${data.zhStep[n-1]}</tspan></text><text x="116" y="196" font-family="${SER}" ${FV} font-size="66" fill="${dark?'#fff':U}">${h}</text><text x="120" y="244" font-family="${ZH}" font-weight="300" font-size="28" letter-spacing="3" fill="${dark?'rgba(255,255,255,.6)':G}">${data.zhTitle[n-1]}</text></g>`;
const svg=document.createElementNS(NS,'svg');svg.setAttribute('viewBox','0 0 1600 900');svg.setAttribute('role','img');svg.setAttribute('aria-label',data.label);
const L=data.land,sea=data.sea,seaS=data.seaS,cy=data.cities;
svg.innerHTML=`<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="24" stdDeviation="26" flood-color="#2B211B" flood-opacity=".18"/></filter>
<pattern id="gr" width="80" height="80" patternUnits="userSpaceOnUse"><path d="M80 0H0V80" fill="none" stroke="rgba(255,255,255,.05)"/></pattern></defs>
<rect width="1600" height="900" fill="${SH}"/>
<g id="s0"><rect width="1600" height="900" fill="${SH}"/>
 <clipPath id="mkc"><rect id="mkr" x="560" y="170" width="0" height="250"/></clipPath>
 <g id="mk"><image href="/brand/saweli-mark.svg" x="560" y="170" width="480" height="249" clip-path="url(#mkc)"/></g>
 <text id="i0" x="800" y="560" text-anchor="middle" font-family="${ZH}" font-weight="300" font-size="30" letter-spacing="14" fill="${T}">两个市场的交汇处</text>
 <text id="i1" x="800" y="650" text-anchor="middle" font-family="${SER}" ${FV} font-size="92" fill="${U}">How <tspan font-style="italic" fill="${T}">Saweli</tspan> works</text>
 <text id="i2" x="800" y="712" text-anchor="middle" font-family="${SAN}" font-weight="400" font-size="26" fill="${G}">From a factory in China to your shop in East Africa</text></g>
<g id="s1"><rect width="1600" height="900" fill="${SH}"/>
 <g id="ph" filter="url(#sh)"><rect x="200" y="110" width="440" height="720" rx="52" fill="#fff"/><rect x="200" y="110" width="440" height="720" rx="52" fill="none" stroke="${LN}" stroke-width="2"/>
  <rect x="360" y="132" width="120" height="10" rx="5" fill="${LN}"/>
  ${txt(244,214,'New order',`font-family="${SER}" ${FV} font-size="38" fill="${U}"`)}
  ${[0,1,2].map(i=>`<g transform="translate(244 ${262+i*120})"><text font-family="${SAN}" font-size="17" fill="${G}">${data.fields[i][0]}</text><rect y="16" width="352" height="62" rx="14" fill="${SH}"/><rect id="fb${i}" y="16" width="352" height="62" rx="14" fill="none" stroke="${T}" stroke-width="2.5" opacity="0"/><text id="fv${i}" x="18" y="56" font-family="${SAN}" font-size="23" fill="${U}"></text></g>`).join('')}
  <rect id="qb" x="244" y="650" width="352" height="70" rx="35" fill="${U}"/>${txt(420,694,'Get a quote',`text-anchor="middle" font-family="${SAN}" font-weight="600" font-size="22" fill="#fff"`)}
  <circle id="tap" cx="420" cy="685" r="0" fill="${T}" opacity=".35"/></g>
  <g>${txt(760,292,`STEP 1<tspan font-family="${ZHS}" font-weight="500" dx="14">${data.zhStep[0]}</tspan>`,`font-family="${SAN}" font-weight="600" font-size="21" letter-spacing="1" fill="${T}"`)}${txt(756,366,'Tell us what you need',`font-family="${SER}" ${FV} font-size="66" fill="${U}"`)}${txt(760,414,data.zhTitle[0],`font-family="${ZH}" font-weight="300" font-size="28" letter-spacing="3" fill="${G}"`)}${txt(760,456,'Send the order, or a supplier you already use.',`font-family="${SAN}" font-size="24" fill="${G}"`)}</g>
 <g id="qc" filter="url(#sh)"><rect x="760" y="480" width="640" height="300" rx="28" fill="#fff"/>
  ${txt(800,538,'Your quote',`font-family="${SER}" ${FV} font-size="32" fill="${U}"`)}${txt(1360,538,'Full cost shown first',`text-anchor="end" font-family="${SAN}" font-weight="600" font-size="18" fill="${T}"`)}
  ${data.cost.map((c,i)=>`<g transform="translate(800 ${580+i*46})">${txt(0,20,c,`font-family="${SAN}" font-size="19" fill="${G}"`)}<rect x="170" y="4" width="390" height="18" rx="9" fill="${SH}"/><rect class="cb" x="170" y="4" width="0" height="18" rx="9" fill="${[T,'#FF8A3D',SUN,U][i]}" data-w="${[300,120,220,70][i]}"/></g>`).join('')}</g></g>
<g id="s2"><rect width="1600" height="900" fill="${SH}"/>${title(2,2,'We check the supplier')}
 ${[0,1,2].map(i=>`<g class="sup" transform="translate(${130+i*470} 290)"><rect class="sbg" width="420" height="470" rx="28" fill="#fff" filter="url(#sh)"/><rect class="sbd" width="420" height="470" rx="28" fill="none" stroke="${T}" stroke-width="4" opacity="0"/>
  <rect x="34" y="34" width="64" height="64" rx="18" fill="${SH}"/><path d="M50 84 V62 l14 -10 v10 l14 -10 v32 z" fill="${G}"/>
  ${txt(118,62,data.sup[i][0],`font-family="${SER}" ${FV} font-size="30" fill="${U}"`)}${txt(118,92,data.sup[i][1],`font-family="${SAN}" font-size="18" fill="${G}"`)}
  ${data.checks.map((c,j)=>`<g transform="translate(34 ${160+j*84})"><rect width="352" height="64" rx="16" fill="${SH}"/>${txt(22,40,c,`font-family="${SAN}" font-size="21" fill="${U}"`)}<g class="mkx" transform="translate(320 32)" opacity="0"><circle r="18" fill="${(i===2&&j===1)?'#B91C1C':T}"/><path d="${(i===2&&j===1)?cross:tick}" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></g></g>`).join('')}
  </g>`).join('')}
 <g id="stamp" transform="translate(470 650)" opacity="0"><g transform="rotate(-10)"><rect x="-130" y="-42" width="260" height="84" rx="12" fill="none" stroke="${T}" stroke-width="6"/>${txt(0,15,'Verified',`text-anchor="middle" font-family="${SER}" ${FV} font-size="46" fill="${T}"`)}</g></g></g>
<g id="s3"><rect width="1600" height="900" fill="${SH}"/>${title(3,3,'Goods inspected before they ship')}
 <rect x="0" y="706" width="1010" height="18" fill="${U}"/>${Array.from({length:22},(_,i)=>`<circle cx="${i*48+20}" cy="715" r="5" fill="${G}"/>`).join('')}
 <g id="boxes">${Array.from({length:7},(_,i)=>`<g class="bx"><rect x="-80" y="-130" width="160" height="130" rx="8" fill="#D9A66B"/><rect x="-80" y="-130" width="160" height="26" fill="#C38F55"/><rect x="-14" y="-130" width="28" height="56" fill="#F3D3A6"/><text x="0" y="-36" text-anchor="middle" font-family="${SAN}" font-weight="700" font-size="16" fill="#7A5230">SAWELI</text></g>`).join('')}</g>
 <g id="mag"><circle r="70" fill="rgba(255,255,255,.35)" stroke="${U}" stroke-width="10"/><line x1="50" y1="50" x2="110" y2="110" stroke="${U}" stroke-width="18" stroke-linecap="round"/></g>
 <g id="rep" filter="url(#sh)"><rect x="1070" y="250" width="430" height="560" rx="28" fill="#fff"/>
  ${txt(1110,316,'Inspection report',`font-family="${SER}" ${FV} font-size="34" fill="${U}"`)}${txt(1110,348,data.ref,`font-family="${SAN}" font-size="17" fill="${G}"`)}
  ${data.insp.map((c,j)=>`<g transform="translate(1110 ${384+j*70})"><rect width="350" height="54" rx="14" fill="${SH}"/>${txt(20,35,c,`font-family="${SAN}" font-size="20" fill="${U}"`)}<g class="ik" transform="translate(318 27)" opacity="0"><circle r="16" fill="${T}"/><path d="${tick}" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" transform="scale(.85)"/></g></g>`).join('')}
  ${[0,1,2].map(i=>`<g class="th" transform="translate(${1110+i*120} 680)"><rect width="106" height="80" rx="12" fill="${['#F3D3A6','#FFE07A','#FFD0B8'][i]}"/><path d="M14 66 l26 -26 l18 18 l14 -12 l22 20 z" fill="rgba(43,33,27,.35)"/><circle cx="78" cy="22" r="9" fill="#fff"/></g>`).join('')}
  ${txt(1110,792,'Sent to you with photos',`id="snt" font-family="${SAN}" font-weight="600" font-size="18" fill="${T}" opacity="0"`)}</g></g>
<g id="s4"><rect width="1600" height="900" fill="${U2}"/><rect width="1600" height="900" fill="url(#gr)"/>
 <g transform="translate(70 120) scale(1.22)"><path d="${L}" fill="#3a2d24" stroke="#55453a"/>
  <path id="r1" d="${sea}" fill="none" stroke="${T}" stroke-width="3.5" stroke-linecap="round"/><path id="r2" d="${seaS}" fill="none" stroke="${T}" stroke-width="3.5" stroke-linecap="round"/>
  ${data.pins.map(([n,dx,an])=>{const [x,y]=cy[n];return `<g class="pin"><circle cx="${x}" cy="${y}" r="16" fill="none" stroke="${T}" stroke-width="2" class="pp"/><circle cx="${x}" cy="${y}" r="6.5" fill="#fff"/><text x="${x+dx}" y="${y+6}" text-anchor="${an}" font-family="${SAN}" font-weight="600" font-size="17" fill="#fff" paint-order="stroke" stroke="${U2}" stroke-width="4">${n}</text></g>`}).join('')}
  <g id="ship"><circle r="11" fill="#fff"/><circle r="22" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"/></g></g>
 ${title(4,4,'Shipped to your port',1)}
 <g id="docs">${data.docs.map((c,i)=>`<g class="doc" transform="translate(1250 ${560+i*70})"><rect width="246" height="58" rx="29" fill="rgba(255,255,255,.08)" stroke="rgba(255,255,255,.18)"/><rect x="18" y="16" width="20" height="26" rx="3" fill="${SUN}"/>${txt(50,36,c,`font-family="${SAN}" font-weight="500" font-size="17" fill="#fff"`)}</g>`).join('')}</g></g>
<g id="s5"><rect width="1600" height="900" fill="${SH}"/>${title(5,5,'Payment through a partner bank')}
 ${txt(120,300,data.payline,`font-family="${SAN}" font-size="25" fill="${G}"`)}
 <line x1="330" y1="520" x2="1270" y2="520" stroke="${LN}" stroke-width="4" stroke-dasharray="2 12" stroke-linecap="round"/>
 <line id="pl1" x1="330" y1="520" x2="800" y2="520" stroke="${T}" stroke-width="5" stroke-linecap="round"/><line id="pl2" x1="800" y1="520" x2="1270" y2="520" stroke="${T}" stroke-width="5" stroke-linecap="round"/>
 ${data.nodes.map(([n,s],i)=>`<g class="nd" transform="translate(${330+i*470} 520)"><circle class="ring" r="96" fill="none" stroke="${T}" stroke-width="3" opacity="0"/><circle r="84" fill="${i===1?U:'#fff'}" filter="url(#sh)"/>${[
  `<circle cy="-14" r="20" fill="${T}"/><path d="M-34 36 a34 30 0 0 1 68 0 z" fill="${T}"/>`,
  `<path d="M-40 -6 L0 -36 L40 -6 Z" fill="${SUN}"/><rect x="-34" y="0" width="68" height="8" fill="${SUN}"/><rect x="-28" y="12" width="10" height="26" fill="${SUN}"/><rect x="-5" y="12" width="10" height="26" fill="${SUN}"/><rect x="18" y="12" width="10" height="26" fill="${SUN}"/><rect x="-38" y="40" width="76" height="8" fill="${SUN}"/>`,
  `<rect x="-38" y="-6" width="76" height="46" fill="${T}"/><path d="M-38 -6 V-30 l24 14 v-14 l24 14 v-14 l28 14 V-6z" fill="#FF8A3D"/>`][i]}
  <g class="ok" transform="translate(60 -60)" opacity="0"><circle r="22" fill="#16A34A"/><path d="${tick}" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>
  ${txt(0,140,n,`text-anchor="middle" font-family="${SER}" ${FV} font-size="32" fill="${U}"`)}${txt(0,174,s,`text-anchor="middle" font-family="${SAN}" font-size="19" fill="${G}"`)}</g>`).join('')}
 <g id="pk"><rect x="-34" y="-42" width="68" height="84" rx="8" fill="#fff" stroke="${U}" stroke-width="3"/><rect x="-20" y="-24" width="40" height="5" fill="${LN}"/><rect x="-20" y="-10" width="40" height="5" fill="${LN}"/><rect x="-20" y="4" width="26" height="5" fill="${LN}"/><circle cx="16" cy="26" r="10" fill="${T}"/></g>
 <g id="coin"><circle r="30" fill="${SUN}" stroke="#E0A800" stroke-width="4"/><path d="M-10 -12 h14 a8 8 0 0 1 0 16 h-8 a8 8 0 0 0 0 16 h14 M0 -18 v36" fill="none" stroke="${U}" stroke-width="4" stroke-linecap="round"/></g></g>
<g id="s6"><rect width="1600" height="900" fill="${U2}"/>
 <g id="mk2"><image href="/brand/saweli-stacked-rev.svg" x="-150" y="-133" width="300" height="266"/></g>
 <text id="e1" x="800" y="610" text-anchor="middle" font-family="${SER}" ${FV} font-size="84" fill="#fff">Start your <tspan font-style="italic" fill="${T}">order</tspan></text>
 <text id="e2" x="800" y="668" text-anchor="middle" font-family="${SAN}" font-size="28" fill="rgba(255,255,255,.75)">saweli.com  ·  ${data.phone}</text>
 <text id="e3" x="800" y="740" text-anchor="middle" font-family="${ZH}" font-weight="300" font-size="28" letter-spacing="12" fill="${SUN}">两个市场的交汇处</text></g>`;
box.prepend(svg);
const q=s=>svg.querySelector(s),qa=s=>[...svg.querySelectorAll(s)];
const g=SC.map((_,i)=>q('#s'+i));
const r1=q('#r1'),r2=q('#r2'),L1=r1.getTotalLength(),L2=r2.getTotalLength();
[r1,r2].forEach((r,i)=>{const l=i?L2:L1;r.style.strokeDasharray=l;r.style.strokeDashoffset=l});
function render(t){
 g.forEach((el,i)=>{const lt=t-START[i],d=SC[i][1];let o=0;if(lt>=0&&lt<d+.5){o=i===0?1:eo(p(lt,0,.5));if(lt>d)o=Math.min(o,1-p(lt,d,d+.5));if(i===SC.length-1&&lt>d)o=1}el.style.opacity=o;el.style.display=o<=0?'none':''});
 let k=t-START[0];// intro
 q('#mkr').setAttribute('width',480*eio(p(k,.2,1.6)));q('#i0').style.opacity=eo(p(k,1.4,2.2));
 q('#i1').style.opacity=eo(p(k,1.9,2.8));q('#i1').setAttribute('transform',`translate(0 ${30*(1-eo(p(k,1.9,2.9)))})`);
 q('#i2').style.opacity=eo(p(k,2.5,3.3));
 k=t-START[1];// order
 q('#ph').setAttribute('transform',`translate(${-60*(1-eo(p(k,0,1)))} 0)`);
 data.fields.forEach(([,v],i)=>{const a=.8+i*1.1,pr=p(k,a,a+.9);q('#fv'+i).textContent=v.slice(0,Math.round(v.length*pr))+(pr>0&&pr<1?'|':'');q('#fb'+i).style.opacity=(pr>0&&pr<1)?1:0});
 const tp=p(k,4.1,4.7);q('#tap').setAttribute('r',90*eo(tp));q('#tap').style.opacity=.4*(1-tp);q('#qb').setAttribute('fill',k>4.1&&k<4.8?T:U);
 const qp=eo(p(k,4.5,5.3));q('#qc').style.opacity=qp;q('#qc').setAttribute('transform',`translate(0 ${50*(1-qp)})`);
 qa('#s1 .cb').forEach((b,i)=>b.setAttribute('width',b.dataset.w*eo(p(k,4.9+i*.2,5.8+i*.2))));

 k=t-START[2];// verify
 qa('.sup').forEach((s,i)=>{const a=eo(p(k,.2+i*.15,1+i*.15));s.style.opacity=a*(i===2?1-.65*p(k,5.6,6.2):1);s.setAttribute('transform',`translate(${130+i*470} ${290+60*(1-a)})`);
  [...s.querySelectorAll('.mkx')].forEach((m,j)=>{const st=1.2+j*.75+i*.18,pp=p(k,st,st+.35);m.style.opacity=pp;m.setAttribute('transform',`translate(320 32) scale(${back(pp)})`)});
  q('.sbd',s)&&(s.querySelector('.sbd').style.opacity=i===0?p(k,6.2,6.7):0)});
 const sp=p(k,6.4,6.9);q('#stamp').style.opacity=sp;q('#stamp').setAttribute('transform',`translate(340 722) scale(${.78*(1+1.2*(1-eo(sp)))})`);
 k=t-START[3];// inspect
 qa('.bx').forEach((b,i)=>{const x=((k*150+i*190)%1330)-160;b.setAttribute('transform',`translate(${x} 706)`)});
 q('#mag').setAttribute('transform',`translate(${520+120*Math.sin(k*1.6)} ${480+16*Math.sin(k*3.2)})`);
 const rp=eo(p(k,.4,1.2));q('#rep').style.opacity=rp;q('#rep').setAttribute('transform',`translate(${60*(1-rp)} 0)`);
 qa('.ik').forEach((m,j)=>{const pp=p(k,1.6+j*.8,2+j*.8);m.style.opacity=pp;m.setAttribute('transform',`translate(318 27) scale(${back(pp)})`)});
 qa('.th').forEach((m,j)=>{const pp=p(k,5+j*.25,5.4+j*.25);m.style.opacity=pp;m.setAttribute('transform',`translate(${1110+j*120} ${680+20*(1-eo(pp))})`)});
 q('#snt').style.opacity=p(k,5.9,6.3);
 k=t-START[4];// ship
 const a1=eio(p(k,.8,5)),a2=eio(p(k,4.6,6.6));r1.style.strokeDashoffset=L1*(1-a1);r2.style.strokeDashoffset=L2*(1-a2);
 const pt=k<4.8?r1.getPointAtLength(L1*a1):r2.getPointAtLength(L2*a2);q('#ship').setAttribute('transform',`translate(${pt.x} ${pt.y})`);q('#ship').style.opacity=p(k,.6,1);
 qa('.pin').forEach((m,i)=>{m.style.opacity=eo(p(k,.3+i*.2,.8+i*.2));const pp=m.querySelector('.pp');const ph=(((k*.9+i*.3)%1)+1)%1;pp.setAttribute('r',8+22*ph);pp.style.opacity=1-ph});
 qa('.doc').forEach((m,i)=>{const pp=eo(p(k,5.6+i*.3,6.2+i*.3));m.style.opacity=pp;m.setAttribute('transform',`translate(${1250+30*(1-pp)} ${560+i*70})`)});
 k=t-START[5];// pay
 qa('.nd').forEach((m,i)=>{const a=eo(p(k,.2+i*.15,.9+i*.15));m.style.opacity=a;m.setAttribute('transform',`translate(${330+i*470} ${520+40*(1-a)})`)});
 const f1=eio(p(k,1.2,2.6)),f2=eio(p(k,3.4,4.8));
 q('#pl1').setAttribute('x2',330+470*f1);q('#pl2').setAttribute('x2',800+470*f2);
 q('#pk').setAttribute('transform',`translate(${330+470*f1} ${430-30*Math.sin(Math.PI*f1)})`);q('#pk').style.opacity=k>1.1&&k<2.9?1:0;
 q('#coin').setAttribute('transform',`translate(${800+470*f2} ${430-30*Math.sin(Math.PI*f2)})`);q('#coin').style.opacity=k>3.3&&k<5?1:0;
 qa('.nd').forEach((m,i)=>{const at=[1.1,2.7,4.9][i],pp=p(k,at,at+.4);const o=m.querySelector('.ok');o.style.opacity=i===0?0:pp;o.setAttribute('transform',`translate(60 -60) scale(${back(pp)})`);const rg=m.querySelector('.ring');const rr=p(k,at,at+.9);rg.setAttribute('r',90+40*rr);rg.style.opacity=(rr>0&&rr<1)?1-rr:0});
 k=t-START[6];// end
 {const m=eo(p(k,0,1));q('#mk2').setAttribute('transform',`translate(800 ${330+20*(1-m)}) scale(${.92+.08*m})`);q('#mk2').style.opacity=m}
 ['#e1','#e2','#e3'].forEach((s,i)=>{const pp=eo(p(k,.4+i*.25,1.2+i*.25));q(s).style.opacity=pp});
 q('#e1').setAttribute('transform',`translate(0 ${30*(1-eo(p(k,.4,1.2)))})`);
}
window.filmRender=render;window.filmTotal=TOTAL;
if(new URLSearchParams(location.search).has('render')){render(0);return}
// player
const pp=box.querySelector('.pp'),chap=box.querySelector('.chap'),snd=box.querySelector('.snd');
const au=new Audio('/media/film-audio.m4a');au.preload='none';let sound=false;
const syncA=()=>{if(!sound)return;if(Math.abs(au.currentTime-t)>.25)au.currentTime=t;if(playing&&au.paused)au.play().catch(()=>{});if(!playing&&!au.paused)au.pause()};
if(snd)snd.addEventListener('click',()=>{sound=!sound;snd.setAttribute('aria-pressed',sound);snd.classList.toggle('on',sound);if(sound){au.currentTime=t;if(!playing)play();else au.play().catch(()=>{})}else au.pause()});
const CH=[[1,data.chap[0]],[2,data.chap[1]],[3,data.chap[2]],[4,data.chap[3]],[5,data.chap[4]]];
chap.innerHTML=CH.map(([i,n])=>`<button type="button" data-s="${i}"><span>${n}</span><i><b></b></i></button>`).join('');
const cb=[...chap.querySelectorAll('button')];
let t=0,playing=false,last=0,seen=false,seen0=false;
const ICON={play:'<svg viewBox="0 0 24 24"><path d="M7 4l13 8-13 8z" fill="currentColor"/></svg>',pause:'<svg viewBox="0 0 24 24"><path d="M6 4h4v16H6zM14 4h4v16h-4z" fill="currentColor"/></svg>',again:'<svg viewBox="0 0 24 24"><path d="M4 12a8 8 0 1 0 2.4-5.7M4 4v5h5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>'};
const ui=()=>{pp.innerHTML=playing?ICON.pause:(t>=TOTAL?ICON.again:ICON.play);pp.setAttribute('aria-label',playing?'Pause':'Play');
 cb.forEach((b,i)=>{const s=START[i+1],e=s+SC[i+1][1]+(i===4?SC[6][1]:0);const f=cl((t-s)/(e-s));b.querySelector('b').style.transform=`scaleX(${f})`;b.classList.toggle('on',t>=s&&t<e)})};
function frame(now){if(!playing)return;if(sound&&!au.paused&&au.currentTime>0){t=au.currentTime}else{t+=(now-last)/1000}last=now;if(t>=TOTAL){t=TOTAL;playing=false;au.pause()}render(t);ui();if(playing)requestAnimationFrame(frame)}
const play=()=>{if(t>=TOTAL||!seen0){t=0;seen0=true}playing=true;last=performance.now();syncA();requestAnimationFrame(frame);ui()};
const pause=()=>{playing=false;au.pause();ui()};
pp.addEventListener('click',()=>playing?pause():play());
cb.forEach((b,i)=>b.addEventListener('click',()=>{seen0=true;t=START[i+1]+.01;if(sound)au.currentTime=t;render(t);if(!playing)play();ui()}));
svg.addEventListener('click',()=>playing?pause():play());
render(START[1]+5.6);ui();
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
if(RM){t=START[1]+3;render(t);ui()}
else new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting&&!seen){seen=true;play()}else if(!e.isIntersecting&&playing)pause()}),{threshold:.45}).observe(box);
})();
