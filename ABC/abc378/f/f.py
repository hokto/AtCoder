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
    N = int(myin())
    G = [[] for _ in range(N)]
    for i in range(N-1):
        u,v = myin_sp_i()
        u-=1
        v-=1
        G[u].append(v)
        G[v].append(u)
    seen = [False]*N
    def dfs(v):
        if seen[v]: return 0
        if len(G[v])==2:
            return 1
        elif len(G[v])!=3:
            return 0
        seen[v] = True
        res = 0
        for vv in G[v]:
            res+=dfs(vv)
        return res
    ans = 0
    for i in range(N):
        if len(G[i])==3:
            res = dfs(i)
            ans+=(res-1)*res//2
    print(ans)

if __name__ == "__main__":
    main()