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
    H,W= myin_sp_i()
    C = []
    row_cnts = [[0]*26 for i in range(H)]
    col_cnts = [[0]*26 for j in range(W)]
    row_kinds = [0]*H
    col_kinds = [0]*W
    for i in range(H):
        C.append(myin())
        for j in range(W):
            idx = ord(C[i][j])-ord("a")
            if row_cnts[i][idx]==0:
                row_kinds[i]+=1
            row_cnts[i][idx]+=1
            if col_cnts[j][idx]==0:
                col_kinds[j]+=1
            col_cnts[j][idx]+=1
    row_sizes = [W]*H
    col_sizes = [H]*W
    st = []
    for i in range(H):
        if row_kinds[i]==1:
            for k in range(26):
                if row_cnts[i][k]>0:
                    st.append((0,i,k)) # 0でrow
                    break
    for j in range(W):
        if col_kinds[j]==1:
            for k in range(26):
                if col_cnts[j][k]>0:
                    st.append((1,j,k)) # 1でcol
                    break
    operated_row = [False]*H
    operated_col = [False]*W
    ans = H*W
    while st:
        t,x,k = st.pop()
        if t==0:
            i = x
            if operated_row[i]: continue
            operated_row[i] = True
            row_cnts[i][k] = 0
            row_kinds[i] = 0
            row_sizes[i] = 0
            for j in range(W):
                if operated_col[j]: continue
                idx = ord(C[i][j])-ord("a")
                if idx == k:
                    ans -=1
                    col_cnts[j][k]-=1
                    col_sizes[j]-=1
                    if col_cnts[j][k]==0:
                        col_kinds[j]-=1
                        if col_kinds[j]==1 and col_sizes[j]>=2:
                            for y in range(26):
                                if col_cnts[j][y]>0: st.append((1,j,y))
        else:
            j = x
            if operated_col[j]: continue
            operated_col[j] = True
            col_cnts[j][k] = 0
            col_kinds[j] = 0
            col_sizes[j] = 0
            for i in range(H):
                if operated_row[i]: continue
                idx = ord(C[i][j])-ord("a")
                if idx == k:
                    ans-=1
                    row_cnts[i][k]-=1
                    row_sizes[i]-=1
                    if row_cnts[i][k]==0:
                        row_kinds[i]-=1
                        if row_kinds[i]==1 and row_sizes[i]>=2:
                            for y in range(26):
                                if row_cnts[i][y]>0: st.append((0,i,y))
    print(ans)
if __name__ == "__main__":
    main()