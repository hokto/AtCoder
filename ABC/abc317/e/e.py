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
    H,W = myin_sp_i()
    A = []
    can_walk = [[True]*W for i in range(H)]
    start_pos = (-1,-1)
    goal_pos = (-1,-1)
    for i in range(H):
        A.append(myin())
        for j in range(W):
            if A[i][j]=="#": can_walk[i][j]=False
            if A[i][j]=="S": start_pos=(i,j)
            if A[i][j]=="G": goal_pos=(i,j)
    # 右に
    for i in range(H):
        is_watch = False
        for j in range(W):
            if A[i][j]!=".": is_watch = False
            if A[i][j]==">": is_watch = True;can_walk[i][j]=False
            if A[i][j]=="." and is_watch: can_walk[i][j]=False
    # 左に
    for i in range(H):
        is_watch = False
        for j in range(W)[::-1]:
            if A[i][j]!=".": is_watch = False
            if A[i][j]=="<": is_watch = True;can_walk[i][j]=False
            if A[i][j]=="." and is_watch: can_walk[i][j]=False
    # 下に
    for j in range(W):
        is_watch = False
        for i in range(H):
            if A[i][j]!=".": is_watch = False
            if A[i][j]=="v": is_watch = True;can_walk[i][j]=False
            if A[i][j]=="." and is_watch: can_walk[i][j]=False
    # 上に
    for j in range(W):
        is_watch = False
        for i in range(H)[::-1]:
            if A[i][j]!=".": is_watch = False
            if A[i][j]=="^": is_watch = True;can_walk[i][j]=False
            if A[i][j]=="." and is_watch: can_walk[i][j]=False
    from collections import deque
    que = deque()
    que.append((start_pos[0],start_pos[1],0))
    INF = H*W+10
    dist = [[INF]*W for i in range(H)]
    DIR = [(-1,0),(1,0),(0,1),(0,-1)]
    while que:
        i,j,d = que.popleft()
        if dist[i][j]!=INF: continue
        dist[i][j] = d
        for di,dj in DIR:
            ni = i+di
            nj = j+dj
            if not(0<=ni<H and 0<=nj<W and can_walk[ni][nj] and dist[ni][nj]==INF): continue
            que.append((ni,nj,d+1))
    if dist[goal_pos[0]][goal_pos[1]]==INF:
        print(-1)
    else:
        print(dist[goal_pos[0]][goal_pos[1]])

if __name__ == "__main__":
    main()