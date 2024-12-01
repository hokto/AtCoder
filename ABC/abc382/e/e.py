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
    P = myin_sp_i()
    dp = [[[0.0]*(X+1) for _ in range(2)]for _ in range(N+1)]
    for i in range(N):
        for j in range(X+1):
            dp[i+1][0][j]+=(dp[i][0][j])*(100-P[i])/100
            dp[i+1][1][j]+=(dp[i][1][j])*P[i]/100
            dp[i+1][1][min(X,j+1)]+=(dp[i][0][j]+1+dp[i][1][j])*P[i]/100
            #dp[i+1][j]+=(dp[i][j]+1)*(100.0-P[i])/100.0
            #dp[i+1][min(X,j+1)]+=(dp[i][j]+1)*P[i]/100.0
    print(dp)
    print(dp[-1][-1])

if __name__ == "__main__":
    main()