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
    N,X = myin_sp_i()
    T = myin_sp_i()
    MOD = 998244353
    inv_N = pow(N,MOD-2,MOD)
    dp = [0 for i in range(X+1)]
    dp[0] = 1
    ans = 0
    if X<T[0]:
        ans=inv_N
    for j in range(1,X+1):
        for i in range(N):
            if j-T[i]>=0:
                dp[j]+=dp[j-T[i]]
        dp[j]*=inv_N
        dp[j]%=MOD
        if j+T[0]>X:
            ans+=dp[j]*inv_N
            ans%=MOD
    print(ans)
        

if __name__ == "__main__":
    main()