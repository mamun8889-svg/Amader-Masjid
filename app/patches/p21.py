s=open('index20.html',encoding='utf8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:70])
    s=s.replace(a,b)
L='''
/* v20.1: লাইট মোডে হেডার/হিরো (লক) */
:root[data-theme="light"] .side,:root[data-theme="light"] body.admin .side{background:linear-gradient(120deg,#0b7a5a 0%,#12997a 55%,#27b08d 100%)!important;border-bottom:2px solid #d9b45a!important}
:root[data-theme="light"] .hero,:root[data-theme="light"] body.admin .hero{background:radial-gradient(420px 220px at 92% -10%,#ffe9a855,transparent 70%),linear-gradient(125deg,#0b7a5a,#139a75 60%,#2fb391)!important}
@media (prefers-color-scheme:light){
 :root:not([data-theme="dark"]) .side,:root:not([data-theme="dark"]) body.admin .side{background:linear-gradient(120deg,#0b7a5a 0%,#12997a 55%,#27b08d 100%)!important;border-bottom:2px solid #d9b45a!important}
 :root:not([data-theme="dark"]) .hero,:root:not([data-theme="dark"]) body.admin .hero{background:radial-gradient(420px 220px at 92% -10%,#ffe9a855,transparent 70%),linear-gradient(125deg,#0b7a5a,#139a75 60%,#2fb391)!important}
}
/* ভাসমান ＋ */
#fab{position:fixed;right:max(16px,env(safe-area-inset-right,0px));bottom:max(18px,env(safe-area-inset-bottom,0px));z-index:80;display:none;flex-direction:column;align-items:flex-end;gap:10px;transition:transform .22s ease,opacity .22s ease}
#fab.on{display:flex}
#fab.hid{transform:translateY(120px);opacity:0;pointer-events:none}
#fabBtn{width:56px;height:56px;border-radius:50%;border:0;background:linear-gradient(135deg,var(--gold2,#e7c872),var(--gold,#c9a24b));color:#2c1f03;font-size:32px;line-height:1;cursor:pointer;box-shadow:0 10px 24px -8px #000a,0 0 0 3px #ffffff40;display:flex;align-items:center;justify-content:center;transition:transform .2s}
#fab.open #fabBtn{transform:rotate(45deg)}
#fabMenu{display:none;flex-direction:column;gap:8px;align-items:flex-end}
#fab.open #fabMenu{display:flex}
#fabMenu button{border:0;border-radius:999px;padding:11px 18px;font-weight:700;font-size:14.5px;background:var(--surface,#fff);color:var(--ink,#111);box-shadow:0 8px 20px -8px #000a;border:1px solid var(--line,#8884);cursor:pointer;white-space:nowrap}
#fabBk{display:none;position:fixed;inset:0;z-index:79;background:#0005}
body.fabopen #fabBk{display:block}
</style>'''
rep('</style>',L)
js=r'''
/* ===== v20.1: ভাসমান ＋ বাটন ===== */
(function(){
  const fab=document.createElement('div');fab.id='fab';
  fab.innerHTML='<div id="fabMenu"></div><button id="fabBtn" type="button" aria-label="নতুন যোগ করুন">＋</button>';
  const bk=document.createElement('div');bk.id='fabBk';
  document.body.appendChild(bk);document.body.appendChild(fab);
  const menu=document.getElementById('fabMenu'),btn=document.getElementById('fabBtn');
  function close(){fab.classList.remove('open');document.body.classList.remove('fabopen')}
  function actions(){
    const a=[{k:'pay',t:'বেতন এন্ট্রি'}];
    if(S.super)a.push({k:'tx',t:'আয়-ব্যয় যোগ'});
    return a;
  }
  function run(k){
    close();
    if(k==='pay'){openTab('salary');try{showPay(true)}catch(e){}}
    else if(k==='tx'){const f=document.getElementById('txForm'),d=f&&f._dlg;let t=d&&d.previousElementSibling;if(t&&t.classList.contains('ftrig'))t.click();else{openTab('transactions')}}
  }
  menu.addEventListener('click',e=>{const b=e.target.closest('button');if(b)run(b.dataset.k)});
  btn.addEventListener('click',()=>{
    const a=actions();
    if(a.length===1){run(a[0].k);return}
    if(fab.classList.contains('open')){close();return}
    menu.innerHTML=a.map(x=>'<button type="button" data-k="'+x.k+'">'+x.t+'</button>').join('');
    fab.classList.add('open');document.body.classList.add('fabopen');
  });
  bk.addEventListener('click',close);
  function upd(){const show=!!(S.started&&S.admin&&isAdminView());fab.classList.toggle('on',show);if(!show)close()}
  {const _ra=renderAll;renderAll=function(){_ra();try{upd()}catch(e){}}}
  {const _am=applyMode;applyMode=function(){_am();try{upd()}catch(e){}}}
  /* স্ক্রল করলে লুকায়, ছাড়লে দেখায় */
  let sy=0,sx=0,tm=0,touching=false;
  const hide=()=>{if(fab.classList.contains('open'))return;fab.classList.add('hid')};
  const show=()=>{clearTimeout(tm);tm=setTimeout(()=>fab.classList.remove('hid'),220)};
  document.addEventListener('touchstart',e=>{if(e.target.closest&&e.target.closest('#fab'))return;touching=true;sy=e.touches[0].clientY;sx=e.touches[0].clientX},{passive:true});
  document.addEventListener('touchmove',e=>{if(!touching)return;const t=e.touches[0];if(Math.abs(t.clientY-sy)>8||Math.abs(t.clientX-sx)>8){clearTimeout(tm);hide()}},{passive:true});
  const end=()=>{if(touching){touching=false;show()}};
  document.addEventListener('touchend',end,{passive:true});document.addEventListener('touchcancel',end,{passive:true});
  let wt=0;window.addEventListener('wheel',()=>{hide();clearTimeout(wt);wt=setTimeout(()=>fab.classList.remove('hid'),450)},{passive:true});
})();
</script>
</body></html>'''
a=s.rindex('</script>\n</body></html>')
s=s[:a]+js
open('index21.html','w',encoding='utf8').write(s)
