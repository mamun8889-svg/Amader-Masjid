s=open('index24.html',encoding='utf8').read()
def rep(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:60],s.count(a)); s=s.replace(a,b)
# reorder TABS
rep(" {id:'payers',t:'বেতনদাতা',i:'people',admin:1},{id:'reports',t:'CSV ও ব্যাকআপ',i:'down',admin:1},{id:'audit',t:'পরিবর্তনের লগ',i:'book',sup:1,admin:1},{id:'dev',"," {id:'payers',t:'বেতনদাতা',i:'people',admin:1},{id:'dev',")
rep("{id:'staff',t:'কর্মচারী',i:'user',admin:1},{id:'access',t:'ব্যবহারকারী',i:'shield',admin:1,sup:1},{id:'settings',t:'সেটিংস',i:'shield',sup:1,admin:1}\n","{id:'staff',t:'কর্মচারী',i:'user',admin:1},\n {id:'reports',t:'CSV ও ব্যাকআপ',i:'down',admin:1,grp:1},{id:'audit',t:'পরিবর্তনের লগ',i:'book',sup:1,admin:1,grp:1},{id:'access',t:'ব্যবহারকারী ও ডিভাইস',i:'shield',admin:1,sup:1,grp:1},{id:'settings',t:'সেটিংস',i:'shield',sup:1,admin:1,grp:1}\n")
# dashboard dues use last DUE month
rep("const pu=paidUnpaid(DY,L);","const LD=Math.max(0,Math.min(L,dueUp(DY))),pu=paidUnpaid(DY,LD),puL=paidUnpaid(DY,L);")
rep("fmt(pu.paid)+' জন দিয়েছেন')+\n   kpi('k-vi','people'","fmt(puL.paid)+' জন দিয়েছেন')+\n   kpi('k-vi','people'")
rep("k+=kpi('k-ro','bell',lm+' মাসে বকেয়া'","k+=kpi('k-ro','bell',M26[LD]+' মাস পর্যন্ত বকেয়া'")
rep("$('duesTitle').textContent=lm+' '+bn(DY)+' — বকেয়া তালিকা'","$('duesTitle').textContent=M26[LD]+' '+bn(DY)+' — বকেয়া তালিকা'")
css='''
.kmore{display:none!important}
.dfull .kmore{display:flex!important;flex-direction:column}
#dashMore{width:100%;margin:2px 0 14px;font-weight:600}
.dlite #dashMore2{display:none}
body:not(.dfullb) #dashSecond>.panel:first-child{display:none}
body:not(.dfullb) #dashSecond{grid-template-columns:1fr}
.grp{display:flex;align-items:center;justify-content:space-between;width:100%;padding:11px 14px;border-radius:12px;background:#ffffff14;font-size:15px;font-weight:700;cursor:pointer;color:inherit}
.grpbox{display:none;flex-direction:column;gap:6px;padding-left:10px;border-left:2px solid #ffffff30;margin:2px 0 6px}
.grpbox.open{display:flex}
'''
rep("</style>",css+"</style>")
rep(' <div class="grid two">\n  <div class="panel"><h4 id="dashT2">',' <div class="grid two" id="dashSecond">\n  <div class="panel"><h4 id="dashT2">')
rep(' <div class="grid kpis" id="kpis"></div>',' <div class="grid kpis" id="kpis"></div>\n <button type="button" class="btn sec" id="dashMore">▾ আরও দেখুন</button>')
js=r'''
/* ===== v24: সরল ড্যাশবোর্ড, ব্যবস্থাপনা গ্রুপ ===== */
(function(){
  const get=()=>{try{return localStorage.getItem('bm_dfull')==='1'}catch(e){return false}};
  const KEYS=['মাসিক বেতন সংগ্রহ','সক্রিয় সদস্য','উন্নয়ন তহবিল','অনুমোদনের'];
  function apply(){
    const full=get();document.body.classList.toggle('dfullb',full);const d=$('dashboard');if(d)d.classList.toggle('dfull',full);
    [...$('kpis').children].forEach(c=>{const t=(c.querySelector('.lb')||c).textContent||'';c.classList.toggle('kmore',KEYS.some(k=>t.includes(k)))});
    $('dashMore').textContent=full?'▴ কম দেখান':'▾ আরও দেখুন';
    $('dashMore').style.display=[...$('kpis').children].some(c=>c.classList.contains('kmore'))||true?'':'none';
  }
  $('dashMore').onclick=()=>{try{localStorage.setItem('bm_dfull',get()?'0':'1')}catch(e){}apply()};
  {const _d=renderDashboard;renderDashboard=function(){_d();try{apply()}catch(e){}}}
  /* ব্যবস্থাপনা গ্রুপ */
  function grp(){
    const nav=$('nav');if(!nav||nav.querySelector('.grp'))return;
    const bs=[...nav.querySelectorAll('button')].filter(b=>(TABS.find(t=>t.id===b.dataset.tab)||{}).grp);if(!bs.length)return;
    const open=bs.some(b=>b.dataset.tab===curTab)||nav.dataset.grp==='1';
    const h=document.createElement('div');h.className='grp';h.innerHTML='<span>⚙ ব্যবস্থাপনা</span><span>'+(open?'▴':'▾')+'</span>';
    const box=document.createElement('div');box.className='grpbox'+(open?' open':'');
    bs[0].before(h);h.after(box);bs.forEach(b=>box.appendChild(b));
    h.onclick=()=>{const o=box.classList.toggle('open');nav.dataset.grp=o?'1':'0';h.lastChild.textContent=o?'▴':'▾'};
  }
  {const _b=buildNav;buildNav=function(){_b();grp()}}
  {const _o=openTab;openTab=function(id,fb){_o(id,fb);const t=TABS.find(x=>x.id===id);if(t&&t.grp){const bx=document.querySelector('#nav .grpbox');if(bx)bx.classList.add('open')}}}
  buildNav();
})();
'''
i=s.rindex('</script>')
s=s[:i]+js+s[i:]
open('index25.html','w',encoding='utf8').write(s)
