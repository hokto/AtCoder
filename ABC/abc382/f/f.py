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
    H,W,N = myin_sp_i()
    Bar = []
    for i in range(N):
        r,c,l, = myin_sp_i()
        r-=1
        c-=1
        Bar.append((r,c,l,i))
    Bar.sort(reverse=True)
    ID = -1
    def mapping(f,x):
        if f==ID:
            return x
        return f
    def composition(f,g):
        if f==ID:
            return g
        return f
    lst = LazySegTree(min,H+1,mapping,composition,ID,W)
    ans = [H+1]*N
    for _,c,l,i in Bar:
        ans[i] = lst.prod(c,c+l)-1
        lst.apply(c,c+l,ans[i])
    print(*ans,sep="\n")


if __name__ == "__main__":
    main()