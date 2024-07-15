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
    from heapq import heapify,heappop,heappush
    N,M,K = myin_sp_i()
    G = [[] for i in range(N)]
    for i in range(M):
        a,b = myin_sp_i()
        a-=1
        b-=1
        G[a].append(b)
        G[b].append(a)
    dist = [-1 for i in range(N)]
    pq = []
    #heapify(pq)
    for k in range(K):
        p,h = myin_sp_i()
        p-=1
        dist[p]=h
        heappush(pq,(-h,p))
    while len(pq)>0:
        _,v = heappop(pq)
        for vv in G[v]:
            if dist[vv] < dist[v]-1:
                dist[vv] = dist[v]-1
                heappush(pq,(-dist[vv],vv))
    ans = []
    for i in range(N):
        if dist[i]>=0:
            ans.append(i+1)
    print(len(ans))
    print(*ans)
if __name__ == "__main__":
    main()