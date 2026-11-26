const {chromium}=require('playwright');const mock=require('./mock.cjs');
(async()=>{
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:412,height:880},hasTouch:true,isMobile:true});
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await mock(p);
 await p.goto('file://'+process.cwd()+'/'+(process.argv[2]||'index13.html'));await p.waitForTimeout(800);
 await p.fill('#lId','hmabdullah8889@gmail.com');await p.fill('#lPw','12345678');await p.waitForTimeout(500);
 await p.evaluate(()=>{document.getElementById('gEnter').disabled=false});await p.click('#gEnter');await p.waitForTimeout(2500);
 await p.screenshot({path:'s1.png'});
 console.log(await p.evaluate(()=>document.body.className+' | '+document.body.innerText.slice(0,200)));
 console.log(errs.slice(0,8));await b.close()})()
