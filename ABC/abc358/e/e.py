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

MOD = 998244353
fac = []
finv = []
inv = []
def combinit(N):
    global fac,finv,inv
    fac = [0 for i in range(N)]
    finv = [0 for i in range(N)]
    inv = [0 for i in range(N)]
    fac[0]=fac[1]=1
    finv[0]=finv[1]=1
    inv[1]=1
    for i in range(2,N):
        fac[i] = fac[i-1]*i % MOD
        inv[i] = MOD - inv[MOD%i]*(MOD//i)%MOD
        finv[i] = finv[i-1]*inv[i]%MOD
def comb(n,r):
    if(n<r): return 0
    if(n<0 or r<0): return 0
    return fac[n]*finv[r]*finv[n-r]%MOD
def main():
    K = int(myin())
    C = myin_sp_i()
    combinit(K+1)
    dp = [[0 for j in range(K+1)] for i in range(26+1)] 
    dp[0][0] = 1
    for i in range(26):
        for j in range(K+1):
            for k in range(max(j-C[i],0),K+1):
                dp[i+1][j]=(dp[i+1][j]+dp[i][k]*comb(j,j-k))%MOD
    print(sum(dp[-1][1:])%MOD)

if __name__ == "__main__":
    main()