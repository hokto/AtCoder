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
    from bisect import bisect_right
    N = int(myin())
    A = myin_sp_i()
    AA = sorted(A)
    accum = [0]*(N+1)
    for i in range(N):
        accum[i+1]=AA[i]+accum[i]
    ans = []
    for i in range(N):
        idx = bisect_right(AA,A[i])
        ans.append(accum[-1]-accum[idx])
    print(*ans)

if __name__ == "__main__":
    main()