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
def dp(v,p,memo,N,G):
    if memo[v]<INF:
        return memo[v]
    sum_e = 0
    for vv,c in G[v]:
        if vv==p: continue
        e = c+dp(vv,v,memo,N,G)
        sum_e+=e
    memo[v] = sum_e
    return memo[v]
    
def dfs(v,p,memo,N,G,sum):
    ans = INF
    s = sum
    for vv,c in G[v]:
        if vv==p:
            s+=c
    sum_e = s
    max_e = s
    for vv,c in G[v]:
        if vv==p:
            continue
        e = c+dp(vv,v,memo,N,G)
        sum_e += e
        if max_e < e:
            max_e = e
        ans = min(ans,dfs(vv,v,memo,N,G,s))
    if sum_e==max_e:
        return INF
    
    ans=min(ans,(sum_e-max_e)*2+max_e)
    print(ans)
    return ans
def main():
    N = int(myin())
    G=[[] for i in range(N)]
    for i in range(N-1):
        a,b,c = myin_sp_i()
        a-=1
        b-=1
        G[a].append((b,c))
        G[b].append((a,c))
    memo = [INF for i in range(N)]
    sum = dp(0,-1,memo,N,G)
    print(dfs(0,-1,memo,N,G,0))
if __name__ == "__main__":
    main()