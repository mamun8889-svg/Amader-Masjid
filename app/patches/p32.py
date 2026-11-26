import subprocess
subprocess.run(['python3','p31.py'],check=True)
s=open('index31.html',encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s,a[:70]
    s=s.replace(a,b,1)
rep("const normId=s=>String(s).trim().toLowerCase();",
"""const normId=s=>{s=String(s).trim().toLowerCase();if(/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(s))return s;
  const b=new TextEncoder().encode(s);let h='';b.forEach(x=>h+=x.toString(16).padStart(2,'0'));
  if(h.length>56){let a=0x811c9dc5,c=0x1b873593;b.forEach(x=>{a=Math.imul(a^x,16777619)>>>0;c=Math.imul(c^x,0x85ebca6b)>>>0});h='h'+a.toString(16)+c.toString(16)+b.length.toString(16)}else h='u'+h;
  return h+'@bm.app'};
const dispId=e=>{e=String(e||'');if(!/@bm\\.app$/.test(e))return e;const l=e.split('@')[0];if(l[0]!=='u')return '';try{const a=l.slice(1).match(/../g)||[];return new TextDecoder().decode(new Uint8Array(a.map(x=>parseInt(x,16))))}catch(_){return ''}};""")
rep('<label for="lId">ইমেইল</label><input id="lId" type="email" inputmode="email"','<label for="lId">ইউজার নেম (ইমেইল / ফোন / নাম)</label><input id="lId" type="text" inputmode="text"')
rep('<label for="aId">ইমেইল</label><input id="aId" type="email" required','<label for="aId">ইউজার নেম (ইমেইল / ফোন / নাম — যা ইচ্ছা)</label><input id="aId" type="text" required')
rep("S.acct={name:r.name||A.email()","S.acct={name:r.name||dispId(A.email())")
rep("(A&&A.email())||'ব্যবহারকারী'","dispId(A&&A.email())||'ব্যবহারকারী'")
rep("$('pfEmail').textContent=(A.email&&A.email())||''","$('pfEmail').textContent=dispId((A.email&&A.email())||'')")
rep("sub:p.email||''","sub:dispId(p.email||'')")
rep("table(['নাম','ইমেইল','ভূমিকা','কাজ']","table(['নাম','ইউজার নেম','ভূমিকা','কাজ']")
rep("<td>${esc(a.email||'')}</td>","<td>${esc(a.uname||dispId(a.email||''))}</td>")
rep("$('aName').value.trim()||id.split('@')[0],email:id,","$('aName').value.trim()||dispId(id)||$('aId').value.trim(),uname:$('aId').value.trim(),email:id,")
rep("'এই ইমেইল আগে থেকেই আছে।","'এই ইউজার নেম আগে থেকেই আছে।")
css='''
@keyframes savePulse{0%,100%{box-shadow:0 0 0 0 rgba(232,146,12,.75);transform:scale(1)}50%{box-shadow:0 0 0 14px rgba(232,146,12,0);transform:scale(1.04)}}
@keyframes saveShine{0%{background-position:0 0}100%{background-position:200% 0}}
#payForm button[type=submit],form#payForm .btn[type=submit]{}
.saveHi{width:100%;font-size:19px!important;font-weight:800;padding:15px 18px!important;color:#2a1a00!important;border:2px solid #fff3!important;background:linear-gradient(110deg,#f6b44a,#ffe08a,#f6b44a,#e8920c)!important;background-size:200% 100%!important;animation:savePulse 1.6s ease-in-out infinite,saveShine 3s linear infinite;justify-content:center}
'''
rep('</style>',css+'</style>')
rep('<button type="submit" class="btn">বেতন সংরক্ষণ</button>','<button type="submit" class="btn saveHi">✔ বেতন সংরক্ষণ করুন</button>')
open('index32.html','w',encoding='utf-8').write(s)
