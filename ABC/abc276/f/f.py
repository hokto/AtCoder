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
    from atcoder.fenwicktree import FenwickTree
    MOD = 998244353
    N = int(myin())
    A = myin_sp_i()
    MAX = max(A)
    ft1 = FenwickTree(MAX+1) # 個数管理
    ft2 = FenwickTree(MAX+1) # Aの値管理
    ans = 0
    for i in range(N):
        ans+=A[i] # i番目のものだけ引いたとき
        ans+=ft1.sum(0,A[i]+1)*A[i]*2 # A[i]以下のものを引いた場合
        ans+=ft2.sum(A[i]+1,MAX+1)*2 # A[i]より大きいものを引いた場合
        ans%=MOD
        ft1.add(A[i],1)
        ft2.add(A[i],A[i])
        print(ans*pow((i+1)*(i+1),MOD-2,MOD)%MOD)

if __name__ == "__main__":
    main()