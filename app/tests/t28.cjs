const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index26.html');p.setDefaultTimeout(8000);
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.waitForTimeout(1500);
 console.log('banner',await p.evaluate(()=>$('remBanner').hidden));
 await p.evaluate(()=>openRemind());await p.waitForTimeout(300);
 console.log(await p.evaluate(()=>[document.querySelectorAll('#mBody button[data-i]').length,$('mTitle').textContent]));
 await p.evaluate(()=>{S.contacts=S.contacts||{};S.contacts.payers=[{name:document.querySelector('#mBody .ml span').innerText.split(' ')[0],phone:'01712345678'}]});
 await p.evaluate(()=>smsDialog({name:'ক',phone:'01712345678',text:'হ্যালো',key:'k',kind:'t'}));await p.waitForTimeout(200);
 console.log(await p.evaluate(()=>[...document.querySelectorAll('#mAct button')].map(b=>b.textContent)));
 await p.evaluate(()=>{window.__u=null;window.Android={wa:u=>{window.__u=u;return true}}});
 await p.click('.waBtn');console.log(await p.evaluate(()=>window.__u));
 console.log(errs);process.exit();
})();
