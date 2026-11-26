s=open('index25.html',encoding='utf8').read()
def rep(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:60],s.count(a)); s=s.replace(a,b)
rep(' <div class="grid kpis" id="kpis"></div>',' <div id="remBanner" class="panel" hidden style="margin-bottom:14px;border-left:4px solid #0ea5e9"></div>\n <div class="grid kpis" id="kpis"></div>')
js=r'''
/* ===== v25: WhatsApp বার্তা ও ৫ তারিখের তাগাদা ===== */
(function(){
  {const _s=smsDialog;smsDialog=function(o){_s(o);const ph=smsPhone(o.phone);const a=$('mAct');if(!ph||!a||!$('smsTx')||a.querySelector('.waBtn'))return;
    const b=document.createElement('button');b.type='button';b.className='btn sec waBtn';b.textContent='WhatsApp';
    b.onclick=()=>{const t=$('smsTx').value.trim();if(!t){toast('বার্তা খালি');return}const u='https://wa.me/88'+ph+'?text='+encodeURIComponent(t);let ok=false;try{if(window.Android&&window.Android.wa)ok=window.Android.wa(u)}catch(e){}if(!ok){try{window.open(u,'_blank');ok=true}catch(e){}}
      if(ok){closeModal();try{logSms({t:Date.now(),name:o.name,phone:ph,kind:(o.kind||'')+' (WhatsApp)',key:o.key,by:(S.acct&&S.acct.name)||''})}catch(e){}}};
    a.insertBefore(b,a.lastChild)}}
  function target(){const n=new Date(),ab=n.getFullYear()*12+n.getMonth()-(n.getDate()<=5?1:0);return {y:Math.floor(ab/12),c:ab%12}}
  function list(){
    const t=target();if(t.y<2025||t.y>2030)return null;let m=-1;const ms=monthsOf(t.y);for(let k=0;k<ms.length;k++)if(monthCal(t.y,k)===t.c)m=k;if(m<0)return null;
    const out=[];rowsOf(t.y).forEach((r,i)=>{if(!(r.amount>0)||r.name==='(নামহীন জমা)')return;const v=val(t.y,i,m);if(v==='x'||v==='r'||offAfter(t.y,r,m))return;
      const due=Math.max(0,r2(r.amount-(isNum(v)?v:0)-waivedAmt(t.y,r.name,m)));if(due>0)out.push({i,r,due})});
    return {t,m,out,mn:ms[m]};
  }
  function remind(){
    const L=list();if(!L)return;
    const row=x=>{const rec=payerRec(x.r.name)||{},ph=smsPhone(rec.phone);return `<div class="ml"><span>${esc(x.r.name)} <b>${fmt(x.due)}</b>${ph?'':' <small style="color:var(--muted)">(নম্বর নেই)</small>'}</span><button class="btn sm" type="button" data-i="${x.i}" ${ph?'':'disabled'}>বার্তা</button></div>`};
    openModal({title:L.mn+' '+bn(L.t.y)+' — তাগাদা',sub:fmt(L.out.length)+' জনের এখনো বাকি · "বার্তা" চাপলে SMS বা WhatsApp-এ পাঠানো যায়',body:'<div class="mb" style="max-height:50vh;overflow:auto">'+(L.out.map(row).join('')||'<div class="empty">সবাই দিয়েছেন 🎉</div>')+'</div>',actions:[{label:'বন্ধ',cls:'sec',fn:closeModal}]});
    document.querySelectorAll('#mBody button[data-i]').forEach(b=>b.onclick=()=>{const x=L.out.find(z=>z.i===+b.dataset.i),rec=payerRec(x.r.name)||{};
      const text='আসসালামু আলাইকুম, '+x.r.name+'। '+L.mn+' '+bn(L.t.y)+' এর মাসিক বেতন বাবদ '+bn(x.due)+' টাকা এখনো পাওয়া যায়নি। মাসের ৫ তারিখের মধ্যে পরিশোধের অনুরোধ রইল। জাযাকাল্লাহু খাইরান। '+MOSQUE_SIG;
      smsDialog({name:x.r.name,phone:rec.phone,text,key:'rem:'+L.t.y+':'+x.i+':'+L.m+':'+todayIso().slice(0,7),kind:'মাসিক তাগাদা'})});
  }
  window.openRemind=remind;
  function banner(){
    const el=$('remBanner');if(!el)return;if(!isAdminView()){el.hidden=true;return}
    const n=new Date(),d=n.getDate(),last=new Date(n.getFullYear(),n.getMonth()+1,0).getDate();
    if(!(d<=5||d>=last-2)){el.hidden=true;return}
    const L=list();if(!L){el.hidden=true;return}
    el.hidden=false;el.innerHTML='<b>'+(d<=5?'৫ তারিখের মধ্যে বেতন সংগ্রহের সময়':'মাস শেষ হয়ে আসছে')+'</b><div class="hint2">'+esc(L.mn)+' '+bn(L.t.y)+': এখনো '+fmt(L.out.length)+' জনের বেতন বাকি। </div><button class="btn sm" id="remBtn" type="button">তাগাদা পাঠান</button>';
    $('remBtn').onclick=remind;
  }
  {const _d=renderDashboard;renderDashboard=function(){_d();try{banner()}catch(e){}}}
})();
'''
i=s.rindex('</script>')
s=s[:i]+js+s[i:]
open('index26.html','w',encoding='utf8').write(s)
