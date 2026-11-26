const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index33.html');
 await p.waitForTimeout(1500);
 console.log(await p.evaluate(()=>[...document.querySelectorAll('#kpis .vl')].map(e=>e.textContent).join('|')));
 await p.evaluate(()=>{S.super=false;renderAll()});await p.waitForTimeout(1800);
 console.log(await p.evaluate(()=>[...document.querySelectorAll('#adminHome .ahb .n,#adminHome .pbar i')].map(e=>e.textContent||e.style.width).join('|')));
 await p.screenshot({path:'a1.png'});
 await p.evaluate(()=>{S.super=true;renderAll();openTab('salary')});await p.waitForTimeout(1500);
 console.log(await p.evaluate(()=>document.querySelector('#salStats').innerText.replace(/\n/g,' ')));
 console.log(p.errs);process.exit()})();
