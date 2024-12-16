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
    # N-1回の移動でどのパターンも網羅できるため，それ以上みる必要はない
    # k回目の移動で新しく増えるパターンは，k個の空き部屋ができて，そのk人がN-k個の部屋のいずれに移動する方法
    # k個の空き部屋ができるパターンはnCk,k人がN-k個の部屋に移動する方法は，1人もその部屋に移動しない方法も考慮してN-kHk
    N,K = myin_sp_i()
    MOD = 10**9+7
    fact = [1]*(N+1)
    fact_inv = [1]*(N+1)
    inv = [1]*(N+1)
    for i in range(2,N+1):
        fact[i] = fact[i-1]*i % MOD
        inv[i] = -inv[MOD%i] * (MOD//i) % MOD
        fact_inv[i] = fact_inv[i-1] * inv[i] % MOD
    
    def C(n,k):
        return fact[n]*fact_inv[k]*fact_inv[n-k]%MOD

    def H(n,k):
        return C(n+k-1,k)
    
    ans = 1
    K = min(K,N-1)
    for i in range(1,K+1):
        ans+=C(N,i)*H(N-i,i)%MOD
        ans%=MOD
    print(ans)
if __name__ == "__main__":
    main()