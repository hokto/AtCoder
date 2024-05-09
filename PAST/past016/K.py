N = int(input())
#N=1500
S = []
for i in range(N):
    S.append(input())
    #S.append(["." for _ in range(N)]) 
dir = [[0,1],[1,0],[-1,0],[0,-1]]
def bfs(k):
    dist = [[INF for i in range(N)]for j in range(N)]
    dist[s[0]][s[1]]=0
    que = [s]
    while len(que)>0:
        i,j = que.pop()
        for di,dj in dir:
            ni = i+di*k
            nj = j+dj*k
            if ni<0 or ni>=N or nj<0 or nj>=N or dist[ni][nj]!=INF:
                continue
            if di==0:
                j1 = j
                j2 = nj
                if j1>j2:
                    j1,j2 = j2,j1
                if l_cnt[i][j2+1]-l_cnt[i][j1]!=0:
                    continue
            if dj==0:
                i1 = i
                i2 = ni
                if i1>i2:
                    i1,i2 = i2,i1
                if up_cnt[i2+1][j]-up_cnt[i1][j]!=0:
                    continue
            dist[ni][nj] = dist[i][j]+1
            que.append([ni,nj])
    res = INF
    for i in range(N):
        for j in range(N):
            if g[i][j]:
                res = min(res,dist[i][j])
    if res==INF:
        return -1
    return res


INF = N*N+1
l_cnt = [[0 for i in range(N+1)]for j in range(N)]
up_cnt = [[0 for i in range(N)]for j in range(N+1)]
for i in range(N):
    for j in range(N):
        l_cnt[i][j+1]=l_cnt[i][j]
        up_cnt[i+1][j] = up_cnt[i][j]
        if S[i][j]=="X":
            l_cnt[i][j+1]+=1
            up_cnt[i+1][j]+=1

s = (-1,-1)
g = [[False for i in range(N)]for j in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j] == "S":
            s = [i,j]
        if S[i][j]=="G":
            g[i][j]=True
for k in range(1,N):
    ans = bfs(k)
    print(ans)
