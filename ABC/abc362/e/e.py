from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 7)
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

MOD = 998244353
memo = {}
def dp(i,j,k,N,A):
    if j==1:
        return 1
    if (i,j,k) in memo:
        return memo[(i,j,k)]
    res = 0
    for ii in range(i+1,N):
        if A[ii]-A[i]==k:
            res=(res+dp(ii,j-1,k,N,A))%MOD
    memo[(i,j,k)]=res
    return res
def main():
    N=int(myin())
    A = myin_sp_i()
    ans = [N]
    for j in range(2,N+1):
        res=0
        for i in range(N):
            for ii in range(i+1,N):
                res=(res+dp(ii,j-1,A[ii]-A[i],N,A))%MOD
        ans.append(res)
    print(*ans)
if __name__ == "__main__":
    main()