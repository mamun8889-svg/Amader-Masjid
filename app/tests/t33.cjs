const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index30.html');p.setDefaultTimeout(8000);
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.waitForTimeout(1500);
 const r=await p.evaluate(()=>{const out={};out.nav=[...document.querySelectorAll('#nav button')].map(b=>b.textContent.trim()).join('|');out.ver=!document.getElementById('verBanner');out.remIn=document.getElementById('remBanner').closest('#salary')?1:0;
 openTab('salary');H.stack=['dashboard','salary'];window.__bt=0;openTab('summary');H.stack.push('salary');window.__back();const a=curTab;window.__back();out.after2=curTab;out.a=a;return out});
 console.log(JSON.stringify(r),errs);
 process.exit();
})();
