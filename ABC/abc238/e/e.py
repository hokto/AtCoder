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
    from atcoder.dsu import DSU
    N,Q = myin_sp_i()
    dsu = DSU(N+1)
    for q in range(Q):
        l,r = myin_sp_i()
        l-=1
        dsu.merge(l,r)
    if dsu.same(0,N):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()