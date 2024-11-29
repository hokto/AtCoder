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
    from collections import deque
    N,M = myin_sp_i()
    G = [[] for _ in range(N)]
    INF = N*N+100
    def bfs(r,dist):
        dist[r] = 0
        deq = deque()
        deq.append(r)
        while deq:
            v = deq.popleft()
            for vv in G[v]:
                if dist[vv]!=INF: continue
                dist[vv] = dist[v]+1
                deq.append(vv)
    for i in range(M):
        a,b = myin_sp_i()
        a-=1
        b-=1
        G[a].append(b)
        G[b].append(a)
    K = int(myin())
    CC = myin_sp_i()
    C = [c-1 for c in CC]
    stone_cnt = [[INF]*N for _ in range(K)]
    for k in range(K):
        bfs(C[k],stone_cnt[k])
    #print(stone_cnt)
    dp = [[INF]*K for _ in range(1<<K)] # dp[S][k]:=bit集合Sに対し，kを端とした時の並べ方の石の最小個数(なければINF)
    for k in range(K):
        dp[(1<<k)][k] = 1
    for s in range(1<<K):
        for k in range(K):
            if s&(1<<k):
                for j in range(K):
                    if (s&(1<<j))==0:
                        dp[s|(1<<j)][j]=min(dp[s|(1<<j)][j],dp[s][k]+stone_cnt[k][C[j]])
    if min(dp[-1])>=INF:
        print(-1)
    else:
        print(min(dp[-1]))

if __name__ == "__main__":
    main()