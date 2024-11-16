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
    import math
    N = int(myin())
    P = myin_sp_i()
    INF = 10**10
    dp = [-INF for i in range(N+1)]
    for i in range(N):
        for j in range(i+1+1)[::-1]:
            if j>=1:
                if j==1:
                    dp[j] = max(dp[j],P[i])
                else:
                    dp[j]=max(dp[j],0.9*dp[j-1]+P[i])
    #print(dp)
    ans = -INF
    bunsi = 1.0
    for k in range(1,N+1):
        res = dp[k]/bunsi-1200.0/math.sqrt(k)
        ans = max(ans,res)
        bunsi=0.9*bunsi+1.0
    print(round(ans,7))

if __name__ == "__main__":
    main()