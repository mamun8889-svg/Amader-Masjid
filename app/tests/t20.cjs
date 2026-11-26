const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start(process.argv[2]||'index18.html');p.setDefaultTimeout(8000);
 await p.evaluate(()=>openTab('contacts'));await p.waitForTimeout(1500);
 console.log(await p.evaluate(()=>{
  const W=document.documentElement.clientWidth;const out=[];
  document.querySelectorAll('#contacts *').forEach(e=>{const r=e.getBoundingClientRect();if(r.right>W+2||r.left<-2)out.push(e.tagName+'.'+e.className+'#'+e.id+' '+Math.round(r.left)+'-'+Math.round(r.right))});
  return [W,document.documentElement.scrollWidth,document.body.scrollWidth,out.slice(0,12)]}));
 await p.screenshot({path:'ct.png'});process.exit();
})();
