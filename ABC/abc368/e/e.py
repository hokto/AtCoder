from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import math
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
    N,M,X1 = myin_sp_i()
    query = []
    G = [[] for i in range(N)]
    for i in range(M):
        a,b,s,t = myin_sp_i()
        a-=1
        b-=1
        query.append((a,b,s,t))
        G[a].append((b,s,t,i))
    from heapq import heapify,heappop,heappush
    INF = 10**10
    X = [INF]*M
    pq = [(query[0][2]+X1,X1,query[0][1],0)]
    heapify(pq)
    while pq:
        tx,x,p,i = heappop(pq)
        if X[p]<x:
            continue
        X[p]=x
        for v,s,t,j in G[p]:
            if 
        
if __name__ == "__main__":
    main()