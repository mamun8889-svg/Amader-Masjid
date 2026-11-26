
/* ===== v32: অ্যানিমেশন ও মাইক্রো-ইন্টারঅ্যাকশন (ডেটা অপরিবর্তিত) ===== */
(function(){
  const RM=()=>matchMedia('(prefers-reduced-motion: reduce)').matches;
  const re=/^([^০-৯]*?)([০-৯][০-৯,\.]*)([^০-৯]*)$/;
  function count(el){
    if(RM()||el.dataset.cu)return;const t=el.textContent.trim(),m=re.exec(t);if(!m)return;
    const target=Number(toEn(m[2]).replace(/,/g,''));if(!isFinite(target)||target<=0)return;
    el.dataset.cu='1';const pre=m[1],suf=m[3],t0=performance.now(),D=750;
    (function f(n){const k=Math.min(1,(n-t0)/D),e=1-Math.pow(1-k,3);
      if(!el.isConnected)return;
      el.textContent=k>=1?t:pre+fmt(target%1===0?Math.round(target*e):Math.round(target*e*100)/100)+suf;
      if(k<1)requestAnimationFrame(f)})(t0);
  }
  function runCount(root){
    (root||document).querySelectorAll('.section.active .kpi .vl,.section.active .ahb .n,.section.active .ahb .a,.section.active .ahx .n').forEach(count);
  }
  function bars(){
    /* বেতন সংগ্রহ অনুপাত — মাসিক বেতন পাতার কার্ড */
    const st=document.getElementById('salStats');if(!st)return;
    const k=st.querySelectorAll('.kpi');if(k.length<3)return;const c=k[2];if(c.querySelector('.pbar'))return;
    const v=/([০-৯,]+)\s*জন/.exec(c.querySelector('.vl')&&c.querySelector('.vl').textContent||''),u=/([০-৯,]+)\s*জন/.exec(c.querySelector('.sb')&&c.querySelector('.sb').textContent||'');
    if(!v||!u)return;const a=+toEn(v[1]).replace(/,/g,''),b=+toEn(u[1]).replace(/,/g,'');if(!(a+b>0))return;
    const pct=Math.round(a*100/(a+b));
    c.insertAdjacentHTML('beforeend',`<div class="pbar"><i style="width:0"></i></div><div class="sb">${bn(pct)}% জন দিয়েছেন</div>`);
    const i=c.querySelector('.pbar i');requestAnimationFrame(()=>requestAnimationFrame(()=>{i.style.width=pct+'%'}));
  }
  function stagger(id){
    if(RM())return;const s=document.getElementById(id);if(!s)return;s.classList.remove('stg');void s.offsetWidth;s.classList.add('stg');setTimeout(()=>s.classList.remove('stg'),1100);
  }
  function pbarsAH(){document.querySelectorAll('#adminHome .pbar i[data-w]').forEach(i=>{if(i.style.width)return;requestAnimationFrame(()=>requestAnimationFrame(()=>{i.style.width=i.dataset.w+'%'}))})}
  {const _o=openTab;openTab=function(a,b){_o(a,b);setTimeout(()=>{try{stagger(curTab);runCount();bars();pbarsAH()}catch(e){}},40)}}
  let first=false;
  {const _d=renderDashboard;renderDashboard=function(){_d();try{pbarsAH();if(!first){const k=document.querySelector('#kpis .vl,#adminHome .ahb .n');if(k&&k.textContent.trim()){first=true;stagger('dashboard');runCount()}}}catch(e){}}}
  const sx=document.getElementById('salStats');if(sx)new MutationObserver(()=>{try{bars()}catch(e){}}).observe(sx,{childList:true});
  try{bars()}catch(e){}
})();
