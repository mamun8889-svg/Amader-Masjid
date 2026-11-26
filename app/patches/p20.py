s=open('index18.html',encoding='utf8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:70])
    s=s.replace(a,b)
css='''
/* v20: হেডার লক */
.sbrand>div:last-child{min-width:0;flex:1 1 auto}
.sbrand b{white-space:normal!important;overflow:visible!important;text-overflow:clip!important;overflow-wrap:anywhere;line-height:1.2}
.sright{flex:none}.side .row{flex-wrap:nowrap}
.slogo{cursor:pointer;flex:none;position:relative}
.slogo::after{content:"";position:absolute;right:-3px;bottom:-3px;width:14px;height:14px;border-radius:50%;background:var(--gold,#c9a24b) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23332' stroke-width='3.5' stroke-linecap='round'%3E%3Cpath d='M5 7h14M5 12h14M5 17h14'/%3E%3C/svg%3E") center/10px no-repeat}
@media(max-width:380px){.side .row{flex-wrap:wrap!important}}
/* ড্রয়ার মেনু */
#bkRemind{display:none!important}
#navBk{display:none}
@media(max-width:1000px){
 .side .tabs#nav{position:fixed;left:0;top:64px;bottom:0;width:min(80vw,300px);max-width:none;margin:0;flex-direction:column;flex-wrap:nowrap;overflow-y:auto;overflow-x:hidden;padding:12px 12px 24px;gap:4px;background:linear-gradient(170deg,#07553f,#0b2a3f);transform:translateX(-110%);transition:transform .25s ease;z-index:200;touch-action:pan-y!important;scroll-snap-type:none!important;box-shadow:8px 0 28px -8px #000a;cursor:default}
 .side .tabs#nav button{width:100%;justify-content:flex-start;background:#ffffff14;font-size:15px;padding:11px 14px}
 .side .tabs#nav .sep{width:auto;height:1px;margin:6px 4px;background:#ffffff30}
 body.navopen .side .tabs#nav{transform:none}
 body.navopen #navBk{display:block;position:fixed;inset:0;background:#0007;z-index:190}
 .side .tabs#nav::after{content:"";display:block;height:20px;flex:none}
}
/* প্রোফাইল */
.pfhead{display:flex;gap:14px;align-items:center;margin-bottom:12px}
.pfhead img,.pfav{width:84px;height:84px;border-radius:50%;object-fit:cover;background:#8884;border:2px solid var(--gold,#c9a24b);flex:none}
.pfgrid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.pfgrid label{display:block;font-size:12.5px;margin:6px 0 3px;opacity:.85}
.pfgrid .full{grid-column:1/-1}
@media(max-width:520px){.pfgrid{grid-template-columns:1fr}}
.pfrow{display:flex;gap:10px;align-items:center;padding:9px 0;border-top:1px dashed #8884}
.pfrow img{width:38px;height:38px;border-radius:50%;object-fit:cover;background:#8884;flex:none}
.pfrow .t{flex:1;min-width:0}.pfrow .t b,.pfrow .t small{display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pfview dt{font-size:12px;opacity:.7;margin-top:8px}.pfview dd{margin:0;font-weight:600}
</style>'''
rep('</style>',css)
# backdrop + nav
rep('<nav class="tabs" id="nav" role="tablist"></nav>','<div id="navBk"></div>\n  <nav class="tabs" id="nav" role="tablist"></nav>')
# settings backup panel
rep('<section id="settings" class="section">\n <div class="sec-head"><div><h3>সেটিংস</h3><div class="sub">শুধু সুপার অ্যাডমিন বদলাতে পারেন</div></div></div>\n',
'''<section id="settings" class="section">
 <div class="sec-head"><div><h3>সেটিংস</h3><div class="sub">শুধু সুপার অ্যাডমিন বদলাতে পারেন</div></div></div>
 <div class="panel" style="margin-bottom:14px"><h4>ব্যাকআপ</h4><div class="hint2" id="bkInfo2">—</div>
  <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px"><button class="btn" id="sbkMake" type="button">এখনই ব্যাকআপ নিন</button><button class="btn sec" id="sbkRestore" type="button">ব্যাকআপ থেকে ফেরান</button></div></div>
''')
# TABS: profile
rep("TABS.splice(i+1,0,{id:'chat',t:'চ্যাট',i:'chat',login:1})}","TABS.splice(i+1,0,{id:'chat',t:'চ্যাট',i:'chat',login:1});TABS.splice(i+2,0,{id:'profile',t:'প্রোফাইল',i:'user',login:1})}")
# profile section + JS appended before </script></body>
js=r'''
/* ===== v20: ড্রয়ার মেনু, ব্যাকআপ (সেটিংস), প্রোফাইল ===== */
(function(){
  const body=document.body;
  function navClose(){body.classList.remove('navopen')}
  function navToggle(){
    if(window.innerWidth>1000)return;
    if(body.classList.contains('navopen')){navClose();return}
    const r=document.querySelector('.side .row').getBoundingClientRect();
    $('nav').style.top=Math.max(0,Math.round(r.bottom))+'px';
    body.classList.add('navopen');
  }
  document.querySelector('.slogo').addEventListener('click',e=>{e.stopPropagation();navToggle()});
  $('navBk').addEventListener('click',navClose);
  $('nav').addEventListener('click',e=>{if(e.target.closest('button'))navClose()});
  window.addEventListener('resize',()=>{if(window.innerWidth>1000)navClose()});
  /* ব্যাকআপ বোতাম */
  $('sbkMake').onclick=()=>$('bkMake').click();$('sbkRestore').onclick=()=>$('bkRestore').click();
  function bkInfo(){const e=$('bkInfo2');if(e)e.textContent=S.lastBk?'সর্বশেষ ব্যাকআপ: '+new Date(S.lastBk).toLocaleString('bn-BD'):'এই ফোন থেকে এখনো ব্যাকআপ নেওয়া হয়নি'}
  {const _ra=renderAll;renderAll=function(){_ra();try{bkInfo()}catch(e){}}}
  /* প্রোফাইল */
  const uid=()=>(A&&A.uid())||'';
  const sec=document.createElement('section');sec.id='profile';sec.className='section';
  const BG=['','A+','A-','B+','B-','O+','O-','AB+','AB-'];
  sec.innerHTML=`<div class="sec-head"><div><h3>আমার প্রোফাইল</h3><div class="sub">এই তথ্য শুধু আপনি ও সুপার অ্যাডমিন দেখতে পারেন</div></div></div>
  <div class="panel" style="margin-bottom:14px"><form id="pfForm">
   <div class="pfhead"><img id="pfImg" alt=""><div><button class="btn sec sm" id="pfPick" type="button">ছবি বদলান</button> <button class="btn sec sm" id="pfDelImg" type="button">ছবি সরান</button><input type="file" id="pfFile" accept="image/*" hidden><div class="hint2" id="pfEmail" style="margin-top:6px"></div></div></div>
   <div class="pfgrid">
    <div class="full"><label for="pfName">পূর্ণ নাম</label><input id="pfName" maxlength="60"></div>
    <div><label for="pfPhone">মোবাইল নম্বর</label><input id="pfPhone" maxlength="20" inputmode="tel" placeholder="01XXXXXXXXX"></div>
    <div><label for="pfPhone2">বিকল্প নম্বর</label><input id="pfPhone2" maxlength="20" inputmode="tel"></div>
    <div><label for="pfDob">জন্ম তারিখ</label><input id="pfDob" type="date"></div>
    <div><label for="pfSex">লিঙ্গ</label><select id="pfSex" style="width:100%"><option value="">—</option><option>পুরুষ</option><option>মহিলা</option></select></div>
    <div><label for="pfBg">রক্তের গ্রুপ</label><select id="pfBg" style="width:100%">${BG.map(x=>'<option value="'+x+'">'+(x||'—')+'</option>').join('')}</select></div>
    <div><label for="pfJob">পেশা</label><input id="pfJob" maxlength="60"></div>
    <div><label for="pfFather">পিতার নাম</label><input id="pfFather" maxlength="60"></div>
    <div><label for="pfMother">মাতার নাম</label><input id="pfMother" maxlength="60"></div>
    <div class="full"><label for="pfAddr">বর্তমান ঠিকানা</label><input id="pfAddr" maxlength="160"></div>
    <div class="full"><label for="pfPerm">স্থায়ী ঠিকানা</label><input id="pfPerm" maxlength="160"></div>
   </div>
   <div class="row-actions" style="margin-top:14px"><button class="btn" type="submit">সংরক্ষণ করুন</button></div>
  </form></div>
  <div class="panel" id="pfAll" hidden><h4>সবার প্রোফাইল (সুপার অ্যাডমিন)</h4><div class="hint2">শুধু দেখা যায়, বদলানো যায় না।</div><div id="pfList"></div></div>`;
  document.querySelector('main').appendChild(sec);
  const F=['Name','Phone','Phone2','Dob','Sex','Bg','Job','Father','Mother','Addr','Perm'];
  let PF=null,photo='',loadedFor='';
  const dflt='data:image/svg+xml;utf8,'+encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96"><rect width="96" height="96" fill="#7b8794"/><circle cx="48" cy="36" r="17" fill="#e5e9ee"/><path d="M14 90c3-22 17-30 34-30s31 8 34 30z" fill="#e5e9ee"/></svg>');
  function fill(o){o=o||{};F.forEach(k=>{$('pf'+k).value=o[k.toLowerCase()]||''});photo=o.photo||'';$('pfImg').src=photo||dflt;$('pfEmail').textContent=(A.email&&A.email())||'';
    if(!o.name&&S.acct&&S.acct.name)$('pfName').value=S.acct.name}
  async function load(){
    if(!S.DB||!uid())return;
    try{const g=await S.DB.doc('profiles/'+uid()).get();PF=g.exists?g.data():{};loadedFor=uid();fill(PF);
      if(PF.photo)$('suImg').src=PF.photo}catch(e){fill({})}
  }
  $('pfPick').onclick=()=>$('pfFile').click();
  $('pfDelImg').onclick=()=>{photo='';$('pfImg').src=dflt};
  $('pfFile').onchange=e=>{const f=e.target.files&&e.target.files[0];if(!f)return;
    const im=new Image(),u=URL.createObjectURL(f);
    im.onload=()=>{const n=192,c=document.createElement('canvas');c.width=c.height=n;const x=c.getContext('2d'),m=Math.min(im.width,im.height);
      x.drawImage(im,(im.width-m)/2,(im.height-m)/2,m,m,0,0,n,n);photo=c.toDataURL('image/jpeg',.78);$('pfImg').src=photo;URL.revokeObjectURL(u)};
    im.onerror=()=>toast('ছবিটি পড়া যায়নি');im.src=u;e.target.value=''};
  $('pfForm').addEventListener('submit',async e=>{e.preventDefault();if(!needDb())return;
    const o={photo,updated:Date.now(),email:(A.email&&A.email())||'',role:S.super?'super':S.admin?'admin':'viewer'};
    F.forEach(k=>{o[k.toLowerCase()]=$('pf'+k).value.trim()});
    const ok=await safe(S.DB.doc('profiles/'+uid()).set(o),'প্রোফাইল সংরক্ষিত হয়েছে');
    if(ok){PF=o;if(photo)$('suImg').src=photo}});
  /* সুপার: সবার তালিকা */
  let subbed=false;
  function view(p){
    const row=(l,v)=>v?`<dt>${l}</dt><dd>${esc(v)}</dd>`:'';
    openModal({title:p.name||'প্রোফাইল',sub:p.email||'',body:`<div style="text-align:center"><img src="${p.photo||dflt}" style="width:96px;height:96px;border-radius:50%;object-fit:cover;border:2px solid var(--gold,#c9a24b)"></div><dl class="pfview">${row('মোবাইল',p.phone)}${row('বিকল্প নম্বর',p.phone2)}${row('জন্ম তারিখ',p.dob)}${row('লিঙ্গ',p.sex)}${row('রক্তের গ্রুপ',p.bg)}${row('পেশা',p.job)}${row('পিতার নাম',p.father)}${row('মাতার নাম',p.mother)}${row('বর্তমান ঠিকানা',p.addr)}${row('স্থায়ী ঠিকানা',p.perm)}</dl>`,actions:[{label:'বন্ধ করুন',cls:'sec',fn:closeModal}]})}
  function renderList(){
    const box=$('pfAll');box.hidden=!S.super;if(!S.super)return;
    const P=S.profiles||{},acc=S.accounts||[];
    const ids=[...new Set([...acc.map(a=>a.id),...Object.keys(P)])];
    $('pfList').innerHTML=ids.map(id=>{const p=P[id],a=acc.find(x=>x.id===id)||{};
      return `<div class="pfrow"><img src="${(p&&p.photo)||dflt}" alt=""><div class="t"><b>${esc((p&&p.name)||a.name||'—')}</b><small>${esc(a.role==='super'?'সুপার অ্যাডমিন':a.role==='admin'?'অ্যাডমিন':'সদস্য')} · ${p?esc(p.phone||'ফোন নেই'):'তথ্য দেননি'}</small></div>${p?`<button class="btn sec sm" data-pf="${esc(id)}" type="button">দেখুন</button>`:''}</div>`}).join('')||'<div class="hint2">কেউ নেই</div>';
  }
  $('pfList').addEventListener('click',e=>{const b=e.target.closest('[data-pf]');if(b&&S.profiles&&S.profiles[b.dataset.pf])view(S.profiles[b.dataset.pf])});
  const _ot=openTab;openTab=function(id,fb){_ot(id,fb);if(id==='profile'){if(loadedFor!==uid())load();else fill(PF);
    if(S.super&&!subbed&&S.DB){subbed=true;S.DB.collection('profiles').onSnapshot(s=>{S.profiles={};s.docs.forEach(d=>{S.profiles[d.id]=d.data()});renderList()},()=>{})}renderList()}};
  /* ছবি সাইডবারে */
  setInterval(()=>{if(S.started&&uid()&&loadedFor!==uid())load()},1500);
})();
</script>
</body></html>'''
a=s.rindex('</script>\n</body></html>')
s=s[:a]+js
open('index20.html','w',encoding='utf8').write(s)
