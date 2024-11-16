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

def main():
    H,W,K = myin_sp_i()
    S = []
    for _ in range(H):
        S.append(myin())
    ans = 0
    DIR = [(-1,0),(1,0),(0,1),(0,-1)]
    def dfs(i,j,d,visited):
        nonlocal ans
        if visited[i][j]: return
        if d==K:
            ans+=1
            return
        visited[i][j] = True
        for di,dj in DIR:
            ni = i+di
            nj = j+dj
            if not(0<=ni<H and 0<=nj<W and S[ni][nj]=="."): continue
            dfs(ni,nj,d+1,visited)
        visited[i][j] = False
    for i in range(H):
        for j in range(W):
            if S[i][j]==".":
                dfs(i,j,0,[[False]*W for _ in range(H)])
    print(ans)
if __name__ == "__main__":
    main()