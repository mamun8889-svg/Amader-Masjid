
/* ===== v33: বার্তা (SMS/WhatsApp/ইমো), একসাথে পাঠানো, আয়-ব্যয় ড্রপডাউন, মসজিদ কমিটি ===== */
(function(){
  const AN=()=>window.Android||{};
  const CH={sms:'SMS',wa:'WhatsApp',imo:'ইমো'};
  const lsCh=()=>{try{return localStorage.getItem('bm_ch')||'wa'}catch(e){return 'wa'}};
  const setCh=v=>{try{localStorage.setItem('bm_ch',v)}catch(e){}};
  window.openExt=function(u){let ok=false;try{if(AN().wa)ok=AN().wa(u)}catch(e){}if(!ok){try{location.href=u;ok=true}catch(e){}}return ok};
  function send(ch,ph,t){
    let ok=false;const q=encodeURIComponent(t);
    try{navigator.clipboard.writeText(t)}catch(e){}
    if(ch==='sms'){try{if(AN().sms)ok=AN().sms(ph,t)}catch(e){}if(!ok){try{location.href='sms:'+ph+'?body='+q;ok=true}catch(e){}}}
    else if(ch==='wa'){try{if(AN().wa)ok=AN().wa('whatsapp://send?phone=88'+ph+'&text='+q)||AN().wa('https://wa.me/88'+ph+'?text='+q)}catch(e){}}
    else{try{if(AN().share)ok=AN().share('com.imo.android.imoim',t)||AN().share('com.imo.android.imoimbeta',t)}catch(e){}if(ok)toast('ইমো খুলেছে — ব্যক্তিকে বেছে নিন (বার্তা কপি করা আছে)')}
    if(!ok)toast(CH[ch]+' খোলা যায়নি — বার্তা কপি হয়েছে, নিজে পাঠান');
    return ok;
  }
  const chBtns=cur=>Object.keys(CH).map(k=>`<button type="button" class="btn ${k===cur?'':'sec'} sm" data-ch="${k}">${CH[k]}</button>`).join(' ');
  /* একক বার্তা */
  smsDialog=function({name,phone,text,key,kind}){
    const ph=smsPhone(phone);
    if(!ph){toast(phone?'মোবাইল নম্বরটি সঠিক নয় (01XXXXXXXXX হতে হবে)। তথ্য সম্পাদনা থেকে ঠিক করুন।':'এই বেতনদাতার মোবাইল নম্বর নেই। তথ্য সম্পাদনা থেকে নম্বর যোগ করুন।');return}
    const prev=((S.smsLog&&S.smsLog.items)||[]).filter(x=>x.key===key).pop();
    openModal({title:'বার্তা — '+name,sub:'নম্বর: '+ph+(prev?' · আগে '+new Date(prev.t).toLocaleDateString('bn-BD')+' তারিখে খোলা হয়েছিল':''),
      body:`<div class="mform"><label for="smsTx">বার্তা (বদলাতে পারেন)</label><textarea id="smsTx" style="width:100%;height:150px">${esc(text)}</textarea></div><div class="hint2" style="margin:10px 0 6px">কোন মাধ্যমে পাঠাবেন বেছে নিন:</div><div class="row-actions" id="chRow">${['sms','wa','imo'].map(k=>`<button type="button" class="btn sm" data-ch="${k}">${CH[k]}</button>`).join('')}</div>`,
      actions:[{label:'বন্ধ',cls:'sec',fn:closeModal},{label:'কপি',cls:'sec',fn:()=>copyText($('smsTx').value)}]});
    document.querySelectorAll('#chRow [data-ch]').forEach(b=>b.onclick=async()=>{
      const t=$('smsTx').value.trim();if(!t){toast('বার্তা খালি');return}
      if(prev&&!await askConfirm('এই বার্তা আগেই একবার পাঠানোর জন্য খোলা হয়েছে। আবার খুলবেন?','হ্যাঁ, আবার খুলুন'))return;
      const ch=b.dataset.ch;setCh(ch);
      if(send(ch,ph,t)){closeModal();try{logSms({t:Date.now(),name,phone:ph,kind:(kind||'')+' ('+CH[ch]+')',key,by:(S.acct&&S.acct.name)||''})}catch(e){}}});
  };
  /* একসাথে অনেককে */
  function bulk(cfg){
    const st={ch:lsCh(),type:cfg.types[0].id,items:[],edit:-1};
    const T=()=>cfg.types.find(x=>x.id===st.type);
    function load(){st.items=T().build().map(x=>({...x,ph:smsPhone(x.phone)}));st.items.forEach(x=>x.on=!!x.ph);st.edit=-1}
    function rows(){
      const sel=st.items.filter(x=>x.on).length;
      return `<div class="row-actions" style="margin-bottom:8px">${cfg.types.map(t=>`<button type="button" class="btn ${t.id===st.type?'':'sec'} sm" data-ty="${t.id}">${t.label}</button>`).join('')}</div>
      <div class="hint2" style="margin:6px 0">মাধ্যম:</div><div class="row-actions" style="margin-bottom:10px">${chBtns(st.ch)}</div>
      <label class="ml" style="gap:8px"><span><input type="checkbox" id="bmAll" ${sel&&sel===st.items.filter(x=>x.ph).length?'checked':''}> সবাইকে বাছাই (${bn(st.items.filter(x=>x.ph).length)} জন)</span><b>${bn(sel)} জন বাছাই</b></label>
      <div class="bmlist">${st.items.map((x,i)=>`<div class="bmr"><label style="display:flex;gap:8px;align-items:center;flex:1;min-width:0"><input type="checkbox" data-k="${i}" ${x.on?'checked':''} ${x.ph?'':'disabled'}><span style="min-width:0"><b>${esc(x.name)}</b>${x.amt?' · '+esc(x.amt):''}<br><small class="hint2">${x.ph?x.ph:'নম্বর নেই'}</small></span></label><button type="button" class="btn sec sm" data-e="${i}">সংশোধন</button></div>${st.edit===i?`<textarea data-t="${i}" style="width:100%;height:120px;margin:4px 0 8px">${esc(x.text)}</textarea>`:''}`).join('')||'<div class="empty">কেউ নেই</div>'}</div>`;
    }
    function paint(){
      const keep=document.querySelector('#bmWrap .bmlist');const sc=keep?keep.scrollTop:0;
      $('bmWrap').innerHTML=rows();const l=document.querySelector('#bmWrap .bmlist');if(l)l.scrollTop=sc;wire();
    }
    function wire(){
      const w=$('bmWrap');
      w.querySelectorAll('[data-ty]').forEach(b=>b.onclick=()=>{st.type=b.dataset.ty;load();paint()});
      w.querySelectorAll('[data-ch]').forEach(b=>b.onclick=()=>{st.ch=b.dataset.ch;setCh(st.ch);paint()});
      w.querySelector('#bmAll').onchange=e=>{st.items.forEach(x=>{if(x.ph)x.on=e.target.checked});paint()};
      w.querySelectorAll('[data-k]').forEach(c=>c.onchange=()=>{st.items[+c.dataset.k].on=c.checked;paint()});
      w.querySelectorAll('[data-e]').forEach(b=>b.onclick=()=>{const i=+b.dataset.e;st.edit=st.edit===i?-1:i;paint()});
      w.querySelectorAll('[data-t]').forEach(t=>t.oninput=()=>{st.items[+t.dataset.t].text=t.value});
    }
    function start(){
      const q=st.items.filter(x=>x.on&&x.ph);if(!q.length){toast('কাউকে বাছাই করা হয়নি');return}
      let k=0,sent=0;
      function show(){
        const x=q[k];
        openModal({title:'পাঠানো — '+bn(k+1)+' / '+bn(q.length),sub:CH[st.ch]+' · '+x.name+' · '+x.ph,
          body:`<div class="mform"><label>বার্তা (বদলাতে পারেন)</label><textarea id="bmQ" style="width:100%;height:150px">${esc(x.text)}</textarea></div><button type="button" class="btn" id="bmGo" style="width:100%;margin-top:10px;font-size:17px">${CH[st.ch]} খুলুন</button><div class="hint2" id="bmSt" style="margin-top:8px">পাঠিয়ে ফিরে এসে "পরের জন" চাপুন।</div>`,
          actions:[{label:'বন্ধ',cls:'sec',fn:closeModal},{label:k+1<q.length?'পরের জন →':'শেষ করুন',fn:()=>{if(k+1<q.length){k++;show()}else{closeModal();toast('শেষ — '+bn(sent)+' জনের বার্তা খোলা হয়েছে')}}}]});
        $('bmGo').onclick=()=>{const t=$('bmQ').value.trim();if(!t){toast('বার্তা খালি');return}
          if(send(st.ch,x.ph,t)){sent++;$('bmSt').textContent='খোলা হয়েছে ✓ — পাঠিয়ে ফিরে এসে "পরের জন" চাপুন।';try{logSms({t:Date.now(),name:x.name,phone:x.ph,kind:(x.kind||cfg.kind||'')+' ('+CH[st.ch]+')',key:x.key,by:(S.acct&&S.acct.name)||''})}catch(e){}}};
      }
      show();
    }
    load();
    openModal({title:cfg.title,sub:cfg.sub||'টিক দিন, দরকারে "সংশোধন" করুন — প্রত্যেকের নামসহ আলাদা বার্তা যাবে',body:'<div id="bmWrap"></div>',actions:[{label:'বন্ধ',cls:'sec',fn:closeModal},{label:'বাছাইকৃতদের পাঠান',fn:start}]});
    paint();
  }
  window.bulkMsg=bulk;
  /* মাসভিত্তিক তাগাদা/বকেয়া/প্রাপ্তি */
  function openBulkMsg(){
    const H=window.__ah;if(!H)return;const n=new Date(),abs=n.getFullYear()*12+n.getMonth()-(n.getDate()<=5?1:0),L=H.locate(abs);
    if(!L){toast('এই মাসের তথ্য নেই');return}
    const mn=H.mLab(L.y,L.m),R=H.rep(L.y,L.m),ym=todayIso().slice(0,7);
    const ph=nm=>(payerRec(nm)||{}).phone;
    const sig=' জাযাকাল্লাহু খাইরান। '+MOSQUE_SIG;
    bulk({title:'বার্তা পাঠান — '+mn,kind:'মাসিক বার্তা',types:[
      {id:'due',label:'তাগাদা (দেননি)',build:()=>R.unpaid.map(x=>({name:x.name,phone:ph(x.name),amt:'৳ '+fmt(x.rest),kind:'মাসিক তাগাদা',key:'rem:'+L.y+':'+x.i+':'+L.m+':'+ym,text:'আসসালামু আলাইকুম, '+x.name+'। '+mn+' এর মাসিক বেতন বাবদ '+bn(x.rest)+' টাকা এখনো পাওয়া যায়নি। মাসের ৫ তারিখের মধ্যে পরিশোধের অনুরোধ রইল।'+sig}))},
      {id:'arr',label:'মোট বকেয়া',build:()=>H.arrears(1e9).map(o=>({name:o.name,phone:ph(o.name),amt:'৳ '+fmt(o.amt),kind:'বকেয়া স্মরণ',key:'arr:'+nameKey(o.name)+':'+o.amt+':'+ym,text:'আসসালামু আলাইকুম, '+o.name+'। আপনার মসজিদের মাসিক বেতন বকেয়া আছে: '+o.items.map(x=>x.lab).join(', ')+' — মোট '+bn(o.amt)+' টাকা। সুবিধামতো পরিশোধ করার অনুরোধ রইল।'+sig}))},
      {id:'paid',label:'প্রাপ্তি (দিয়েছেন)',build:()=>R.paid.map(x=>({name:x.name,phone:ph(x.name),amt:'৳ '+fmt(x.amt),kind:'বেতন প্রাপ্তি',key:'got:'+L.y+':'+x.i+':'+L.m+':'+x.amt,text:'আসসালামু আলাইকুম, '+x.name+'। '+mn+' এর বেতন বাবদ '+bn(x.amt)+' টাকা গ্রহণ করা হয়েছে।'+(x.rest>0?' এই মাসে আরও '+bn(x.rest)+' টাকা বাকি আছে।':'')+sig}))}
    ]});
  }
  window.openRemind=openBulkMsg;window.openBulkMsg=openBulkMsg;
  document.addEventListener('click',e=>{if(e.target.closest('#remBtn')||e.target.closest('#salMsgBtn')){e.stopPropagation();e.preventDefault();openBulkMsg()}},true);
  (function(){const row=document.querySelector('#salary .sec-head .row-actions');if(row&&!$('salMsgBtn')){const b=document.createElement('button');b.type='button';b.id='salMsgBtn';b.className='btn sec sm adminonly';b.textContent='বার্তা পাঠান';row.insertBefore(b,row.firstChild)}})();
})();

/* ===== আয়-ব্যয় একসাথে (ড্রপডাউনসহ) ===== */
(function(){
  const X={y:'all',m:'all'};
  function build(){
    const M=getModel(),mo=M.months,vis=['sal','gen','ram'].filter(f=>!(M.hide||{})[f]);
    const years=[...new Set(mo.map(m=>m.y))].sort();
    let host=$('txSel');
    if(!host){host=document.createElement('div');host.id='txSel';host.className='tools';$('txStats').before(host)}
    host.innerHTML=`<select id="txY" aria-label="বছর"><option value="all">সব বছর</option>${years.map(y=>`<option value="${y}"${String(y)===String(X.y)?' selected':''}>${bn(y)}</option>`).join('')}</select><select id="txM" aria-label="মাস"><option value="all">সব মাস</option>${BN_M.map((n,c)=>`<option value="${c}"${String(c)===String(X.m)?' selected':''}>${n}</option>`).join('')}</select>`;
    $('txY').onchange=e=>{X.y=e.target.value;build()};$('txM').onchange=e=>{X.m=e.target.value;build()};
    const list=mo.filter(m=>(X.y==='all'||m.y===+X.y)&&(X.m==='all'||m.c===+X.m));
    const lab=(X.y==='all'?'সব বছর':bn(X.y)+' সাল')+(X.m==='all'?'':' · '+BN_M[+X.m]);
    const pend=(S.tx||[]).filter(x=>x.type==='expense'&&x.status==='pending').length;
    const last=mo[mo.length-1];
    const card=(f,cls)=>{const inc=r2(list.reduce((s,m)=>s+m[f].incT,0)),exp=r2(list.reduce((s,m)=>s+m[f].expT,0)),cl=list.length?list[list.length-1][f].close:0;
      return `<div class="card kpi ${cls}" style="grid-column:1/-1"><div class="lb"><b>${sumFundNames[f]}</b> — ${lab}</div><div class="fx3"><div><span>আয়</span><b class="g">${money(inc)}</b></div><div><span>ব্যয়</span><b class="r">${money(exp)}</b></div><div><span>${X.m==='all'&&X.y==='all'?'বর্তমান':'সমাপনী'} উদ্বৃত্ত</span><b>${money(cl)}</b></div></div>${last&&!(X.y==='all'&&X.m==='all')?'<div class="sb">বর্তমান মোট উদ্বৃত্ত: '+money(last[f].close)+'</div>':''}</div>`};
    $('txStats').innerHTML=vis.map(f=>card(f,f==='sal'?'k-em':f==='gen'?'k-in':'k-vi')).join('')+kpi('k-am','bell','অনুমোদনের অপেক্ষায়',fmt(pend),'ব্যয়ের আবেদন');
  }
  {const _r=renderTx;renderTx=function(){_r();try{build()}catch(e){console.error(e)}}}
})();

/* ===== মসজিদ কমিটি ===== */
(function(){
  const CM={list:[],sub:false};
  const me=()=>(window.BMAUTH&&BMAUTH.uid&&BMAUTH.uid())||'';
  const canEdit=x=>S.super||(me()&&x.id===me());
  const val=(o,k)=>String((o&&o[k])||'').trim();
  function link(kind,v){
    v=String(v||'').trim();if(!v)return '';
    const d=toEn(v).replace(/[\s-]/g,'').replace(/^\+?88/,'');
    if(kind==='tel')return 'tel:'+v.replace(/\s/g,'');
    if(kind==='wa')return 'https://wa.me/88'+d;
    if(kind==='mail')return 'mailto:'+v;
    if(kind==='fb')return /^https?:/.test(v)?v:'https://'+v;
    return '';
  }
  function render(){
    const el=$('cmList');if(!el)return;
    const L=[...CM.list].sort((a,b)=>(+a.ord||999)-(+b.ord||999)||String(a.name||'').localeCompare(String(b.name||''),'bn'));
    const mine=L.find(x=>x.id===me());
    $('cmTop').innerHTML=(me()&&!mine?'<button class="btn" id="cmMine" type="button">আমার তথ্য যোগ করুন</button> ':'')+(S.super?'<button class="btn sec" id="cmAdd" type="button">＋ সদস্য যোগ (সুপার অ্যাডমিন)</button>':'');
    el.innerHTML=L.length?L.map(x=>{
      const rows=[['মোবাইল',val(x,'phone'),link('tel',x.phone)],['ইমেইল',val(x,'email'),link('mail',x.email)],['WhatsApp',val(x,'wa'),link('wa',x.wa)],['ইমো',val(x,'imo'),''],['Facebook',val(x,'fb'),link('fb',x.fb)],['অন্যান্য',val(x,'other'),/^https?:/.test(val(x,'other'))?val(x,'other'):'']].filter(r=>r[1]);
      return `<div class="card cmc"><div class="cmn">${esc(x.name||'—')}${x.id===me()?' <span class="tag in">আপনি</span>':''}</div><div class="cmr">${esc(x.role||'')}</div>
      ${rows.map(r=>`<div class="ml"><span>${r[0]}</span>${r[2]?`<a href="#" data-u="${esc(r[2])}" class="cml">${esc(r[1])}</a>`:`<span>${esc(r[1])}</span>`}</div>`).join('')||'<div class="hint2">কোনো যোগাযোগের তথ্য নেই</div>'}
      <div class="row-actions" style="margin-top:10px">${val(x,'phone')?`<button class="btn sm" data-u="${esc(link('tel',x.phone))}" type="button">ফোন</button>`:''}${val(x,'wa')?`<button class="btn sm" data-u="${esc(link('wa',x.wa))}" type="button">WhatsApp</button>`:''}${canEdit(x)?`<button class="btn sec sm" data-ed="${esc(x.id)}" type="button">তথ্য বদলান</button>`:''}${S.super?`<button class="btn dng sm" data-del="${esc(x.id)}" type="button">মুছুন</button>`:''}</div></div>`}).join(''):'<div class="empty">এখনো কমিটির তথ্য যোগ হয়নি</div>';
  }
  function form(x){
    const isNew=!x.id,own=x.id===me();
    const f=(k,l,ph)=>`<div><label>${l}</label><input id="cm_${k}" value="${esc(val(x,k))}" placeholder="${ph||''}"></div>`;
    openModal({title:isNew?'নতুন সদস্য':'কমিটির তথ্য',sub:'সবাই শুধু নিজের তথ্য বদলাতে পারেন; সুপার অ্যাডমিন সবার',body:`<div class="mform" style="display:grid;gap:10px">${f('name','নাম *')}${f('role','পদবী (সভাপতি, সেক্রেটারি…)')}${f('phone','মোবাইল','01XXXXXXXXX')}${f('email','ইমেইল')}${f('wa','WhatsApp নম্বর')}${f('imo','ইমো নম্বর')}${f('fb','Facebook লিংক')}${f('other','অন্যান্য সোশ্যাল মিডিয়া (লিংক/লেখা)')}${S.super?f('ord','ক্রম (ছোট নম্বর আগে)'):''}</div>`,
      actions:[{label:'বাতিল',cls:'sec',fn:closeModal},{label:'সংরক্ষণ',fn:async()=>{
        if(!needDb())return;const o={};['name','role','phone','email','wa','imo','fb','other'].forEach(k=>o[k]=$('cm_'+k).value.trim());
        if(S.super)o.ord=Number(toEn($('cm_ord').value))||0;else o.ord=x.ord||0;
        if(!o.name){toast('নাম লিখুন');return}
        const id=x.id||(own?me():newId());o.updated=Date.now();o.by=(S.acct&&S.acct.name)||'';
        if(await safe(S.DB.collection('committee').doc(id).set(o),'সংরক্ষিত হয়েছে'))closeModal();}}]});
  }
  document.addEventListener('click',async e=>{
    const u=e.target.closest('#committee [data-u]');if(u){e.preventDefault();openExt(u.dataset.u);return}
    const ed=e.target.closest('#committee [data-ed]');if(ed){const x=CM.list.find(z=>z.id===ed.dataset.ed);if(x)form(x);return}
    if(e.target.closest('#cmMine')){form({id:me(),name:(S.acct&&S.acct.name)||''});return}
    if(e.target.closest('#cmAdd')){form({});return}
    const d=e.target.closest('#committee [data-del]');if(d&&S.super){if(await askConfirm('এই সদস্যের তথ্য মুছবেন?','মুছুন'))safe(S.DB.collection('committee').doc(d.dataset.del).delete(),'মুছে ফেলা হয়েছে')}
  });
  function start(){if(CM.sub||!S.started||!S.acct||!S.DB)return;CM.sub=true;
    S.DB.collection('committee').onSnapshot(s=>{CM.list=s.docs.map(d=>({id:d.id,...d.data()}));render()},()=>{})}
  {const _r=renderAll;renderAll=function(){_r();try{start();render()}catch(e){}}}
  {const _o=openTab;openTab=function(a,b){_o(a,b);if(a==='committee')render()}}
})();
