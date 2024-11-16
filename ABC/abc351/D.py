from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
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

DIR =[(-1,0),(1,0),(0,-1),(0,1)]
now=0
from collections import deque
def bfs(ri,rj,H,W,is_magnetic,find):
    deq = deque()
    deq.append((ri,rj,-1,-1))
    cnt=0
    while deq:
        i,j,pi,pj = deq.popleft()
        if find[i][j]==now:
            continue
        find[i][j] = now
        if is_magnetic[i][j]:
            cnt+=1
            continue
        cnt+=1
        for di,dj in DIR:
            ni = i+di
            nj = j+dj
            if not(0<=ni<H and 0<=nj<W):
                continue
            if ni==pi and nj==pj:
                continue
            deq.append((ni,nj,i,j))
    return cnt
def main():
    global now
    H,W = myin_sp_i()
    S = []
    for i in range(H):
        S.append(myin())
    is_magnetic = [[False]*W for i in range(H)]
    find = [[-1]*W for i in range(H)] 
    for i in range(H):
        for j in range(W):
            for di,dj in DIR:
                ni = i+di
                nj = j+dj
                if not(0<=ni<H and 0<=nj<W):
                    continue
                if S[ni][nj]=="#":
                    is_magnetic[i][j]=True
    ans = 1
    for i in range(H):
        for j in range(W):
            if find[i][j]>-1:
                continue
            if S[i][j]=="#":
                continue
            now+=1
            res = bfs(i,j,H,W,is_magnetic,find)
            ans=max(ans,res)
    #print(find)
    print(ans)
    
if __name__ == "__main__":
    main()