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
    N = int(myin())
    P = []
    R = set()
    C = set()
    for i in range(N):
        r,c,x = myin_sp_i()
        R.add(r)
        C.add(c)
        P.append((r,c,x))
    R = sorted(list(R))
    C = sorted(list(C))
    MR = len(R)
    MC = len(C)
    chr_row_idx = {}
    chr_col_idx = {}
    for i in range(MR):
        chr_row_idx[R[i]]=i
    for i in range(MC):
        chr_col_idx[C[i]]=i
    rows = [0]*MR
    cols = [0]*MC
    col_pos = [[] for _ in range(MC)]
    for r,c,x in P:
        r = chr_row_idx[r]
        c = chr_col_idx[c]
        rows[r]+=x
        cols[c]+=x
        col_pos[c].append((r,x))
    rows_st = SegTree(max,0,rows)
    ans = 0
    for c in range(MC):
        res = cols[c]
        for r,x in col_pos[c]:
            rows_st.set(r,rows_st.get(r)-x)
        res += rows_st.all_prod()
        ans = max(ans,res)
        for r,x in col_pos[c]:
            rows_st.set(r,rows_st.get(r)+x)
    print(ans)
    

if __name__ == "__main__":
    main()