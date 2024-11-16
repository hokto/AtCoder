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
    INF = 10**18
    N,A,B,C = myin_sp_i()
    D = []
    for i in range(N):
        D.append(myin_sp_i())
    def dijkstra(r,type):
        pq = [(0,r)]
        heapify(pq)
        dist = [INF]*N
        while pq:
            c,v = heappop(pq)
            if dist[v]<=c: continue
            dist[v] = c
            for vv in range(N):
                if vv==v: continue
                cost = 0
                if type==0:
                    cost=D[v][vv]*A
                else:
                    cost=D[v][vv]*B+C
                if dist[vv]>dist[v]+cost:
                    heappush(pq,(dist[v]+cost,vv))
        return dist
    dist1 = dijkstra(0,type=0)
    dist2 = dijkstra(N-1,type=1)
    ans = INF
    for i in range(N):
        ans = min(ans,dist1[i]+dist2[i])
    print(ans)

if __name__ == "__main__":
    main()