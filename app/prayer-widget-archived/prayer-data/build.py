import sys,math,json,datetime
sys.path.insert(0,'/tmp/claude-0/-home-claude/62b2875e-3675-586f-8357-42a4b5062fa0/scratchpad/w')
import io,contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import sunfit
mdays=[31,28,31,30,31,30,31,31,30,31,30,31]
def m(t,pm=False):
    h,mi=map(int,t.split(':'))
    if pm and h<12:h+=12
    return h*60+mi
rows=[]
for mo in range(12):
    L=[l.split() for l in open('m%02d.txt'%(mo+1)) if l.strip()]
    assert len(L)==mdays[mo],(mo+1,len(L))
    for d,x in enumerate(L,1):
        s,f,r,z,a,mg,i=x
        rows.append([mo+1,d,m(s),m(f),m(r),m(z),m(a,1),m(mg,1),m(i,1)])
names=['sehri','fajr','sunrise','zuhr','asr','maghrib','isha']
bad=[]
for c in range(7):
    for k in range(1,len(rows)):
        dd=rows[k][2+c]-rows[k-1][2+c]
        lim=3 if c in(0,1) else 2
        if abs(dd)>lim: bad.append((rows[k][0],rows[k][1],names[c],dd))
# curvature check
for c in range(7):
    for k in range(2,len(rows)):
        v=rows[k][2+c]-2*rows[k-1][2+c]+rows[k-2][2+c]
        if abs(v)>2: bad.append((rows[k][0],rows[k][1],names[c],'curv%d'%v))
# sun model cross-check (sunrise, maghrib)
import numpy as np
doy=0;res=[]
for k,r in enumerate(rows):
    rise,sset=sunfit.sun(k+1)
    res.append((r[4]-rise%1440, r[7]-sset%1440))
res=np.array(res);print('median offset sunrise/maghrib',np.median(res,0))
for k in range(len(rows)):
    for j,nm in ((0,'sunrise'),(1,'maghrib')):
        if abs(res[k][j]-np.median(res[:,j]))>3: bad.append((rows[k][0],rows[k][1],nm,'sun%.1f'%(res[k][j]-np.median(res[:,j]))))
print(len(bad));[print(b) for b in bad]
json.dump(rows,open('rows.json','w'))
