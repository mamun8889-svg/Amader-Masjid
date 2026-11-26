import subprocess
subprocess.run(['python3','p32.py'],check=True)
s=open('index32.html',encoding='utf-8').read()
css='''
/* ===== অ্যানিমেশন (হালকা, রিডিউসড-মোশন সমর্থিত) ===== */
@keyframes upIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@keyframes glowIn{0%{box-shadow:0 0 0 0 rgba(246,180,74,0)}40%{box-shadow:0 0 26px 2px rgba(246,180,74,.38)}100%{box-shadow:var(--shadow)}}
@keyframes bellPulse{0%{box-shadow:0 0 0 0 rgba(224,69,91,.65)}70%,100%{box-shadow:0 0 0 9px rgba(224,69,91,0)}}
@keyframes fabF{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
@keyframes popIn{from{opacity:0;transform:translateY(10px) scale(.97)}to{opacity:1;transform:none}}
body{animation:fade .5s ease}
.hero{animation:glowIn 2.6s ease-out 1}
.section.stg .kpi,.section.stg .ahc,.section.stg .ahrep,.section.stg .panel,.section.stg .tools{animation:upIn .5s cubic-bezier(.2,.7,.2,1) both}
.section.stg .kpi:nth-child(2),.section.stg .ahc:nth-child(2){animation-delay:.07s}.section.stg .kpi:nth-child(3),.section.stg .ahrep{animation-delay:.14s}
.section.stg .kpi:nth-child(4){animation-delay:.21s}.section.stg .kpi:nth-child(5){animation-delay:.28s}.section.stg .kpi:nth-child(n+6){animation-delay:.35s}
.card,.panel,.ahc,.ahrep{transition:border-color .3s,box-shadow .3s}
.card:hover,.panel:hover,.ahc:hover,.card:active,.ahc:active{border-color:rgba(232,146,12,.5)}
.btn,.ahb,.ahx,.ahmore,#fabBtn,.seg button{transition:transform .12s ease,box-shadow .25s,background-color .25s}
.btn:active,.ahb:active,.ahx:active,#fabBtn:active,.seg button:active{transform:scale(.95)}
select,input,textarea{transition:border-color .2s,box-shadow .25s}
select:focus,input:focus,textarea:focus{box-shadow:0 0 0 3px rgba(232,146,12,.28);outline:none}
#bellN:not([hidden]){animation:bellPulse 2.2s ease-out infinite}
#fabBtn{animation:fabF 3.6s ease-in-out infinite}
body.fabopen #fabBtn{animation:none}
.modal>*{animation:popIn .22s ease}
.pbar{height:6px;border-radius:6px;background:var(--line);overflow:hidden;margin-top:8px}
.pbar i{display:block;height:100%;width:0;border-radius:6px;background:linear-gradient(90deg,var(--emerald),var(--amber));transition:width .9s cubic-bezier(.2,.7,.2,1)}
@media(prefers-reduced-motion:reduce){.pbar i{transition:none}}
'''
s=s.replace('</style>',css+'</style>',1)
i=s.rindex('</script>');s=s[:i]+open('anim.js',encoding='utf-8').read()+s[i:]
open('index33.html','w',encoding='utf-8').write(s)
