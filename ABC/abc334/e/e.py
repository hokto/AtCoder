from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')

# お借りした先: https://kntychance.hatenablog.jp/entry/2022/09/16/161858
class LowLink():
    def __init__(self, adj):
        self.n = len(adj)
        self.ord = [None]*self.n
        self.low = [None]*self.n
        self.son = [[] for _ in range(self.n)] # son[i] := 頂点iの子を格納したlist
        self.back_edge = [[] for _ in range(self.n)] # back_edge[i] := 頂点iから出る後退辺の終点を格納したlist
        self.tps = [] # 頂点のトポロジカルソート

        # DFSでord, son, tpsを求め、lowを初期化
        t = 0 # 今までに訪れた頂点数
        stack = [(None, 0)] # 直前にいた頂点, 今いる頂点
        while stack: 
            pre, now = stack.pop()
            if self.ord[now] is not None: # 直前に通った辺が後退辺ならば
                if self.ord[pre] < self.ord[now]: continue # 後退辺を根側から進んでいた場合は無視
                self.low[pre] = min(self.low[pre], self.ord[now]) # low[pre]をord[now]でchmin
                self.back_edge[pre].append(now)
                continue
            if pre is not None:
                self.son[pre].append(now)
            self.tps.append(now)
            self.ord[now] = t # 行きがけ順を書き込む
            self.low[now] = self.ord[now] # low[now]をord[now]で初期化
            t += 1
            for next in adj[now]:
                if next == pre: continue
                stack.append((now, next))
        
        # ボトムアップ順にchminしてlowを求める
        for u in reversed(self.tps[1:]):
            for v in self.son[u]:
                self.low[u] = min(self.low[u], self.low[v])
def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

DIR = [(1,0),(-1,0),(0,1),(0,-1)]
from collections import deque
cnt = 0
def bfs(ri,rj,connected,S,H,W):
    global cnt
    deq = deque()
    deq.append((ri,rj))
    connected[ri][rj]=cnt
    while deq:
        i,j = deq.popleft()
        for di,dj in DIR:
            ni = i+di
            nj = j+dj
            if not(0<=ni<H and 0<=nj<W):
                continue
            if S[ni][nj]=="." or connected[ni][nj]!=-1:
                continue
            connected[ni][nj]=cnt
            deq.append((ni,nj))
    cnt+=1
def main():
    from atcoder.math import inv_mod
    MOD = 998244353
    H,W = myin_sp_i()
    S = []
    for i in range(H):
        S.append(myin())
    connected = [[-1]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j]=="#" and connected[i][j]==-1:
                bfs(i,j,connected,S,H,W)
    G = [[] for i in range(H*W)]
    for i in range(H):
        for j in range(W):
            if S[i][j]==".":
                continue
            for di,dj in DIR:
                ni = i+di
                nj = j+dj
                if not(0<=ni<H and 0<=nj<W):
                    continue
                if S[ni][nj]=="#":
                    G[i*W+j].append(ni*W+nj)
                    G[ni*W+nj].append(i*W+j)
            
    base_con = cnt
    ll = LowLink(G)
    ans = 0
    rd_cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j]=="#":
                red_cnt+=1
                kind = {}
                for di,dj in DIR:
                    ni = i+di
                    nj = j+dj
                    if not(0<=ni<H and 0<=nj<W):
                        continue
                    if S[ni][nj]=="#":
                        kind[connected[ni][nj]]=1
                        
                ans+=base_con-(len(kind)-1)
    
    print(ans*inv_mod(red_cnt,MOD)%MOD)

if __name__ == "__main__":
    main()