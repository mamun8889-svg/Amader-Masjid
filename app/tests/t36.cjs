const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index32.html');
 const r=await p.evaluate(()=>[normId('Karim'),normId('01712345678'),normId('আব্দুল করিম'),dispId(normId('আব্দুল করিম')),normId('a@b.com'),normId('খুব লম্বা একটা নাম যেটা অনেক বড় হয়ে যাচ্ছে'),dispId(normId('খুব লম্বা একটা নাম যেটা অনেক বড় হয়ে যাচ্ছে'))]);
 console.log(JSON.stringify(r));
 await p.evaluate(()=>{S.super=false;renderAll();openTab('payentry')});await p.waitForTimeout(400);
 await p.evaluate(()=>document.querySelector('.saveHi').scrollIntoView());await p.screenshot({path:'s1.png'});
 await p.evaluate(()=>{openTab('dashboard')});await p.waitForTimeout(300);await p.screenshot({path:'s2.png'});
 console.log(p.errs);process.exit()})();
