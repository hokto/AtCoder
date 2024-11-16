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
    dist = [[-1]*N for _ in range(N)]
    def bfs(r):
        deq = deque()
        deq.append((0,r))
        while deq:
            c,v = deq.popleft()
            if dist[r][v]!=-1: continue
            dist[r][v]=c
            for vv in G[v]:
                if dist[r][vv]!=-1: continue
                deq.append((c+1,vv))
            
    for i in range(M):
        u,v = myin_sp_i()
        u-=1
        v-=1
        G[u].append(v)
        G[v].append(u)
    for i in range(N):
        bfs(i)
    K = int(myin())
    color = [1]*N
    P=[]
    for k in range(K):
        p,d = myin_sp_i()
        p-=1
        for v in range(N):
            if dist[p][v]<d:
                color[v]=0
        P.append((p,d))
    ans = True
    for k in range(K):
        p,d = P[k]
        f = False
        for v in range(N):
            if dist[p][v]==d and color[v]==1:
                f = True
                break
        if not f:
            ans = False
    if ans:
        print("Yes")
        print("".join(map(str,color)))
    else:
        print("No")

if __name__ == "__main__":
    main()