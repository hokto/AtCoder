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
    P = []
    for i in range(N):
        x,y = myin_sp_i()
        P.append((x,y))
    INF = 10**9
    dp = [(INF,N-2)]*N
    dp[0] = (0,0)
    for i in range(N):
        for j in range(i+1,N):
            d1 = dp[j][0]+int(2**(dp[j][1]-1))
            d2 = dp[i][0]+math.sqrt((P[i][0]-P[j][0])**2+(P[i][1]-P[j][1])**2)+int(2**(dp[i][1]+j-i-2))
            if d1>d2:
                dp[j] = (d2-int(2**(dp[i][1]+j-i-2)),dp[i][1]+j-i-1)
    print(dp)
    print(dp[-1][0]+int(2**(dp[-1][1]-1)))

if __name__ == "__main__":
    main()