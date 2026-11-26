const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index29.html');p.setDefaultTimeout(8000);
 await p.waitForTimeout(1200);
 await p.evaluate(()=>openTab('prayer'));await p.waitForTimeout(400);
 await p.evaluate(()=>{const S=pwSample();const c=document.createElement('canvas');c.id='pvx';c.style.cssText='position:fixed;left:0;top:0;width:360px;z-index:9999';document.body.appendChild(c);pwPaint(c,pwLays({d:1,l:'a',h:1,s:1,c:1,j:0,r:1})[1],S)});
 await (await p.$('#pvx')).screenshot({path:'w_prev2.png',omitBackground:true});
 process.exit();
})();
