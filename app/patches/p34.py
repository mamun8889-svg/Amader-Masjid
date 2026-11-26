import subprocess,re
subprocess.run(['python3','p33.py'],check=True)
s=open('index33.html',encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s,a[:70]
    s=s.replace(a,b,1)
# members see everything (signed-in viewers)
rep("const pubSet=()=>Object.assign({},PUB_DEF,S.pset||{});","const pubSet=()=>(S.acct&&!S.admin)?Object.assign({},S.pset||{},PUB_DEF):Object.assign({},PUB_DEF,S.pset||{});")
# ramadan card in 'আরও দেখুন'
rep("const KEYS=['মাসিক বেতন সংগ্রহ','সক্রিয় সদস্য','উন্নয়ন তহবিল','অনুমোদনের'];","const KEYS=['মাসিক বেতন সংগ্রহ','সক্রিয় সদস্য','উন্নয়ন তহবিল','অনুমোদনের','রমজান ফান্ড'];")
# committee tab
rep("{id:'notices',t:'নোটিশ',i:'bell'},","{id:'notices',t:'নোটিশ',i:'bell'},{id:'committee',t:'মসজিদ কমিটি',i:'people'},")
rep("function tabOk(t){\n  const adm=isAdminView();","function tabOk(t){\n  const adm=isAdminView();\n  if(t.id==='committee')return !!S.acct;")
rep('<section id="summary" class="section">','''<section id="committee" class="section">
 <div class="sec-head"><div><h3>মসজিদ কমিটি</h3><div class="sub">কমিটির সদস্যদের যোগাযোগের তথ্য — প্রত্যেকে নিজের তথ্য বদলাতে পারেন</div></div></div>
 <div class="row-actions" id="cmTop" style="margin-bottom:12px"></div>
 <div class="grid two" id="cmList"></div>
</section>

<section id="summary" class="section">''')
rep('</style>','''.fx3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:8px}.fx3 span{display:block;font-size:12px;color:var(--muted)}.fx3 b{font-size:clamp(15px,4.4vw,20px)}.fx3 .g{color:var(--emerald-d)}.fx3 .r{color:var(--rose)}
.cmc .cmn{font-family:var(--serif);font-weight:700;font-size:18px}.cmc .cmr{color:var(--amber);font-weight:600;margin-bottom:8px}.cml{color:var(--indigo);font-weight:600}
.bmr{display:flex;gap:8px;align-items:center;justify-content:space-between;padding:8px 0;border-bottom:1px dashed var(--line)}.bmlist{max-height:46vh;overflow:auto;margin-top:6px}
</style>''')
js=open('p34.js',encoding='utf-8').read()
i=s.rindex('</script>');s=s[:i]+js+s[i:]
# expose ah helpers
rep("  window.__arr=arrears;","  window.__arr=arrears;window.__ah={locate,rep,arrears,mLab:(y,m)=>monthsOf(y)[m]+' '+bn(y),absOf};")
open('index34.html','w',encoding='utf-8').write(s)
# native
a=open('proj/smali/com/baitulmamur/app/Wv.smali').read()
a=a.replace('''    const-string v0, "http"
    invoke-virtual {p2, v0}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z
    move-result v1
    if-nez v1, :pass
''','')
open('proj/smali/com/baitulmamur/app/Wv.smali','w').write(a)
m=open('proj/smali/com/baitulmamur/app/MainActivity.smali').read()
if 'public share(' not in m:
    m+='''
.method public share(Ljava/lang/String;Ljava/lang/String;)Z
    .locals 4
    .annotation runtime Landroid/webkit/JavascriptInterface;
    .end annotation

    :try_start_0
    new-instance v0, Landroid/content/Intent;

    const-string v1, "android.intent.action.SEND"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v1, "text/plain"

    invoke-virtual {v0, v1}, Landroid/content/Intent;->setType(Ljava/lang/String;)Landroid/content/Intent;

    const-string v1, "android.intent.extra.TEXT"

    invoke-virtual {v0, v1, p2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {v0, p1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {p0, v0}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V

    const/4 v0, 0x1

    return v0
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0

    :catch_0
    const/4 v0, 0x0

    return v0
.end method
'''
    open('proj/smali/com/baitulmamur/app/MainActivity.smali','w').write(m)
