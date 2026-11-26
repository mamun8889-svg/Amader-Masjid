const {chromium}=require('playwright');const mock=require('./mock.cjs');
(async()=>{
 const b=await chromium.launch();
 for(const w of [320,360,412]){
  const ctx=await b.newContext({viewport:{width:w,height:800},isMobile:true,deviceScaleFactor:2});const p=await ctx.newPage();
  const errs=[];p.on('pageerror',e=>errs.push(e.message));
  await p.route(/fonts\.g/,r=>r.abort());await mock(p);
  await p.goto('file://'+process.cwd()+'/index18.html');await p.waitForTimeout(800);
  await p.evaluate(()=>document.getElementById('loginBtn').click());
  await p.fill('#lId','hmabdullah8889@gmail.com');await p.fill('#lPw','12345678');
  await p.evaluate(()=>{document.getElementById('gEnter').disabled=false});
  const t0=Date.now();await p.click('#gEnter');
  await p.waitForFunction(()=>!document.getElementById('app').hidden,null,{timeout:15000});
  console.log(w,'login ms',Date.now()-t0);
  await p.waitForTimeout(600);
  const ov=await p.evaluate(()=>{const els=[...document.querySelectorAll('.side .row > *, .sright > *:not([hidden]), .sbrand > *')].filter(e=>e.offsetParent!==null);const bx=els.map(e=>[e.id||e.className,e.getBoundingClientRect()]);const o=[];
   const top=[...document.querySelectorAll('.sright > *')].filter(e=>e.offsetParent!==null).map(e=>[e.id||e.className,e.getBoundingClientRect()]);
   for(let i=0;i<top.length;i++){for(let j=i+1;j<top.length;j++){const a=top[i][1],c=top[j][1];if(a.left<c.right-1&&c.left<a.right-1&&a.top<c.bottom-1&&c.top<a.bottom-1)o.push(top[i][0]+'x'+top[j][0])}}
   const br=document.querySelector('.sbrand').getBoundingClientRect(),sr=document.querySelector('.sright').getBoundingClientRect();
   return {o,sw:document.documentElement.scrollWidth,brandRight:br.right,srightLeft:sr.left,sameRow:Math.abs(br.top-sr.top)<20}});
  console.log(w,JSON.stringify(ov));
  await p.screenshot({path:'hd'+w+'.png',clip:{x:0,y:0,width:w,height:330}});
  await p.evaluate(()=>openTab('contacts'));await p.waitForTimeout(800);
  if(w===360)await p.screenshot({path:'ct360.png'});
  console.log(errs);await ctx.close();
 }
 process.exit();
})();
