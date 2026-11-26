const {chromium}=require('playwright');const mock=require('./mock.cjs');
exports.start=async(file,vp)=>{
 const b=await chromium.launch();const ctx=await b.newContext({viewport:vp||{width:412,height:880},hasTouch:true,isMobile:true,deviceScaleFactor:1.5});const p=await ctx.newPage();
 p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));
 await p.route(/fonts\.g/,r=>r.abort());await mock(p);
 await p.goto('file://'+process.cwd()+'/'+file);await p.waitForTimeout(1200);
 await p.evaluate(()=>document.getElementById('loginBtn').click());await p.waitForTimeout(300);
 await p.fill('#lId','hmabdullah8889@gmail.com');await p.fill('#lPw','12345678');
 await p.evaluate(()=>{document.getElementById('gEnter').disabled=false});await p.click('#gEnter');await p.waitForTimeout(2500);
 return {b,p}};
