const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index28.html');p.setDefaultTimeout(8000);
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.waitForTimeout(1500);
 await p.evaluate(()=>openTab('prayer'));await p.waitForTimeout(800);
 console.log(await p.evaluate(()=>document.getElementById('pzToday').innerText.slice(0,400)));
 await p.evaluate(()=>{document.getElementById('pzOT').value='05:40';document.getElementById('pzOW').value='1';document.getElementById('pzOR').value='পরীক্ষা'});
 await p.click('#pzOSave');await p.waitForTimeout(600);
 console.log(await p.evaluate(()=>[JSON.stringify(PZ.ov.hist.map(h=>[h.o,h.n])),document.getElementById('pzToday').innerText.includes('✎')]));
 await p.click('#pzJamSave');await p.waitForTimeout(300);
 await p.evaluate(()=>{window.__pz=null;window.Android={setPrayer:j=>{window.__pz=j}};pzPush()});
 console.log(await p.evaluate(()=>[window.__pz&&window.__pz.length,window.__pz&&Object.keys(JSON.parse(window.__pz).days).length]));
 await p.screenshot({path:'pz1.png',fullPage:false});
 console.log(errs);process.exit();
})();
