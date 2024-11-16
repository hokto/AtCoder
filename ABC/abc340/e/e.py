from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def op(l,r):
    return l+r
def mapping(a,f):
    return a+f

def composition(f,g):
    return f+g
def main():
    from atcoder.lazysegtree import LazySegTree
    N,M = myin_sp_i()
    A = myin_sp_i()
    B = myin_sp_i()
    e = 0
    id = 0
    lst = LazySegTree(op,e,mapping,composition,id,A)
    for b in B:
        num = lst.get(b)
        lst.set(b,0)
        x = num//N
        y = num%N
        lst.apply(0,N,x)
        if y>0:
            if b+1+y<N:
                lst.apply(b+1,b+y+1,1)
            else:
                lst.apply(b+1,N,1)
                lst.apply(0,(b+1+y)%N,1)
    ans = [0]*N
    for i in range(N):
        ans[i] = lst.get(i)
    print(*ans)
if __name__ == "__main__":
    main()