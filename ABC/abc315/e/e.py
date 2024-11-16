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
    G = [[] for i in range(N)]
    for i in range(N):
        C,*P = myin_sp_i()
        for p in P:
            G[i].append(p-1)
    ans = []
    visited = [False]*N
    def dfs(v):
        if visited[v]: return
        visited[v]=True
        for vv in G[v]:
            dfs(vv)
        ans.append(v+1)
    dfs(0)
    print(*ans[:-1])

if __name__ == "__main__":
    main()