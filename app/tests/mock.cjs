const D=require('fs').readFileSync(__dirname+'/data.json','utf8');
const J1=o=>({fields:{j:{stringValue:JSON.stringify(o)}}});
const DB={'roles/u1':{role:'super'},'pub/settings':{},'appdata/main':J1(JSON.parse(D)),'adminData/dev':J1({}),'adminData/ips':J1({}),'adminData/contacts':J1({payers:[]})};
const ts=()=>new Date().toISOString();
function encf(v){const f={};for(const k in v){const x=v[k];f[k]=typeof x==='string'?{stringValue:x}:{integerValue:String(x)}}return f}
module.exports=async function(p){
 await p.route(/identitytoolkit|securetoken/,r=>{const u=r.request().url();
  const b=JSON.stringify({localId:'u1',email:'hmabdullah8889@gmail.com',idToken:'t',refreshToken:'r',expiresIn:'3600'});r.fulfill({status:200,contentType:'application/json',body:b})});
 await p.route(/firestore\.googleapis/,async r=>{
  const req=r.request(),m=req.method(),u=new URL(req.url());
  const path=decodeURIComponent(u.pathname.split('/documents/')[1]||'');
  const J=(o,s=200)=>r.fulfill({status:s,contentType:'application/json',body:JSON.stringify(o)});
  if(m==='GET'){
   if(path.split('/').length===2&&DB[path])return J({name:'x/'+path,fields:DB[path].fields||encf(DB[path]),updateTime:ts()});
   if(path.split('/').length===2)return J({},404);
   const docs=Object.keys(DB).filter(k=>k.startsWith(path+'/')).map(k=>({name:'x/'+k,fields:DB[k].fields||encf(DB[k]),updateTime:ts()}));
   return J({documents:docs});
  }
  if(m==='PATCH'){const b=JSON.parse(req.postData()||'{}');DB[path]={fields:b.fields};return J({name:'x/'+path,fields:b.fields,updateTime:ts()})}
  if(m==='DELETE'){delete DB[path];return J({})}
  return J({});
 });
};
