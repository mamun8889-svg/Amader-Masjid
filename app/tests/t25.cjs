const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index23.html');p.setDefaultTimeout(8000);
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.waitForTimeout(1500);
 console.log('super',await p.evaluate(()=>S.super));
 console.log('run1',await p.evaluate(()=>runAutoBk(true)));
 console.log('run2',await p.evaluate(()=>runAutoBk(true)));
 console.log('run3',await p.evaluate(()=>runAutoBk(true)));
 console.log(await p.evaluate(async()=>{const m=await S.DB.doc('backups/auto-meta').get();const s=await S.DB.collection('backups').get();return [JSON.stringify(m.data()),s.docs.length,$('autoBkInfo').textContent]}));
 await p.evaluate(()=>openTab('settings'));await p.waitForTimeout(300);
 await p.click('#autoBkRestore');await p.waitForTimeout(600);
 console.log('btns',await p.evaluate(()=>document.querySelectorAll('button[data-k]').length));
 await p.screenshot({path:'ab1.png'});
 await p.click('button[data-k="0"]');await p.waitForTimeout(500);
 await p.screenshot({path:'ab2.png'});
 console.log(errs);process.exit();
})();
