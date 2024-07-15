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

def main():
    N,M = myin_sp_i()
    A = myin_sp_i()
    G = [[] for i in range(N)]
    for i in range(M):
        u,v,b = myin_sp_i()
        u-=1
        v-=1
        G[u].append([v,b+A[v]])
        G[v].append([u,b+A[u]])
    INF = 10**15
    dist = [INF for i in range(N)]
    dist[0]=A[0]
    from heapq import heapify,heappop,heappush
    pq = [(A[0],0)]
    heapify(pq)
    while len(pq)>0:
        cost,v = heappop(pq)
        if dist[v]<cost:
            continue
        for vv,c in G[v]:
            if dist[vv]>dist[v]+c:
                dist[vv]=dist[v]+c
                heappush(pq,(dist[vv],vv))
    print(*dist[1:])
    

if __name__ == "__main__":
    main()