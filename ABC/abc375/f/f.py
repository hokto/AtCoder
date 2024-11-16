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
    N,M,Q = myin_sp_i()
    E = []
    INF = 10**15
    dist = [[INF]*N for i in range(N)]
    for i in range(N):
        dist[i][i]=0
    for i in range(M):
        a,b,c = myin_sp_i()
        a-=1
        b-=1
        dist[a][b] = c
        dist[b][a] = c
        E.append((a,b,c))
    QUERY = []
    for q in range(Q):
        query = myin_sp_i()
        QUERY.append(query)
        if query[0]==1:
            i = query[1]
            i-=1
            dist[E[i][0]][E[i][1]]=INF
            dist[E[i][1]][E[i][0]]=INF
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    ans = []
    for query in QUERY[::-1]:
        if query[0]==1:
            i = query[1]
            i-=1
            dist[E[i][0]][E[i][1]]=min(dist[E[i][0]][E[i][1]],E[i][2])
            dist[E[i][1]][E[i][0]]=dist[E[i][0]][E[i][1]]
            for k in range(N):
                dist[E[i][0]][k] = min(dist[E[i][0]][k],dist[E[i][0]][E[i][1]]+dist[E[i][1]][k])
                dist[k][E[i][0]] = min(dist[k][E[i][0]],dist[k][E[i][1]]+dist[E[i][1]][E[i][0]])
            for k in range(N):
                dist[E[i][1]][k] = min(dist[E[i][1]][k],dist[E[i][1]][E[i][0]]+dist[E[i][0]][k])
                dist[k][E[i][1]] = min(dist[k][E[i][1]],dist[k][E[i][0]]+dist[E[i][0]][E[i][1]])
            for k in E[i][:2]:
                for i in range(N):
                    for j in range(N):
                        dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        else:
            x = query[1]
            x-=1
            y = query[2]
            y-=1
            if dist[x][y]==INF:
                ans.append(-1)
            else:
                ans.append(dist[x][y])
    print(*ans[::-1],sep="\n")
if __name__ == "__main__":
    main()