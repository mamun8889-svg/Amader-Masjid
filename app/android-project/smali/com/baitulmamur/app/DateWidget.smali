.class public Lcom/baitulmamur/app/DateWidget;
.super Landroid/appwidget/AppWidgetProvider;

.method public constructor <init>()V
    .locals 0
    invoke-direct {p0}, Landroid/appwidget/AppWidgetProvider;-><init>()V
    return-void
.end method

.method static ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    .locals 0
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    return-void
.end method

.method static bn(I)Ljava/lang/String;
    .locals 6
    invoke-static {p0}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;
    move-result-object v0
    new-instance v1, Ljava/lang/StringBuilder;
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V
    const/4 v2, 0x0
    invoke-virtual {v0}, Ljava/lang/String;->length()I
    move-result v3
    :loop
    if-ge v2, v3, :done
    invoke-virtual {v0, v2}, Ljava/lang/String;->charAt(I)C
    move-result v4
    add-int/lit16 v4, v4, 0x9b6
    int-to-char v4, v4
    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;
    add-int/lit8 v2, v2, 0x1
    goto :loop
    :done
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    return-object v0
.end method

.method static pick(Ljava/lang/String;I)Ljava/lang/String;
    .locals 2
    const-string v0, ","
    invoke-virtual {p0, v0}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;
    move-result-object v0
    aget-object v0, v0, p1
    return-object v0
.end method

.method static isLeap(I)Z
    .locals 2
    rem-int/lit8 v0, p0, 0x4
    if-nez v0, :no
    rem-int/lit8 v0, p0, 0x64
    if-nez v0, :yes
    rem-int/lit16 v0, p0, 0x190
    if-eqz v0, :yes
    :no
    const/4 v0, 0x0
    return v0
    :yes
    const/4 v0, 0x1
    return v0
.end method

.method static texts()[Ljava/lang/String;
    .locals 16
    invoke-static {}, Ljava/util/Calendar;->getInstance()Ljava/util/Calendar;
    move-result-object v0
    const/4 v7, 0x1
    invoke-virtual {v0, v7}, Ljava/util/Calendar;->get(I)I
    move-result v1
    const/4 v7, 0x2
    invoke-virtual {v0, v7}, Ljava/util/Calendar;->get(I)I
    move-result v2
    const/4 v7, 0x5
    invoke-virtual {v0, v7}, Ljava/util/Calendar;->get(I)I
    move-result v3
    const/4 v7, 0x6
    invoke-virtual {v0, v7}, Ljava/util/Calendar;->get(I)I
    move-result v4
    const/4 v7, 0x7
    invoke-virtual {v0, v7}, Ljava/util/Calendar;->get(I)I
    move-result v5
    const/4 v7, 0x7
    new-array v6, v7, [Ljava/lang/String;

    invoke-static {v3}, Lcom/baitulmamur/app/DateWidget;->bn(I)Ljava/lang/String;
    move-result-object v7
    const/4 v8, 0x0
    aput-object v7, v6, v8

    const-string v7, "রবিবার,সোমবার,মঙ্গলবার,বুধবার,বৃহস্পতিবার,শুক্রবার,শনিবার"
    add-int/lit8 v8, v5, -0x1
    invoke-static {v7, v8}, Lcom/baitulmamur/app/DateWidget;->pick(Ljava/lang/String;I)Ljava/lang/String;
    move-result-object v7
    const/4 v8, 0x1
    aput-object v7, v6, v8

    new-instance v9, Ljava/lang/StringBuilder;
    invoke-direct {v9}, Ljava/lang/StringBuilder;-><init>()V
    invoke-static {v3}, Lcom/baitulmamur/app/DateWidget;->bn(I)Ljava/lang/String;
    move-result-object v7
    invoke-static {v9, v7}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v7, " "
    invoke-static {v9, v7}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v7, "জানুয়ারি,ফেব্রুয়ারি,মার্চ,এপ্রিল,মে,জুন,জুলাই,আগস্ট,সেপ্টেম্বর,অক্টোবর,নভেম্বর,ডিসেম্বর"
    invoke-static {v7, v2}, Lcom/baitulmamur/app/DateWidget;->pick(Ljava/lang/String;I)Ljava/lang/String;
    move-result-object v7
    invoke-static {v9, v7}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v7, ", "
    invoke-static {v9, v7}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    invoke-static {v1}, Lcom/baitulmamur/app/DateWidget;->bn(I)Ljava/lang/String;
    move-result-object v7
    invoke-static {v9, v7}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v7
    const/4 v8, 0x2
    aput-object v7, v6, v8

    invoke-static {v1}, Lcom/baitulmamur/app/DateWidget;->isLeap(I)Z
    move-result v7
    const/16 v8, 0x68
    if-eqz v7, :a
    const/16 v8, 0x69
    :a
    if-lt v4, v8, :before
    sub-int v9, v4, v8
    add-int/lit16 v10, v1, -0x251
    add-int/lit8 v11, v1, 0x1
    invoke-static {v11}, Lcom/baitulmamur/app/DateWidget;->isLeap(I)Z
    move-result v11
    goto :go
    :before
    add-int/lit8 v11, v1, -0x1
    invoke-static {v11}, Lcom/baitulmamur/app/DateWidget;->isLeap(I)Z
    move-result v12
    const/16 v13, 0x16d
    const/16 v14, 0x68
    if-eqz v12, :b
    const/16 v13, 0x16e
    const/16 v14, 0x69
    :b
    sub-int v9, v13, v14
    add-int/2addr v9, v4
    add-int/lit16 v10, v1, -0x252
    move v11, v7
    :go
    const/4 v12, 0x0
    :loop
    const/16 v13, 0x1f
    const/4 v14, 0x5
    if-lt v12, v14, :chk
    const/16 v13, 0x1e
    const/16 v14, 0xa
    if-ne v12, v14, :chk
    if-eqz v11, :chk
    const/16 v13, 0x1f
    :chk
    if-lt v9, v13, :done
    sub-int/2addr v9, v13
    add-int/lit8 v12, v12, 0x1
    goto :loop
    :done
    add-int/lit8 v9, v9, 0x1
    new-instance v7, Ljava/lang/StringBuilder;
    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V
    invoke-static {v9}, Lcom/baitulmamur/app/DateWidget;->bn(I)Ljava/lang/String;
    move-result-object v8
    invoke-static {v7, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v8, " "
    invoke-static {v7, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v8, "বৈশাখ,জ্যৈষ্ঠ,আষাঢ়,শ্রাবণ,ভাদ্র,আশ্বিন,কার্তিক,অগ্রহায়ণ,পৌষ,মাঘ,ফাল্গুন,চৈত্র"
    invoke-static {v8, v12}, Lcom/baitulmamur/app/DateWidget;->pick(Ljava/lang/String;I)Ljava/lang/String;
    move-result-object v8
    invoke-static {v7, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v8, " "
    invoke-static {v7, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    invoke-static {v10}, Lcom/baitulmamur/app/DateWidget;->bn(I)Ljava/lang/String;
    move-result-object v8
    invoke-static {v7, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v8, " বঙ্গাব্দ"
    invoke-static {v7, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v7
    const/4 v8, 0x3
    aput-object v7, v6, v8

    :try_start_0
    new-instance v7, Landroid/icu/util/IslamicCalendar;
    invoke-direct {v7}, Landroid/icu/util/IslamicCalendar;-><init>()V
    sget-object v8, Landroid/icu/util/IslamicCalendar$CalculationType;->ISLAMIC_UMALQURA:Landroid/icu/util/IslamicCalendar$CalculationType;
    invoke-virtual {v7, v8}, Landroid/icu/util/IslamicCalendar;->setCalculationType(Landroid/icu/util/IslamicCalendar$CalculationType;)V
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v8
    const-wide/32 v10, 0x5265c00
    sub-long/2addr v8, v10
    invoke-virtual {v7, v8, v9}, Landroid/icu/util/IslamicCalendar;->setTimeInMillis(J)V
    const/4 v8, 0x5
    invoke-virtual {v7, v8}, Landroid/icu/util/IslamicCalendar;->get(I)I
    move-result v9
    const/4 v8, 0x2
    invoke-virtual {v7, v8}, Landroid/icu/util/IslamicCalendar;->get(I)I
    move-result v10
    const/4 v8, 0x1
    invoke-virtual {v7, v8}, Landroid/icu/util/IslamicCalendar;->get(I)I
    move-result v11
    new-instance v12, Ljava/lang/StringBuilder;
    invoke-direct {v12}, Ljava/lang/StringBuilder;-><init>()V
    invoke-static {v9}, Lcom/baitulmamur/app/DateWidget;->bn(I)Ljava/lang/String;
    move-result-object v8
    invoke-static {v12, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v8, " "
    invoke-static {v12, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v8, "মুহাররম,সফর,রবিউল আউয়াল,রবিউস সানি,জমাদিউল আউয়াল,জমাদিউস সানি,রজব,শাবান,রমজান,শাওয়াল,জিলকদ,জিলহজ"
    invoke-static {v8, v10}, Lcom/baitulmamur/app/DateWidget;->pick(Ljava/lang/String;I)Ljava/lang/String;
    move-result-object v8
    invoke-static {v12, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v8, " "
    invoke-static {v12, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    invoke-static {v11}, Lcom/baitulmamur/app/DateWidget;->bn(I)Ljava/lang/String;
    move-result-object v8
    invoke-static {v12, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v8, " হি."
    invoke-static {v12, v8}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    invoke-virtual {v12}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v8
    const/4 v9, 0x4
    aput-object v8, v6, v9
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0
    goto :ret
    :catch_0
    move-exception v8
    const-string v8, "—"
    const/4 v9, 0x4
    aput-object v8, v6, v9
    :ret
    const-string v7, "352.55714,42.26509,-0.22922,3.87301,9.33261,0.87676,-0.52729"
    invoke-static {v7, v4, v1}, Lcom/baitulmamur/app/DateWidget;->sun(Ljava/lang/String;II)Ljava/lang/String;
    move-result-object v7
    const-string v8, "সূর্যোদয় "
    invoke-virtual {v8, v7}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v7
    const/4 v8, 0x5
    aput-object v7, v6, v8
    const-string v7, "1081.65246,-43.07778,14.94584,2.90891,9.34205,-0.88426,0.48897"
    invoke-static {v7, v4, v1}, Lcom/baitulmamur/app/DateWidget;->sun(Ljava/lang/String;II)Ljava/lang/String;
    move-result-object v7
    const-string v8, "সূর্যাস্ত "
    invoke-virtual {v8, v7}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v7
    const/4 v8, 0x6
    aput-object v7, v6, v8
    return-object v6
.end method

.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    .locals 5
    invoke-super {p0, p1, p2}, Landroid/appwidget/AppWidgetProvider;->onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;
    move-result-object v0
    if-eqz v0, :end
    const-string v1, "android.intent.action.DATE_CHANGED"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v2
    if-nez v2, :upd
    const-string v1, "android.intent.action.TIME_SET"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v2
    if-nez v2, :upd
    const-string v1, "android.intent.action.TIMEZONE_CHANGED"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v2
    if-nez v2, :upd
    goto :end
    :upd
    invoke-static {p1}, Landroid/appwidget/AppWidgetManager;->getInstance(Landroid/content/Context;)Landroid/appwidget/AppWidgetManager;
    move-result-object v1
    new-instance v2, Landroid/content/ComponentName;
    const-class v3, Lcom/baitulmamur/app/DateWidget;
    invoke-direct {v2, p1, v3}, Landroid/content/ComponentName;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    invoke-virtual {v1, v2}, Landroid/appwidget/AppWidgetManager;->getAppWidgetIds(Landroid/content/ComponentName;)[I
    move-result-object v2
    invoke-virtual {p0, p1, v1, v2}, Lcom/baitulmamur/app/DateWidget;->onUpdate(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;[I)V
    :end
    return-void
.end method

.method static sun(Ljava/lang/String;II)Ljava/lang/String;
    .locals 16
    move-object/from16 v15, p0
    const-string v0, ","
    invoke-virtual {v15, v0}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;
    move-result-object v0
    const/4 v1, 0x0
    aget-object v1, v0, v1
    invoke-static {v1}, Ljava/lang/Double;->parseDouble(Ljava/lang/String;)D
    move-result-wide v2
    add-int/lit8 v4, p1, -0x1
    int-to-double v4, v4
    const-wide v6, 0x401921fb54442d18L
    mul-double/2addr v4, v6
    const-wide v6, 0x4076d40000000000L
    div-double/2addr v4, v6
    const/4 v8, 0x1
    :lp
    const/4 v9, 0x3
    if-gt v8, v9, :done
    int-to-double v9, v8
    mul-double/2addr v9, v4
    invoke-static {v9, v10}, Ljava/lang/Math;->cos(D)D
    move-result-wide v11
    invoke-static {v9, v10}, Ljava/lang/Math;->sin(D)D
    move-result-wide v9
    mul-int/lit8 v13, v8, 0x2
    add-int/lit8 v14, v13, -0x1
    aget-object v14, v0, v14
    invoke-static {v14}, Ljava/lang/Double;->parseDouble(Ljava/lang/String;)D
    move-result-wide v14
    mul-double/2addr v11, v14
    add-double/2addr v2, v11
    aget-object v11, v0, v13
    invoke-static {v11}, Ljava/lang/Double;->parseDouble(Ljava/lang/String;)D
    move-result-wide v11
    mul-double/2addr v9, v11
    add-double/2addr v2, v9
    add-int/lit8 v8, v8, 0x1
    goto :lp
    :done
    invoke-static {v2, v3}, Ljava/lang/Math;->round(D)J
    move-result-wide v2
    long-to-int v2, v2
    div-int/lit8 v3, v2, 0x3c
    rem-int/lit8 v4, v2, 0x3c
    const/16 v5, 0xc
    if-le v3, v5, :hok
    sub-int/2addr v3, v5
    :hok
    new-instance v5, Ljava/lang/StringBuilder;
    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V
    invoke-static {v3}, Lcom/baitulmamur/app/DateWidget;->bn(I)Ljava/lang/String;
    move-result-object v6
    invoke-static {v5, v6}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const-string v6, ":"
    invoke-static {v5, v6}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    const/16 v6, 0xa
    if-ge v4, v6, :two
    const-string v6, "\u09e6"
    invoke-static {v5, v6}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    :two
    invoke-static {v4}, Lcom/baitulmamur/app/DateWidget;->bn(I)Ljava/lang/String;
    move-result-object v6
    invoke-static {v5, v6}, Lcom/baitulmamur/app/DateWidget;->ap(Ljava/lang/StringBuilder;Ljava/lang/String;)V
    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v5
    return-object v5
.end method

# fitted text draw: T(Canvas,Paint,Typeface,String,x,y,size,color,align,maxW)
.method static T(Landroid/graphics/Canvas;Landroid/graphics/Paint;Landroid/graphics/Typeface;Ljava/lang/String;FFFIIF)V
    .locals 4
    invoke-virtual {p1, p2}, Landroid/graphics/Paint;->setTypeface(Landroid/graphics/Typeface;)Landroid/graphics/Typeface;
    invoke-virtual {p1, p7}, Landroid/graphics/Paint;->setColor(I)V
    if-eqz p8, :left
    sget-object v0, Landroid/graphics/Paint$Align;->CENTER:Landroid/graphics/Paint$Align;
    goto :setal
    :left
    sget-object v0, Landroid/graphics/Paint$Align;->LEFT:Landroid/graphics/Paint$Align;
    :setal
    invoke-virtual {p1, v0}, Landroid/graphics/Paint;->setTextAlign(Landroid/graphics/Paint$Align;)V
    const/4 v1, 0x0
    cmpl-float v1, p9, v1
    if-lez v1, :draw
    :fit
    invoke-virtual {p1, p6}, Landroid/graphics/Paint;->setTextSize(F)V
    invoke-virtual {p1, p3}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F
    move-result v2
    cmpg-float v1, v2, p9
    if-lez v1, :draw
    const/high16 v3, 0x3f000000
    sub-float/2addr p6, v3
    const/high16 v3, 0x41000000
    cmpl-float v1, p6, v3
    if-gtz v1, :fit
    :draw
    invoke-virtual {p1, p6}, Landroid/graphics/Paint;->setTextSize(F)V
    invoke-virtual {p0, p3, p4, p5, p1}, Landroid/graphics/Canvas;->drawText(Ljava/lang/String;FFLandroid/graphics/Paint;)V
    return-void
.end method

.method static draw(Landroid/content/Context;IIF[Ljava/lang/String;)Landroid/graphics/Bitmap;
    .locals 133
    move/from16 v12, p1
    move/from16 v13, p2
    move/from16 v14, p3
    move-object/from16 v15, p4
    move-object/from16 v16, p0
    move/from16 v0, v12
    int-to-float v0, v0
    move/from16 v17, v0
    move/from16 v0, v13
    int-to-float v0, v0
    move/from16 v18, v0
    sget-object v19, Landroid/graphics/Bitmap$Config;->ARGB_8888:Landroid/graphics/Bitmap$Config;
    move/from16 v0, v12
    move/from16 v1, v13
    move-object/from16 v2, v19
    invoke-static/range {v0 .. v2}, Landroid/graphics/Bitmap;->createBitmap(IILandroid/graphics/Bitmap$Config;)Landroid/graphics/Bitmap;
    move-result-object v20
    new-instance v21, Landroid/graphics/Canvas;
    move-object/from16 v0, v21
    move-object/from16 v1, v20
    invoke-direct/range {v0 .. v1}, Landroid/graphics/Canvas;-><init>(Landroid/graphics/Bitmap;)V
    new-instance v22, Landroid/graphics/Paint;
    const v23, 0x1
    move-object/from16 v0, v22
    move/from16 v1, v23
    invoke-direct/range {v0 .. v1}, Landroid/graphics/Paint;-><init>(I)V
    const v24, 0x42dc0000
    mul-float v25, v14, v24
    div-float v26, v18, v25
    const v27, 0x3f800000
    const v28, 0x3f0ccccd
    move/from16 v0, v26
    move/from16 v1, v27
    invoke-static/range {v0 .. v1}, Ljava/lang/Math;->min(FF)F
    move-result v26
    move/from16 v0, v26
    move/from16 v1, v28
    invoke-static/range {v0 .. v1}, Ljava/lang/Math;->max(FF)F
    move-result v26
    mul-float v29, v14, v26
    const v30, 0x42dc0000
    mul-float v31, v29, v30
    sub-float v32, v18, v31
    const v33, 0x3f000000
    mul-float v34, v32, v33
    const v35, 0x0
    move-object/from16 v0, v21
    move/from16 v1, v35
    move/from16 v2, v34
    invoke-virtual/range {v0 .. v2}, Landroid/graphics/Canvas;->translate(FF)V
    move/from16 v18, v31
    const v36, 0x0
    const v37, 0x0
    const v38, 0xa60b1d3a
    const v39, 0xa60f7a5a
    sget-object v40, Landroid/graphics/Shader$TileMode;->CLAMP:Landroid/graphics/Shader$TileMode;
    new-instance v41, Landroid/graphics/LinearGradient;
    move-object/from16 v0, v41
    move/from16 v1, v36
    move/from16 v2, v36
    move/from16 v3, v17
    move/from16 v4, v18
    move/from16 v5, v38
    move/from16 v6, v39
    move-object/from16 v7, v40
    invoke-direct/range {v0 .. v7}, Landroid/graphics/LinearGradient;-><init>(FFFFIILandroid/graphics/Shader$TileMode;)V
    move-object/from16 v0, v22
    move-object/from16 v1, v41
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setShader(Landroid/graphics/Shader;)Landroid/graphics/Shader;
    new-instance v42, Landroid/graphics/RectF;
    move-object/from16 v0, v42
    move/from16 v1, v36
    move/from16 v2, v36
    move/from16 v3, v17
    move/from16 v4, v18
    invoke-direct/range {v0 .. v4}, Landroid/graphics/RectF;-><init>(FFFF)V
    const v43, 0x41a00000
    mul-float v44, v29, v43
    move-object/from16 v0, v21
    move-object/from16 v1, v42
    move/from16 v2, v44
    move/from16 v3, v44
    move-object/from16 v4, v22
    invoke-virtual/range {v0 .. v4}, Landroid/graphics/Canvas;->drawRoundRect(Landroid/graphics/RectF;FFLandroid/graphics/Paint;)V
    move-object/from16 v0, v22
    move-object/from16 v1, v37
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setShader(Landroid/graphics/Shader;)Landroid/graphics/Shader;
    sget-object v45, Landroid/graphics/Paint$Style;->STROKE:Landroid/graphics/Paint$Style;
    sget-object v46, Landroid/graphics/Paint$Style;->FILL:Landroid/graphics/Paint$Style;
    move-object/from16 v0, v22
    move-object/from16 v1, v45
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    move-object/from16 v0, v22
    move/from16 v1, v14
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setStrokeWidth(F)V
    const v47, 0x44ffffff
    move-object/from16 v0, v22
    move/from16 v1, v47
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setColor(I)V
    const v43, 0x3f000000
    mul-float v48, v14, v43
    sub-float v49, v17, v48
    sub-float v50, v18, v48
    new-instance v51, Landroid/graphics/RectF;
    move-object/from16 v0, v51
    move/from16 v1, v48
    move/from16 v2, v48
    move/from16 v3, v49
    move/from16 v4, v50
    invoke-direct/range {v0 .. v4}, Landroid/graphics/RectF;-><init>(FFFF)V
    move-object/from16 v0, v21
    move-object/from16 v1, v51
    move/from16 v2, v44
    move/from16 v3, v44
    move-object/from16 v4, v22
    invoke-virtual/range {v0 .. v4}, Landroid/graphics/Canvas;->drawRoundRect(Landroid/graphics/RectF;FFLandroid/graphics/Paint;)V
    move-object/from16 v0, v22
    move-object/from16 v1, v46
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    move-object/from16 v0, v16
    invoke-virtual/range {v0 .. v0}, Landroid/content/Context;->getAssets()Landroid/content/res/AssetManager;
    move-result-object v52
    const-string v53, "sans-serif-medium"
    const-string v54, "sans-serif"
    const v55, 0x0
    const v56, 0x1
    move-object/from16 v0, v53
    move/from16 v1, v55
    invoke-static/range {v0 .. v1}, Landroid/graphics/Typeface;->create(Ljava/lang/String;I)Landroid/graphics/Typeface;
    move-result-object v57
    move-object/from16 v0, v54
    move/from16 v1, v56
    invoke-static/range {v0 .. v1}, Landroid/graphics/Typeface;->create(Ljava/lang/String;I)Landroid/graphics/Typeface;
    move-result-object v58
    const v59, 0xffffffff
    const v60, 0xfff6c453
    const v61, 0xfff2f2f2
    const v62, 0xffffe08a
    const v63, 0x0
    const v64, 0x1
    const v43, 0x41000000
    mul-float v65, v29, v43
    const v43, 0x40000000
    mul-float v66, v65, v43
    sub-float v67, v17, v66
    const v43, 0x3f000000
    mul-float v68, v17, v43
    const v43, 0x41600000
    mul-float v69, v29, v43
    const v43, 0x41500000
    mul-float v70, v29, v43
    add-float v71, v65, v70
    const-string v72, "রাধানগর পশ্চিম পাড়া বাইতুল মা'মুর জামে মসজিদ"
    move-object/from16 v0, v21
    move-object/from16 v1, v22
    move-object/from16 v2, v58
    move-object/from16 v3, v72
    move/from16 v4, v68
    move/from16 v5, v71
    move/from16 v6, v69
    move/from16 v7, v59
    move/from16 v8, v64
    move/from16 v9, v67
    invoke-static/range {v0 .. v9}, Lcom/baitulmamur/app/DateWidget;->T(Landroid/graphics/Canvas;Landroid/graphics/Paint;Landroid/graphics/Typeface;Ljava/lang/String;FFFIIF)V
    const v43, 0x41300000
    mul-float v73, v29, v43
    add-float v74, v71, v70
    const-string v75, "— রাধানগর, রায়পুরা, নরসিংদী। —"
    move-object/from16 v0, v21
    move-object/from16 v1, v22
    move-object/from16 v2, v57
    move-object/from16 v3, v75
    move/from16 v4, v68
    move/from16 v5, v74
    move/from16 v6, v73
    move/from16 v7, v60
    move/from16 v8, v64
    move/from16 v9, v67
    invoke-static/range {v0 .. v9}, Lcom/baitulmamur/app/DateWidget;->T(Landroid/graphics/Canvas;Landroid/graphics/Paint;Landroid/graphics/Typeface;Ljava/lang/String;FFFIIF)V
    const v43, 0x40e00000
    mul-float v76, v29, v43
    add-float v77, v74, v76
    sub-float v78, v18, v65
    sub-float v79, v17, v65
    const v80, 0x1affffff
    move-object/from16 v0, v22
    move/from16 v1, v80
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setColor(I)V
    new-instance v81, Landroid/graphics/RectF;
    move-object/from16 v0, v81
    move/from16 v1, v65
    move/from16 v2, v77
    move/from16 v3, v79
    move/from16 v4, v78
    invoke-direct/range {v0 .. v4}, Landroid/graphics/RectF;-><init>(FFFF)V
    const v43, 0x41600000
    mul-float v82, v29, v43
    move-object/from16 v0, v21
    move-object/from16 v1, v81
    move/from16 v2, v82
    move/from16 v3, v82
    move-object/from16 v4, v22
    invoke-virtual/range {v0 .. v4}, Landroid/graphics/Canvas;->drawRoundRect(Landroid/graphics/RectF;FFLandroid/graphics/Paint;)V
    move-object/from16 v0, v22
    move-object/from16 v1, v45
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    const v83, 0x33ffffff
    move-object/from16 v0, v22
    move/from16 v1, v83
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setColor(I)V
    move-object/from16 v0, v21
    move-object/from16 v1, v81
    move/from16 v2, v82
    move/from16 v3, v82
    move-object/from16 v4, v22
    invoke-virtual/range {v0 .. v4}, Landroid/graphics/Canvas;->drawRoundRect(Landroid/graphics/RectF;FFLandroid/graphics/Paint;)V
    move-object/from16 v0, v22
    move-object/from16 v1, v46
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    sub-float v84, v78, v77
    const v43, 0x42080000
    mul-float v85, v29, v43
    add-float v86, v65, v85
    const v43, 0x42380000
    mul-float v87, v29, v43
    const v43, 0x42080000
    mul-float v88, v29, v43
    const v43, 0x3f000000
    mul-float v89, v84, v43
    move/from16 v0, v88
    move/from16 v1, v89
    invoke-static/range {v0 .. v1}, Ljava/lang/Math;->min(FF)F
    move-result v90
    const v43, 0x3f1eb852
    mul-float v91, v84, v43
    add-float v92, v77, v91
    const/16 v93, 0x0
    aget-object v94, v15, v93
    move-object/from16 v0, v21
    move-object/from16 v1, v22
    move-object/from16 v2, v58
    move-object/from16 v3, v94
    move/from16 v4, v86
    move/from16 v5, v92
    move/from16 v6, v90
    move/from16 v7, v60
    move/from16 v8, v64
    move/from16 v9, v87
    invoke-static/range {v0 .. v9}, Lcom/baitulmamur/app/DateWidget;->T(Landroid/graphics/Canvas;Landroid/graphics/Paint;Landroid/graphics/Typeface;Ljava/lang/String;FFFIIF)V
    const v43, 0x41300000
    mul-float v95, v29, v43
    const v43, 0x3e2e147b
    mul-float v96, v84, v43
    move/from16 v0, v95
    move/from16 v1, v96
    invoke-static/range {v0 .. v1}, Ljava/lang/Math;->min(FF)F
    move-result v97
    const v43, 0x3f666666
    mul-float v91, v84, v43
    add-float v98, v77, v91
    const/16 v99, 0x1
    aget-object v100, v15, v99
    move-object/from16 v0, v21
    move-object/from16 v1, v22
    move-object/from16 v2, v57
    move-object/from16 v3, v100
    move/from16 v4, v86
    move/from16 v5, v98
    move/from16 v6, v97
    move/from16 v7, v59
    move/from16 v8, v64
    move/from16 v9, v87
    invoke-static/range {v0 .. v9}, Lcom/baitulmamur/app/DateWidget;->T(Landroid/graphics/Canvas;Landroid/graphics/Paint;Landroid/graphics/Typeface;Ljava/lang/String;FFFIIF)V
    const v43, 0x42800000
    mul-float v101, v29, v43
    add-float v102, v65, v101
    const v103, 0x43960000
    mul-float v104, v14, v103
    cmpl-float v105, v17, v104
    const v43, 0x41200000
    mul-float v106, v29, v43
    const v43, 0x42a00000
    mul-float v107, v29, v43
    const v43, 0x41000000
    mul-float v108, v29, v43
    const v43, 0x40c00000
    mul-float v109, v29, v43
    sub-float v110, v79, v106
    sub-float v111, v110, v107
    sub-float v112, v111, v108
    sub-float v113, v110, v36
    if-lez v105, :nosun
    move/from16 v114, v112
    goto :gotm
    :nosun
    move/from16 v114, v113
    :gotm
    sub-float v115, v114, v102
    const v43, 0x41500000
    mul-float v116, v29, v43
    const v43, 0x3e4ccccd
    mul-float v117, v84, v43
    move/from16 v0, v116
    move/from16 v1, v117
    invoke-static/range {v0 .. v1}, Ljava/lang/Math;->min(FF)F
    move-result v118
    const/16 v119, 0x2
    aget-object v120, v15, v119
    const v43, 0x3e8a3d71
    mul-float v91, v84, v43
    add-float v121, v77, v91
    move-object/from16 v0, v21
    move-object/from16 v1, v22
    move-object/from16 v2, v58
    move-object/from16 v3, v120
    move/from16 v4, v102
    move/from16 v5, v121
    move/from16 v6, v118
    move/from16 v7, v59
    move/from16 v8, v63
    move/from16 v9, v115
    invoke-static/range {v0 .. v9}, Lcom/baitulmamur/app/DateWidget;->T(Landroid/graphics/Canvas;Landroid/graphics/Paint;Landroid/graphics/Typeface;Ljava/lang/String;FFFIIF)V
    const/16 v119, 0x3
    aget-object v122, v15, v119
    const v43, 0x3f0f5c29
    mul-float v91, v84, v43
    add-float v121, v77, v91
    move-object/from16 v0, v21
    move-object/from16 v1, v22
    move-object/from16 v2, v57
    move-object/from16 v3, v122
    move/from16 v4, v102
    move/from16 v5, v121
    move/from16 v6, v118
    move/from16 v7, v61
    move/from16 v8, v63
    move/from16 v9, v115
    invoke-static/range {v0 .. v9}, Lcom/baitulmamur/app/DateWidget;->T(Landroid/graphics/Canvas;Landroid/graphics/Paint;Landroid/graphics/Typeface;Ljava/lang/String;FFFIIF)V
    const/16 v119, 0x4
    aget-object v123, v15, v119
    const v43, 0x3f59999a
    mul-float v91, v84, v43
    add-float v121, v77, v91
    move-object/from16 v0, v21
    move-object/from16 v1, v22
    move-object/from16 v2, v57
    move-object/from16 v3, v123
    move/from16 v4, v102
    move/from16 v5, v121
    move/from16 v6, v118
    move/from16 v7, v61
    move/from16 v8, v63
    move/from16 v9, v115
    invoke-static/range {v0 .. v9}, Lcom/baitulmamur/app/DateWidget;->T(Landroid/graphics/Canvas;Landroid/graphics/Paint;Landroid/graphics/Typeface;Ljava/lang/String;FFFIIF)V
    if-lez v105, :end
    sub-float v124, v111, v109
    const v43, 0x3e4ccccd
    mul-float v125, v84, v43
    add-float v126, v77, v125
    sub-float v127, v78, v125
    const v128, 0x44ffffff
    move-object/from16 v0, v22
    move/from16 v1, v128
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setColor(I)V
    move-object/from16 v0, v22
    move-object/from16 v1, v45
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    move-object/from16 v0, v21
    move/from16 v1, v124
    move/from16 v2, v126
    move/from16 v3, v124
    move/from16 v4, v127
    move-object/from16 v5, v22
    invoke-virtual/range {v0 .. v5}, Landroid/graphics/Canvas;->drawLine(FFFFLandroid/graphics/Paint;)V
    move-object/from16 v0, v22
    move-object/from16 v1, v46
    invoke-virtual/range {v0 .. v1}, Landroid/graphics/Paint;->setStyle(Landroid/graphics/Paint$Style;)V
    const v43, 0x41400000
    mul-float v129, v29, v43
    const v43, 0x3e428f5c
    mul-float v130, v84, v43
    move/from16 v0, v129
    move/from16 v1, v130
    invoke-static/range {v0 .. v1}, Ljava/lang/Math;->min(FF)F
    move-result v131
    const/16 v119, 0x5
    aget-object v132, v15, v119
    const v43, 0x3ed70a3d
    mul-float v91, v84, v43
    add-float v121, v77, v91
    move-object/from16 v0, v21
    move-object/from16 v1, v22
    move-object/from16 v2, v57
    move-object/from16 v3, v132
    move/from16 v4, v111
    move/from16 v5, v121
    move/from16 v6, v131
    move/from16 v7, v62
    move/from16 v8, v63
    move/from16 v9, v107
    invoke-static/range {v0 .. v9}, Lcom/baitulmamur/app/DateWidget;->T(Landroid/graphics/Canvas;Landroid/graphics/Paint;Landroid/graphics/Typeface;Ljava/lang/String;FFFIIF)V
    const/16 v119, 0x6
    aget-object v132, v15, v119
    const v43, 0x3f47ae14
    mul-float v91, v84, v43
    add-float v121, v77, v91
    move-object/from16 v0, v21
    move-object/from16 v1, v22
    move-object/from16 v2, v57
    move-object/from16 v3, v132
    move/from16 v4, v111
    move/from16 v5, v121
    move/from16 v6, v131
    move/from16 v7, v62
    move/from16 v8, v63
    move/from16 v9, v107
    invoke-static/range {v0 .. v9}, Lcom/baitulmamur/app/DateWidget;->T(Landroid/graphics/Canvas;Landroid/graphics/Paint;Landroid/graphics/Typeface;Ljava/lang/String;FFFIIF)V
    :end
    return-object v20
.end method

.method public onUpdate(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;[I)V
    .locals 4
    array-length v0, p3
    const/4 v1, 0x0
    :lp
    if-ge v1, v0, :end
    aget v2, p3, v1
    invoke-virtual {p0, p1, p2, v2}, Lcom/baitulmamur/app/DateWidget;->one(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;I)V
    add-int/lit8 v1, v1, 0x1
    goto :lp
    :end
    return-void
.end method

.method public onAppWidgetOptionsChanged(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;ILandroid/os/Bundle;)V
    .locals 0
    invoke-virtual {p0, p1, p2, p3}, Lcom/baitulmamur/app/DateWidget;->one(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;I)V
    return-void
.end method

.method one(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;I)V
    .locals 12
    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;
    move-result-object v8
    invoke-virtual {v8}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;
    move-result-object v0
    iget v1, v0, Landroid/util/DisplayMetrics;->density:F
    invoke-virtual {p2, p3}, Landroid/appwidget/AppWidgetManager;->getAppWidgetOptions(I)Landroid/os/Bundle;
    move-result-object v2
    const-string v3, "appWidgetMinWidth"
    invoke-virtual {v2, v3}, Landroid/os/Bundle;->getInt(Ljava/lang/String;)I
    move-result v4
    const-string v3, "appWidgetMaxHeight"
    invoke-virtual {v2, v3}, Landroid/os/Bundle;->getInt(Ljava/lang/String;)I
    move-result v5
    if-gtz v4, :w
    const/16 v4, 0x154
    :w
    if-gtz v5, :h
    const/16 v5, 0x96
    :h
    int-to-float v4, v4
    mul-float/2addr v4, v1
    float-to-int v4, v4
    int-to-float v5, v5
    mul-float/2addr v5, v1
    float-to-int v5, v5
    invoke-static {}, Lcom/baitulmamur/app/DateWidget;->texts()[Ljava/lang/String;
    move-result-object v6
    invoke-static {p1, v4, v5, v1, v6}, Lcom/baitulmamur/app/DateWidget;->draw(Landroid/content/Context;IIF[Ljava/lang/String;)Landroid/graphics/Bitmap;
    move-result-object v7
    invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    move-result-object v9
    const-string v3, "date_widget"
    const-string v4, "layout"
    invoke-virtual {v8, v3, v4, v9}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I
    move-result v3
    new-instance v10, Landroid/widget/RemoteViews;
    invoke-direct {v10, v9, v3}, Landroid/widget/RemoteViews;-><init>(Ljava/lang/String;I)V
    const-string v3, "w_img"
    const-string v4, "id"
    invoke-virtual {v8, v3, v4, v9}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I
    move-result v3
    invoke-virtual {v10, v3, v7}, Landroid/widget/RemoteViews;->setImageViewBitmap(ILandroid/graphics/Bitmap;)V
    invoke-virtual {p2, p3, v10}, Landroid/appwidget/AppWidgetManager;->updateAppWidget(ILandroid/widget/RemoteViews;)V
    return-void
.end method
