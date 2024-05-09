import sys
sys.setrecursionlimit(2*10**7)
S = sys.stdin.readline()
G = {}
N = len(S)
def dfs(l):
    if S[l]!="(":
        G[(l,l+1)] = []
        return [l,l+1]
    child = []
    r = l+1
    while r<N and S[r]!=")":
        ll,rr = dfs(r)
        child.append([ll,rr])
        r=rr
    G[(l,r+1)] = child
    return [l,r+1]
find = set()
def solve(v:tuple,type):
    global find 
    #print(v)
    if v in find:
        return ""
    find.add(v)
    if v[1]==v[0]+1:
        if type == 1:
            return S[v[0]]
        else:
            return S[v[0]].swapcase()
    size = len(G[v])
    idx = 0
    step = 1
    if type == 1:
        idx = size-1
        step = -1
    res = ""
    i = 0
    while i<size:
        res+=solve(tuple(G[v][idx]),type=(type+1)%2)
        idx+=step
        i+=1
    return res
i = 0
while i<N:
    l,r = dfs(i)
    i= r

keys = sorted(G.keys())
ans = ""
for k in keys:
    if k in find:
        continue
    if k[1]==k[0]+1:
        ans+=S[k[0]]
        find.add(k)
    else:
        ans+=solve(k,type=1)
print(ans)