import re
SQL_ERR=re.compile(r"(sql syntax|mysql|postgresql|sqlite|ora-|mssql)",re.I)

def detect_sqli(fetch, base, params):
    out=[]
    for p in params:
        r0=fetch(base,{p:"1"})
        r1=fetch(base,{p:"'"})
        err=bool(SQL_ERR.search(r1.text))
        sim=abs(len(r0.text)-len(r1.text))>200
        if err or sim:
            out.append({
                "param":p,
                "error_sig":err,
                "behavior_delta":sim,
                "confidence":0.9 if err and sim else 0.7
            })
    return out
