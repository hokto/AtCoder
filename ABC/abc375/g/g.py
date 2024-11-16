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
    from heapq import heapify,heappop,heappush
    N,M = myin_sp_i()
    G = [[] for _ in range(N)]
    E = []
    for i in range(M):
        a,b,c = myin_sp_i()
        a-=1
        b-=1
        G[a].append((b,c))
        G[b].append((a,c))
        E.append((a,b,c))
    INF = 10**15+100
    def dijkstra(r):
        dist = [INF]*N
        pq = [(0,r)]
        heapify(pq)
        while pq:
            c,v = heappop(pq)
            if dist[v]<=c: continue
            dist[v]=c
            for vv,cc in G[v]:
                if dist[vv]<=c+cc: continue
                heappush(pq,(c+cc,vv))
        return dist
    dist1 = dijkstra(0)
    dist2 = dijkstra(N-1)
    ans = dist1[-1]
    for a,b,c in E:
        v = a
        res = INF
        for vv,cc in G[v]:
            if vv!=b: res=min(res,dist1[v]+dist2[vv]+cc)
        print(res)
        if ans==res:
            print("No")
        else:
            print("Yes")
        

if __name__ == "__main__":
    main()