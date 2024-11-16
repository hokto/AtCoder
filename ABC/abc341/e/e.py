from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

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
def main():
    # 10100 -> [1,1,1,0]
    # [1,3]? -> sum([1,3])=3->True
    # [1,5]? -> sum([1,5])=3!=4->False
    # [1,4]! -> rev([1,4])=[1,1,1,1] rev:=端の0,1を反転する(ただし，端が端っこなら)
    from atcoder.segtree import SegTree
    N,Q = myin_sp_i()
    S = myin()
    st = SegTree(op,0,N-1)
    for i in range(N-1):
        if S[i]!=S[i+1]:
            st.set(i,1)
        else:
            st.set(i,0)
    for q in range(Q):
        t,l,r = myin_sp_i()
        l-=1
        r-=1
        if(t==1):
            if l-1>=0:
                st.set(l-1,(st.get(l-1)+1)%2)
            if r<N-1:
                st.set(r,(st.get(r)+1)%2)
        else:
            if st.prod(l,r)==r-l:
                print("Yes")
            else:
                print("No")
            
if __name__ == "__main__":
    main()