from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
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
    H,W,Y = myin_sp_i()
    A = []
    for i in range(H):
        A.append(myin_sp_i())
    INF = 10**10
    from collections import defaultdict
    cnt = defaultdict(int)
    B = [[INF for j in range(W)] for i in range(H)]
    cnt[INF]=H*W
    DIR = [[-1,0],[1,0],[0,-1],[0,1]]
    from heapq import heapify,heappop,heappush
    pq = []
    heapify(pq)
    for i in range(H):
        heappush(pq,(A[i][0],i,0))
        heappush(pq,(A[i][W-1],i,W-1))
        B[i][0]=A[i][0]
        B[i][W-1]=A[i][W-1]
        cnt[B[i][0]]+=1
        cnt[B[i][W-1]]+=1
        cnt[INF]-=2
    for j in range(W):
        heappush(pq,(A[0][j],0,j))
        heappush(pq,(A[H-1][j],H-1,j))
        B[0][j]=A[0][j]
        B[H-1][j]=A[H-1][j]
        cnt[B[0][j]]+=1
        cnt[B[H-1][j]]+=1
        cnt[INF]-=2
    while len(pq)>0:
        #print(pq)
        a,i,j = heappop(pq)
        if B[i][j]<a:
            continue
        #B[i][j] = a
        for di,dj in DIR:
            ni = i+di
            nj = j+dj
            
            if not(0<=ni<=H-1 and 0<=nj<=W-1):
                continue
            c = max(A[ni][nj],a)
            if B[ni][nj]>c:
                cnt[B[ni][nj]]-=1
                cnt[c]+=1
                B[ni][nj] = c
                heappush(pq,(c,ni,nj))
    #print(B)
    accum = 0
    for y in range(1,Y+1):
        accum+=cnt[y]
        print(H*W-accum)
if __name__ == "__main__":
    main()