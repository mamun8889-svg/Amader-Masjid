const L=require('./lib.cjs');
(async()=>{const {b,p}=await L.start('index13.html');
 console.log(await p.evaluate(()=>document.body.className));
 await p.evaluate(()=>openTab('salary'));await p.waitForTimeout(600);await p.screenshot({path:'a_sal.png'});
 await p.evaluate(()=>openTab('payers'));await p.waitForTimeout(500);await p.screenshot({path:'a_pay.png'});
 await p.click('.ftrig >> visible=true');await p.waitForTimeout(400);await p.screenshot({path:'a_dlg.png'});
 console.log(p.errs);await b.close()})()
