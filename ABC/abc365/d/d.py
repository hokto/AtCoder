from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

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
    S = myin()
    INF = N+10
    dp = [[-INF]*3 for i in range(N+1)] # 0:R,1:P,2:S
    dp[0][0]=dp[0][1]=dp[0][2]=0
    RPS = {"R":0,"P":1,"S":2}
    for i in range(N):
        for j in range(3):
            # 勝ちの場合
            k = (RPS[S[i]]+1)%3
            if k!=j: dp[i+1][k]=max(dp[i+1][k],dp[i][j]+1)
            # あいこの場合
            k = RPS[S[i]]
            if k!=j: dp[i+1][k]=max(dp[i+1][k],dp[i][j])
    print(max(dp[-1]))

if __name__ == "__main__":
    main()