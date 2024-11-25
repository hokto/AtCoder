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
    N = myin()
    N = N
    L = len(N)
    MAX = 10**7
    # dp[i][j]:=下の桁から見てi番目において，j==1の場合は次の桁で1枚多く支払う，j==0の時はピッタリ支払う場合の最小枚数
    dp = [[MAX for _ in range(2)]for _ in range(L+1)]
    dp[0][0] = 0
    for i in range(L):
        for j in range(2):
            if j==1 and int(N[L-1-i])==9:
                dp[i+1][1] = min(dp[i+1][1],dp[i][1])
            else:
                c = 0
                if j==1: c+=1
                dp[i+1][0] = min(dp[i+1][0],dp[i][j]+c+int(N[L-1-i]))
                dp[i+1][1] = min(dp[i+1][1],dp[i][j]+10-int(N[L-1-i])-c)
    ans = min(dp[-1][0],dp[-1][1]+1)
    print(ans)
if __name__ == "__main__":
    main()