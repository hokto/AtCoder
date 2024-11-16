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
    T = int(myin())
    for t in range(T):
        N,K = myin_sp_i()
        A = myin_sp_i()
        B = myin_sp_i()
        AB = []
        for i in range(N):
            AB.append((A[i],B[i],i))
        AB.sort()
        sum_b = 0
        pq = []
        heapify(pq)
        for i in range(K):
            sum_b+=AB[i][1]
            heappush(pq,-AB[i][1])
        ans = AB[K-1][0]*sum_b
        for k in range(K,N):
            sum_b+=AB[k][1]
            sum_b+=heappop(pq)
            heappush(pq,-AB[k][1])
            ans=min(ans,AB[k][0]*sum_b)
        print(ans)

if __name__ == "__main__":
    main()