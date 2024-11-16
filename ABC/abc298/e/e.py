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
    MOD = 998244353
    N,A,B,P,Q = myin_sp_i()
    inv_PQ = pow(P*Q,MOD-2,MOD)
    dp = [[0]*(N+1) for _ in range(N+1)] # dp[i][j]:=高橋くんはi,青木くんはjにいる時の確率
    dp[A][B]=1
    for i in range(A,N):
        for j in range(B,N):
            for p in range(1,P+1):
                for q in range(1,Q+1):
                    ni = min(i+p,N)
                    nj = min(j+q,N)
                    dp[ni][nj]+=dp[i][j]*inv_PQ
                    dp[ni][nj]%=MOD
    ans = 0
    for j in range(B,N+1):
        ans+=dp[N][j]
        ans%=MOD
    print(ans)

if __name__ == "__main__":
    main()