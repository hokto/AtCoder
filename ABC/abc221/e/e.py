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
    inv_2 = pow(2,MOD-2,MOD)
    N = int(myin())
    A = myin_sp_i()
    B = list(set(sorted(A)))
    change = {}
    for i,b in enumerate(B):
        change[b] = i
    M = len(change)
    X = [] #座圧
    for a in A:
        X.append(change[a])
    ft = FenwickTree(M)
    for i in range(N):
        ft.add(X[i],pow(2,i,MOD))
    ans = 0
    for i in range(N):
        ft.add(X[i],-pow(2,i,MOD)) # 現在の分を引いておく
        ans += ft.sum(X[i],M)*pow(inv_2,i+1,MOD)
        ans%=MOD
    print(ans)

if __name__ == "__main__":
    main()