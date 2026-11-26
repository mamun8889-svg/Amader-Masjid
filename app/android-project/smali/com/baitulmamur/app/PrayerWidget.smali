.class public Lcom/baitulmamur/app/PrayerWidget;
.super Landroid/appwidget/AppWidgetProvider;

.field static cv:Landroid/graphics/Canvas;
.field static pt:Landroid/graphics/Paint;
.field static k:F
.field static ox:F
.field static oy:F
.field static km:Lorg/json/JSONObject;
.field static tk:[Ljava/lang/String;
.field static nx:I
.field static ram:I

.method public constructor <init>()V
    .locals 0
    invoke-direct {p0}, Landroid/appwidget/AppWidgetProvider;-><init>()V
    return-void
.end method

.method static pad2(I)Ljava/lang/String;
    .locals 3
    const/16 v0, 0xa
    if-ge p0, v0, :big
    new-instance v1, Ljava/lang/StringBuilder;
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V
    const-string v2, "0"
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v1
    return-object v1
    :big
    invoke-static {p0}, Ljava/lang/Integer;->toString(I)Ljava/lang/String;
    move-result-object v1
    return-object v1
.end method

.method static bn(Ljava/lang/String;)Ljava/lang/String;
    .locals 6
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V
    invoke-virtual {p0}, Ljava/lang/String;->length()I
    move-result v1
    const/4 v2, 0x0
    :lp
    if-ge v2, v1, :done
    invoke-virtual {p0, v2}, Ljava/lang/String;->charAt(I)C
    move-result v3
    const/16 v4, 0x30
    if-lt v3, v4, :oth
    const/16 v4, 0x39
    if-gt v3, v4, :oth
    add-int/lit16 v3, v3, 0x9b6
    :oth
    int-to-char v3, v3
    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;
    add-int/lit8 v2, v2, 0x1
    goto :lp
    :done
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    return-object v0
.end method

.method static bi(I)Ljava/lang/String;
    .locals 2
    invoke-static {p0}, Ljava/lang/Integer;->toString(I)Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, Lcom/baitulmamur/app/PrayerWidget;->bn(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v0
    return-object v0
.end method

.method static cdf(I)Ljava/lang/String;
    .locals 5
    div-int/lit8 v0, p0, 0x3c
    rem-int/lit8 v1, p0, 0x3c
    invoke-static {v1}, Lcom/baitulmamur/app/PrayerWidget;->bi(I)Ljava/lang/String;
    move-result-object v2
    new-instance v3, Ljava/lang/StringBuilder;
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V
    if-lez v0, :nh
    invoke-static {v0}, Lcom/baitulmamur/app/PrayerWidget;->bi(I)Ljava/lang/String;
    move-result-object v4
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const-string v4, " ঘণ্টা "
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    :nh
    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const-string v4, " মিনিট"
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v3
    return-object v3
.end method

.method static ymd(Ljava/util/Calendar;I)Ljava/lang/String;
    .locals 6
    invoke-virtual {p0}, Ljava/util/Calendar;->clone()Ljava/lang/Object;
    move-result-object v0
    check-cast v0, Ljava/util/Calendar;
    const/4 v1, 0x5
    invoke-virtual {v0, v1, p1}, Ljava/util/Calendar;->add(II)V
    new-instance v2, Ljava/lang/StringBuilder;
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V
    const/4 v1, 0x1
    invoke-virtual {v0, v1}, Ljava/util/Calendar;->get(I)I
    move-result v3
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    const-string v4, "-"
    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const/4 v1, 0x2
    invoke-virtual {v0, v1}, Ljava/util/Calendar;->get(I)I
    move-result v3
    add-int/lit8 v3, v3, 0x1
    invoke-static {v3}, Lcom/baitulmamur/app/PrayerWidget;->pad2(I)Ljava/lang/String;
    move-result-object v5
    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const/4 v1, 0x5
    invoke-virtual {v0, v1}, Ljava/util/Calendar;->get(I)I
    move-result v3
    invoke-static {v3}, Lcom/baitulmamur/app/PrayerWidget;->pad2(I)Ljava/lang/String;
    move-result-object v5
    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v2
    return-object v2
.end method

.method static cnd(Ljava/lang/String;)Z
    .locals 5
    invoke-virtual {p0}, Ljava/lang/String;->length()I
    move-result v0
    if-nez v0, :has
    const/4 v0, 0x1
    return v0
    :has
    const/4 v0, 0x0
    invoke-virtual {p0, v0}, Ljava/lang/String;->charAt(I)C
    move-result v1
    sget v2, Lcom/baitulmamur/app/PrayerWidget;->nx:I
    sget v3, Lcom/baitulmamur/app/PrayerWidget;->ram:I
    const/16 v4, 0x52
    if-ne v1, v4, :a
    const/4 v4, 0x1
    if-ne v3, v4, :no
    goto :yes
    :a
    const/16 v4, 0x72
    if-ne v1, v4, :b
    if-nez v3, :no
    goto :yes
    :b
    const/4 v0, 0x1
    invoke-virtual {p0, v0}, Ljava/lang/String;->charAt(I)C
    move-result v0
    add-int/lit8 v0, v0, -0x30
    const/16 v4, 0x6e
    if-ne v1, v4, :c
    if-ne v0, v2, :no
    goto :yes
    :c
    const/16 v4, 0x4e
    if-ne v1, v4, :yes
    if-eq v0, v2, :no
    :yes
    const/4 v0, 0x1
    return v0
    :no
    const/4 v0, 0x0
    return v0
.end method

.method static sub(Ljava/lang/String;)Ljava/lang/String;
    .locals 9
    sget-object v0, Lcom/baitulmamur/app/PrayerWidget;->tk:[Ljava/lang/String;
    const-string v1, "{nx}"
    const/4 v2, 0x0
    aget-object v3, v0, v2
    invoke-virtual {p0, v1, v3}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object p0
    const-string v1, "{nt}"
    const/4 v2, 0x1
    aget-object v3, v0, v2
    invoke-virtual {p0, v1, v3}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object p0
    const-string v1, "{cd}"
    const/4 v2, 0x2
    aget-object v3, v0, v2
    invoke-virtual {p0, v1, v3}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object p0
    const-string v1, "{ic}"
    const/4 v2, 0x3
    aget-object v3, v0, v2
    invoke-virtual {p0, v1, v3}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object p0
    sget-object v0, Lcom/baitulmamur/app/PrayerWidget;->km:Lorg/json/JSONObject;
    if-eqz v0, :ret
    invoke-virtual {v0}, Lorg/json/JSONObject;->keys()Ljava/util/Iterator;
    move-result-object v4
    :lp
    invoke-interface {v4}, Ljava/util/Iterator;->hasNext()Z
    move-result v5
    if-eqz v5, :ret
    invoke-interface {v4}, Ljava/util/Iterator;->next()Ljava/lang/Object;
    move-result-object v5
    check-cast v5, Ljava/lang/String;
    new-instance v6, Ljava/lang/StringBuilder;
    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V
    const-string v7, "{"
    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v6, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const-string v7, "}"
    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v6
    invoke-virtual {v0, v5}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v7
    invoke-virtual {p0, v6, v7}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object p0
    goto :lp
    :ret
    return-object p0
.end method

.method static fa(Lorg/json/JSONArray;I)F
    .locals 2
    invoke-virtual {p0, p1}, Lorg/json/JSONArray;->optDouble(I)D
    move-result-wide v0
    double-to-float v0, v0
    return v0
.end method

.method static px(Lorg/json/JSONArray;I)F
    .locals 3
    invoke-static {p0, p1}, Lcom/baitulmamur/app/PrayerWidget;->fa(Lorg/json/JSONArray;I)F
    move-result v0
    sget v1, Lcom/baitulmamur/app/PrayerWidget;->k:F
    mul-float/2addr v0, v1
    sget v1, Lcom/baitulmamur/app/PrayerWidget;->ox:F
    add-float/2addr v0, v1
    return v0
.end method

.method static py(Lorg/json/JSONArray;I)F
    .locals 3
    invoke-static {p0, p1}, Lcom/baitulmamur/app/PrayerWidget;->fa(Lorg/json/JSONArray;I)F
    move-result v0
    sget v1, Lcom/baitulmamur/app/PrayerWidget;->k:F
    mul-float/2addr v0, v1
    sget v1, Lcom/baitulmamur/app/PrayerWidget;->oy:F
    add-float/2addr v0, v1
    return v0
.end method

.method static sz(Lorg/json/JSONArray;I)F
    .locals 3
    invoke-static {p0, p1}, Lcom/baitulmamur/app/PrayerWidget;->fa(Lorg/json/JSONArray;I)F
    move-result v0
    sget v1, Lcom/baitulmamur/app/PrayerWidget;->k:F
    mul-float/2addr v0, v1
    return v0
.end method

.method static ci(Lorg/json/JSONArray;I)I
    .locals 3
    invoke-virtual {p0, p1}, Lorg/json/JSONArray;->optLong(I)J
    move-result-wide v0
    long-to-int v0, v0
    return v0
.end method

.method static cond(Lorg/json/JSONArray;I)Z
    .locals 2
    invoke-virtual {p0, p1}, Lorg/json/JSONArray;->optString(I)Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, Lcom/baitulmamur/app/PrayerWidget;->cnd(Ljava/lang/String;)Z
    move-result v0
    return v0
.end method

.method static drawR(Lorg/json/JSONArray;)V
    .locals 12
    const/4 v0, 0x7
    invoke-static {p0, v0}, Lcom/baitulmamur/app/PrayerWidget;->cond(Lorg/json/JSONArray;I)Z
    move-result v0
    if-eqz v0, :end
    new-instance v0, Landroid/graphics/RectF;
    const/4 v1, 0x1
    invoke-static {p0, v1}, Lcom/baitulmamur/app/PrayerWidget;->px(Lorg/json/JSONArray;I)F
    move-result v1
    const/4 v2, 0x2
    invoke-static {p0, v2}, Lcom/baitulmamur/app/PrayerWidget;->py(Lorg/json/JSONArray;I)F
    move-result v2
    const/4 v3, 0x3
    invoke-static {p0, v3}, Lcom/baitulmamur/app/PrayerWidget;->sz(Lorg/json/JSONArray;I)F
    move-result v3
    const/4 v4, 0x4
    invoke-static {p0, v4}, Lcom/baitulmamur/app/PrayerWidget;->sz(Lorg/json/JSONArray;I)F
    move-result v4
    add-float/2addr v3, v1
    add-float/2addr v4, v2
    invoke-direct {v0, v1, v2, v3, v4}, Landroid/graphics/RectF;-><init>(FFFF)V
    const/4 v1, 0x5
    invoke-static {p0, v1}, Lcom/baitulmamur/app/PrayerWidget;->sz(Lorg/json/JSONArray;I)F
    move-result v5
    const/4 v1, 0x6
    invoke-static {p0, v1}, Lcom/baitulmamur/app/PrayerWidget;->ci(Lorg/json/JSONArray;I)I
    move-result v6
    sget-object v7, Lcom/baitulmamur/app/PrayerWidget;->pt:Landroid/graphics/Paint;
    sget-object v8, Lcom/baitulmamur/app/PrayerWidget;->cv:Landroid/graphics/Canvas;
    const/4 v9, 0x0
    invoke-virtual {v7, v9}, Landroid/graphics/Paint;->setShader(Landroid/graphics/Shader;)Landroid/graphics/Shader;
    invoke-virtual {v7, v6}, Landroid/graphics/Paint;->setColor(I)V
    const/16 v1, 0x8
    invoke-static {p0, v1}, Lcom/baitulmamur/app/PrayerWidget;->fa(Lorg/json/JSONArray;I)F
    move-result v10
    const/4 v11, 0x0
    cmpl-float v11, v10, v11
    if-lez v11, :fill
    sget-object v9, Landroid/graphics/Paint$Style;->STROKE:Landroid/graphics/Paint$Style;
    invoke-virtual {v7, v9}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    sget v11, Lcom/baitulmamur/app/PrayerWidget;->k:F
    mul-float/2addr v10, v11
    invoke-virtual {v7, v10}, Landroid/graphics/Paint;->setStrokeWidth(F)V
    goto :go
    :fill
    sget-object v9, Landroid/graphics/Paint$Style;->FILL:Landroid/graphics/Paint$Style;
    invoke-virtual {v7, v9}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    :go
    invoke-virtual {v8, v0, v5, v5, v7}, Landroid/graphics/Canvas;->drawRoundRect(Landroid/graphics/RectF;FFLandroid/graphics/Paint;)V
    :end
    return-void
.end method


.method static drawG(Lorg/json/JSONArray;)V
    .locals 20
    move-object/from16 v9, p0
    const/16 v0, 0x8
    invoke-static {v9, v0}, Lcom/baitulmamur/app/PrayerWidget;->cond(Lorg/json/JSONArray;I)Z
    move-result v0
    if-eqz v0, :end
    new-instance v0, Landroid/graphics/RectF;
    const/4 v1, 0x1
    invoke-static {v9, v1}, Lcom/baitulmamur/app/PrayerWidget;->px(Lorg/json/JSONArray;I)F
    move-result v1
    const/4 v2, 0x2
    invoke-static {v9, v2}, Lcom/baitulmamur/app/PrayerWidget;->py(Lorg/json/JSONArray;I)F
    move-result v2
    const/4 v3, 0x3
    invoke-static {v9, v3}, Lcom/baitulmamur/app/PrayerWidget;->sz(Lorg/json/JSONArray;I)F
    move-result v3
    const/4 v4, 0x4
    invoke-static {v9, v4}, Lcom/baitulmamur/app/PrayerWidget;->sz(Lorg/json/JSONArray;I)F
    move-result v4
    add-float/2addr v3, v1
    add-float/2addr v4, v2
    invoke-direct {v0, v1, v2, v3, v4}, Landroid/graphics/RectF;-><init>(FFFF)V
    const/4 v5, 0x5
    invoke-static {v9, v5}, Lcom/baitulmamur/app/PrayerWidget;->sz(Lorg/json/JSONArray;I)F
    move-result v5
    const/4 v6, 0x6
    invoke-static {v9, v6}, Lcom/baitulmamur/app/PrayerWidget;->ci(Lorg/json/JSONArray;I)I
    move-result v6
    const/4 v7, 0x7
    invoke-static {v9, v7}, Lcom/baitulmamur/app/PrayerWidget;->ci(Lorg/json/JSONArray;I)I
    move-result v7
    new-instance v10, Landroid/graphics/LinearGradient;
    move/from16 v11, v1
    move/from16 v12, v2
    move/from16 v13, v1
    move/from16 v14, v4
    move/from16 v15, v6
    move/from16 v16, v7
    sget-object v17, Landroid/graphics/Shader$TileMode;->CLAMP:Landroid/graphics/Shader$TileMode;
    invoke-direct/range {v10 .. v17}, Landroid/graphics/LinearGradient;-><init>(FFFFIILandroid/graphics/Shader$TileMode;)V
    sget-object v8, Lcom/baitulmamur/app/PrayerWidget;->pt:Landroid/graphics/Paint;
    sget-object v9, Lcom/baitulmamur/app/PrayerWidget;->cv:Landroid/graphics/Canvas;
    invoke-virtual {v8, v10}, Landroid/graphics/Paint;->setShader(Landroid/graphics/Shader;)Landroid/graphics/Shader;
    sget-object v11, Landroid/graphics/Paint$Style;->FILL:Landroid/graphics/Paint$Style;
    invoke-virtual {v8, v11}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    invoke-virtual {v9, v0, v5, v5, v8}, Landroid/graphics/Canvas;->drawRoundRect(Landroid/graphics/RectF;FFLandroid/graphics/Paint;)V
    const/4 v11, 0x0
    invoke-virtual {v8, v11}, Landroid/graphics/Paint;->setShader(Landroid/graphics/Shader;)Landroid/graphics/Shader;
    :end
    return-void
.end method

.method static drawT(Lorg/json/JSONArray;)V
    .locals 14
    const/16 v0, 0x9
    invoke-static {p0, v0}, Lcom/baitulmamur/app/PrayerWidget;->cond(Lorg/json/JSONArray;I)Z
    move-result v0
    if-eqz v0, :end
    sget-object v7, Lcom/baitulmamur/app/PrayerWidget;->pt:Landroid/graphics/Paint;
    sget-object v8, Lcom/baitulmamur/app/PrayerWidget;->cv:Landroid/graphics/Canvas;
    const/16 v0, 0x8
    invoke-virtual {p0, v0}, Lorg/json/JSONArray;->optString(I)Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, Lcom/baitulmamur/app/PrayerWidget;->sub(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v0
    const/4 v1, 0x1
    invoke-static {p0, v1}, Lcom/baitulmamur/app/PrayerWidget;->px(Lorg/json/JSONArray;I)F
    move-result v1
    const/4 v2, 0x2
    invoke-static {p0, v2}, Lcom/baitulmamur/app/PrayerWidget;->py(Lorg/json/JSONArray;I)F
    move-result v2
    const/4 v3, 0x3
    invoke-static {p0, v3}, Lcom/baitulmamur/app/PrayerWidget;->sz(Lorg/json/JSONArray;I)F
    move-result v3
    const/4 v4, 0x4
    invoke-static {p0, v4}, Lcom/baitulmamur/app/PrayerWidget;->ci(Lorg/json/JSONArray;I)I
    move-result v4
    const/4 v9, 0x0
    invoke-virtual {v7, v9}, Landroid/graphics/Paint;->setShader(Landroid/graphics/Shader;)Landroid/graphics/Shader;
    sget-object v9, Landroid/graphics/Paint$Style;->FILL:Landroid/graphics/Paint$Style;
    invoke-virtual {v7, v9}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    invoke-virtual {v7, v4}, Landroid/graphics/Paint;->setColor(I)V
    const/4 v5, 0x5
    invoke-virtual {p0, v5}, Lorg/json/JSONArray;->optInt(I)I
    move-result v5
    if-nez v5, :c1
    sget-object v9, Landroid/graphics/Paint$Align;->LEFT:Landroid/graphics/Paint$Align;
    goto :al
    :c1
    const/4 v6, 0x1
    if-ne v5, v6, :c2
    sget-object v9, Landroid/graphics/Paint$Align;->CENTER:Landroid/graphics/Paint$Align;
    goto :al
    :c2
    sget-object v9, Landroid/graphics/Paint$Align;->RIGHT:Landroid/graphics/Paint$Align;
    :al
    invoke-virtual {v7, v9}, Landroid/graphics/Paint;->setTextAlign(Landroid/graphics/Paint$Align;)V
    const/4 v5, 0x6
    invoke-virtual {p0, v5}, Lorg/json/JSONArray;->optInt(I)I
    move-result v5
    if-nez v5, :bd
    sget-object v9, Landroid/graphics/Typeface;->DEFAULT:Landroid/graphics/Typeface;
    goto :tf
    :bd
    sget-object v9, Landroid/graphics/Typeface;->DEFAULT_BOLD:Landroid/graphics/Typeface;
    :tf
    invoke-virtual {v7, v9}, Landroid/graphics/Paint;->setTypeface(Landroid/graphics/Typeface;)Landroid/graphics/Typeface;
    invoke-virtual {v7, v3}, Landroid/graphics/Paint;->setTextSize(F)V
    const/4 v5, 0x7
    invoke-static {p0, v5}, Lcom/baitulmamur/app/PrayerWidget;->sz(Lorg/json/JSONArray;I)F
    move-result v5
    const/4 v6, 0x0
    cmpl-float v6, v5, v6
    if-lez v6, :draw
    invoke-virtual {v7, v0}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F
    move-result v6
    cmpl-float v9, v6, v5
    if-lez v9, :draw
    mul-float/2addr v3, v5
    div-float/2addr v3, v6
    invoke-virtual {v7, v3}, Landroid/graphics/Paint;->setTextSize(F)V
    :draw
    invoke-virtual {v8, v0, v1, v2, v7}, Landroid/graphics/Canvas;->drawText(Ljava/lang/String;FFLandroid/graphics/Paint;)V
    :end
    return-void
.end method

.method static drawL(Lorg/json/JSONArray;)V
    .locals 10
    const/4 v0, 0x7
    invoke-static {p0, v0}, Lcom/baitulmamur/app/PrayerWidget;->cond(Lorg/json/JSONArray;I)Z
    move-result v0
    if-eqz v0, :end
    sget-object v0, Lcom/baitulmamur/app/PrayerWidget;->cv:Landroid/graphics/Canvas;
    const/4 v6, 0x1
    invoke-static {p0, v6}, Lcom/baitulmamur/app/PrayerWidget;->px(Lorg/json/JSONArray;I)F
    move-result v1
    const/4 v6, 0x2
    invoke-static {p0, v6}, Lcom/baitulmamur/app/PrayerWidget;->py(Lorg/json/JSONArray;I)F
    move-result v2
    const/4 v6, 0x3
    invoke-static {p0, v6}, Lcom/baitulmamur/app/PrayerWidget;->px(Lorg/json/JSONArray;I)F
    move-result v3
    const/4 v6, 0x4
    invoke-static {p0, v6}, Lcom/baitulmamur/app/PrayerWidget;->py(Lorg/json/JSONArray;I)F
    move-result v4
    sget-object v5, Lcom/baitulmamur/app/PrayerWidget;->pt:Landroid/graphics/Paint;
    const/4 v6, 0x0
    invoke-virtual {v5, v6}, Landroid/graphics/Paint;->setShader(Landroid/graphics/Shader;)Landroid/graphics/Shader;
    sget-object v6, Landroid/graphics/Paint$Style;->STROKE:Landroid/graphics/Paint$Style;
    invoke-virtual {v5, v6}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    const/4 v6, 0x5
    invoke-static {p0, v6}, Lcom/baitulmamur/app/PrayerWidget;->sz(Lorg/json/JSONArray;I)F
    move-result v7
    invoke-virtual {v5, v7}, Landroid/graphics/Paint;->setStrokeWidth(F)V
    const/4 v6, 0x6
    invoke-static {p0, v6}, Lcom/baitulmamur/app/PrayerWidget;->ci(Lorg/json/JSONArray;I)I
    move-result v7
    invoke-virtual {v5, v7}, Landroid/graphics/Paint;->setColor(I)V
    invoke-virtual/range {v0 .. v5}, Landroid/graphics/Canvas;->drawLine(FFFFLandroid/graphics/Paint;)V
    :end
    return-void
.end method

.method static drawEl(Lorg/json/JSONArray;)V
    .locals 3
    const/4 v0, 0x0
    invoke-virtual {p0, v0}, Lorg/json/JSONArray;->optString(I)Ljava/lang/String;
    move-result-object v0
    const-string v1, "r"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v2
    if-eqz v2, :n1
    invoke-static {p0}, Lcom/baitulmamur/app/PrayerWidget;->drawR(Lorg/json/JSONArray;)V
    return-void
    :n1
    const-string v1, "g"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v2
    if-eqz v2, :n2
    invoke-static {p0}, Lcom/baitulmamur/app/PrayerWidget;->drawG(Lorg/json/JSONArray;)V
    return-void
    :n2
    const-string v1, "t"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v2
    if-eqz v2, :n3
    invoke-static {p0}, Lcom/baitulmamur/app/PrayerWidget;->drawT(Lorg/json/JSONArray;)V
    return-void
    :n3
    const-string v1, "l"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v2
    if-eqz v2, :n4
    invoke-static {p0}, Lcom/baitulmamur/app/PrayerWidget;->drawL(Lorg/json/JSONArray;)V
    :n4
    return-void
.end method

.method static asp(Lorg/json/JSONObject;)F
    .locals 6
    const-string v0, "w"
    invoke-virtual {p0, v0}, Lorg/json/JSONObject;->optDouble(Ljava/lang/String;)D
    move-result-wide v0
    const-string v2, "h"
    invoke-virtual {p0, v2}, Lorg/json/JSONObject;->optDouble(Ljava/lang/String;)D
    move-result-wide v2
    div-double/2addr v0, v2
    double-to-float v0, v0
    return v0
.end method

.method static pick(Lorg/json/JSONObject;FI)Lorg/json/JSONObject;
    .locals 12
    const-string v0, "lays"
    invoke-virtual {p0, v0}, Lorg/json/JSONObject;->optJSONArray(Ljava/lang/String;)Lorg/json/JSONArray;
    move-result-object v0
    if-nez v0, :ok
    const/4 v0, 0x0
    return-object v0
    :ok
    const-string v1, "mode"
    const-string v2, "a"
    invoke-virtual {p0, v1, v2}, Lorg/json/JSONObject;->optString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v1
    const/4 v3, 0x1
    const/4 v4, 0x0
    const/4 v5, 0x0
    const v6, 0x7f7fffff
    invoke-virtual {v0}, Lorg/json/JSONArray;->length()I
    move-result v7
    :lp
    if-ge v4, v7, :done
    invoke-virtual {v0, v4}, Lorg/json/JSONArray;->optJSONObject(I)Lorg/json/JSONObject;
    move-result-object v8
    const-string v9, "id"
    const-string v10, ""
    invoke-virtual {v8, v9, v10}, Lorg/json/JSONObject;->optString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v9
    const-string v10, "m"
    invoke-virtual {v10, v9}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v10
    if-eqz v10, :notm
    if-ne p2, v3, :next
    return-object v8
    :notm
    invoke-virtual {v1, v9}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v10
    if-eqz v10, :auto
    return-object v8
    :auto
    invoke-static {v8}, Lcom/baitulmamur/app/PrayerWidget;->asp(Lorg/json/JSONObject;)F
    move-result v10
    sub-float/2addr v10, p1
    invoke-static {v10}, Ljava/lang/Math;->abs(F)F
    move-result v10
    cmpg-float v11, v10, v6
    if-gez v11, :next
    move v6, v10
    move-object v5, v8
    :next
    add-int/lit8 v4, v4, 0x1
    goto :lp
    :done
    return-object v5
.end method

.method static msg(Ljava/lang/String;Ljava/lang/String;II)V
    .locals 12
    sget-object v0, Lcom/baitulmamur/app/PrayerWidget;->pt:Landroid/graphics/Paint;
    sget-object v1, Lcom/baitulmamur/app/PrayerWidget;->cv:Landroid/graphics/Canvas;
    const/4 v2, 0x0
    invoke-virtual {v0, v2}, Landroid/graphics/Paint;->setShader(Landroid/graphics/Shader;)Landroid/graphics/Shader;
    sget-object v2, Landroid/graphics/Paint$Style;->FILL:Landroid/graphics/Paint$Style;
    invoke-virtual {v0, v2}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    const v3, 0xcc0b1d3a
    invoke-virtual {v0, v3}, Landroid/graphics/Paint;->setColor(I)V
    int-to-float v4, p2
    int-to-float v5, p3
    const/4 v6, 0x0
    new-instance v7, Landroid/graphics/RectF;
    invoke-direct {v7, v6, v6, v4, v5}, Landroid/graphics/RectF;-><init>(FFFF)V
    const v8, 0x3dcccccd
    mul-float/2addr v8, v5
    invoke-virtual {v1, v7, v8, v8, v0}, Landroid/graphics/Canvas;->drawRoundRect(Landroid/graphics/RectF;FFLandroid/graphics/Paint;)V
    const v3, 0xffffffff
    invoke-virtual {v0, v3}, Landroid/graphics/Paint;->setColor(I)V
    sget-object v2, Landroid/graphics/Paint$Align;->CENTER:Landroid/graphics/Paint$Align;
    invoke-virtual {v0, v2}, Landroid/graphics/Paint;->setTextAlign(Landroid/graphics/Paint$Align;)V
    sget-object v2, Landroid/graphics/Typeface;->DEFAULT_BOLD:Landroid/graphics/Typeface;
    invoke-virtual {v0, v2}, Landroid/graphics/Paint;->setTypeface(Landroid/graphics/Typeface;)Landroid/graphics/Typeface;
    const v8, 0x3e23d70a
    mul-float/2addr v8, v5
    invoke-virtual {v0, v8}, Landroid/graphics/Paint;->setTextSize(F)V
    const v9, 0x3f000000
    mul-float/2addr v9, v4
    const v10, 0x3ee66666
    mul-float/2addr v10, v5
    invoke-virtual {v1, p0, v9, v10, v0}, Landroid/graphics/Canvas;->drawText(Ljava/lang/String;FFLandroid/graphics/Paint;)V
    const v3, 0xfff6c453
    invoke-virtual {v0, v3}, Landroid/graphics/Paint;->setColor(I)V
    const v8, 0x3de147ae
    mul-float/2addr v8, v5
    invoke-virtual {v0, v8}, Landroid/graphics/Paint;->setTextSize(F)V
    const v10, 0x3f400000
    mul-float/2addr v10, v5
    invoke-virtual {v1, p1, v9, v10, v0}, Landroid/graphics/Canvas;->drawText(Ljava/lang/String;FFLandroid/graphics/Paint;)V
    return-void
.end method


.method static paintAll(Landroid/content/Context;II)V
    .locals 16
    move-object/from16 v3, p0
    move/from16 v4, p1
    move/from16 v5, p2
    const-string v0, "bm_prayer"
    const/4 v1, 0x0
    invoke-virtual {v3, v0, v1}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;
    move-result-object v0
    const-string v1, "d"
    const/4 v2, 0x0
    invoke-interface {v0, v1, v2}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v9
    const-string v1, "l"
    invoke-interface {v0, v1, v2}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v10
    if-nez v9, :hd
    const-string v0, "উইজেট প্রস্তুত নয়"
    const-string v1, "অ্যাপ একবার খুলুন"
    invoke-static {v0, v1, v4, v5}, Lcom/baitulmamur/app/PrayerWidget;->msg(Ljava/lang/String;Ljava/lang/String;II)V
    return-void
    :hd
    if-nez v10, :hl
    const-string v0, "উইজেট প্রস্তুত নয়"
    const-string v1, "অ্যাপের উইজেট সেটিংস খুলুন"
    invoke-static {v0, v1, v4, v5}, Lcom/baitulmamur/app/PrayerWidget;->msg(Ljava/lang/String;Ljava/lang/String;II)V
    return-void
    :hl
    new-instance v6, Lorg/json/JSONObject;
    invoke-direct {v6, v10}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V
    new-instance v7, Lorg/json/JSONObject;
    invoke-direct {v7, v9}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V
    invoke-static {}, Ljava/util/Calendar;->getInstance()Ljava/util/Calendar;
    move-result-object v8
    const/4 v9, 0x0
    invoke-static {v8, v9}, Lcom/baitulmamur/app/PrayerWidget;->ymd(Ljava/util/Calendar;I)Ljava/lang/String;
    move-result-object v9
    const-string v10, "days"
    invoke-virtual {v7, v10}, Lorg/json/JSONObject;->optJSONObject(Ljava/lang/String;)Lorg/json/JSONObject;
    move-result-object v10
    if-eqz v10, :nosched
    invoke-virtual {v10, v9}, Lorg/json/JSONObject;->optJSONObject(Ljava/lang/String;)Lorg/json/JSONObject;
    move-result-object v9
    if-eqz v9, :nosched
    const-string v11, "k"
    invoke-virtual {v9, v11}, Lorg/json/JSONObject;->optJSONObject(Ljava/lang/String;)Lorg/json/JSONObject;
    move-result-object v11
    if-eqz v11, :nosched
    sput-object v11, Lcom/baitulmamur/app/PrayerWidget;->km:Lorg/json/JSONObject;
    const-string v12, "ram"
    invoke-virtual {v11, v12}, Lorg/json/JSONObject;->optInt(Ljava/lang/String;)I
    move-result v12
    sput v12, Lcom/baitulmamur/app/PrayerWidget;->ram:I
    const-string v13, "m"
    invoke-virtual {v9, v13}, Lorg/json/JSONObject;->optJSONArray(Ljava/lang/String;)Lorg/json/JSONArray;
    move-result-object v13
    if-eqz v13, :nosched
    const/16 v14, 0xb
    invoke-virtual {v8, v14}, Ljava/util/Calendar;->get(I)I
    move-result v14
    mul-int/lit8 v14, v14, 0x3c
    const/16 v15, 0xc
    invoke-virtual {v8, v15}, Ljava/util/Calendar;->get(I)I
    move-result v15
    add-int/2addr v14, v15
    const/4 v15, 0x0
    :kl
    const/4 v0, 0x5
    if-ge v15, v0, :tom
    const/4 v0, 0x2
    if-ge v15, v0, :hi
    mul-int/lit8 v0, v15, 0x2
    add-int/lit8 v0, v0, 0x1
    goto :got
    :hi
    add-int/lit8 v0, v15, 0x2
    :got
    invoke-virtual {v13, v0}, Lorg/json/JSONArray;->optInt(I)I
    move-result v1
    if-gt v1, v14, :found
    add-int/lit8 v15, v15, 0x1
    goto :kl
    :found
    sub-int/2addr v1, v14
    invoke-static {v0}, Ljava/lang/Integer;->toString(I)Ljava/lang/String;
    move-result-object v2
    const-string v0, "s"
    invoke-virtual {v0, v2}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v2
    invoke-virtual {v11, v2}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v2
    goto :tok
    :tom
    const/4 v0, 0x1
    invoke-static {v8, v0}, Lcom/baitulmamur/app/PrayerWidget;->ymd(Ljava/util/Calendar;I)Ljava/lang/String;
    move-result-object v0
    invoke-virtual {v10, v0}, Lorg/json/JSONObject;->optJSONObject(Ljava/lang/String;)Lorg/json/JSONObject;
    move-result-object v0
    if-eqz v0, :nosched
    const-string v1, "m"
    invoke-virtual {v0, v1}, Lorg/json/JSONObject;->optJSONArray(Ljava/lang/String;)Lorg/json/JSONArray;
    move-result-object v1
    if-eqz v1, :nosched
    const/4 v2, 0x1
    invoke-virtual {v1, v2}, Lorg/json/JSONArray;->optInt(I)I
    move-result v1
    add-int/lit16 v1, v1, 0x5a0
    sub-int/2addr v1, v14
    const-string v2, "k"
    invoke-virtual {v0, v2}, Lorg/json/JSONObject;->optJSONObject(Ljava/lang/String;)Lorg/json/JSONObject;
    move-result-object v0
    if-eqz v0, :nosched
    const-string v2, "s1"
    invoke-virtual {v0, v2}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v2
    const/4 v15, 0x0
    :tok
    sput v15, Lcom/baitulmamur/app/PrayerWidget;->nx:I
    const/4 v7, 0x4
    new-array v0, v7, [Ljava/lang/String;
    const-string v7, "ফজর,যোহর,আসর,মাগরিব,এশা"
    const-string v8, ","
    invoke-virtual {v7, v8}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;
    move-result-object v7
    aget-object v7, v7, v15
    const/4 v8, 0x0
    aput-object v7, v0, v8
    const/4 v8, 0x1
    aput-object v2, v0, v8
    invoke-static {v1}, Lcom/baitulmamur/app/PrayerWidget;->cdf(I)Ljava/lang/String;
    move-result-object v7
    const/4 v8, 0x2
    aput-object v7, v0, v8
    const-string v7, ""
    const/4 v8, 0x1
    if-ne v12, v8, :noic
    const/4 v8, 0x5
    invoke-virtual {v13, v8}, Lorg/json/JSONArray;->optInt(I)I
    move-result v8
    sub-int/2addr v8, v14
    if-lez v8, :noic
    invoke-static {v8}, Lcom/baitulmamur/app/PrayerWidget;->cdf(I)Ljava/lang/String;
    move-result-object v7
    :noic
    const/4 v8, 0x3
    aput-object v7, v0, v8
    sput-object v0, Lcom/baitulmamur/app/PrayerWidget;->tk:[Ljava/lang/String;
    int-to-float v7, v4
    int-to-float v8, v5
    div-float v0, v7, v8
    invoke-static {v6, v0, v12}, Lcom/baitulmamur/app/PrayerWidget;->pick(Lorg/json/JSONObject;FI)Lorg/json/JSONObject;
    move-result-object v9
    if-eqz v9, :nosched
    const-string v10, "w"
    invoke-virtual {v9, v10}, Lorg/json/JSONObject;->optDouble(Ljava/lang/String;)D
    move-result-wide v10
    double-to-float v10, v10
    const-string v0, "h"
    invoke-virtual {v9, v0}, Lorg/json/JSONObject;->optDouble(Ljava/lang/String;)D
    move-result-wide v0
    double-to-float v0, v0
    div-float v2, v7, v10
    div-float v1, v8, v0
    invoke-static {v2, v1}, Ljava/lang/Math;->min(FF)F
    move-result v2
    sput v2, Lcom/baitulmamur/app/PrayerWidget;->k:F
    const/high16 v12, 0x3f000000
    mul-float v1, v10, v2
    sub-float v1, v7, v1
    mul-float/2addr v1, v12
    sput v1, Lcom/baitulmamur/app/PrayerWidget;->ox:F
    mul-float v1, v0, v2
    sub-float v1, v8, v1
    mul-float/2addr v1, v12
    sput v1, Lcom/baitulmamur/app/PrayerWidget;->oy:F
    const-string v0, "e"
    invoke-virtual {v9, v0}, Lorg/json/JSONObject;->optJSONArray(Ljava/lang/String;)Lorg/json/JSONArray;
    move-result-object v7
    if-eqz v7, :end
    invoke-virtual {v7}, Lorg/json/JSONArray;->length()I
    move-result v8
    const/4 v10, 0x0
    :el
    if-ge v10, v8, :end
    invoke-virtual {v7, v10}, Lorg/json/JSONArray;->optJSONArray(I)Lorg/json/JSONArray;
    move-result-object v0
    if-eqz v0, :nx2
    invoke-static {v0}, Lcom/baitulmamur/app/PrayerWidget;->drawEl(Lorg/json/JSONArray;)V
    :nx2
    add-int/lit8 v10, v10, 0x1
    goto :el
    :end
    return-void
    :nosched
    const-string v0, "আজকের সময়সূচি পাওয়া যায়নি"
    const-string v1, "অ্যাপ খুলে সময়সূচি হালনাগাদ করুন"
    invoke-static {v0, v1, v4, v5}, Lcom/baitulmamur/app/PrayerWidget;->msg(Ljava/lang/String;Ljava/lang/String;II)V
    return-void
.end method

.method static render(Landroid/content/Context;II)Landroid/graphics/Bitmap;
    .locals 8
    sget-object v0, Landroid/graphics/Bitmap$Config;->ARGB_8888:Landroid/graphics/Bitmap$Config;
    invoke-static {p1, p2, v0}, Landroid/graphics/Bitmap;->createBitmap(IILandroid/graphics/Bitmap$Config;)Landroid/graphics/Bitmap;
    move-result-object v1
    new-instance v2, Landroid/graphics/Canvas;
    invoke-direct {v2, v1}, Landroid/graphics/Canvas;-><init>(Landroid/graphics/Bitmap;)V
    new-instance v3, Landroid/graphics/Paint;
    const/4 v4, 0x1
    invoke-direct {v3, v4}, Landroid/graphics/Paint;-><init>(I)V
    sput-object v2, Lcom/baitulmamur/app/PrayerWidget;->cv:Landroid/graphics/Canvas;
    sput-object v3, Lcom/baitulmamur/app/PrayerWidget;->pt:Landroid/graphics/Paint;
    :ts
    invoke-static {p0, p1, p2}, Lcom/baitulmamur/app/PrayerWidget;->paintAll(Landroid/content/Context;II)V
    :te
    .catch Ljava/lang/Throwable; {:ts .. :te} :err
    return-object v1
    :err
    const-string v4, "উইজেট আঁকা যায়নি"
    const-string v5, "অ্যাপ আপডেট করে দেখুন"
    invoke-static {v4, v5, p1, p2}, Lcom/baitulmamur/app/PrayerWidget;->msg(Ljava/lang/String;Ljava/lang/String;II)V
    return-object v1
.end method

.method static draw(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;I)V
    .locals 12
    :ts
    invoke-virtual {p1, p2}, Landroid/appwidget/AppWidgetManager;->getAppWidgetOptions(I)Landroid/os/Bundle;
    move-result-object v0
    const-string v1, "appWidgetMinWidth"
    const/16 v2, 0xfa
    invoke-virtual {v0, v1, v2}, Landroid/os/Bundle;->getInt(Ljava/lang/String;I)I
    move-result v3
    const-string v1, "appWidgetMaxHeight"
    const/16 v2, 0x6e
    invoke-virtual {v0, v1, v2}, Landroid/os/Bundle;->getInt(Ljava/lang/String;I)I
    move-result v4
    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;
    move-result-object v5
    invoke-virtual {v5}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;
    move-result-object v6
    iget v6, v6, Landroid/util/DisplayMetrics;->density:F
    const/high16 v7, 0x40400000
    invoke-static {v6, v7}, Ljava/lang/Math;->min(FF)F
    move-result v6
    int-to-float v3, v3
    mul-float/2addr v3, v6
    float-to-int v3, v3
    int-to-float v4, v4
    mul-float/2addr v4, v6
    float-to-int v4, v4
    invoke-static {p0, v3, v4}, Lcom/baitulmamur/app/PrayerWidget;->render(Landroid/content/Context;II)Landroid/graphics/Bitmap;
    move-result-object v8
    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    move-result-object v9
    const-string v1, "date_widget"
    const-string v2, "layout"
    invoke-virtual {v5, v1, v2, v9}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I
    move-result v10
    new-instance v11, Landroid/widget/RemoteViews;
    invoke-direct {v11, v9, v10}, Landroid/widget/RemoteViews;-><init>(Ljava/lang/String;I)V
    const-string v1, "w_img"
    const-string v2, "id"
    invoke-virtual {v5, v1, v2, v9}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I
    move-result v10
    invoke-virtual {v11, v10, v8}, Landroid/widget/RemoteViews;->setImageViewBitmap(ILandroid/graphics/Bitmap;)V
    invoke-virtual {p1, p2, v11}, Landroid/appwidget/AppWidgetManager;->updateAppWidget(ILandroid/widget/RemoteViews;)V
    :te
    .catch Ljava/lang/Throwable; {:ts .. :te} :err
    :err
    return-void
.end method

.method static schedule(Landroid/content/Context;)V
    .locals 10
    :ts
    const-string v0, "alarm"
    invoke-virtual {p0, v0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;
    move-result-object v0
    check-cast v0, Landroid/app/AlarmManager;
    new-instance v7, Landroid/content/Intent;
    const-class v8, Lcom/baitulmamur/app/PrayerWidget;
    invoke-direct {v7, p0, v8}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    const-string v8, "com.baitulmamur.app.TICK"
    invoke-virtual {v7, v8}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;
    const/4 v8, 0x0
    const v9, 0xc000000
    invoke-static {p0, v8, v7, v9}, Landroid/app/PendingIntent;->getBroadcast(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;
    move-result-object v6
    const/4 v1, 0x1
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v2
    const-wide/32 v4, 0xea60
    add-long/2addr v2, v4
    invoke-virtual/range {v0 .. v6}, Landroid/app/AlarmManager;->setRepeating(IJJLandroid/app/PendingIntent;)V
    :te
    .catch Ljava/lang/Throwable; {:ts .. :te} :err
    :err
    return-void
.end method

.method static redraw(Landroid/content/Context;)V
    .locals 8
    :ts
    invoke-static {p0}, Landroid/appwidget/AppWidgetManager;->getInstance(Landroid/content/Context;)Landroid/appwidget/AppWidgetManager;
    move-result-object v0
    new-instance v1, Landroid/content/ComponentName;
    const-class v2, Lcom/baitulmamur/app/PrayerWidget;
    invoke-direct {v1, p0, v2}, Landroid/content/ComponentName;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    invoke-virtual {v0, v1}, Landroid/appwidget/AppWidgetManager;->getAppWidgetIds(Landroid/content/ComponentName;)[I
    move-result-object v2
    array-length v3, v2
    const/4 v4, 0x0
    :lp
    if-ge v4, v3, :dn
    aget v5, v2, v4
    invoke-static {p0, v0, v5}, Lcom/baitulmamur/app/PrayerWidget;->draw(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;I)V
    add-int/lit8 v4, v4, 0x1
    goto :lp
    :dn
    if-lez v3, :te
    invoke-static {p0}, Lcom/baitulmamur/app/PrayerWidget;->schedule(Landroid/content/Context;)V
    :te
    .catch Ljava/lang/Throwable; {:ts .. :te} :err
    :err
    return-void
.end method

.method public onUpdate(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;[I)V
    .locals 6
    :ts
    array-length v0, p3
    const/4 v1, 0x0
    :lp
    if-ge v1, v0, :dn
    aget v2, p3, v1
    invoke-static {p1, p2, v2}, Lcom/baitulmamur/app/PrayerWidget;->draw(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;I)V
    add-int/lit8 v1, v1, 0x1
    goto :lp
    :dn
    invoke-static {p1}, Lcom/baitulmamur/app/PrayerWidget;->schedule(Landroid/content/Context;)V
    :te
    .catch Ljava/lang/Throwable; {:ts .. :te} :err
    :err
    return-void
.end method

.method public onAppWidgetOptionsChanged(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;ILandroid/os/Bundle;)V
    .locals 1
    invoke-static {p1, p2, p3}, Lcom/baitulmamur/app/PrayerWidget;->draw(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;I)V
    return-void
.end method

.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    .locals 4
    :ts
    invoke-super {p0, p1, p2}, Landroid/appwidget/AppWidgetProvider;->onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;
    move-result-object v0
    if-eqz v0, :te
    const-string v1, "android.appwidget.action.APPWIDGET_UPDATE"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v2
    if-nez v2, :te
    invoke-static {p1}, Lcom/baitulmamur/app/PrayerWidget;->redraw(Landroid/content/Context;)V
    :te
    .catch Ljava/lang/Throwable; {:ts .. :te} :err
    :err
    return-void
.end method
