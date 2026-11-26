s=open('index26.html',encoding='utf8').read()
def rep(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:60],s.count(a)); s=s.replace(a,b)
rep(' <div id="remBanner"',' <div id="myDues" class="panel" hidden style="margin-bottom:14px;border-left:4px solid #10b981"></div>\n <div id="verBanner" class="panel" hidden style="margin-bottom:14px;border-left:4px solid #8b5cf6"></div>\n <div id="remBanner"')
rep('<button class="btn sec" id="sbkRestore" type="button">ব্যাকআপ থেকে ফেরান</button></div>','<button class="btn sec" id="sbkRestore" type="button">ব্যাকআপ থেকে ফেরান</button><button class="btn sec" id="verPush" type="button">নতুন সংস্করণ জানান</button></div>')
js=r'''
/* ===== v26: সার্চ, নিজের হিসাব, অফলাইন বার্তা, নতুন সংস্করণ ===== */
(function(){
  const APP_VER=26;
  /* সার্চ: আয়-ব্যয় ও কর্মচারী */
  [['txTable','আয়-ব্যয় খুঁজুন…'],['staffTable','কর্মচারী খুঁজুন…']].forEach(([id,ph])=>{
    const t=$(id);if(!t)return;const inp=document.createElement('input');inp.placeholder=ph;inp.style.cssText='width:100%;margin:10px 0 0';inp.type='search';t.before(inp);
    const f=()=>{const q=toEn(inp.value.trim().toLowerCase());t.querySelectorAll('tbody tr').forEach(r=>{r.style.display=!q||r.textContent.toLowerCase().includes(q)?'':'none'})};
    inp.oninput=f;new MutationObserver(f).observe(t,{childList:true,subtree:true});
  });
  /* সদস্যের নিজের বকেয়া */
  function mine(){
    const el=$('myDues');if(!el)return;
    if(isAdminView()||!S.acct||!S.acct.name){el.hidden=true;return}
    let rows='',tot=0,found=false;
    for(const y of [2025,2026,2027,2028,2029,2030]){const i=payerIndex(y,S.acct.name);if(i<0)continue;found=true;const st=payerStats(y,i);if(!st.paid&&!st.due)continue;tot+=st.due;
      rows+=`<div class="ml"><span>${bn(y)} — দিয়েছেন ${money(st.paid)}</span><span>${st.due>0?'<b style="color:#b45309">বকেয়া '+money(st.due)+'</b>':'বকেয়া নেই'}</span></div>`}
    if(!found){el.hidden=true;return}
    el.hidden=false;el.innerHTML='<b>আমার হিসাব</b><div class="mb" style="margin-top:8px">'+(rows||'<div class="hint2">এখনো কোনো এন্ট্রি নেই</div>')+'</div>'+(tot>0?'<div class="hint2">৫ তারিখের মধ্যে চলতি মাসের বেতন পরিশোধ করার অনুরোধ রইল।</div>':'');
  }
  /* নতুন সংস্করণ */
  function ver(){const el=$('verBanner');if(!el)return;const v=S.pset&&Number(S.pset.appVer)||0;if(v>APP_VER){el.hidden=false;el.innerHTML='<b>নতুন সংস্করণ এসেছে</b><div class="hint2">আরও ভালো কাজের জন্য অ্যাপের নতুন সংস্করণ নিন (সংস্করণ '+bn(v)+')। বর্তমান: '+bn(APP_VER)+'</div>'}else el.hidden=true}
  $('verPush').onclick=async()=>{if(!S.super||!needDb())return;const v=await askText('নতুন সংস্করণ নম্বর','যে নম্বরের APK দিয়েছেন সেটি লিখুন (বর্তমান '+APP_VER+')। এর চেয়ে পুরোনো অ্যাপে নোটিশ দেখাবে।',String(APP_VER+1),'জানান');if(v===null)return;const n=Number(toEn(v));if(!(n>0)){toast('সঠিক নম্বর দিন');return}
    try{await S.DB.doc('pub/settings').update({appVer:n});toast('জানানো হয়েছে');audit('নতুন সংস্করণের নোটিশ','সংস্করণ '+n)}catch(e){toast('সংরক্ষণ হয়নি')}};
  {const _d=renderDashboard;renderDashboard=function(){_d();try{mine();ver()}catch(e){}}}
  /* অফলাইন */
  const ob=document.createElement('div');ob.id='offBar';ob.style.cssText='position:fixed;left:0;right:0;top:0;z-index:400;background:#b45309;color:#fff;text-align:center;font-size:14px;padding:6px 10px;display:none';ob.textContent='ইন্টারনেট নেই — নেট এলে তথ্য নিজে থেকে মিলবে। এখন নতুন এন্ট্রি করবেন না।';document.body.appendChild(ob);
  const up=()=>{ob.style.display=navigator.onLine===false?'block':'none'};addEventListener('online',()=>{up();toast('ইন্টারনেট ফিরেছে')});addEventListener('offline',up);up();
})();
'''
i=s.rindex('</script>')
s=s[:i]+js+s[i:]
open('index27.html','w',encoding='utf8').write(s)
