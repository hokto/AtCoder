from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
from collections import defaultdict
def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def op(l,r):
    mxl,mx2l,cntl,cnt2l = l
    mxr,mx2r,cntr,cnt2r = r
    mxl_arr = [mxl,mx2l]
    mxl_cnt_arr = [cntl,cnt2l]
    mxr_arr = [mxr,mx2r]
    mxr_cnt_arr = [cntr,cnt2r]
    l_idx = 0
    r_idx = 0
    mx = -1
    mx2 = -1
    cnt = 0
    cnt2 = 0
    while (l_idx!=2 or r_idx!=2) and (mx==-1 or mx2==-1):
        if l_idx==2:
            if mx==-1:
                mx = mxr_arr[r_idx]
                cnt = mxr_cnt_arr[r_idx]
            else:
                mx2 = mxr_arr[r_idx]
                cnt2 = mxr_cnt_arr[r_idx]
            r_idx+=1
        elif r_idx==2:
            if mx==-1:
                mx = mxl_arr[l_idx]
                cnt = mxl_cnt_arr[l_idx]
            else:
                mx2 = mxl_arr[l_idx]
                cnt2 = mxl_cnt_arr[l_idx]
            l_idx+=1
        elif mxl_arr[l_idx]>mxr_arr[r_idx]:
            if mx==-1:
                mx = mxl_arr[l_idx]
                cnt = mxl_cnt_arr[l_idx]
            else:
                mx2 = mxl_arr[l_idx]
                cnt2 = mxl_cnt_arr[l_idx]
            l_idx+=1
        elif mxl_arr[l_idx] < mxr_arr[r_idx]:
            if mx==-1:
                mx = mxr_arr[r_idx]
                cnt = mxr_cnt_arr[r_idx]
            else:
                mx2 = mxr_arr[r_idx]
                cnt2 = mxr_cnt_arr[r_idx]
            r_idx+=1
        else:
            if mx==-1:
                mx = mxl_arr[l_idx]
                cnt = mxl_cnt_arr[l_idx]+mxr_cnt_arr[r_idx]
            else:
                mx2 = mxl_arr[l_idx]
                cnt2 = mxl_cnt_arr[l_idx]+mxr_cnt_arr[r_idx]
            l_idx+=1
            r_idx+=1
    return (mx,mx2,cnt,cnt2)
def main():
    from atcoder.segtree import SegTree
    # (mx,mx2,cnt,cnt2)を持って，cnt2を答えればいい？
    e = (-1,-1,0,0)
    N,Q = myin_sp_i()
    A = myin_sp_i()
    B = [(-1,-1,0,0) for i in range(N)]
    for i in range(N):
        B[i] = (A[i],-1,1,0)
    st = SegTree(op,e,v=B)
    for q in range(Q):
        query = myin_sp_i()
        if query[0]==1:
            _,p,x = query
            p-=1
            st.set(p,(x,-1,1,0))
        else:
            _,l,r = query
            l-=1
            r-=1
            mx,mx2,cnt,cnt2 = st.prod(l,r+1)
            print(cnt2)
if __name__ == "__main__":
    main()