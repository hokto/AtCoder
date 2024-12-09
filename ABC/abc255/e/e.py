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
    N,M = myin_sp_i()
    S = myin_sp_i()
    X = myin_sp_i()
    idx = {}
    for i,x in enumerate(X):
        idx[x] = i
    dp = [[0]*(M+1) for i in range(N)] # dp[i][j]:=i番目までで良い数列を作り，X_jを選択した時のラッキーナンバーの最大個数(ただし，j=0の時はラッキーナンバー以外を選択)
    for i in range(1,M+1):
        dp[0][i] = 1
    for i in range(N-1):
        s = S[i]
        dp[i+1][0] = max(dp[i])
        for j in range(M):
            dp[i+1][j+1] = max(dp[i][j+1],dp[i][0])
            if s-X[j] in idx:
                dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][idx[s-X[j]]+1]+1)
    print(dp)
    print(max(dp[-1]))
if __name__ == "__main__":
    main()