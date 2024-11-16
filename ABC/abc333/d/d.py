from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
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

def main():
    N = int(myin())
    T = [[] for i in range(N)]
    for i in range(N-1):
        u,v = myin_sp_i()
        u-=1
        v-=1
        T[u].append(v)
        T[v].append(u)
    dp = [0]*N
    def dfs(v,p):
        nonlocal dp
        dp[v]=1
        for vv in T[v]:
            if vv==p: continue
            dp[v]+=dfs(vv,v)
        return dp[v]
    dfs(0,-1)
    mx = 0
    for v in T[0]:
        mx = max(mx,dp[v])
    print(N-mx)

if __name__ == "__main__":
    main()