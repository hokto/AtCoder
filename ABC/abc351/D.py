H,W = list(map(int,input().split()))
S = []
for _ in range(H):
    S.append(input())
memo = [[0 for i in range(W)]for j in range(H)]
dir = [[-1,0],[1,0],[0,-1],[0,1]]
que = []
for i in range(H):
    for j in range(W):
        que.append([i,j,i*W+j])
while len(que)>0:
    i,j,k = que.pop(0)
    if S[i][j]!="#" and memo[i][j]==0:
        memo[i][j] = k
        flag = True
        for di,dj in dir:
            ni = di+i
            nj = dj+j
            if 0>ni or ni>=H or 0>nj or nj>=W:
                continue
            if i==ni and j==nj:
                continue
            if S[ni][nj] == "#":
                flag = False
                break
        if flag:
            for di,dj in dir:
                ni = di+i
                nj = dj+j
                if 0>ni or ni>=H or 0>nj or nj>=W:
                    continue
                if i==ni and j==nj:
                    continue
                que.insert(0,[ni,nj,k])
        else:
            if memo[i][j]==W*i+j:
                memo[i][j] = 0
cnt = {}
#print(memo)
for arr in memo:
    for v in arr:
        if v not in cnt:
            cnt[v] = 1
        else:
            cnt[v] += 1
cnt[0] = 0
#print(cnt)
ans = max(cnt.values())
if ans == 0:
    ans+=1
print(ans)