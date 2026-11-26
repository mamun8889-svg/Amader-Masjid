import re
s=open('index30.html',encoding='utf-8').read()
js=open('ah.js',encoding='utf-8').read()
css='''
.kpi .ic{display:none!important}.kpi{padding-top:17px}
body:not(.onHome) .hero{display:none!important}
body.ahOn #dashboard>*:not(#adminHome){display:none!important}
#salary .sec-head{flex-wrap:wrap!important}
#salary .sec-head .row-actions{flex-direction:row!important;width:100%;gap:8px}
#salary .sec-head .row-actions .btn{flex:1;justify-content:center}
#adminHome .ahenter{width:100%;font-size:17px;padding:13px;margin:4px 0 14px}
.ahcards{display:grid;gap:12px;margin-bottom:16px}
.ahc{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:14px;box-shadow:var(--shadow)}
.ahc.on{border-color:var(--emerald);box-shadow:0 0 0 2px var(--emerald-s),var(--shadow)}
.aht{font-family:var(--serif);font-weight:700;font-size:17px}.ahm{color:var(--muted);font-size:14px;font-weight:600;margin-left:6px}
.ahs{font-size:13px;margin:4px 0 10px;color:var(--muted)}.ahs.on{color:var(--emerald);font-weight:700}.ahs.soon{color:var(--amber)}.ahs.end{color:var(--rose)}
.ahg2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ahb,.ahx{border:0;border-radius:14px;padding:12px 10px;text-align:left;font:inherit;color:var(--ink);background:var(--surface2);cursor:pointer;display:flex;flex-direction:column;gap:2px;width:100%}
.ahb .n{font-size:24px;font-weight:800}.ahb .l{font-size:13px;color:var(--muted)}.ahb .a{font-size:16px;font-weight:700}
.ahb.ok{background:var(--emerald-s)}.ahb.ok .n,.ahb.ok .a{color:var(--emerald-d)}
.ahb.no{background:var(--rose-s)}.ahb.no .n,.ahb.no .a{color:var(--rose)}
.ahrep{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:14px;margin-bottom:16px}
.ahrep h4{margin:0 0 10px;font-family:var(--serif)}
.ahsel{display:grid;grid-template-columns:1fr 1.4fr;gap:10px}
.ahgrid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ahx .l{font-size:12.5px;color:var(--muted)}.ahx .n{font-size:21px;font-weight:800}.ahx .n.g{color:var(--emerald-d)}.ahx .n.r{color:var(--rose)}
.ahx.ok{background:var(--emerald-s)}.ahx.no{background:var(--rose-s)}.ahx.wide{grid-column:1/-1}
.ahtwo{display:grid;gap:12px;margin-top:14px}
.ahp{border-radius:14px;padding:12px;border:1px solid var(--line)}.ahp h5{margin:0 0 8px;font-size:15px}
.ahp.ok{background:var(--emerald-s)}.ahp.no{background:var(--rose-s)}
.ahr{display:flex;justify-content:space-between;gap:8px;padding:5px 0;border-bottom:1px dashed var(--line);font-size:14px}
.ahmore{margin-top:8px;border:0;background:transparent;color:var(--indigo);font:inherit;font-weight:700;padding:4px 0}
.tg{background:var(--amber-s);color:var(--amber);border-radius:6px;padding:1px 6px;font-size:11px}
.pdue{border-radius:12px;padding:10px 12px;margin:10px 0;border:1px solid var(--line)}.pdue.warn{background:var(--rose-s);border-color:var(--rose)}.pdue.okk{background:var(--emerald-s)}
#mBody .tablewrap td .btn.sm{padding:5px 9px;font-size:12.5px;min-width:0}#mBody .tablewrap table{font-size:13.5px}#mBody .tablewrap td,#mBody .tablewrap th{padding:8px 6px}
.pdue .ptag{font-weight:800;font-size:15px;margin:6px 0}.pdue.warn .ptag{color:var(--rose)}.pdue.okk .ptag{color:var(--emerald-d)}
'''
s=s.replace('</style>',css+'</style>',1)
s=s.replace('<section id="dashboard" class="section active">','<section id="dashboard" class="section active">\n <div id="adminHome" hidden></div>',1)
i=s.rindex('</script>')
s=s[:i]+js+s[i:]
open('index31.html','w',encoding='utf-8').write(s)
