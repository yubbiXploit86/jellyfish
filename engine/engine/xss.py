def detect_xss(fetch, base, params):
    findings=[]
    markers=["jfx","jfx_attr","jfx_js"]
    for p in params:
        evid=[]
        for m in markers:
            payload=f"<{m}>"
            r=fetch(base, {p:payload})
            if payload in r.text:
                ctx="HTML"
                if f'="{payload}"' in r.text: ctx="ATTR"
                if f"'{payload}'" in r.text: ctx="JS"
                evid.append(ctx)
        if len(set(evid))>=1:
            findings.append({
                "param":p,
                "contexts":list(set(evid)),
                "confidence":0.85 if len(evid)>1 else 0.75
            })
    return findings
