from atcoder.string import suffix_array,lcp_array
N = int(input())
S=list(map(str,input().split()))
B = ""
for s in S:
    B+=s
B_SA = suffix_array(B)
print(B_SA)
SA = []
prev = 0
for s in S:
    SA.append(B_SA[prev:len(s)])
    prev += len(s)
print(SA)
def f(g,d):
    if len(g)<=1:
        return 0
    s = SA[g[0]]
    group = {}
    for i in range(1,len(g)):
        t = SA[g[i]]
        ln = min(lcp_array(s,t)[d:])
        if ln not in group:
            group[ln]={i}
        else:
            group[ln].append(i)
    res = 0
    for key,val in group.items():
        res+=len(val)*int(key)+f(val,d+key)
    return res
print(f(list(range(N)),0))