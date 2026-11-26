.class public Lcom/baitulmamur/app/Wv;
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
