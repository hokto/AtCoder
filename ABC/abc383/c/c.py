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
    from collections import deque
    H,W,D = myin_sp_i()
    S = []
    for i in range(H):
        S.append(myin())
    que = deque()
    for i in range(H):
        for j in range(W):
            if S[i][j]=="H": que.append((i,j,0))
    INF = D+1
    dist = [[INF]*W for _ in range(H)]
    DIR = [(-1,0),(1,0),(0,-1),(0,1)]
    ans = 0
    while que:
        i,j,d = que.popleft()
        if dist[i][j]<=d: continue
        dist[i][j]=d
        ans+=1
        for di,dj in DIR:
            ni = i+di
            nj = j+dj
            if not(0<=ni<H and 0<=nj<W): continue
            if S[ni][nj]=="#": continue
            if dist[ni][nj]<=d+1: continue
            que.append((ni,nj,d+1))
    print(ans)

if __name__ == "__main__":
    main()