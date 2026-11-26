import json
s=open('index27.html',encoding='utf8').read()
rows=json.load(open('prow.json'))
def rep(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:60],s.count(a)); s=s.replace(a,b)
rep("{id:'notices',t:'নোটিশ',i:'bell'},","{id:'notices',t:'নোটিশ',i:'bell'},{id:'prayer',t:'নামাজের সময়',i:'cal'},")
html='''
<section id="prayer" class="section">
 <div class="sec-head"><div><h3>নামাজের সময়</h3><div class="sub" id="pzSub"></div></div></div>
 <div class="panel" id="pzToday" style="margin-bottom:14px"></div>
 <div class="panel" style="margin-bottom:14px"><div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap"><h4 style="margin:0;flex:1">মাসের সময়সূচি</h4><select id="pzMon"></select></div><div class="tablewrap" id="pzMonth" style="margin-top:10px;max-height:60vh"></div><div class="hint2" id="pzSrc" style="margin-top:8px"></div></div>
 <div class="panel adminonly" id="pzAdmin" style="margin-bottom:14px"><h4>জামাতের সময় (মসজিদ কর্তৃপক্ষ)</h4><div class="hint2">জামাতের সময় ওয়াক্তের সময় থেকে আলাদা। ফাঁকা রাখলে দেখানো হবে না।</div>
  <div class="mform" id="pzJam" style="margin-top:8px"></div><button class="btn sm" id="pzJamSave" type="button" style="margin-top:8px">জামাতের সময় সংরক্ষণ</button>
  <h4 style="margin-top:18px">সাময়িক সংশোধন (মূল সময় অক্ষত থাকে)</h4>
  <div class="mform"><label for="pzOD">কার্যকর তারিখ</label><input id="pzOD" type="date"><label for="pzOW">ওয়াক্ত</label><select id="pzOW"><option value="1">ফজর</option><option value="2">সূর্যোদয়</option><option value="3">যোহর</option><option value="4">আসর</option><option value="5">মাগরিব</option><option value="6">এশা</option><option value="0">সাহরির শেষ</option></select>
  <label for="pzOT">নতুন সময়</label><input id="pzOT" type="time"><label for="pzOR">কারণ (বাধ্যতামূলক)</label><input id="pzOR" maxlength="120"></div>
  <button class="btn sm" id="pzOSave" type="button" style="margin-top:8px">সংশোধন সংরক্ষণ</button>
  <div class="tablewrap" id="pzHist" style="margin-top:12px;max-height:40vh"></div></div>
 <div class="panel superonly" id="pzSuper" style="margin-bottom:14px"><h4>সময়সূচি হালনাগাদ (সুপার অ্যাডমিন)</h4><div class="hint2">নতুন সময়সূচির প্রতি লাইনে: <b>মাস-দিন সাহরি ফজর সূর্যোদয় যোহর আসর মাগরিব এশা</b> (২৪ ঘণ্টা, যেমন 01-15 05:18 05:24 06:41 12:09 15:55 17:34 18:51)। যাচাই করা না থাকলে দেবেন না।</div>
  <textarea id="pzImp" style="width:100%;height:110px;margin-top:8px" placeholder="01-01 05:14 05:20 ..."></textarea>
  <input id="pzNote" placeholder="উৎস ও যাচাইয়ের নোট (যেমন: ইসলামিক ফাউন্ডেশন ২০২৭, যাচাইকৃত)" style="width:100%;margin-top:6px" maxlength="160">
  <div style="display:flex;gap:8px;margin-top:8px;flex-wrap:wrap"><button class="btn sm" id="pzImpSave" type="button">হালনাগাদ করুন</button><button class="btn sec sm" id="pzImpReset" type="button">মূল (অ্যাপের) সময়সূচিতে ফিরুন</button></div></div>
</section>
'''
rep('<section id="donate" class="section">',html+'\n<section id="donate" class="section">')
js=r'''
/* ===== v27: নামাজের সময় ===== */
const PZ_BASE=%s;
const PZ_NOTE='নরসিংদী জেলার সময়সূচি (ছবি থেকে সংগৃহীত)। ইসলামিক ফাউন্ডেশনের মূল সূচির সাথে যাচাই বাকি — সরকারি বলে দাবি করা হচ্ছে না।';
const PZ={rows:null,note:'',ov:{jamat:{},ov:{},hist:[]},loaded:false};
(function(){
  const NM=['সাহরির শেষ','ফজর','সূর্যোদয়','যোহর','আসর','মাগরিব','এশা'],PR=[1,3,4,5,6],PN=['ফজর','যোহর','আসর','মাগরিব','এশা'],JK=['fajr','zuhr','asr','maghrib','isha'];
  const pad=n=>String(n).padStart(2,'0');
  const ymd=d=>d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate());
  function fmt12(m){let h=Math.floor(m/60)%%24,mi=m%%60;const ap=h>=12?'PM':'AM';h=h%%12||12;return bn(h+':'+pad(mi))+' '+ap}
  function t24(s){const g=String(s||'').match(/^(\d{1,2}):(\d{2})$/);return g?(+g[1])*60+(+g[2]):null}
  function baseRow(mo,d){if(mo===2&&d===29)d=28;const src=PZ.rows||PZ_BASE;return src.find(r=>r[0]===mo&&r[1]===d)}
  function day(date){const r=baseRow(date.getMonth()+1,date.getDate());if(!r)return null;const orig=r.slice(2),t=orig.slice(),mask=[],o=(PZ.ov.ov||{})[ymd(date)]||{};
    Object.keys(o).forEach(k=>{const e=o[k];if(e&&!e.revoked&&Number.isFinite(e.n)){t[+k]=e.n;mask[+k]=e}});return {t,orig,mask}}
  function isRam(date){try{const p=new Intl.DateTimeFormat('en-u-ca-islamic-umalqura',{month:'numeric'}).formatToParts(new Date(date.getFullYear(),date.getMonth(),date.getDate()+HIJRI_ADJ,12));return +p.find(x=>x.type==='month').value===9}catch(e){return false}}
  window.pzDay=day;window.pzIsRam=isRam;window.pzFmt=fmt12;
  function nextInfo(now){const d=day(now);if(!d)return null;const nm=now.getHours()*60+now.getMinutes()+now.getSeconds()/60;
    for(let k=0;k<5;k++)if(d.t[PR[k]]>nm)return {k,min:d.t[PR[k]],diff:d.t[PR[k]]-nm,d};
    const tm=new Date(now.getFullYear(),now.getMonth(),now.getDate()+1),dt=day(tm);if(!dt)return null;return {k:0,min:dt.t[1],diff:dt.t[1]+1440-nm,d,tomorrow:true}}
  function cd(diff){const m=Math.max(0,Math.floor(diff)),h=Math.floor(m/60);return h>0?bn(h)+' ঘণ্টা '+bn(m%%60)+' মিনিট':bn(m)+' মিনিট'}
  function render(){
    if(!$('pzToday'))return;const now=new Date(),d=day(now),ram=isRam(now),dt=bnDates(now);
    $('pzSub').textContent=dt.wd+', '+dt.g+' · '+dt.h;
    if(!d){$('pzToday').innerHTML='<div class="empty">আজকের সময়সূচি পাওয়া যায়নি</div>';return}
    const nx=nextInfo(now),J=PZ.ov.jamat||{};
    let h=nx?`<div style="text-align:center;margin-bottom:10px"><div class="hint2">পরবর্তী ওয়াক্ত${nx.tomorrow?' (আগামীকাল)':''}</div><div style="font-size:26px;font-weight:700">${PN[nx.k]} · ${fmt12(nx.min)}</div><div style="font-size:16px;color:var(--gold,#b8860b)">${cd(nx.diff)} বাকি</div></div>`:'';
    const rowsH=[];
    if(ram)rowsH.push([0,'সাহরির শেষ সময়']);
    rowsH.push([1,'ফজর'],[2,'সূর্যোদয়'],[3,'যোহর'],[4,'আসর'],[5,ram?'মাগরিব (ইফতার)':'মাগরিব'],[6,'এশা']);
    h+='<table style="width:100%%"><thead><tr><th>ওয়াক্ত</th><th class="num">ওয়াক্তের সময়</th><th class="num">জামাত</th></tr></thead><tbody>'+rowsH.map(([i,n])=>{const k=PR.indexOf(i),j=k>=0?J[JK[k]]:'',hi=nx&&!nx.tomorrow&&k===nx.k?' style="background:#10b98122;font-weight:700"':(nx&&nx.tomorrow&&k===0?' style="background:#10b98122;font-weight:700"':'');
      return `<tr${hi}><td>${n}${d.mask[i]?' <small title="সংশোধিত" style="color:#b45309">✎</small>':''}</td><td class="num">${fmt12(d.t[i])}</td><td class="num">${j?fmt12(t24(j)):'—'}</td></tr>`}).join('')+'</tbody></table>';
    if(ram)h+=`<div class="hint2" style="margin-top:8px">ইফতার পর্যন্ত বাকি: ${d.t[5]>now.getHours()*60+now.getMinutes()?cd(d.t[5]-(now.getHours()*60+now.getMinutes())):'ইফতারের সময় হয়েছে'}</div>`;
    $('pzToday').innerHTML=h;
    $('pzSrc').textContent=(PZ.note||PZ_NOTE)+' ফেব্রুয়ারি ২৯ তারিখে ২৮ ফেব্রুয়ারির সময় ধরা হয়।';
    renderMonth();
    if(isAdminView())renderAdmin();
  }
  function renderMonth(){
    const sel=$('pzMon');if(!sel.options.length){sel.innerHTML=BN_M.map((m,i)=>`<option value="${i}">${m}</option>`).join('');sel.value=new Date().getMonth();sel.onchange=renderMonth}
    const y=new Date().getFullYear(),mo=+sel.value,n=new Date(y,mo+1,0).getDate(),td=ymd(new Date());let b='';
    for(let i=1;i<=n;i++){const dd=new Date(y,mo,i),x=day(dd);if(!x)continue;const cur=ymd(dd)===td;
      b+=`<tr${cur?' style="background:#10b98122;font-weight:700"':''}><td>${bn(i)}</td>`+[0,1,2,3,4,5,6].map(c=>`<td class="num">${fmt12(x.t[c]).replace(' AM','').replace(' PM','')}${x.mask[c]?'✎':''}</td>`).join('')+'</tr>'}
    $('pzMonth').innerHTML='<table><thead><tr><th>তারিখ</th><th class="num">সাহরি</th><th class="num">ফজর</th><th class="num">সূর্যোদয়</th><th class="num">যোহর</th><th class="num">আসর</th><th class="num">মাগরিব</th><th class="num">এশা</th></tr></thead><tbody>'+b+'</tbody></table>';
  }
  function renderAdmin(){
    const J=PZ.ov.jamat||{};if(!$('pzJam').dataset.b){$('pzJam').dataset.b=1;$('pzJam').innerHTML=PN.map((n,k)=>`<label for="pzJ${k}">${n} জামাত</label><input id="pzJ${k}" type="time">`).join('')}
    PN.forEach((n,k)=>{const e=$('pzJ'+k);if(e&&document.activeElement!==e)e.value=J[JK[k]]||''});
    if(!$('pzOD').value)$('pzOD').value=ymd(new Date());
    const H=(PZ.ov.hist||[]).slice().reverse();
    $('pzHist').innerHTML=H.length?'<table><thead><tr><th>তারিখ</th><th>ওয়াক্ত</th><th class="num">মূল</th><th class="num">নতুন</th><th>কারণ / কে / কখন</th><th></th></tr></thead><tbody>'+H.map(e=>`<tr><td>${esc(e.date)}</td><td>${NM[e.i]}</td><td class="num">${fmt12(e.o)}</td><td class="num">${e.revoked?'<s>'+fmt12(e.n)+'</s>':fmt12(e.n)}</td><td>${esc(e.why)}<br><small>${esc(e.by)} · ${esc(new Date(e.at).toLocaleString('bn-BD'))}${e.revoked?' · বাতিল':''}</small></td><td>${e.revoked?'':`<button class="btn sec sm" data-id="${e.id}">বাতিল</button>`}</td></tr>`).join('')+'</tbody></table>':'<div class="empty">এখনো কোনো সংশোধন নেই</div>';
  }
  async function saveOv(){try{await S.DB.doc('pub/prayerOv').set(PZ.ov);return true}catch(e){toast('সংরক্ষণ হয়নি। rules (v12) Publish করা আছে কি দেখুন');return false}}
  function bind(){
    $('pzJamSave').onclick=async()=>{if(!isAdminView()||!needDb())return;const J={};PN.forEach((n,k)=>{const v=$('pzJ'+k).value;if(v)J[JK[k]]=v});PZ.ov.jamat=J;if(await saveOv()){toast('জামাতের সময় সংরক্ষিত');audit('জামাতের সময়',JSON.stringify(J));render();pzPush()}};
    $('pzOSave').onclick=async()=>{if(!isAdminView()||!needDb())return;const ds=$('pzOD').value,i=+$('pzOW').value,nt=t24($('pzOT').value),why=$('pzOR').value.trim();
      if(!ds||nt==null){toast('তারিখ ও নতুন সময় দিন');return}if(!why){toast('কারণ লিখতে হবে');return}
      const dd=new Date(ds+'T12:00:00'),b=baseRow(dd.getMonth()+1,dd.getDate());if(!b){toast('তারিখ ঠিক নয়');return}
      const e={id:'o'+Date.now().toString(36),date:ds,i,o:b[2+i],n:nt,why,by:(S.acct&&S.acct.name)||'',at:Date.now()};
      PZ.ov.ov=PZ.ov.ov||{};PZ.ov.ov[ds]=PZ.ov.ov[ds]||{};PZ.ov.ov[ds][i]={n:nt,id:e.id};PZ.ov.hist=(PZ.ov.hist||[]).concat([e]).slice(-300);
      if(await saveOv()){toast('সংশোধন সংরক্ষিত (মূল সময় অক্ষত)');audit('নামাজের সময় সংশোধন',ds+' '+NM[i]+' '+$('pzOT').value+' — '+why);$('pzOR').value='';render();pzPush()}};
    $('pzHist').onclick=async ev=>{const b=ev.target.closest('button[data-id]');if(!b)return;const e=(PZ.ov.hist||[]).find(x=>x.id===b.dataset.id);if(!e||!await askConfirm('এই সংশোধন বাতিল করে মূল সময় ফেরাবেন?','বাতিল করুন'))return;
      e.revoked=true;e.revBy=(S.acct&&S.acct.name)||'';e.revAt=Date.now();const o=(PZ.ov.ov||{})[e.date];if(o&&o[e.i]&&o[e.i].id===e.id)delete o[e.i];if(await saveOv()){toast('বাতিল হয়েছে');audit('সংশোধন বাতিল',e.date+' '+NM[e.i]);render();pzPush()}};
    $('pzImpSave').onclick=async()=>{if(!S.super||!needDb())return;const out=[],bad=[];String($('pzImp').value).split('\n').forEach((l,n)=>{l=toEn(l.trim());if(!l)return;const p=l.split(/\s+/);const g=p[0].match(/^(\d{1,2})-(\d{1,2})$/);const t=p.slice(1).map(t24);if(!g||t.length!==7||t.some(x=>x==null))bad.push(n+1);else out.push([+g[1],+g[2]].concat(t))});
      if(bad.length){toast('ভুল লাইন: '+bad.slice(0,8).join(', '));return}if(out.length<365){toast('অন্তত ৩৬৫ দিনের সারি দিতে হবে (এখন '+out.length+')');return}
      if(!await askConfirm(out.length+' দিনের নতুন সময়সূচি বসানো হবে। মূল অ্যাপ-সূচি অক্ষত থাকবে, চাইলে ফেরা যাবে।','হালনাগাদ করুন'))return;
      try{await S.DB.doc('pub/prayer').set({rows:JSON.stringify(out),note:$('pzNote').value.trim(),at:Date.now(),by:(S.acct&&S.acct.name)||''});toast('সময়সূচি হালনাগাদ হয়েছে');audit('নামাজের সময়সূচি হালনাগাদ',out.length+' দিন')}catch(e){toast('সংরক্ষণ হয়নি। rules (v12) দেখুন')}};
    $('pzImpReset').onclick=async()=>{if(!S.super||!needDb()||!await askConfirm('অ্যাপে থাকা মূল সময়সূচিতে ফিরবেন?','ফিরুন'))return;try{await S.DB.doc('pub/prayer').delete();toast('মূল সূচিতে ফেরা হয়েছে');audit('নামাজের সূচি রিসেট','')}catch(e){toast('হয়নি')}};
  }
  /* অ্যান্ড্রয়েড ব্রিজ: আগামী ৯০ দিনের সময় ফোনে সংরক্ষণ (উইজেটের জন্য) */
  window.pzPush=function(){try{if(!(window.Android&&window.Android.setPrayer))return;const days={},now=new Date();
    for(let i=0;i<90;i++){const dd=new Date(now.getFullYear(),now.getMonth(),now.getDate()+i),x=day(dd);if(!x)continue;const dt=bnDates(dd);
      days[ymd(dd)]={m:x.t,k:Object.assign({dt:dt.wd+', '+dt.g,bd:dt.b,hj:dt.h,ram:isRam(dd)?1:0},...x.t.map((t,c)=>({['s'+c]:fmt12(t).replace(' ',' ')})),...JK.map((k,c)=>({['j'+c]:((PZ.ov.jamat||{})[k]?fmt12(t24(PZ.ov.jamat[k])):'')})))}}
    window.Android.setPrayer(JSON.stringify({v:Date.now(),note:PZ.note||PZ_NOTE,last:ymd(new Date(now.getFullYear(),now.getMonth(),now.getDate()+89)),days}))}catch(e){}};
  let sub=false,tick=0;
  function start(){if(sub||!S.DB||!S.psetLoaded)return;sub=true;
    S.DB.doc('pub/prayer').onSnapshot(s=>{const d=s.exists?s.data():null;PZ.rows=null;PZ.note='';if(d&&d.rows){try{const r=JSON.parse(d.rows);if(Array.isArray(r)&&r.length>=365){PZ.rows=r;PZ.note=d.note||''}}catch(e){}}PZ.loaded=true;render();pzPush()},()=>{});
    S.DB.doc('pub/prayerOv').onSnapshot(s=>{const d=s.exists?s.data():null;PZ.ov=Object.assign({jamat:{},ov:{},hist:[]},d||{});render();pzPush()},()=>{});}
  bind();
  {const _r=renderAll;renderAll=function(){_r();try{start();if(curTab==='prayer')render()}catch(e){}}}
  {const _o=openTab;openTab=function(id,fb){_o(id,fb);if(id==='prayer'){render();clearInterval(tick);tick=setInterval(()=>{if(curTab==='prayer'&&!document.hidden)render();else clearInterval(tick)},30000)}}}
  setTimeout(()=>{try{pzPush()}catch(e){}},3000);
})();
''' % json.dumps(rows,separators=(',',':'))
js=js.replace('%%','%')
i=s.rindex('</script>')
s=s[:i]+js+s[i:]
open('index28.html','w',encoding='utf8').write(s)
