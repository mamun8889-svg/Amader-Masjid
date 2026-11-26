const L=require('./lib.cjs');
(async()=>{
 const {p}=await L.start('index31.html');
 await p.evaluate(()=>{S.super=false;renderAll()});
 const r=await p.evaluate(()=>{try{return JSON.stringify([__arr(9999).map(o=>o.name+':'+o.amt),__arr(9999).length,nameKey('Kashem Miya')])}catch(e){return 'ERR '+e.message+e.stack}});
 console.log(r);process.exit()})();
