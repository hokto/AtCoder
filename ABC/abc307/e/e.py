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
    N,M = myin_sp_i()
    dp = [[0]*2 for i in range(N)]
    dp[0][1] = M
    for i in range(N-1):
        dp[i+1][0]=(dp[i][0]*(M-2)+dp[i][1]*(M-1))%MOD
        dp[i+1][1] = dp[i][0]
    print(dp[-1][0])
if __name__ == "__main__":
    main()