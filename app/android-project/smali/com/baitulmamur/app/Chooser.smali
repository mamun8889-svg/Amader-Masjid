.class public Lcom/baitulmamur/app/Chooser;
.super Landroid/webkit/WebChromeClient;


# instance fields
.field private act:Lcom/baitulmamur/app/MainActivity;


# direct methods
.method public constructor <init>(Lcom/baitulmamur/app/MainActivity;)V
    .locals 0

    invoke-direct {p0}, Landroid/webkit/WebChromeClient;-><init>()V

    iput-object p1, p0, Lcom/baitulmamur/app/Chooser;->act:Lcom/baitulmamur/app/MainActivity;

    return-void
.end method


# virtual methods
.method public onShowFileChooser(Landroid/webkit/WebView;Landroid/webkit/ValueCallback;Landroid/webkit/WebChromeClient$FileChooserParams;)Z
    .locals 3

    iget-object v0, p0, Lcom/baitulmamur/app/Chooser;->act:Lcom/baitulmamur/app/MainActivity;

    invoke-virtual {v0, p2}, Lcom/baitulmamur/app/MainActivity;->setCb(Landroid/webkit/ValueCallback;)V

    :try_start_0
    invoke-virtual {p3}, Landroid/webkit/WebChromeClient$FileChooserParams;->createIntent()Landroid/content/Intent;

    move-result-object v1

    const/16 v2, 0x4d2

    invoke-virtual {v0, v1, v2}, Landroid/app/Activity;->startActivityForResult(Landroid/content/Intent;I)V

    const/4 v2, 0x1

    return v2
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0

    :catch_0
    invoke-virtual {v0}, Lcom/baitulmamur/app/MainActivity;->abortCb()V

    const/4 v2, 0x1

    return v2
.end method
