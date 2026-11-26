const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index22.html');p.setDefaultTimeout(8000);
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.waitForTimeout(1200);
 console.log(await p.evaluate(()=>{const n=new Date();return [n.toISOString(),dueUp(2026),dueUp(2025)]}));
 await p.evaluate(()=>openTab('salary'));await p.waitForTimeout(500);
 await p.evaluate(()=>{$('salMonth').value='0';renderSalary()});
 console.log(await p.evaluate(()=>[...document.querySelectorAll('#salStats .kpi')].map(k=>k.innerText.replace(/\n/g,' | '))));
 console.log(await p.evaluate(()=>{const o=[];for(let m=7;m<=10;m++)o.push(m+':'+paidUnpaid(2026,m).unpaid.length);return o.join(' ')}));
 console.log(errs);process.exit();
})();
