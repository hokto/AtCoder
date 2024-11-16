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
    N,M = myin_sp_i()
    AA = myin_sp_i()
    A = [a%M for a in AA]
    ft = FenwickTree(M)
    s = 0
    for i in range(N):
        s=(s+A[i])%M
        ft.add(s,1)
    ans = 0
    for i in range(N):
        ans += ft.sum(0,M)
        
    
    print(ans)

if __name__ == "__main__":
    main()