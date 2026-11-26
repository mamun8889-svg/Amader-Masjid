import re
s=open('index29.html',encoding='utf-8').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)>=1,a[:60]
    s=s.replace(a,b,cnt)
# 1 banners
rep('<div id="verBanner" class="panel" hidden style="margin-bottom:14px;border-left:4px solid #8b5cf6"></div>\n','')
rep(' <div id="remBanner" class="panel" hidden style="margin-bottom:14px;border-left:4px solid #0ea5e9"></div>','')
rep('<section id="salary" class="section">','<section id="salary" class="section">\n <div id="remBanner" class="panel" hidden style="margin-bottom:14px;border-left:4px solid #0ea5e9"></div>')
rep("function ver(){const el=$('verBanner');if(!el)return;","function ver(){return;const el=$('verBanner');if(!el)return;")
rep("await S.DB.doc('pub/settings').update({appVer:n});toast('জানানো হয়েছে')","await S.DB.doc('pub/settings').update({appVer:n});try{S.DB.collection('notifs').doc(newId()).set({t:Date.now(),uid:(window.BMAUTH&&BMAUTH.uid())||'',by:(S.acct&&S.acct.name)||'সুপার অ্যাডমিন',ti:'নতুন সংস্করণ এসেছে',bo:'অ্যাপের নতুন সংস্করণ ('+n+') নিন।',ty:'notice'}).catch(()=>{})}catch(_){}toast('জানানো হয়েছে')")
# renderDashboard wrapper for banner already calls banner(); ensure also on tab open
rep("{const _d=renderDashboard;renderDashboard=function(){_d();try{banner()}catch(e){}}}","{const _d=renderDashboard;renderDashboard=function(){_d();try{banner()}catch(e){}}}\n  {const _o=openTab;openTab=function(a,b){_o(a,b);if(a==='salary'||a==='dashboard')try{banner()}catch(e){}}}")
# 2 prayer removal
rep("{id:'prayer',t:'নামাজের সময়',i:'cal'},","")
rep("function start(){if(sub||","function start(){return;if(sub||")
rep("setTimeout(()=>{try{pzPush()}catch(e){}},3000);","")
rep("function push(){const c=cfg();try{","function push(){return;const c=cfg();try{")
# 3 whatsapp
old=s[s.index("const u='https://wa.me/88'+ph"):s.index("if(ok){closeModal();try{logSms")]
new="""const q=encodeURIComponent(t);let ok=false;const A=window.Android;try{if(A&&A.wa)ok=A.wa('whatsapp://send?phone=88'+ph+'&text='+q)||A.wa('https://wa.me/88'+ph+'?text='+q)}catch(e){}if(!ok){try{navigator.clipboard.writeText(t)}catch(e){}toast('WhatsApp খোলা যায়নি — বার্তা কপি হয়েছে');return}
      """
s=s.replace(old,new)
# 4 back
rep("document.addEventListener('keydown',e=>{if(e.key==='Escape')window.__closeDlg()});","document.addEventListener('keydown',e=>{if(e.key==='Escape')window.__closeDlg()});\n  {const o2=window.__back;window.__back=function(){const n=Date.now(),q=n-(window.__bt||0);window.__bt=n;if(q<700&&curTab!=='dashboard'&&$('modal').hidden){H.stack.length=0;openTab('dashboard',true);return}return o2.apply(this,arguments)}}")
# 5 speed
s=re.sub(r'<link rel="stylesheet" href="(https://fonts.googleapis.com/css2[^"]*)">',lambda m:'<link rel="stylesheet" href="'+m.group(1)+('' if 'display=swap' in m.group(1) else '&display=swap')+'" media="print" onload="this.media=\'all\'">',s,1)
open('index30.html','w',encoding='utf-8').write(s)
# native
m=open('proj/AndroidManifest.xml').read()
m=re.sub(r'\s*<receiver android:exported="true" android:label="@string/w_name2".*?</receiver>','',m,flags=re.S)
open('proj/AndroidManifest.xml','w').write(m)
a=open('proj/smali/com/baitulmamur/app/MainActivity.smali').read()
a=a.replace("""    new-instance v3, Landroid/webkit/WebViewClient;

    invoke-direct {v3}, Landroid/webkit/WebViewClient;-><init>()V""","""    new-instance v3, Lcom/baitulmamur/app/Wv;

    invoke-direct {v3, p0}, Lcom/baitulmamur/app/Wv;-><init>(Landroid/app/Activity;)V""")
open('proj/smali/com/baitulmamur/app/MainActivity.smali','w').write(a)
open('proj/smali/com/baitulmamur/app/Wv.smali','w').write(""".class public Lcom/baitulmamur/app/Wv;
.super Landroid/webkit/WebViewClient;

.field private a:Landroid/app/Activity;

.method public constructor <init>(Landroid/app/Activity;)V
    .locals 0
    invoke-direct {p0}, Landroid/webkit/WebViewClient;-><init>()V
    iput-object p1, p0, Lcom/baitulmamur/app/Wv;->a:Landroid/app/Activity;
    return-void
.end method

.method public shouldOverrideUrlLoading(Landroid/webkit/WebView;Ljava/lang/String;)Z
    .locals 4
    const-string v0, "http"
    invoke-virtual {p2, v0}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z
    move-result v1
    if-nez v1, :pass
    const-string v0, "file:"
    invoke-virtual {p2, v0}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z
    move-result v1
    if-nez v1, :pass
    const-string v0, "javascript:"
    invoke-virtual {p2, v0}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z
    move-result v1
    if-nez v1, :pass
    const-string v0, "about:"
    invoke-virtual {p2, v0}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z
    move-result v1
    if-nez v1, :pass
    const-string v0, "data:"
    invoke-virtual {p2, v0}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z
    move-result v1
    if-nez v1, :pass
    :try_start_0
    new-instance v0, Landroid/content/Intent;
    const-string v1, "android.intent.action.VIEW"
    invoke-static {p2}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;
    move-result-object v2
    invoke-direct {v0, v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V
    iget-object v3, p0, Lcom/baitulmamur/app/Wv;->a:Landroid/app/Activity;
    invoke-virtual {v3, v0}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0
    :catch_0
    const/4 v0, 0x1
    return v0
    :pass
    const/4 v0, 0x0
    return v0
.end method
""")
