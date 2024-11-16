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
    pq1 = list(range(N))
    heapify(pq1)
    pq2 = []
    heapify(pq2)
    ans = [0]*N
    for _ in range(M):
        t,w,s = myin_sp_i()
        while pq2 and pq2[0][0]<=t:
            _,idx = heappop(pq2)
            heappush(pq1,idx)
        if pq1:
            i = heappop(pq1)
            ans[i]+=w
            heappush(pq2,(t+s,i))
    print(*ans,sep="\n")
if __name__ == "__main__":
    main()