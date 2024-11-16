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
    N = int(myin())
    A = myin_sp_i()
    INF = 10**20
    dp = [[-INF]*2 for i in range(N+1)] # dp[i][j]:=i番目まででj(mod 2)回の倒す行動をした時の経験値の最大値
    dp[0][0]=0
    for i in range(N):
        dp[i+1][0] = max(dp[i][0],dp[i][1]+A[i]*2)
        dp[i+1][1]=max(dp[i][1],dp[i][0]+A[i])
    #print(dp)
    print(max(dp[-1]))
if __name__ == "__main__":
    main()