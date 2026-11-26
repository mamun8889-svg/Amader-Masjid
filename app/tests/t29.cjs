const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index27.html');p.setDefaultTimeout(8000);
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.waitForTimeout(1500);
 await p.evaluate(()=>{openTab('transactions')});await p.waitForTimeout(300);
 console.log(await p.evaluate(()=>[document.querySelectorAll('#transactions input[type=search]').length]));
 await p.evaluate(()=>{S.super=false;S.admin=false;S.acct={name:rowsOf(2026)[0].name,role:'viewer'};renderAll()});await p.waitForTimeout(300);
 console.log(await p.evaluate(()=>[$('myDues').hidden,$('myDues').innerText]));
 await p.evaluate(()=>{S.pset=Object.assign({},S.pset,{appVer:30});renderAll()});await p.waitForTimeout(300);
 console.log(await p.evaluate(()=>[$('verBanner').hidden]));
 console.log(errs);process.exit();
})();
