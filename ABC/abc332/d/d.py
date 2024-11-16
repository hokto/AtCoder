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
    from copy import deepcopy
    from collections import deque
    H,W = myin_sp_i()
    A = []
    for i in range(H):
        A.append(myin_sp_i())
    B = []
    for i in range(H):
        B.append(myin_sp_i())
    
    def is_same(X,Y):
        for i in range(H):
            for j in range(W):
                if X[i][j]!=Y[i][j]:
                    return False
        return True
    
    def swap_row(X,prev_rows,swap_rows):
        Y = deepcopy(X)
        for idx in range(len(prev_rows)):
            for j in range(W):
                Y[prev_rows[idx]][j]=X[swap_rows[idx]][j]
        return Y
    def swap_col(X,prev_cols,swap_cols):
        Y = deepcopy(X)
        for idx in range(len(prev_cols)):
            for i in range(H):
                Y[i][prev_cols[idx]]=X[i][swap_cols[idx]]
        return Y
    if is_same(A,B):
        print(0)
        return
    
    INF = 1<<30
    ans = INF
    memo_rows = {}
    memo_cols = {}
    def bfs_row():
        nonlocal memo_rows
        que = deque()
        que.append((list(range(H)),0))
        while que:
            rows,cnt = que.popleft()
            memo_rows[tuple(rows)]=cnt
            for i in range(H-1):
                rows[i],rows[i+1]=rows[i+1],rows[i]
                if tuple(rows) not in memo_rows:
                    que.append((deepcopy(rows),cnt+1))
                rows[i],rows[i+1]=rows[i+1],rows[i]
    
    def bfs_col():
        nonlocal memo_cols
        que = deque()
        que.append((list(range(W)),0))
        while que:
            cols,cnt = que.popleft()
            memo_cols[tuple(cols)]=cnt
            for i in range(W-1):
                cols[i],cols[i+1]=cols[i+1],cols[i]
                if tuple(cols) not in memo_cols:
                    que.append((deepcopy(cols),cnt+1))
                cols[i],cols[i+1]=cols[i+1],cols[i]
    bfs_row()
    bfs_col()
    for rows,cnt_row in memo_rows.items():
        for cols,cnt_col in memo_cols.items():
            AA = swap_row(A,list(range(H)),rows)
            AA = swap_col(AA,list(range(W)),cols)
            if is_same(AA,B):
                ans=min(ans,cnt_col+cnt_row)

    if ans==INF:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()