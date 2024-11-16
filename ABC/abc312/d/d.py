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
    S = myin()
    N = len(S)
    MOD = 998244353
    dp = [[0]*(N+1) for i in range(N+1)]
    # dp[i][j]:=i番目までで対応していない'('の個数がjだった時の置き換え方の総数
    # Si='('なら，対応しないものが増えるためj+1,Si=')'なら対応しないものが減るためj-1,'?'なら両方へ遷移する
    dp[0][0] = 1
    for i in range(N):
        for j in range(N+1):
            if S[i]=="(":
                if j<N: dp[i+1][j+1]+=dp[i][j]
            elif S[i]==")":
                if j-1>=0: dp[i+1][j-1]+=dp[i][j]
            else:
                if j<N: dp[i+1][j+1]+=dp[i][j]
                if j-1>=0: dp[i+1][j-1]+=dp[i][j]
    print(dp[-1][0]%MOD)

if __name__ == "__main__":
    main()