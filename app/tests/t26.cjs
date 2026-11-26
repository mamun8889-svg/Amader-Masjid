const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index24.html');p.setDefaultTimeout(8000);
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.waitForTimeout(1500);
 await p.evaluate(()=>{openTab('salary');showPay(true)});await p.waitForTimeout(400);
 await p.click('#bulkBtn');await p.waitForTimeout(500);
 console.log(await p.evaluate(()=>[$('bkM').value,$('bkList').children.length,$('bkSum').innerText]));
 await p.screenshot({path:'bk1.png'});
 await p.click('#bkDue');await p.waitForTimeout(200);
 console.log(await p.evaluate(()=>$('bkSum').innerText));
 const before=await p.evaluate(()=>S.payments.length);
 await p.click('#mAct button:nth-child(2)');await p.waitForTimeout(500);
 await p.click('#mAct button:nth-child(2)');await p.waitForTimeout(1500);
 console.log('payments',before,await p.evaluate(()=>S.payments.length),await p.evaluate(()=>[...document.querySelectorAll('.toast,#toast')].map(t=>t.innerText)));
 console.log(errs);process.exit();
})();
