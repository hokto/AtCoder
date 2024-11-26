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
    MOD = 10**9+7
    L = myin()
    N = len(L)
    dp = [[[0]*2 for _ in range(2)]for _ in range(N+1)]
    dp[0][1][0] = 1
    for i in range(N):
        for k in range(2):
            dp[i+1][0][k]+=(dp[i][0][0]+dp[i][0][1])*(k+1)
            if k<int(L[i]):
                dp[i+1][0][k]+=(dp[i][1][0]+dp[i][1][1])*(k+1)
            if int(L[i])==k:
                dp[i+1][1][k] += (dp[i][1][0]+dp[i][1][1])*(k+1)
            dp[i+1][1][k]%=MOD
            dp[i+1][0][k]%=MOD
    #print(dp)
    print((dp[-1][0][0]+dp[-1][0][1]+dp[-1][1][0]+dp[-1][1][1])%MOD)
            

if __name__ == "__main__":
    main()