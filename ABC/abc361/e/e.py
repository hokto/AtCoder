from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 9)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))


INF = 10**15
def dfs(v,p,cost,G,dist):
    dist[v]=cost
    for vv,c in G[v]:
        if vv==p: continue
        dfs(vv,v,cost+c,G,dist)
        
def dfs2(v,p,g,G):
    if v==g:
        return True,0
    res=0
    flag = False
    for vv,c in G[v]:
        if vv==p: continue
        f,cost = dfs2(vv,v,g,G)
        res+=cost+c
        if not f: res+=c
        flag|=f
    return flag,res
def main():
    N = int(myin())
    G=[[] for i in range(N)]
    for i in range(N-1):
        a,b,c = myin_sp_i()
        a-=1
        b-=1
        G[a].append((b,c))
        G[b].append((a,c))
    dist1 = [INF]*N
    dfs(0,-1,0,G,dist1)
    next_r = -1
    mx = 0
    for i in range(N):
        if mx < dist1[i]:
            mx = dist1[i]
            next_r = i
    dist2 = [INF]*N
    dfs(next_r,-1,0,G,dist2)
    g = -1
    mx = 0
    for i in range(N):
        if mx<dist2[i]:
            mx = dist2[i]
            g = i
    #print(next_r,g)
    print(dfs2(next_r,-1,g,G)[1])
if __name__ == "__main__":
    main()