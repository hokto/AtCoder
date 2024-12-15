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
    from heapq import heapify,heappop,heappush
    # s<1/x*tなら吸収可能
    # x*s<t(sがスライムの強さ，tが高橋君の強さ)
    H,W,X = myin_sp_i()
    P,Q = myin_sp_i()
    P-=1
    Q-=1
    S = []
    for i in range(H):
        S.append(myin_sp_i())
    ans = S[P][Q]
    DIR = [[-1,0],[1,0],[0,-1],[0,1]]
    pq = []
    heapify(pq)
    for di,dj in DIR:
        ni = P+di
        nj = Q+dj
        if not(0<=ni<H and 0<=nj<W): continue
        heappush(pq,(S[ni][nj],ni,nj))
    visited = [[False]*W for _ in range(H)]
    visited[P][Q] = True
    while pq:
        s,i,j = heappop(pq)
        if visited[i][j] or X*s>=ans: continue
        visited[i][j] = True
        ans+=s
        for di,dj in DIR:
            ni = i+di
            nj = j+dj
            if not(0<=ni<H and 0<=nj<W): continue
            if visited[ni][nj]: continue
            heappush(pq,(S[ni][nj],ni,nj))
    print(ans)

if __name__ == "__main__":
    main()