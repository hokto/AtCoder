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
    from atcoder.fenwicktree import FenwickTree
    from itertools import accumulate
    N = int(myin())
    A = myin_sp_i()
    M = max(A)
    C = [0 for i in range(M+1)]
    for a in A:
        C[a]+=1
    C_sum = list(accumulate(C))
    ans=0
    for i in range(1,M+1):
        cnt = C[i]
        k = 1
        while i*k<=M:
            ans+=cnt*k*(C_sum[min((k+1)*i-1,M)]-C_sum[k*i-1])
            k+=1
        ans-=cnt*(cnt+1) //2
    print(ans)
if __name__ == "__main__":
    main()