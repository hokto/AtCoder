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
    import copy
    import bisect
    N,M,K = myin_sp_i()
    A = myin_sp_i()
    if N==M:
        print(*([0]*N))
        return
    B = copy.deepcopy(A)
    B.sort()
    accum = [0]*(N+1)
    for i in range(N):
        accum[i+1]=accum[i]+B[i]
    KK = K-sum(A)
    ans = []
    for i in range(N):
        ng = -1
        ok = KK+1
        while ok-ng>1:
            m = ng+(ok-ng)//2
            idx = bisect.bisect_right(B,A[i]+m)
            over_cnt = N-idx # A[i]+mをすでに超えている人数
            if over_cnt>=M:
                ng = m
                continue
            inc = 0
            if N-1-M>=0 and B[N-1-M]<A[i]:
                inc+=1
            res = accum[idx]-accum[N-M-inc]-A[i]*inc
            if (A[i]+m+1)*(M-over_cnt)-res>KK-m:
                ok = m
            else:
                ng = m
        if ok>KK: ans.append(-1)
        else: ans.append(ok)
    print(*ans)

if __name__ == "__main__":
    main()