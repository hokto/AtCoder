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
    N = int(myin())
    # dp[i]:=iから始めてNに一致する確率
    # dp[i]=1/6(dp[i]+dp[2i]+dp[3i]+dp[4i]+dp[5i]+dp[6i])
    # 5/6dp[i]=1/6(dp[2i]+dp[3i]+dp[4i]+dp[5i]+dp[6i])
    # dp[i]=1/5(dp[2i]+dp[3i]+dp[4i]+dp[5i]+dp[6i])
    memo = {}
    inv_5 = pow(5,MOD-2,MOD)
    def dp(i):
        if N<i:
            return 0
        if N==i:
            return 1
        if i in memo:
            return memo[i]
        res = (dp(2*i)+dp(3*i)+dp(4*i)+dp(5*i)+dp(6*i))*inv_5%MOD
        memo[i] = res
        return memo[i]
    print(dp(1))

if __name__ == "__main__":
    main()