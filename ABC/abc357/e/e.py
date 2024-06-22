from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
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

def dfs(v,p,dp,G,E,SCC):
    if dp[v]>-1:
        return dp[v]
    dp[v]=0
    for e in G[v]:
        vv = SCC[E[e]]
        if vv == p:
            continue
        dp[v]+=dfs(vv,v,dp,G,E,SCC)
    dp[v]+=len(G[v])
    return dp[v]
def main():
    from atcoder.scc import SCCGraph
    N = int(myin())
    A = myin_sp_i()
    E = [-1 for i in range(N)]
    
    G = SCCGraph(N)
    for i in range(N):
        a = A[i]
        G.add_edge(i,a-1)
        E[i]=a-1
    SCC = [-1 for i in range(N)]
    sccG = G.scc()
    M = len(sccG)
    for i in range(M):
        for v in sccG[i]:
            SCC[v]=i
    dp = [-1 for i in range(M)]
    for i in range(M):
        dfs(i,-1,dp,sccG,E,SCC)
        #print(dp)
    ans = 0
    for i in range(M):
        ans+=dp[i]*len(sccG[i])
    print(ans)
if __name__ == "__main__":
    main()