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

# 拝借:https://tjkendev.github.io/procon-library/python/graph/auxiliary_tree.html
# Auxiliary Tree を保持する
G0 = None

S = None
FS = LS = depth = None
lg = None
st = None
# 前計算 O(N log N)
def construct(N, G):
    global S, FS, LS, depth, G0, lg, st
    G0 = [None] * N

    S = []
    FS = [0]*N; LS = [0]*N
    depth = [0]*N
    # Euler tour technique
    def dfs(v, p, d):
        depth[v] = d
        FS[v] = len(S)
        S.append(v)
        for w in G[v]:
            if w == p:
                continue
            dfs(w, v, d+1)
            S.append(v)
        LS[v] = len(S)
        S.append(v)
    dfs(0, -1, 0)

    # Sparse Table
    L = len(S)
    lg = [0]*(L+1)
    for i in range(2, L+1):
        lg[i] = lg[i >> 1] + 1
    st = [[L]*(L - (1 << i) + 1) for i in range(lg[L]+1)]
    st[0][:] = S
    b = 1
    for i in range(lg[L]):
        st0 = st[i]
        st1 = st[i+1]
        for j in range(L - (b<<1) + 1):
            st1[j] = (st0[j] if depth[st0[j]] <= depth[st0[j+b]] else st0[j+b])
        b <<= 1

# 頂点リストvsを含むAuxiliary Treeを構築 O(K log K)
def auxiliary_tree(k, vs):
    vs.sort(key=FS.__getitem__)
    for i in range(k-1):
        x = FS[vs[i]]; y = FS[vs[i+1]]
        l = lg[y - x + 1]
        w = st[l][x] if depth[st[l][x]] <= depth[st[l][y - (1 << l) + 1]] else st[l][y - (1 << l) + 1]
        vs.append(w)
    vs.sort(key=FS.__getitem__)
    stk = []
    prv = -1
    for v in vs:
        if v == prv:
            continue
        while stk and LS[stk[-1]] < FS[v]:
            stk.pop()
        if stk:
            G0[stk[-1]].append(v)
        G0[v] = []
        stk.append(v)
        prv = v
MOD = 998244353

def dp(v,p):
    res = 0
    s=0
    s_list = []
    for vv in G0[v]:
        if vv==p:continue
        tmp = dp(vv,v)
        s+=tmp
        s_list.append(tmp)
    for i in range(len(s_list)):
        tmp-=s_list[i]
        res+=s_list[i]*tmp;res%=MOD
    return res
def main():
    global G0
    N = int(myin())
    C = myin_sp_i()
    M = max(C)
    colors = [[] for i in range(M)]
    for i in range(N):
        c = C[i]
        c-=1
        colors[c].append(i)
    G = [[] for i in range(N)]
    for i in range(N-1):
        a,b = myin_sp_i()
        a-=1
        b-=1
        G[a].append(b)
        G[b].append(a)
    ans = 0
    construct(N,G)
    for i in range(M):
        if not colors[i]:
            continue
        auxiliary_tree(len(colors[i]),colors[i])
        print(G0)
        ans+=dp(0,-1);ans%=MOD
    print(ans)

if __name__ == "__main__":
    main()