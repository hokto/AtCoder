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
    from atcoder.dsu import DSU
    N = int(myin())
    G = [[] for _ in range(N)]
    E = []
    for _ in range(N):
        u,v = myin_sp_i()
        u-=1
        v-=1
        G[u].append(v)
        G[v].append(u)
        E.append((u,v))
    lowlink = [-1]*N
    order = [-1]*N
    order_num = 0
    def dfs(v,p):
        nonlocal order_num
        if order[v]!=-1:
            return lowlink[v]
        order[v] = order_num
        lowlink[v] = order_num
        order_num += 1
        for vv in G[v]:
            if vv==p: continue
            lowlink[v] = min(lowlink[v],dfs(vv,v))
        return lowlink[v]
    def is_bridge(u,v):
        if order[u]>order[v]: u,v = v,u
        return (order[u] < lowlink[v])
    dfs(0,-1)
    dsu = DSU(N)
    for u,v in E:
        if is_bridge(u,v):
            dsu.merge(u,v)
    Q = int(myin())
    for q in range(Q):
        x,y = myin_sp_i()
        x-=1
        y-=1
        if dsu.same(x,y):
            print("Yes")
        else:
            print("No")
if __name__ == "__main__":
    main()