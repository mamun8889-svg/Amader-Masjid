s=open('index23.html',encoding='utf8').read()
def rep(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:60],s.count(a)); s=s.replace(a,b)
rep('<div class="panel" style="margin-bottom:14px"><form id="payForm" style="margin-top:6px">','<div class="panel" style="margin-bottom:14px"><button type="button" class="btn" id="bulkBtn" style="width:100%;margin-bottom:10px">☑ একসাথে অনেকের বেতন এন্ট্রি</button><form id="payForm" style="margin-top:6px">')
js=r'''
/* ===== v23: একসাথে অনেকের বেতন এন্ট্রি ===== */
(function(){
  const bm={busy:false};
  function defYM(){const n=new Date(),ab=n.getFullYear()*12+n.getMonth()-(n.getDate()<=5?1:0);return {y:Math.floor(ab/12),c:ab%12}}
  const idxOf=(y,c)=>{const ms=monthsOf(y);for(let m=0;m<ms.length;m++)if(monthCal(y,m)===c)return m;return -1};
  function rowsFor2(y,m){
    const prevC=monthCal(y,m)-1,pm=prevC>=0?idxOf(y,prevC):-1;
    return rowsOf(y).map((r,i)=>({r,i})).filter(x=>x.r.amount>0&&x.r.name!=='(নামহীন জমা)'&&val(y,x.i,m)!=='x'&&val(y,x.i,m)!=='r'&&!offAfter(y,x.r,m)).map(x=>{
      const v=val(y,x.i,m),paid=isNum(v)?v:0,due=Math.max(0,r2(x.r.amount-paid-waivedAmt(y,x.r.name,m)));
      const pv=pm>=0?val(y,x.i,pm):null;return {...x,paid,due,prev:isNum(pv)&&pv>0}});
  }
  function open(){
    if(!isAdminView()||!needDb())return;
    const d=defYM(),y0=[2025,2026,2027,2028,2029,2030].includes(d.y)?d.y:2026;let m0=idxOf(y0,d.c);if(m0<0)m0=0;
    openModal({title:'একসাথে বেতন এন্ট্রি',sub:'নাম টিক দিন, দরকার হলে অঙ্ক বদলান, তারপর সংরক্ষণ চাপুন',
     body:`<div class="mform"><div style="display:flex;gap:8px"><select id="bkY" style="flex:1">${[2026,2027,2028,2029,2030,2025].map(y=>`<option value="${y}"${y===y0?' selected':''}>${bn(y)}</option>`).join('')}</select><select id="bkM" style="flex:2"></select></div>
      <div style="display:flex;gap:8px"><input id="bkD" type="date" style="flex:1" value="${today()}"><select id="bkMt" style="flex:1">${METHODS.map(x=>`<option>${x}</option>`).join('')}</select></div>
      <input id="bkQ" placeholder="নাম বা নং খুঁজুন…" style="width:100%">
      <div style="display:flex;gap:6px;flex-wrap:wrap"><button type="button" class="btn sec sm" id="bkPrev">আগের মাসে যারা দিয়েছেন</button><button type="button" class="btn sec sm" id="bkDue">যাদের বাকি আছে</button><button type="button" class="btn sec sm" id="bkNone">সব বাদ</button></div>
      <div id="bkList" style="max-height:42vh;overflow:auto;margin:8px 0"></div><div id="bkSum" class="hint2"></div></div>`,
     actions:[{label:'বন্ধ',cls:'sec',fn:closeModal},{label:'সংরক্ষণ',fn:save}]});
    const fillM=()=>{const y=+$('bkY').value,ms=monthsOf(y);$('bkM').innerHTML=ms.map((n,i)=>`<option value="${i}">${n}</option>`).join('');$('bkM').value=y===y0?m0:String(ms.length-1)};
    fillM();let st=null;
    const draw=(pre)=>{
      const y=+$('bkY').value,m=+$('bkM').value;const all=rowsFor2(y,m);
      if(pre||!st)st=new Map(all.map(x=>[x.i,{on:x.prev&&x.due>0,amt:x.due}]));
      const q=toEn($('bkQ').value.trim().toLowerCase());
      $('bkList').innerHTML=all.filter(x=>!q||String(x.r.name).toLowerCase().includes(q)||String(x.r.no??'').includes(q)).map(x=>{const z=st.get(x.i)||{on:false,amt:x.due};
        return `<label style="display:flex;gap:8px;align-items:center;padding:6px 0;border-bottom:1px solid #8883"><input type="checkbox" class="bkc" data-i="${x.i}" ${z.on?'checked':''} ${x.due<=0?'disabled':''} style="width:auto"><span style="flex:1;min-width:0">${esc(x.r.name)}<small style="display:block;color:var(--muted)">${x.due<=0?'এ মাসে পরিশোধিত':'নির্ধারিত '+fmt(x.r.amount)+(x.paid?' · দিয়েছেন '+fmt(x.paid):'')}</small></span><input class="bka" data-i="${x.i}" inputmode="decimal" value="${z.amt}" ${x.due<=0?'disabled':''} style="width:80px"></label>`}).join('')||'<div class="empty">কেউ নেই</div>';
      sum()};
    const sum=()=>{if(!st)return;let n=0,t=0;st.forEach(z=>{if(z.on){n++;t+=Number(toEn(String(z.amt)))||0}});$('bkSum').innerHTML='বেছেছেন <b>'+fmt(n)+' জন</b> · মোট <b>'+money(r2(t))+'</b>'};
    $('bkList').addEventListener('input',e=>{const i=+e.target.dataset.i,z=st.get(i);if(!z)return;if(e.target.classList.contains('bkc'))z.on=e.target.checked;else z.amt=e.target.value;sum()});
    $('bkY').onchange=()=>{fillM();st=null;draw(true)};$('bkM').onchange=()=>{st=null;draw(true)};$('bkQ').oninput=()=>draw(false);
    $('bkPrev').onclick=()=>draw(true);
    $('bkDue').onclick=()=>{const y=+$('bkY').value,m=+$('bkM').value;st=new Map(rowsFor2(y,m).map(x=>[x.i,{on:x.due>0,amt:x.due}]));draw(false)};
    $('bkNone').onclick=()=>{st.forEach(z=>z.on=false);draw(false)};
    draw(true);
    async function save(){
      if(bm.busy)return;const y=+$('bkY').value,m=+$('bkM').value,date=$('bkD').value,method=$('bkMt').value;
      const pick=[];st.forEach((z,i)=>{const a=r2(Number(toEn(String(z.amt)))||0);if(z.on&&a>0)pick.push({i,a})});
      if(!pick.length){toast('কাউকে বাছা হয়নি');return}if(!date){toast('তারিখ দিন');return}
      if(!await askConfirm(fmt(pick.length)+' জনের মোট '+money(r2(pick.reduce((s,x)=>s+x.a,0)))+' সংরক্ষণ করবেন? প্রত্যেকের আলাদা রসিদ হবে।','সংরক্ষণ করুন'))return;
      bm.busy=true;toast('সংরক্ষণ হচ্ছে…');
      const yy=date.slice(0,4);let mx=(S.payments||[]).reduce((q,p)=>{const g=String(p.receipt||'').match(/^R-(\d{4})-(\d+)$/);return g&&g[1]===yy?Math.max(q,+g[2]):q},0);let ok=0;
      for(const x of pick){const r=rowsOf(y)[x.i];
        const sig=[y,x.i,date,x.a,'pay',m+':'+x.a].join('|');
        if((S.payments||[]).some(p=>p.status!=='void'&&p.sig===sig))continue;
        mx++;const pay={y,i:x.i,name:r.name,kind:'pay',dateEst:false,date,method,ref:'',note:'একসাথে এন্ট্রি',total:x.a,alloc:[{m,amt:x.a}],status:'active',sig,receipt:'R-'+yy+'-'+String(mx).padStart(4,'0'),created:Date.now()+ok,by:(S.acct&&S.acct.name)||''};
        try{await col('payments').doc(newId()).set(pay);const cur=val(y,x.i,m);await setCell(y,x.i,m,r2((isNum(cur)?cur:0)+x.a));ok++;audit('পেমেন্ট এন্ট্রি',pay.receipt+' · '+pay.name+' · '+pay.total)}catch(e){mx--;break}}
      bm.busy=false;closeModal();toast(ok+' জনের বেতন সংরক্ষিত হয়েছে'+(ok<pick.length?' (বাকিগুলো হয়নি/আগেই ছিল)':''));
    }
  }
  $('bulkBtn').onclick=open;window.openBulkPay=open;
})();
'''
i=s.rindex('</script>')
s=s[:i]+js+s[i:]
open('index24.html','w',encoding='utf8').write(s)
