from collections import deque
N = int(input())
C= []
for i in range(N):
    C.append(input())

def bfs(s,type):
    DIR = [[0,1],[1,0],[0,-1],[-1,0]]
    deq = deque()
    deq.append(s)
    dist = [[-1 for i in range(N)] for j in range(N)]
    dist[s[0]][s[1]]=0
    log = [[[-1,-1] for i in range(N)]for j in range(N)]
    while len(deq)>0:
        pi,pj = deq.popleft()
        for di,dj in DIR:
            ni = pi+di
            nj = pj+dj
            if(ni<0 or nj<0 or ni>=N or nj>=N):
                continue
            if(dist[ni][nj]!=-1):
                continue
            if(C[ni][nj]==type or C[ni][nj]=="P"):
                dist[ni][nj]=dist[pi][pj]
                deq.appendleft([ni,nj])
            else:
                dist[ni][nj]=dist[pi][pj]+1
                deq.append([ni,nj])
            log[ni][nj]=[pi,pj]
    return dist,log

ans1_dist,log1 = bfs([0,0],"R")
ni,nj = log1[-1][-1]
while(ni==0 and nj==0):
    if(C[ni][nj]=="B"):
        C[ni][nj]="P"
    ni,nj = log1[ni][nj]
ans2_dist,_ = bfs([0,N-1],"B")
#print(ans2_dist)
print(ans1_dist[-1][-1]+ans2_dist[-1][0])