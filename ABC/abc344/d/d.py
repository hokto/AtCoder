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
    T = myin()
    N = int(myin())
    Ss = []
    A = []
    for i in range(N):
        a,*s = myin_sp_s()
        a = int(a)
        A.append(a)
        Ss.append(s)
    M_T = len(T)
    INF = N+1
    dp = [[INF]*(M_T+1) for i in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(M_T+1):
            dp[i+1][j] = dp[i][j]
        for j in range(A[i]):
            s = Ss[i][j]
            m = len(s)
            for k in reversed(range(M_T-m+1)):
                can = True
                for t in range(m):
                    if T[k+t]!=s[t]:
                        can = False
                if can:
                    dp[i+1][k+m]=min(dp[i+1][k+m],dp[i][k]+1)
    #print(dp[2])
    ans = dp[-1][-1]
    if ans >= INF:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()