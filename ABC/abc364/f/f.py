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

def add(l,r):
    return (l[0]+r[0],l[1]+r[1])

def update(f,s):
    return (f*s[1],s[1])

def composition(f,g):
    return min(f,g)
def main():
    from atcoder.lazysegtree import LazySegTree
    N,Q = myin_sp_i()
    edges = []
    for q in range(Q):
        l,r,c = myin_sp_i()
        l-=1
        r-=1
        edges.append((c,l,r))
    edges.sort(lambda x:x[0])
    lst = LazySegTree(add,(1,1),update,composition,1,N-1)
    #lst.apply(0,N-1,0)
    ans = 0
    for c,l,r in edges:
        ans+=c
        cnt,_ = lst.prod(l,r)
        print(cnt)
        print([lst.get(i) for i in range(N-1)])
        ans+=cnt*c
        lst.apply(l,r,0)
    print(ans)
if __name__ == "__main__":
    main()