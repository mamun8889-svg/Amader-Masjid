const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index25.html');p.setDefaultTimeout(8000);
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.waitForTimeout(1500);
 console.log(await p.evaluate(()=>[[...$('kpis').children].map(c=>(c.querySelector('.lb')||c).textContent.slice(0,22)+(c.classList.contains('kmore')?'(hid)':'')),$('duesTitle').textContent]));
 await p.screenshot({path:'d1.png'});
 await p.click('#dashMore');await p.waitForTimeout(300);await p.screenshot({path:'d2.png'});
 console.log(await p.evaluate(()=>[...document.querySelectorAll('#kpis > .kmore')].map(c=>getComputedStyle(c).display)));
 await p.click('.slogo');await p.waitForTimeout(400);
 console.log(await p.evaluate(()=>[document.querySelectorAll('#nav button').length,!!document.querySelector('#nav .grp'),getComputedStyle(document.querySelector('.grpbox')).display]));
 await p.click('.grp');await p.waitForTimeout(200);await p.screenshot({path:'d3.png'});
 await p.click('#nav button[data-tab=settings]');await p.waitForTimeout(500);
 console.log(await p.evaluate(()=>[curTab,document.querySelector('#settings').classList.contains('active')]));
 console.log(errs);process.exit();
})();
