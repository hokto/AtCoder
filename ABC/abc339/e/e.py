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
    from atcoder.segtree import SegTree
    N,D = myin_sp_i()
    A = myin_sp_i()
    MAX = max(A)
    st = SegTree(max,0,MAX+1)
    for a in A:
        l = max(1,a-D)
        r = min(MAX,a+D)
        val = st.prod(l,r+1)
        st.set(a,val+1)
    print(st.all_prod())

if __name__ == "__main__":
    main()