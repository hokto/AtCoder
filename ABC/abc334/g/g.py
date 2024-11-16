from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')

DIR = [(1,0),(-1,0),(0,1),(0,-1)]
# お借りした先: https://kntychance.hatenablog.jp/entry/2022/09/16/161858
class LowLink():
    def __init__(self,S,H,W):
        self.n = H*W
        self.ord = [None]*self.n
        self.low = [None]*self.n
        self.son = [[] for _ in range(self.n)] # son[i] := 頂点iの子を格納したlist
        self.back_edge = [[] for _ in range(self.n)] # back_edge[i] := 頂点iから出る後退辺の終点を格納したlist
        #self.tps = [] # 頂点のトポロジカルソート
        self.roots = []
        self.split_cnt = [1]*self.n
        # DFSでord, son, tpsを求め、lowを初期化
        t = 0 # 今までに訪れた頂点数
        for root in range(self.n):
            self.tps = [] # 頂点のトポロジカルソート
            if S[root//W][root%W]=="." or self.low[root] is not None:
                continue
            self.split_cnt[root]=0
            self.roots.append(root)
            stack = [(None, root)] # 直前にいた頂点, 今いる頂点
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
                for di,dj in DIR:
                    ni = now//W+di
                    nj = now%W+dj
                    next = ni*W+nj
                    if next == pre: continue
                    if not(0<=ni<H and 0<=nj<W):
                        continue
                    if S[ni][nj]=="#":
                        stack.append((now, next))
            
            # ボトムアップ順にchminしてlowを求める
            for u in reversed(self.tps[1:]):
                for v in self.son[u]:
                    self.low[u] = min(self.low[u], self.low[v])
            for u in self.tps:
                for v in self.son[u]:
                    if self.ord[u]<=self.low[v]:
                        self.split_cnt[u]+=1
def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    from atcoder.math import inv_mod
    MOD = 998244353
    H,W = myin_sp_i()
    S = []
    for i in range(H):
        S.append(myin())
    ll = LowLink(S,H,W)
    base_con = len(ll.roots)
    exist_roots = {}
    for root in ll.roots:
        exist_roots[root]=1
    #print(ll.ord)
    #print(ll.low)
    #print(ll.split_cnt)
    ans = 0
    green_cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j]=="#":
                green_cnt+=1
                ans+=base_con-1+ll.split_cnt[i*W+j]
                #print(ans)
    print(ans*inv_mod(green_cnt,MOD)%MOD)

if __name__ == "__main__":
    main()