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
    X,Y,Z = myin_sp_i()
    S = myin()
    N = len(S)
    INF = 10**20
    dp = [[INF]*2 for i in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        if S[i]=="A":
            dp[i+1][1] = min(dp[i][1]+X,dp[i][0]+Z+min(X,Y))
            dp[i+1][0] = min(dp[i][0]+Y,dp[i][1]+min(X,Y)+Z)
        else:
            dp[i+1][0] = min(dp[i][0]+X,dp[i][1]+Z+min(X,Y))
            dp[i+1][1] = min(dp[i][1]+Y,dp[i][0]+min(X,Y)+Z)
    print(min(dp[-1]))

if __name__ == "__main__":
    main()