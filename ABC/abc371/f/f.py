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

class S:
    def __init__(self,value,size) -> None:
        self.value = value
        self.size = size
def main():
    from atcoder.lazysegtree import LazySegTree
    ID = 2*10**9
    op =lambda x,y: S(x.value+y.value,x.size+y.size)
    e = S(0,0)
    def mapping(f,x):
        if f!=ID:
            x.value = x.size*f
        return X
    def composition(f,g):
        if f==ID:
            return g
        return f
    id = ID
    N = int(myin())
    X = myin_sp_i()
    Q = int(myin())
    B = X[0]
    lst = LazySegTree(op,e,mapping,composition,id,N-1)
    for i in range(N-1):
        lst.set(i,S(X[i+1]-X[i],1))
    for q in range(Q):
        t,g = myin_sp_i()
        t-=1
        ok = -1
        ng = N
        while ng-ok>1:
            m = ok+(ng-ok)//2

if __name__ == "__main__":
    main()