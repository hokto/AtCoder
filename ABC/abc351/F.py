
from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
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
    N = int(myin())
    A = myin_sp_i()
    AA = [(a,i) for i,a in enumerate(A)]
    AA.sort(reverse=True)
    op = lambda x,y: (x[0]+y[0],x[1]+y[1])
    e=(0,0)
    st = SegTree(op,e,N)
    ans = 0
    for a,i in AA:
        st.set(i,(a,1))
        s,cnt = st.prod(i+1,N)
        ans+=s-cnt*a
    print(ans)
if __name__ == "__main__":
    main()