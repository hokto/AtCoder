from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
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
    N = int(myin())
    INF = 10**18
    G = [[] for i in range(N)]
    for i in range(N-1):
        a,b,x = myin_sp_i()
        x-=1
        G[i].append((i+1,a))
        G[i].append((x,b))
    pq = [(0,0)]
    ans = [INF]*N
    heapify(pq)
    while pq:
        c,v = heappop(pq)
        if ans[v]<=c:
            continue
        ans[v] = c
        for vv,cost in G[v]:
            if c+cost < ans[vv]:
                heappush(pq,(c+cost,vv))
                
    print(ans[-1])
if __name__ == "__main__":
    main()