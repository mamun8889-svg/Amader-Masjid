const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index21.html');p.setDefaultTimeout(8000);
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.waitForTimeout(1200);
 console.log('fab on',await p.evaluate(()=>document.getElementById('fab').classList.contains('on')));
 await p.click('#fabBtn');await p.waitForTimeout(300);
 console.log('menu',await p.evaluate(()=>document.getElementById('fabMenu').textContent));
 await p.click('#fabMenu [data-k=pay]');await p.waitForTimeout(800);
 console.log('pay open',await p.evaluate(()=>[!document.getElementById('payWrap').hidden,curTab]));
 await p.screenshot({path:'fab1.png'});
 await p.evaluate(()=>showPay(false));await p.evaluate(()=>openTab('dashboard'));await p.waitForTimeout(300);
 await p.click('#fabBtn');await p.click('#fabMenu [data-k=tx]');await p.waitForTimeout(800);
 console.log('tx dlg',await p.evaluate(()=>!!document.querySelector('.fdlg.open')));
 await p.screenshot({path:'fab2.png'});
 await p.evaluate(()=>{window.__closeDlg&&window.__closeDlg()});await p.waitForTimeout(300);
 // light theme
 await p.evaluate(()=>{document.documentElement.dataset.theme='light'});await p.waitForTimeout(300);
 await p.screenshot({path:'light.png'});
 console.log('side bg',await p.evaluate(()=>getComputedStyle(document.querySelector('.side')).backgroundImage.slice(0,70)));
 // admin role: fake
 await p.evaluate(()=>{S.super=false;renderAll()});await p.waitForTimeout(300);
 console.log('admin menu single -> pay',await p.evaluate(()=>{document.getElementById('fabBtn').click();return [!document.getElementById('payWrap').hidden]}));
 await p.evaluate(()=>{S.super=false;S.admin=false;renderAll()});
 console.log('member fab',await p.evaluate(()=>document.getElementById('fab').classList.contains('on')));
 console.log(errs);process.exit();
})();
