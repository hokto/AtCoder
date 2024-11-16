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

INF = 10**20
def calc_dist(dist,edge_perm,Edge,N):
    ans = INF
    for bit in range(1<<len(edge_perm)):
        res = 0
        now = 0
        for i,edge_idx in enumerate(edge_perm):
            u,v,t = Edge[edge_idx-1]
            if bit&(1<<i)>0:
                u,v = v,u
            res+=dist[now][u]
            res+=t
            now = v
        res+=dist[now][N-1]
        if ans>res:
            ans=res
    return ans
def main():
    from itertools import permutations
    N,M = myin_sp_i()
    Edge = []
    dist = [[INF for j in range(N)] for i in range(N)]
    for i in range(N):
        dist[i][i]=0
    for i in range(M):
        u,v,t = myin_sp_i()
        u-=1
        v-=1
        Edge.append([u,v,t])
        if dist[u][v]>t: dist[u][v]=t
        dist[v][u]=dist[u][v]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d = dist[i][k]+dist[k][j]
                if dist[i][j]>d:
                    dist[i][j] = d
    
    Q = int(myin())
    for q in range(Q):
        K = int(myin())
        B = myin_sp_i()
        ans = INF
        for edge_perm in permutations(B):
            res = calc_dist(dist,edge_perm,Edge,N)
            if ans>res:
                ans=res
        print(ans)

if __name__ == "__main__":
    main()