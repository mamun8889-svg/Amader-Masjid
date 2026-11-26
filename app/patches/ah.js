
/* ===== v30: সাধারণ অ্যাডমিনের বেতন-ড্যাশবোর্ড ===== */
(function(){
  const NOW=()=>{const n=new Date();return {y:n.getFullYear(),c:n.getMonth(),d:n.getDate(),abs:n.getFullYear()*12+n.getMonth()}};
  const AH={y:0,m:0,init:false};
  const isAH=()=>{try{return !!(isAdminView()&&!S.super)}catch(e){return false}};
  const idxOf=(y,cal)=>{const ms=monthsOf(y);for(let k=0;k<ms.length;k++)if(monthCal(y,k)===cal)return k;return -1};
  const absOf=(y,m)=>y*12+monthCal(y,m);
  const locate=abs=>{const y=Math.floor(abs/12),c=abs%12;if(y<2025||y>2030)return null;const m=idxOf(y,c);return m<0?null:{y,m}};
  const lastDate=(y,name,m)=>{let d='';(S.payments||[]).forEach(p=>{if(p.status==='void'||p.kind==='waive'||p.y!==y||nameKey(p.name)!==nameKey(name))return;if((p.alloc||[]).some(a=>a.m===m)&&String(p.date||'')>d)d=String(p.date||'')});return d};
  /* নির্বাচিত মাসের রিপোর্ট (শুধু পড়া, কোনো তথ্য বদলায় না) */
  function rep(y,m){
    const paid=[],unpaid=[];let sched=0,coll=0,pend=0;
    rowsOf(y).forEach((r,i)=>{
      if(!(r.amount>0)||r.name==='(নামহীন জমা)')return;
      const v=val(y,i,m);if(v==='x'||v==='r'||offAfter(y,r,m))return;
      const w=waivedAmt(y,r.name,m),p=isNum(v)&&v>0?v:0,need=Math.max(0,r2(r.amount-w)),rest=Math.max(0,r2(need-p));
      sched+=need;coll+=p;pend+=rest;
      if(p>0)paid.push({y,i,m,name:r.name,amt:p,sched:need,rest,date:lastDate(y,r.name,m)});
      if(rest>0)unpaid.push({y,i,m,name:r.name,sched:need,got:p,rest});
    });
    return {paid,unpaid,sched:r2(sched),coll:r2(coll),pend:r2(pend),total:paid.length+unpaid.filter(u=>!u.got).length};
  }
  /* ব্যক্তিভিত্তিক বকেয়া (মাসভিত্তিক), selAbs পর্যন্ত */
  function arrears(selAbs,only){
    const map={};
    for(let y=2025;y<=2030;y++){
      let rows;try{rows=rowsOf(y)}catch(e){continue}
      rows.forEach((r,i)=>{
        if(!(r.amount>0)||r.name==='(নামহীন জমা)')return;
        if(only&&nameKey(r.name)!==nameKey(only))return;
        const st=payerStats(y,i);
        st.rows.forEach(x=>{if(typeof x.m!=='number'||!(x.due>0))return;if(absOf(y,x.m)>selAbs)return;
          const k=nameKey(r.name),o=map[k]||(map[k]={name:r.name,items:[],amt:0,y,i});
          o.items.push({lab:x.name+' '+bn(y),amt:x.due,abs:absOf(y,x.m)});o.amt=r2(o.amt+x.due)});
      });
    }
    const list=Object.values(map).sort((a,b)=>b.amt-a.amt);
    list.forEach(o=>o.items.sort((a,b)=>a.abs-b.abs));
    return list;
  }
  window.__arr=arrears;
  const mLab=(y,m)=>monthsOf(y)[m]+' '+bn(y);
  function status(abs){
    const n=NOW();
    if(abs===n.abs)return n.d>=25?{t:'সংগ্রহ চলছে — ৫ তারিখ পর্যন্ত',k:'on'}:{t:'চলতি মাস — ২৫ তারিখ থেকে সংগ্রহ',k:'soon'};
    if(abs===n.abs-1)return n.d<=5?{t:'সংগ্রহ চলছে — '+bn(5)+' তারিখ পর্যন্ত',k:'on'}:{t:'সংগ্রহের সময় শেষ',k:'end'};
    if(abs<n.abs)return {t:'পুরোনো মাস — শুধু দেখা',k:'old'};
    return {t:'ভবিষ্যৎ মাস',k:'old'};
  }
  const nm=(x)=>esc(x);
  /* ছোট সারসংক্ষেপ কার্ড (চলতি/গত মাস) */
  function sumCard(title,abs){
    const loc=locate(abs);
    if(!loc)return `<div class="ahc"><div class="aht">${title}</div><div class="ahs">এই মাসের তথ্য নেই</div></div>`;
    const R=rep(loc.y,loc.m),st=status(abs);
    return `<div class="ahc ${st.k==='on'?'on':''}"><div class="aht">${title} <span class="ahm">${esc(mLab(loc.y,loc.m))}</span></div><div class="ahs ${st.k}">${st.t}</div>
     ${(()=>{const tot=R.paid.length+R.unpaid.filter(u=>!u.got).length,pc=tot?Math.round(R.paid.length*100/tot):0;return '<div class="pbar"><i data-w="'+pc+'"></i></div><div class="hint2" style="margin:4px 0 10px">'+bn(pc)+'% জন বেতন দিয়েছেন</div>'})()}<div class="ahg2"><button class="ahb ok" data-act="paid" data-y="${loc.y}" data-m="${loc.m}"><span class="n">${bn(R.paid.length)} জন</span><span class="l">বেতন দিয়েছেন</span><span class="a">${money(R.coll)}</span></button>
     <button class="ahb no" data-act="unpaid" data-y="${loc.y}" data-m="${loc.m}"><span class="n">${bn(R.unpaid.length)} জন</span><span class="l">বেতন দেননি</span><span class="a">${money(R.pend)}</span></button></div></div>`;
  }
  function plist(arr,kind,y,m){
    if(!arr.length)return '<div class="hint2">কেউ নেই</div>';
    const cap=6;
    return arr.slice(0,cap).map(x=>kind==='paid'
      ?`<div class="ahr"><span>${nm(x.name)}</span><b>${money(x.amt)}</b></div>`
      :`<div class="ahr"><span>${nm(x.name)}${x.got?' <small class="tg">আংশিক</small>':''}</span><b>${money(x.rest)}</b></div>`).join('')
      +(arr.length>cap?`<button class="ahmore" data-act="${kind}" data-y="${y}" data-m="${m}">সব ${bn(arr.length)} জন দেখুন</button>`:`<button class="ahmore" data-act="${kind}" data-y="${y}" data-m="${m}">বিস্তারিত দেখুন</button>`);
  }
  function selReport(){
    const y=AH.y,m=AH.m,abs=absOf(y,m),R=rep(y,m),A=arrears(abs),st=status(abs),aTot=r2(A.reduce((s,o)=>s+o.amt,0));
    const yo=[2025,2026,2027,2028,2029,2030].map(v=>`<option value="${v}"${v===y?' selected':''}>${bn(v)}</option>`).join('');
    const mo=monthsOf(y).map((n,k)=>`<option value="${k}"${k===m?' selected':''}>${n}</option>`).join('');
    return `<div class="ahsel"><select id="ahY" aria-label="বছর">${yo}</select><select id="ahM" aria-label="মাস">${mo}</select></div>
     <div class="ahs ${st.k}" style="margin:6px 0 10px">${esc(mLab(y,m))} — ${st.t}</div>${(()=>{const pc=R.total?Math.round(R.paid.length*100/R.total):0;return '<div class="pbar"><i data-w="'+pc+'"></i></div><div class="hint2" style="margin:4px 0 10px">'+bn(pc)+'% জন বেতন দিয়েছেন</div>'})()}
     <div class="ahgrid">
      <div class="ahx"><span class="l">মোট বেতনভোগী</span><span class="n">${bn(R.total)} জন</span></div>
      <button class="ahx ok" data-act="paid" data-y="${y}" data-m="${m}"><span class="l">বেতন দিয়েছেন</span><span class="n">${bn(R.paid.length)} জন</span></button>
      <button class="ahx no" data-act="unpaid" data-y="${y}" data-m="${m}"><span class="l">বেতন দেননি</span><span class="n">${bn(R.unpaid.length)} জন</span></button>
      <button class="ahx" data-act="paid" data-y="${y}" data-m="${m}"><span class="l">মোট আদায়</span><span class="n g">${money(R.coll)}</span></button>
      <button class="ahx" data-act="unpaid" data-y="${y}" data-m="${m}"><span class="l">মোট অনাদায়</span><span class="n r">${money(R.pend)}</span></button>
      <div class="ahx"><span class="l">মোট নির্ধারিত</span><span class="n">${money(R.sched)}</span></div>
     </div>
    `;
  }
  function render(){
    const el=$('adminHome');if(!el)return;
    const on=isAH();document.body.classList.toggle('ahOn',on);
    if(!on){el.hidden=true;return}
    el.hidden=false;
    const n=NOW();
    if(!AH.init){const L=locate(n.abs)||locate(n.abs-1)||{y:2026,m:0};AH.y=L.y;AH.m=L.m;AH.init=true}
    el.innerHTML=`<div class="sec-head"><div><h3>বেতন ব্যবস্থাপনা</h3><div class="sub">${bn(n.d)} ${['জানুয়ারি','ফেব্রুয়ারি','মার্চ','এপ্রিল','মে','জুন','জুলাই','আগস্ট','সেপ্টেম্বর','অক্টোবর','নভেম্বর','ডিসেম্বর'][n.c]} ${bn(n.y)} — সংগ্রহ: প্রতি মাসের ২৫ তারিখ থেকে পরের মাসের ৫ তারিখ</div></div></div>
     <div class="ahcards">${sumCard('চলতি মাস',n.abs)}${sumCard('গত মাস',n.abs-1)}</div>
     <div class="ahrep"><h4>মাস ও বছর বাছাই করে রিপোর্ট</h4><div id="ahBody">${selReport()}</div></div>`;
  }
  function modalList(kind,y,m){
    const R=rep(y,m),abs=absOf(y,m),canEnter=abs<=NOW().abs;
    const A={};arrears(abs).forEach(o=>{A[nameKey(o.name)]=o});
    const btn=()=>'';
    let h,rows,title;
    if(kind==='paid'){
      title='বেতন দিয়েছেন — '+mLab(y,m);
      h=['নাম','তারিখ','দিয়েছেন','বকেয়া'];
      rows=R.paid.map(x=>{const a=A[nameKey(x.name)];const due=(x.rest>0?x.rest:0)+(a?0:0);const tot=a?a.amt:0;
        return `<tr><td>${nm(x.name)}</td><td>${x.date?payDate(x.date):'—'}</td><td class="num">${fmt(x.amt)}</td><td class="num">${tot?'<span class="v low">'+fmt(tot)+'</span>':(x.rest>0?'<span class="v low">'+fmt(x.rest)+'</span>':'—')}</td></tr>`});
      rows.push(`<tr><td><b>মোট ${bn(R.paid.length)} জন</b></td><td></td><td class="num"><b>${fmt(R.coll)}</b></td><td></td></tr>`);
    }else if(kind==='unpaid'){
      title='বেতন দেননি — '+mLab(y,m);
      h=['নাম','নির্ধারিত','এ মাসে বাকি','মোট বকেয়া'];
      rows=R.unpaid.map(x=>{const a=A[nameKey(x.name)];
        return `<tr><td>${nm(x.name)}${x.got?' <small class="tg">আংশিক '+fmt(x.got)+'</small>':''}</td><td class="num">${fmt(x.sched)}</td><td class="num">${fmt(x.rest)}</td><td class="num">${a?'<span class="v low">'+fmt(a.amt)+'</span>':'—'}</td></tr>`});
      rows.push(`<tr><td><b>মোট ${bn(R.unpaid.length)} জন</b></td><td></td><td class="num"><b>${fmt(R.pend)}</b></td><td></td></tr>`);
    }else{
      title='বকেয়া তালিকা — '+mLab(y,m)+' পর্যন্ত';
      const L=arrears(abs);h=['নাম','বকেয়া মাস','মোট বকেয়া'];
      rows=L.map(o=>`<tr><td>${nm(o.name)}</td><td>${bn(o.items.length)} মাস: ${esc(o.items.map(x=>x.lab).join(', '))}</td><td class="num"><span class="v low">${fmt(o.amt)}</span></td></tr>`);
      rows.push(`<tr><td><b>মোট ${bn(L.length)} জন</b></td><td></td><td class="num"><b>${fmt(r2(L.reduce((s,o)=>s+o.amt,0)))}</b></td></tr>`);
    }
    openModal({title,sub:'শুধু দেখার তালিকা — এখান থেকে কিছু বদলায় না',body:'<div class="tablewrap" style="max-height:60vh;overflow:auto">'+table(h,rows)+'</div>',actions:[{label:'বন্ধ করুন',cls:'sec',fn:closeModal}]});
    document.querySelectorAll('#mBody [data-ent]').forEach(b=>b.onclick=()=>{const [yy,ii,mm]=b.dataset.ent.split('|').map(Number);entry(yy,ii,mm)});
  }
  function entry(y,i,m){
    closeModal();openTab('payentry');
    try{$('pYear').value=String(y);payerOptions();$('pPayer').value=String(i);PAY.sel=new Set(m!=null?[m]:[]);$('pTotal').value='';renderPayMonths();if(m!=null)autoAlloc(true)}catch(e){}
  }
  /* ইভেন্ট */
  document.addEventListener('click',e=>{
    const b=e.target.closest('#adminHome [data-act]');
    if(b){modalList(b.dataset.act,+b.dataset.y,+b.dataset.m);return}
  });
  document.addEventListener('change',e=>{
    if(e.target.id==='ahY'){AH.y=+e.target.value;const ms=monthsOf(AH.y);if(AH.m>=ms.length)AH.m=ms.length-1;$('ahBody').innerHTML=selReport()}
    else if(e.target.id==='ahM'){AH.m=+e.target.value;$('ahBody').innerHTML=selReport()}
  });
  /* বেতন এন্ট্রি ফর্মে ব্যক্তিভিত্তিক বকেয়া */
  function dueBox(){
    const pi=$('pInfo');if(!pi)return;let box=$('pDue');if(!box){box=document.createElement('div');box.id='pDue';pi.parentNode.insertBefore(box,pi.nextSibling)}
    const y=+$('pYear').value,i=$('pPayer').value;if(i===''){box.innerHTML='';return}
    const r=rowsOf(y)[+i],name=r.name,n=NOW(),A=arrears(1e9,name)[0]||{items:[],amt:0};
    /* সর্বশেষ কোন মাস পর্যন্ত পরিশোধ */
    let lastAbs=-1,lastLab='—';
    for(let yy=2025;yy<=2030;yy++){const ii=payerIndex(yy,name);if(ii<0)continue;payerStats(yy,ii).rows.forEach(x=>{if(typeof x.m==='number'&&x.paid>0&&absOf(yy,x.m)>lastAbs){lastAbs=absOf(yy,x.m);lastLab=x.name+' '+bn(yy)}})}
    /* চলতি মাস */
    let cur='',curPend=0;const L=locate(n.abs);
    if(L){const ci=payerIndex(L.y,name);if(ci>=0){const rr=rowsOf(L.y)[ci],v=val(L.y,ci,L.m);
      if(rr.amount>0&&v!=='x'&&v!=='r'&&!offAfter(L.y,rr,L.m)){const p=isNum(v)?v:0,w=waivedAmt(L.y,rr.name,L.m),rest=Math.max(0,r2(rr.amount-w-p));
        const inArr=n.abs<=dueUp(L.y)+L.y*12;curPend=inArr?0:rest;
        cur=`<div class="ml"><span>চলতি মাসের বেতন (${esc(mLab(L.y,L.m))})</span><span>${rest>0?money(rest)+(p>0?' বাকি':''):'পরিশোধিত'}</span></div>`}}}
    const total=r2(A.amt+curPend);
    box.innerHTML=`<div class="pdue ${A.amt>0?'warn':'okk'}">
      <div class="ml"><span>নাম</span><b>${esc(name)}</b></div>
      <div class="ml"><span>নির্ধারিত মাসিক বেতন</span><span>${r.amount?money(r.amount):'নেই'}</span></div>
      <div class="ml"><span>সর্বশেষ পরিশোধ</span><span>${esc(lastLab)} পর্যন্ত</span></div>
      <div class="ptag">${A.amt>0?'বকেয়া রয়েছে: '+bn(A.items.length)+' মাস | মোট বকেয়া: '+money(A.amt):'বকেয়া নেই।'}</div>
      ${A.amt>0?'<div class="hint2">'+esc(A.items.map(x=>x.lab+' '+fmt(x.amt)).join(' · '))+'</div>':''}
      ${cur}
      <div class="ml tot"><span>সব মিলিয়ে মোট প্রদেয়</span><b>${money(total)}</b></div></div>`;
  }
  {const _r=renderPayMonths;renderPayMonths=function(){_r();try{dueBox()}catch(e){}}}
  /* একই মাস দ্বিতীয়বার নেওয়ার সতর্কতা */
  {const _s=sumAlloc;sumAlloc=function(){_s();try{
    const y=+$('pYear').value,i=$('pPayer').value;if(i===''||$('pKind')&&$('pKind').value==='waive')return;
    const r=rowsOf(y)[+i],dup=readAlloc().filter(a=>a.amt>0&&r.amount>0&&(()=>{const v=val(y,+i,a.m);return isNum(v)&&v>=r.amount})()).map(a=>monthsOf(y)[a.m]);
    if(dup.length)$('pSum').insertAdjacentHTML('beforeend',' <span class="tag bad">সতর্কতা: '+esc(dup.join(', '))+' মাসের বেতন আগেই পুরো পরিশোধ হয়েছে — আবার নিচ্ছেন?</span>');
  }catch(e){}}}
  /* রেন্ডার হুক */
  {const _d=renderDashboard;renderDashboard=function(){_d();try{render()}catch(e){console.error(e)}}}
  {const _o=openTab;openTab=function(a,b){_o(a,b);document.body.classList.toggle('onHome',curTab==='dashboard');if(a==='payentry'||a==='salary')try{dueBox()}catch(e){}}}
  document.body.classList.add('onHome');
  try{render()}catch(e){}
})();
