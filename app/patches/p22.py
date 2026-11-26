s=open('index21.html',encoding='utf8').read()
def rep(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:60],s.count(a)); s=s.replace(a,b)
# due cutoff: month M counts as arrears only after the 5th of M+1
rep("const uptoCal=y=>","const dueUp=y=>{const n=new Date(),ab=n.getFullYear()*12+n.getMonth()-(n.getDate()>5?1:2);return Math.min(11,ab-y*12)};\nconst uptoCal=y=>")
rep("function cellDue(y,i,m){const r=rowsOf(y)[i],v=val(y,i,m);if(!(r.amount>0)||","function cellDue(y,i,m){const r=rowsOf(y)[i],v=val(y,i,m);if(typeof m==='number'&&monthCal(y,m)>dueUp(y))return 0;if(!(r.amount>0)||")
rep("st=dueStart(y,i),up=uptoCal(y),rows=[]","st=dueStart(y,i),up=dueUp(y),rows=[]")
rep("const st=payerStats(yy,ii),up=uptoCal(yy);","const st=payerStats(yy,ii),up=dueUp(yy);")
# salary cards always running month
rep("const pu=paidUnpaid(y,mi),tot=rowsOf(y)","const _n=new Date(),rm=y===_n.getFullYear()?_n.getMonth():(y<_n.getFullYear()?ms.length-1:0),pu=paidUnpaid(y,rm),notPaid=rowsOf(y).filter((r,i)=>{const v=val(y,i,rm);return r.amount>0&&v!=='x'&&v!=='r'&&!(isNum(v)&&v>0)&&r.name!=='(নামহীন জমা)'&&!offAfter(y,r,rm)}).length,tot=rowsOf(y)")
rep("kpi('k-sk','cal',ms[mi]+' মাসে সংগ্রহ',money(colSum(y,mi)),'')+kpi('k-am','people',ms[mi]+' মাসে অংশগ্রহণ',fmt(pu.paid)+' জন দিয়েছেন',ed?'বকেয়া '+fmt(pu.unpaid.length)+' জন':'')","kpi('k-sk','cal',ms[rm]+' মাসে সংগ্রহ',money(colSum(y,rm)),'চলতি মাস')+kpi('k-am','people',ms[rm]+' মাসে অংশগ্রহণ',fmt(pu.paid)+' জন দিয়েছেন',ed?'এখনো দেননি '+fmt(notPaid)+' জন':'')")
open('index22.html','w',encoding='utf8').write(s)
