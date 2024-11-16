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
    from atcoder.segtree import SegTree
    from math import sqrt
    def op(x,y):
        return min(x,y)
    def calc_dist(x,y,xx,yy):
        return sqrt((x-xx)**2+(y-yy)**2)
    # dp[i]:=i番目までを配った時に移動した距離の最小値
    # dp[i]=min_{max(0,i-K)<=j<=i-1}{dp[j]+(jからスタート，スタートからj+1に移った時の距離)+(j+1からiまで順に配って行った時の距離)}
    INF = 10**100
    N,K = myin_sp_i()
    Sx,Sy = myin_sp_i()
    X = [None]*(N+1)
    Y = [None]*(N+1)
    X[N]=Sx
    Y[N]=Sy
    for i in range(N):
        X[i],Y[i]=myin_sp_i()
    ans = calc_dist(X[0],Y[0],Sx,Sy)
    d = [0]*N
    for i in range(N):
        dist1 = calc_dist(X[i],Y[i],X[i+1],Y[i+1])
        dist2 = calc_dist(X[i],Y[i],Sx,Sy)+calc_dist(Sx,Sy,X[i+1],Y[i+1])
        ans+=dist1
        d[i]=dist2-dist1
    dp = SegTree(op,INF,N+1)
    dp.set(0,0)
    for i in range(N):
        l = max(i+1-K,0)
        r = i
        prev_dp = dp.prod(l,r+1)
        dp.set(i+1,prev_dp+d[i])
    print(format(ans+dp.get(N),".7f"))
    
if __name__ == "__main__":
    main()