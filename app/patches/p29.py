s=open('index28.html',encoding='utf8').read()
def rep(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:60],s.count(a)); s=s.replace(a,b)
# jamat token pre-format, no narrow nbsp
rep("fmt12(t).replace(' ','\u202f')","fmt12(t)")
rep("((PZ.ov.jamat||{})[k]?fmt12(t24(PZ.ov.jamat[k])):'')","((PZ.ov.jamat||{})[k]?'জামাত '+fmt12(t24(PZ.ov.jamat[k])):'')")
html='''
<div class="panel" id="pzWidget" style="margin-bottom:14px"><h4>হোম স্ক্রিন উইজেট</h4>
 <div class="hint2">ফোনের হোম স্ক্রিনে ফাঁকা জায়গায় চেপে ধরে "উইজেট" → "আমাদের মসজিদ" → "নামাজের সময়" বেছে বসান। এখানের পছন্দ ফোনে উইজেটে কার্যকর হবে (প্রতিটি ফোনে আলাদাভাবে)।</div>
 <canvas id="pwPrev" style="width:100%;max-width:420px;border-radius:14px;margin:10px auto;display:block;background:#8883"></canvas>
 <div class="mform"><label for="pwD">ডিজাইন</label><select id="pwD"><option value="1">১. প্রিমিয়াম গ্লাস</option><option value="2">২. ক্লাসিক ইসলামিক</option><option value="3">৩. মিনিমাল ক্লিন</option><option value="4">৪. ডার্ক প্রিমিয়াম</option></select>
 <label for="pwL">আকার/লেআউট</label><select id="pwL"><option value="a">স্বয়ংক্রিয় (উইজেটের মাপ অনুযায়ী)</option><option value="c">কমপ্যাক্ট</option><option value="s">স্ট্যান্ডার্ড</option><option value="e">এক্সপান্ডেড</option></select>
 <label class="chk"><input type="checkbox" id="pwH"> হিজরি তারিখ দেখান</label><label class="chk"><input type="checkbox" id="pwS"> সূর্যোদয় ও সূর্যাস্ত দেখান</label><label class="chk"><input type="checkbox" id="pwC"> Countdown দেখান</label><label class="chk"><input type="checkbox" id="pwJ"> জামাতের সময় দেখান</label><label class="chk"><input type="checkbox" id="pwR"> রমজানে সাহরি-ইফতারের আলাদা উইজেট দেখান</label></div>
 <div class="hint2" id="pwInfo" style="margin-top:6px"></div></div>
'''
rep(' <div class="panel adminonly" id="pzAdmin"',html+' <div class="panel adminonly" id="pzAdmin"')
js=r'''
/* ===== v28: নামাজের উইজেট ডিজাইন, সেটিংস, প্রিভিউ ===== */
(function(){
  const U=h=>parseInt(h,16)>>>0;
  const R=(x,y,w,h,r,c,cd='',st=0)=>['r',x,y,w,h,r,c,cd,st],G=(x,y,w,h,r,a,b,cd='')=>['g',x,y,w,h,r,a,b,cd],
        T=(x,y,sz,c,al,b,txt,cd='',mw=0)=>['t',x,y,sz,c,al,b,mw,txt,cd],Ln=(a,b,c,d,w,col,cd='')=>['l',a,b,c,d,w,col,cd];
  const PN=['ফজর','যোহর','আসর','মাগরিব','এশা'],PT=['s1','s3','s4','s5','s6'];
  const TH={
   1:{c1:U('E6104A3C'),c2:U('E60B2236'),tx:U('FFFFFFFF'),mu:U('FFBFD8CF'),ac:U('FFF6C453'),hi:U('40F6C453'),br:U('55FFFFFF')},
   2:{c1:U('FF0B3D2E'),c2:U('FF0B3D2E'),tx:U('FFFFF6DC'),mu:U('FFE0C878'),ac:U('FFE5B94A'),hi:U('33E5B94A'),br:U('FFE5B94A')},
   3:{c1:U('F2FFFFFF'),c2:U('F2F3F7F5'),tx:U('FF16322B'),mu:U('FF5B6F68'),ac:U('FF0E7C5A'),hi:U('2210B981'),br:U('22000000')},
   4:{c1:U('F20F1318'),c2:U('F2151C24'),tx:U('FFF1F5F9'),mu:U('FF8FA0B3'),ac:U('FF38BDF8'),hi:U('3338BDF8'),br:U('33FFFFFF')}};
  function strip(t,y,h,jam,x0=10,w=340){const cw=w/5,o=[];for(let k=0;k<5;k++){const x=x0+k*cw;o.push(R(x+2,y,cw-4,h,10,t.hi,'n'+k));
    o.push(T(x+cw/2,y+h*(jam?.30:.38),11.5,t.mu,1,0,PN[k],'',cw-4));o.push(T(x+cw/2,y+h*(jam?.62:.74),13,t.tx,1,1,'{'+PT[k]+'}','',cw-4));
    if(jam)o.push(T(x+cw/2,y+h*.92,8.5,t.mu,1,0,'{j'+k+'}','',cw-4))}return o}
  function list(t,x,y,w,rh,jam){const o=[];for(let k=0;k<5;k++){const yy=y+k*rh;o.push(R(x,yy,w,rh-3,8,t.hi,'n'+k));o.push(T(x+10,yy+rh*.66,12.5,t.tx,0,0,PN[k]));
    if(jam)o.push(T(x+w*.5,yy+rh*.66,8.5,t.mu,1,0,'{j'+k+'}','',w*.3));o.push(T(x+w-10,yy+rh*.66,12.5,t.tx,2,1,'{'+PT[k]+'}','',w*.4))}return o}
  const bg=(t,w,h,r,frame)=>{const o=[G(0,0,w,h,r,t.c1,t.c2)];if(t.br)o.push(R(1,1,w-2,h-2,r,t.br,'',frame||1.2));return o};
  const sun=(t,y,show,al=1,x=180)=>show?[T(x,y,10.5,t.mu,al,0,'☀ সূর্যোদয় {s2}   ☾ সূর্যাস্ত {s5}','',330)]:[];
  const dts=(t,y,hj,x=180,al=1)=>[T(x,y,11,t.mu,al,0,'{dt}','',330)].concat(hj?[T(x,y+14,10.5,t.ac,al,0,'{hj}','',330)]:[]);
  function build(d,size,o){const t=TH[d],cd=o.cd,jam=o.jam;let w=360,h,e=[];
   if(size==='m'){h=210;e=bg(t,w,h,d===2?16:26);
     e.push(T(180,26,12,t.ac,1,1,'রমজান মুবারক'+(d===2?' ✦':''),'',300));
     e.push(R(14,40,160,70,14,t.hi));e.push(R(186,40,160,70,14,t.hi));
     e.push(T(94,62,11,t.mu,1,0,'সাহরির শেষ সময়'));e.push(T(94,95,22,t.tx,1,1,'{s0}','',150));
     e.push(T(266,62,11,t.mu,1,0,'ইফতার'));e.push(T(266,95,22,t.ac,1,1,'{s5}','',150));
     if(cd)e.push(T(180,132,13,t.tx,1,1,'ইফতারে বাকি: {ic}','',330));
     e=e.concat(strip(t,142,56,jam));e.push(T(180,h-6,9.5,t.mu,1,0,o.hijri?'{hj}':'{dt}','',330));return {id:'m',w,h,e}}
   if(size==='c'){h=d===3?84:110;e=bg(t,w,h,d===2?14:26);
     if(d===1){e.push(T(22,34,11,t.mu,0,0,'পরবর্তী ওয়াক্ত'));e.push(T(22,74,30,t.tx,0,1,'{nx}','',170));e.push(T(338,74,30,t.ac,2,1,'{nt}','',170));if(cd)e.push(T(180,100,13,t.mu,1,0,'{cd} বাকি','',330))}
     else if(d===2){e.push(T(180,28,11,t.ac,1,0,'✦  পরবর্তী ওয়াক্ত  ✦'));e.push(Ln(40,36,320,36,.8,t.ac));e.push(T(180,72,26,t.tx,1,1,'{nx} · {nt}','',330));if(cd)e.push(T(180,98,12.5,t.mu,1,0,'{cd} বাকি','',330))}
     else if(d===3){e.push(T(18,50,24,t.tx,0,1,'{nx}','',120));e.push(T(150,50,24,t.ac,0,1,'{nt}','',130));if(cd)e.push(T(342,50,13,t.mu,2,0,'{cd}','',170));e.push(T(18,72,10.5,t.mu,0,0,'পরবর্তী ওয়াক্ত'))}
     else{e.push(T(20,62,38,t.ac,0,1,'{nt}','',200));e.push(T(22,92,13,t.mu,0,0,'{nx} ওয়াক্ত','',200));if(cd){e.push(T(340,56,11,t.mu,2,0,'বাকি'));e.push(T(340,86,18,t.tx,2,1,'{cd}','',150))}}
     return {id:'c',w,h,e}}
   if(size==='s'){h=d===3?150:170;e=bg(t,w,h,d===2?16:26);
     if(d===1){e.push(T(180,20,10.5,t.mu,1,0,'রাধানগর পশ্চিম পাড়া বাইতুল মা\'মুর জামে মসজিদ','',330));e.push(T(20,62,24,t.tx,0,1,'{nx}','',140));e.push(T(340,62,24,t.ac,2,1,'{nt}','',160));if(cd)e.push(T(180,84,12.5,t.mu,1,0,'{cd} বাকি','',330));e=e.concat(strip(t,96,66,jam))}
     else if(d===2){e.push(T(180,24,11.5,t.ac,1,1,'বাইতুল মা\'মুর জামে মসজিদ','',320));e.push(Ln(30,32,330,32,.8,t.ac));e.push(R(8,8,344,h-16,10,t.br,'',.8));e.push(T(180,56,15,t.tx,1,1,'পরবর্তী: {nx} {nt}','',320));if(cd)e.push(T(180,74,11.5,t.mu,1,0,'{cd} বাকি','',320));e=e.concat(strip(t,86,70,jam,14,332))}
     else if(d===3){e.push(T(18,34,11,t.mu,0,0,'পরবর্তী ওয়াক্ত'));e.push(T(18,76,30,t.tx,0,1,'{nx}','',150));e.push(T(18,108,22,t.ac,0,1,'{nt}','',150));if(cd)e.push(T(18,134,12,t.mu,0,0,'{cd} বাকি','',150));e=e.concat(list(t,172,10,178,26,jam))}
     else{e.push(T(18,38,34,t.ac,0,1,'{nt}','',170));e.push(T(20,60,12.5,t.mu,0,0,'{nx} ওয়াক্ত','',170));if(cd)e.push(T(20,86,12,t.tx,0,1,'{cd} বাকি','',170));e.push(T(20,150,10,t.mu,0,0,'{dt}','',170));e=e.concat(list(t,190,10,160,29,jam))}
     return {id:'s',w,h,e}}
   h=d===3?240:270;e=bg(t,w,h,d===2?16:26);
   if(d===1){e.push(T(180,20,10.5,t.mu,1,0,'রাধানগর পশ্চিম পাড়া বাইতুল মা\'মুর জামে মসজিদ','',330));e.push(T(20,62,26,t.tx,0,1,'{nx}','',140));e.push(T(340,62,26,t.ac,2,1,'{nt}','',160));if(cd)e.push(T(180,84,12.5,t.mu,1,0,'{cd} বাকি','',330));e=e.concat(strip(t,96,66,jam));e=e.concat(sun(t,190,o.sun));e=e.concat(dts(t,222,o.hijri))}
   else if(d===2){e.push(T(180,26,12.5,t.ac,1,1,'বাইতুল মা\'মুর জামে মসজিদ','',320));e.push(Ln(30,35,330,35,.8,t.ac));e.push(R(8,8,344,h-16,10,t.br,'',.8));e=e.concat(dts(t,56,o.hijri));e.push(T(180,110,16,t.tx,1,1,'পরবর্তী: {nx} {nt}','',320));if(cd)e.push(T(180,130,12,t.mu,1,0,'{cd} বাকি','',320));e=e.concat(strip(t,142,70,jam,14,332));e=e.concat(sun(t,236,o.sun))}
   else if(d===3){e.push(T(18,30,11,t.mu,0,0,'{dt}','',324));if(o.hijri)e.push(T(18,46,10.5,t.ac,0,0,'{hj}','',324));e.push(T(18,92,32,t.tx,0,1,'{nx}','',150));e.push(T(18,126,24,t.ac,0,1,'{nt}','',150));if(cd)e.push(T(18,152,12,t.mu,0,0,'{cd} বাকি','',150));e=e.concat(sun(t,196,o.sun,0,18));e=e.concat(list(t,172,58,178,34,jam))}
   else{e.push(T(20,50,38,t.ac,0,1,'{nt}','',180));e.push(T(22,72,13,t.mu,0,0,'{nx} ওয়াক্ত','',180));if(cd)e.push(T(20,98,13,t.tx,0,1,'{cd} বাকি','',180));e.push(T(20,128,10.5,t.mu,0,0,'{dt}','',160));if(o.hijri)e.push(T(20,144,10.5,t.ac,0,0,'{hj}','',160));e=e.concat(list(t,196,14,150,34,jam));e=e.concat(sun(t,h-14,o.sun))}
   return {id:'e',w,h,e}}
  const cfg=()=>{let c={d:1,l:'a',h:1,s:1,c:1,j:0,r:1};try{c=Object.assign(c,JSON.parse(localStorage.getItem('bm_wcfg')||'{}'))}catch(e){}return c};
  function lays(c){const o={hijri:!!c.h,sun:!!c.s,cd:!!c.c,jam:!!c.j};const a=['c','s','e'].map(z=>build(+c.d,z,o));if(c.r)a.push(build(+c.d,'m',o));return a}
  function sample(){const n=new Date(),dd=pzDay(n),dt=bnDates(n),k={dt:dt.wd+', '+dt.g,bd:dt.b,hj:dt.h};dd.t.forEach((t,c)=>k['s'+c]=pzFmt(t));
    const J=PZ.ov.jamat||{};['fajr','zuhr','asr','maghrib','isha'].forEach((q,i)=>k['j'+i]=J[q]?'জামাত '+pzFmt(+J[q].split(':')[0]*60+ +J[q].split(':')[1]):'');
    const nm=n.getHours()*60+n.getMinutes(),PR=[1,3,4,5,6];let nx=0,diff=0,tm=false;for(let i=0;i<5;i++)if(dd.t[PR[i]]>nm){nx=i;diff=dd.t[PR[i]]-nm;break;}else if(i===4){tm=true;diff=dd.t[1]+1440-nm}
    const cdf=m=>{const h=Math.floor(m/60);return h>0?bn(h)+' ঘণ্টা '+bn(m%60)+' মিনিট':bn(m)+' মিনিট'};
    const ram=pzIsRam(n)?1:0;k.ram=ram;const ic=ram&&dd.t[5]>nm?cdf(dd.t[5]-nm):'';
    return {k,nx,ram,tk:{nx:PN[nx],nt:k['s'+PR[nx]],cd:cdf(diff),ic}}}
  function cond(c,S){if(!c)return true;const ch=c[0];if(ch==='R')return S.ram===1;if(ch==='r')return S.ram===0;const d=+c[1];if(ch==='n')return S.nx===d;if(ch==='N')return S.nx!==d;return true}
  function sub(t,S){let x=t.replace('{nx}',S.tk.nx).replace('{nt}',S.tk.nt).replace('{cd}',S.tk.cd).replace('{ic}',S.tk.ic);Object.keys(S.k).forEach(q=>{x=x.split('{'+q+'}').join(String(S.k[q]))});return x}
  const rgba=n=>{n=n>>>0;return 'rgba('+((n>>16)&255)+','+((n>>8)&255)+','+(n&255)+','+((n>>>24)/255).toFixed(3)+')'};
  function paint(cv,lay,S){const dpr=2,W=lay.w*dpr,H=lay.h*dpr;cv.width=W;cv.height=H;const g=cv.getContext('2d');g.scale(dpr,dpr);g.clearRect(0,0,lay.w,lay.h);
    const rr=(x,y,w,h,r)=>{g.beginPath();g.moveTo(x+r,y);g.arcTo(x+w,y,x+w,y+h,r);g.arcTo(x+w,y+h,x,y+h,r);g.arcTo(x,y+h,x,y,r);g.arcTo(x,y,x+w,y,r);g.closePath()};
    lay.e.forEach(e=>{const ty=e[0];try{
      if(ty==='r'){if(!cond(e[7],S))return;rr(e[1],e[2],e[3],e[4],e[5]);if(e[8]>0){g.lineWidth=e[8];g.strokeStyle=rgba(e[6]);g.stroke()}else{g.fillStyle=rgba(e[6]);g.fill()}}
      else if(ty==='g'){if(!cond(e[8],S))return;const gr=g.createLinearGradient(0,e[2],0,e[2]+e[4]);gr.addColorStop(0,rgba(e[6]));gr.addColorStop(1,rgba(e[7]));rr(e[1],e[2],e[3],e[4],e[5]);g.fillStyle=gr;g.fill()}
      else if(ty==='l'){if(!cond(e[7],S))return;g.beginPath();g.moveTo(e[1],e[2]);g.lineTo(e[3],e[4]);g.lineWidth=e[5];g.strokeStyle=rgba(e[6]);g.stroke()}
      else if(ty==='t'){if(!cond(e[9],S))return;const tx=sub(e[8],S);let sz=e[3];g.font=(e[6]?'bold ':'')+sz+'px sans-serif';g.textAlign=['left','center','right'][e[5]];g.fillStyle=rgba(e[4]);
        if(e[7]>0){const w=g.measureText(tx).width;if(w>e[7]){sz=sz*e[7]/w;g.font=(e[6]?'bold ':'')+sz+'px sans-serif'}}g.fillText(tx,e[1],e[2])}}catch(_){}})}
  window.pwLays=lays;
  function push(){const c=cfg();try{if(window.Android&&window.Android.setWidget)window.Android.setWidget(JSON.stringify({mode:c.l,ram:c.r?1:0,lays:lays(c)}))}catch(e){}}
  function ui(){const c=cfg();$('pwD').value=c.d;$('pwL').value=c.l;$('pwH').checked=!!c.h;$('pwS').checked=!!c.s;$('pwC').checked=!!c.c;$('pwJ').checked=!!c.j;$('pwR').checked=!!c.r;
    try{const S=sample(),L=lays(c);let lay=(c.l==='a'?L.find(x=>x.id==='s'):L.find(x=>x.id===c.l))||L[1];if(S.ram&&c.r&&L.find(x=>x.id==='m')&&(c.l==='a'||c.l==='m'))lay=L.find(x=>x.id==='m');paint($('pwPrev'),lay,S)}catch(e){}
    $('pwInfo').textContent=(window.Android&&window.Android.setWidget)?'উইজেট ফোনে সংরক্ষিত হয়েছে। হোম স্ক্রিনের উইজেটে পরিবর্তন প্রায় সাথে সাথেই দেখা যাবে।':'এটি অ্যান্ড্রয়েড অ্যাপে কাজ করবে (ব্রাউজারে শুধু প্রিভিউ)।'}
  function save(){const c={d:+$('pwD').value,l:$('pwL').value,h:$('pwH').checked?1:0,s:$('pwS').checked?1:0,c:$('pwC').checked?1:0,j:$('pwJ').checked?1:0,r:$('pwR').checked?1:0};try{localStorage.setItem('bm_wcfg',JSON.stringify(c))}catch(e){}ui();push()}
  ['pwD','pwL','pwH','pwS','pwC','pwJ','pwR'].forEach(i=>$(i).addEventListener('change',save));
  window.pwUi=ui;window.pwPush=push;window.pwPaint=paint;window.pwSample=sample;window.pwBuild=build;
  {const _o=openTab;openTab=function(id,fb){_o(id,fb);if(id==='prayer')ui()}}
  {const _p=window.pzPush;window.pzPush=function(){_p();push()}}
  setTimeout(push,3500);
})();
'''
i=s.rindex('</script>')
s=s[:i]+js+s[i:]
open('index29.html','w',encoding='utf8').write(s)
