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
    N,M = myin_sp_i()
    G = [[] for i in range(N)]
    for i in range(M):
        a,b,c = myin_sp_i()
        a-=1
        b-=1
        G[a].append((b,c))
        G[b].append((a,c))
    visited = [False]*N
    def dfs(v):
        ans = 0
        for vv,c in G[v]:
            if visited[vv]: continue
            visited[vv] = True
            res = dfs(vv)+c
            ans = max(ans,res)
            visited[vv]=False
        return ans
    ans = 0
    for i in range(N):
        visited[i]=True
        ans = max(ans,dfs(i))
        visited[i]=False
    print(ans)

if __name__ == "__main__":
    main()