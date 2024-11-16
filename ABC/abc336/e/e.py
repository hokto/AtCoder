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
    # dp[i][j][k][f]:=i桁目までにおいて，桁和jに対してmod j=kとなるものの個数(f=0ならN未満，f=1ならNちょうど)
    # ->s=1~9*14で固定し，kをmod sにしたもので考える
    MAX = 9*14
    N = myin()
    L = len(N)
    ans = 0
    for s in range(1,MAX+1):
        dp = [[[[0]*2 for _ in range(s)]for _ in range(s+1)] for i in range(L+1)]
        dp[0][0][0][1] = 1
        for i in range(L):
            d = int(N[i])
            for dd in range(10):
                for j in range(s-dd+1):
                    for k in range(s):
                        for f in range(2):
                            if(f==1 and dd>d): continue
                            dp[i+1][j+dd][(10*k+dd)%s][(f==1 and d==dd)]+=dp[i][j][k][f]
        ans+=dp[L][s][0][0]+dp[L][s][0][1]
    print(ans)
if __name__ == "__main__":
    main()