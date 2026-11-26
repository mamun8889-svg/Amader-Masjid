const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index29.html');p.setDefaultTimeout(8000);
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.waitForTimeout(1500);
 await p.evaluate(()=>{window.__w=null;window.Android={setWidget:j=>{window.__w=j;return true},setPrayer:()=>true}});
 await p.evaluate(()=>openTab('prayer'));await p.waitForTimeout(500);
 const out=await p.evaluate(()=>{const S=pwSample();const names=[];const wrap=document.createElement('div');wrap.style.cssText='position:fixed;left:0;top:0;z-index:9999;background:#556;width:1500px;display:flex;flex-wrap:wrap;gap:8px;padding:8px';document.body.appendChild(wrap);
  for(let d=1;d<=4;d++){const L=pwLays({d,l:'a',h:1,s:1,c:1,j:1,r:1});L.forEach(l=>{const c=document.createElement('canvas');c.style.cssText='width:350px;background:#667';wrap.appendChild(c);pwPaint(c,l,S);names.push(d+l.id+':'+l.e.length)})}
  return names.join(' ')});
 console.log(out);
 await p.setViewportSize({width:1520,height:1100});await p.screenshot({path:'pwall.png'});
 await p.selectOption('#pwD','2');await p.waitForTimeout(300);
 console.log('pushed',await p.evaluate(()=>window.__w&&JSON.parse(window.__w).lays.map(l=>l.id+l.e.length).join(',')));
 console.log(errs);process.exit();
})();
