s=open('index22.html',encoding='utf8').read()
def rep(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:60],s.count(a)); s=s.replace(a,b)
rep('''<button class="btn sec" id="sbkRestore" type="button">ব্যাকআপ থেকে ফেরান</button></div></div>''','''<button class="btn sec" id="sbkRestore" type="button">ব্যাকআপ থেকে ফেরান</button></div>
  <div style="margin-top:14px;padding-top:12px;border-top:1px dashed var(--line,#8884)"><label style="display:flex;gap:10px;align-items:center"><input type="checkbox" id="autoBkOn" style="width:auto"><b>সাপ্তাহিক স্বয়ংক্রিয় ব্যাকআপ</b></label>
   <div class="hint2" id="autoBkInfo">—</div><button class="btn sec sm" id="autoBkRestore" type="button" style="margin-top:8px">স্বয়ংক্রিয় ব্যাকআপ থেকে ফেরান</button></div></div>''')
js=r'''
/* ===== v22: সাপ্তাহিক স্বয়ংক্রিয় ব্যাকআপ (ক্লাউডে, শেষ ৪টি) ===== */
(function(){
  const AUTO_COLS=BK_COLS.filter(c=>c!=='noticeFiles'),CH=200000,KEEP=4,WEEK=7*864e5;
  const on=()=>{try{return localStorage.getItem('bm_autobk')!=='0'}catch(e){return true}};
  async function meta(){try{const d=await S.DB.doc('backups/auto-meta').get();return d.exists?d.data():{ids:[]}}catch(e){return null}}
  async function dropBk(id){try{const ix=await S.DB.doc('backups/auto-'+id).get();if(ix.exists)for(const p of (ix.data().parts||[]))await S.DB.doc('backups/'+p).delete();await S.DB.doc('backups/auto-'+id).delete()}catch(e){}}
  async function runAuto(force){
    if(!S.super||!needDb())return false;
    const m=await meta();if(!m)return false;S.autoBkT=m.t||0;
    if(!force&&(!on()||Date.now()-(m.t||0)<WEEK)){autoInfo();return false}
    try{
      const data=await bkCollect(),id=todayIso()+'-'+(Date.now()%100000),parts=[];
      for(const c of AUTO_COLS){const j=JSON.stringify(data.cols[c]||{});for(let k=0,n=0;k<j.length||n===0;k+=CH,n++){const pid='auto-'+id+'-'+c+'-'+n;await S.DB.doc('backups/'+pid).set({j:j.slice(k,k+CH),c});parts.push(pid)}}
      {const j=JSON.stringify(data.docs||{});await S.DB.doc('backups/auto-'+id+'-docs').set({j,c:'_docs'});parts.push('auto-'+id+'-docs')}
      await S.DB.doc('backups/auto-'+id).set({t:Date.now(),parts});
      const ids=[id].concat((m.ids||[]).filter(x=>x!==id));const old=ids.slice(KEEP);
      await S.DB.doc('backups/auto-meta').set({t:Date.now(),ids:ids.slice(0,KEEP)});
      for(const o of old)await dropBk(o);
      S.autoBkT=Date.now();audit('স্বয়ংক্রিয় ব্যাকআপ','সাপ্তাহিক, ক্লাউডে');autoInfo();if(force)toast('ব্যাকআপ ক্লাউডে সংরক্ষিত হয়েছে');return true;
    }catch(e){if(force)toast('স্বয়ংক্রিয় ব্যাকআপ ব্যর্থ হয়েছে');return false}
  }
  function autoInfo(){const e=$('autoBkInfo'),c=$('autoBkOn');if(!e)return;c.checked=on();
    e.textContent=(on()?'প্রতি ৭ দিনে একবার নিজে থেকে ক্লাউডে সংরক্ষিত হয় (শেষ ৪টি রাখা হয়)। ':'বন্ধ আছে। ')+(S.autoBkT?'সর্বশেষ: '+new Date(S.autoBkT).toLocaleString('bn-BD'):'এখনো হয়নি')}
  $('autoBkOn').onchange=e=>{try{localStorage.setItem('bm_autobk',e.target.checked?'1':'0')}catch(_){}autoInfo();if(e.target.checked)runAuto(false)};
  $('autoBkRestore').onclick=async()=>{
    if(!S.super||!needDb())return;const m=await meta();if(!m||!(m.ids||[]).length){toast('এখনো কোনো স্বয়ংক্রিয় ব্যাকআপ নেই');return}
    const items=[];for(const id of m.ids){try{const d=await S.DB.doc('backups/auto-'+id).get();if(d.exists)items.push({id,t:d.data().t,parts:d.data().parts})}catch(e){}}
    openModal({title:'স্বয়ংক্রিয় ব্যাকআপ',sub:'যেটি ফেরাতে চান সেটির বোতাম চাপুন',body:'<div class="mb">'+items.map((x,k)=>`<div class="ml"><span>${esc(new Date(x.t).toLocaleString('bn-BD'))}</span><button class="btn sm" data-k="${k}" type="button">ফেরান</button></div>`).join('')+'</div>',actions:[{label:'বন্ধ',cls:'sec',fn:closeModal}]});
    document.querySelectorAll('#mBody button[data-k], .modal button[data-k]').forEach(b=>b.onclick=async()=>{
      const it=items[+b.dataset.k];closeModal();
      if(!await askConfirm(new Date(it.t).toLocaleString('bn-BD')+' এর ব্যাকআপ ফেরালে বর্তমান তথ্যের ওপর এই রেকর্ডগুলো বসবে। আগে বর্তমান তথ্যের নতুন ব্যাকআপ রাখা হবে।','চালিয়ে যান'))return;
      if(!await runAuto(true)){toast('বর্তমান তথ্যের ব্যাকআপ না হলে ফেরানো হবে না');return}
      toast('ফেরানো হচ্ছে…');let ok=0,bad=0;
      try{const bag={};for(const p of it.parts){const d=await S.DB.doc('backups/'+p).get();if(!d.exists)continue;const x=d.data();(bag[x.c]=bag[x.c]||[]).push([p,x.j])}
        for(const c of Object.keys(bag)){const js=bag[c].sort((a,b)=>a[0]<b[0]?-1:1).sort((a,b)=>(+a[0].split('-').pop())-(+b[0].split('-').pop())).map(z=>z[1]).join('');const o=JSON.parse(js);
          if(c==='_docs'){for(const p of Object.keys(o)){try{await S.DB.doc(p).set(o[p]);ok++}catch(e){bad++}}}
          else for(const id of Object.keys(o)){try{await S.DB.doc(c+'/'+id).set(o[id]);ok++}catch(e){bad++}}}
      }catch(e){bad++}
      audit('স্বয়ংক্রিয় ব্যাকআপ থেকে পুনরুদ্ধার',ok+' সফল, '+bad+' ব্যর্থ');toast(bad?ok+' টি ফিরেছে, '+bad+' টি ব্যর্থ':'পুনরুদ্ধার সম্পন্ন: '+ok+' টি রেকর্ড');
    });
  };
  let started=false;
  {const _r=renderAll;renderAll=function(){_r();try{autoInfo()}catch(e){}if(!started&&S.super&&S.psetLoaded){started=true;setTimeout(()=>runAuto(false),7000)}}}
  window.runAutoBk=runAuto;
  /* মাসিক স্মরণ: স্বয়ংক্রিয় ব্যাকআপ থাকলে দেখাবে না */
  {const _b=bkRemind;bkRemind=function(){if(S.autoBkT&&Date.now()-S.autoBkT<WEEK*2){const el=$('bkRemind');if(el)el.hidden=true;return}_b()}}
})();
'''
# insert before final </script>
i=s.rindex('</script>')
s=s[:i]+js+s[i:]
open('index23.html','w',encoding='utf8').write(s)
