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
    N,K = myin_sp_i()
    A = []
    for _ in range(N):
        A.append(myin_sp_i())
    def check(x):
        # x以下のマスがいくつあるか累積する
        # ある区間で，x以下のマスが過半数以上なら任意の区間の中央値の最小が少なくともx以下
        accum = [[0]*(N+1) for _ in range(N+1)]
        for i in range(N):
            for j in range(N):
                c = 1 if A[i][j]<=x else 0
                accum[i+1][j+1]=accum[i+1][j]+accum[i][j+1]-accum[i][j]+c
        for i in range(N-K+1):
            for j in range(N-K+1):
                if accum[i+K][j+K]-accum[i][j+K]-accum[i+K][j]+accum[i][j]>=K*K-(K*K)//2:
                    return True
        return False
    ng = -1
    ok = 10**9+100
    while ok-ng>1:
        m = ng+(ok-ng)//2
        if check(m):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == "__main__":
    main()