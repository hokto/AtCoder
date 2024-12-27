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
    N = int(myin())
    G = [[] for _ in range(N)]
    deg = [0]*N
    for _ in range(N-1):
        u,v = myin_sp_i()
        u-=1
        v-=1
        G[u].append(v)
        G[v].append(u)
        deg[u]+=1
        deg[v]+=1
    ans = N-3
    for u in range(N):
        adj = []
        for v in G[u]:
            adj.append((deg[v],v))
        adj.sort(reverse=True)
        for x in range(len(adj)):
            # x+1個を選択する
            y = adj[x][0]-1 # uと接続している分を除く
            ans = min(ans,N-((x+1)*y+(x+1)+1))
    print(ans)
if __name__ == "__main__":
    main()