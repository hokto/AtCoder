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
    from atcoder.lazysegtree import LazySegTree
    N = int(myin())
    F = []
    for i in range(N):
        F.append(myin_sp_i())
    Q = int(myin())
    X = myin_sp_i()
    Y = [(x,i) for i,x in enumerate(X)]
    Y.sort()
    Z = []
    indices = []
    for i in range(Q):
        Z.append(Y[i][0])
        indices.append(Y[i][1])
    id = 10**10
    e = 0
    def mapping(f,x):
        if f==id:
            return x
        return f

    def composition(f,g):
        if f==id:
            return g
        return f
    lst = LazySegTree(max,e,mapping,composition,id,Z)
    res = []
    for i in range(Q):
        res.append(lst.get(i))
    add = 0
    for a,t in F:
        if t==1:
            add += a
        elif t==2:
            ok = -1
            ng = Q
            while ng-ok>1:
                m = ok+(ng-ok)//2
                if lst.get(m)+add<a:
                    ok = m
                else:
                    ng = m
            lst.apply(0,ok+1,a-add)
        else:
            ng = -1
            ok = Q
            while ok-ng>1:
                m = ng+(ok-ng)//2
                if lst.get(m)+add>a:
                    ok = m
                else:
                    ng = m
            lst.apply(ok,Q,a-add)
    ans = [0]*Q
    for i in range(Q):
        idx = indices[i]
        ans[idx] = lst.get(i)+add
    print(*ans,sep="\n")

if __name__ == "__main__":
    main()