import pandas as pd
d = pd.read_csv("data/ventas.csv")
t = 0
for i in range(len(d)):
    t = t + d.iloc[i]["cantidad"] * d.iloc[i]["precio"]
print("total", t)
p = {}
for i in range(len(d)):
    if d.iloc[i]["cantidad"] > 0 and d.iloc[i]["precio"] > 0:
        if d.iloc[i]["producto"] in p:
            p[d.iloc[i]["producto"]] = p[d.iloc[i]["producto"]] + d.iloc[i]["cantidad"] * d.iloc[i]["precio"]
        else:
            p[d.iloc[i]["producto"]] = d.iloc[i]["cantidad"] * d.iloc[i]["precio"]
l = list(p.items())
for a in range(len(l)):
    for b in range(len(l) - 1):
        if l[b][1] < l[b + 1][1]:
            x = l[b]
            l[b] = l[b + 1]
            l[b + 1] = x
for k in range(5):
    print(l[k][0], l[k][1])
m = {}
for i in range(len(d)):
    f = str(d.iloc[i]["fecha"])[0:7]
    if f in m:
        m[f] = m[f] + d.iloc[i]["cantidad"] * d.iloc[i]["precio"]
    else:
        m[f] = d.iloc[i]["cantidad"] * d.iloc[i]["precio"]
print(m)
