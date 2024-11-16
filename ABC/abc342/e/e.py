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
    G = [[] for i in range(N)]
    for j in range(M):
        l,d,k,c,a,b = myin_sp_i()
        a-=1
        b-=1
        G[b].append([a,(l,d,k,c)])
    from heapq import heapify,heappop,heappush
    # (到着時刻，番号) -> 到着時刻が大きければ大きいほどいい
    INF = 10**20
    pq = [(-INF,N-1)]
    
    T = [-1]*N
    heapify(pq)
    while pq:
        t,v = heappop(pq)
        t*=-1
        if T[v]>=t:
            continue
        T[v] = t
        for vv,(l,d,k,c) in G[v]:
            # 辿り着けない
            if l+c>t:
                continue
            kk = 0
            if l+(k-1)*d+c<=t:
                kk = k-1
            else:
                kk = (t-l-c)//d
            if T[vv]<l+kk*d:
                #T[vv] = l+kk*d
                heappush(pq,(-(l+kk*d),vv))
    for i in range(N-1):
        if T[i]<0:
            print("Unreachable")
        else:
            print(T[i])
        

if __name__ == "__main__":
    main()