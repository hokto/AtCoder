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
    INF = 10**15
    dp = [-1]*(M+1)
    dp[0] = 0.0
    for i in range(N):
        C,P,*S = myin_sp_i()
        for j in range(M+1):
            if dp[j]<0: continue
            for s in S:
                k = min(j+s,M)
                dp[k]=max(dp[k],0.0)+dp[j]/N+C/P
    print(dp[-1])

if __name__ == "__main__":
    main()