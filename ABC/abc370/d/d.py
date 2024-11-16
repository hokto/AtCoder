from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
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

DIR = [[-1,0],[1,0],[0,-1],[0,1]]

    
def main():
    H,W,Q = myin_sp_i()
    next = [[[(-1,-1) for k in range(4)] for j in range(W)] for i in range(H)]
    visited = [[False]*W for i in range(H)]
    def dfs(r,c,idx):
        if r==-1 and c==-1:
            return (-1,-1)
        #global next,visited
        if not visited[r][c]:
            visited[r][c] = True
            for i,(dr,dc) in enumerate(DIR):
                nr =r+dr
                nc = c+dc
                if not(0<=nr<H and 0<=nc<W):
                    continue
                next[r][c][i] = (nr,nc)
            return r,c
        next[r][c][idx] = dfs(next[r][c][idx][0],next[r][c][idx][1],idx)
        return next[r][c][idx]
    for q in range(Q):
        R,C = myin_sp_i()
        R-=1
        C-=1
        if visited[R][C]:
            for i in range(4):
                dfs(R,C,i)
        else:
            visited[R][C] = True
            for i,(dr,dc) in enumerate(DIR):
                nr =R+dr
                nc = C+dc
                if not(0<=nr<H and 0<=nc<W):
                    continue
                next[R][C][i] = (nr,nc)
    ans = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j]: ans+=1
    print(ans)

if __name__ == "__main__":
    main()