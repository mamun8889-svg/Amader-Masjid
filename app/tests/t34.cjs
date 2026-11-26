const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index31.html');p.setDefaultTimeout(8000);
 await p.evaluate(()=>{S.super=false;renderAll();});await p.waitForTimeout(800);
 const r=await p.evaluate(()=>({vis:!document.getElementById('adminHome').hidden,txt:document.getElementById('adminHome').innerText.slice(0,900)}));
 console.log(JSON.stringify(r));
 await p.screenshot({path:'h1.png',fullPage:false});
 await p.evaluate(()=>{document.querySelector('#adminHome [data-act=unpaid]').click()});await p.waitForTimeout(400);
 await p.screenshot({path:'h2.png'});
 await p.evaluate(()=>{closeModal();document.querySelector('#adminHome .ahx[data-act=arr]').click()});await p.waitForTimeout(400);
 await p.screenshot({path:'h3.png'});
 await p.evaluate(()=>{closeModal();openTab('payentry');});await p.waitForTimeout(300);
 const o=await p.evaluate(()=>{const s=document.getElementById('pPayer');s.value=s.options[3].value;s.dispatchEvent(new Event('change'));return document.getElementById('pDue').innerText});
 console.log(o);await p.screenshot({path:'h4.png'});
 console.log(p.errs);
 await p.evaluate(()=>{S.super=true;renderAll();openTab('salary')});await p.waitForTimeout(500);await p.screenshot({path:'h5.png'});
 process.exit();
})();
