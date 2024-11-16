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
    from collections import defaultdict
    from heapq import heapify,heappop,heappush
    N,M = myin_sp_i()
    P = sorted(myin_sp_i())
    L = myin_sp_i()
    D = myin_sp_i()
    coupon = defaultdict(list)
    for i in range(M):
        l = L[i]
        d = D[i]
        ng = -1
        ok = N
        while ok-ng>1:
            m = ng+(ok-ng)//2
            if l<=P[m]:
                ok = m
            else:
                ng = m
        if ok<N:
            ll = P[ok]
            coupon[ll].append(d)
    pq = []
    heapify(pq)
    ans = 0
    for p in P:
        for v in coupon[p]:
            heappush(pq,-v)
        coupon[p] = []
        if not pq:
            ans += p
        else:
            ans+= p + heappop(pq)
    print(ans)
    
    

if __name__ == "__main__":
    main()