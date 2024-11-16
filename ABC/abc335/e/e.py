from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    from atcoder.dsu import DSU
    N,M = myin_sp_i()
    A = myin_sp_i()
    dsu = DSU(N)
    E = [[] for i in range(2*10**5+10)]
    for i in range(M):
        u,v = myin_sp_i()
        u-=1
        v-=1
        if A[u]<A[v]:
            E[A[u]].append((u,v))
        elif A[u]>A[v]:
            E[A[v]].append((v,u))
        else:
            dsu.merge(u,v)
    dp = [-1]*N 
    dp[dsu.leader(0)]=1
    for vp in E:
        if not vp: continue
        for u,v in vp:
            u = dsu.leader(u)
            v = dsu.leader(v)
            if dp[u]>0:
                dp[v]=max(dp[v],dp[u]+1)
    print(max(dp[dsu.leader(N-1)],0))

if __name__ == "__main__":
    main()