from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)

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
    A = myin_sp_i()
    for i in range(H-1):
        A+=myin_sp_i()
    INF = Y+1
    B = [True]*(H*W)
    DIR = [[-1,0],[1,0],[0,-1],[0,1]]
    from collections import deque
    deq = [deque() for i in range(Y+1)]
    for i in range(H):
        for j in range(W):
            if i==0 or j==0 or i==H-1 or j==W-1:
                if A[i*W+j]<=Y:
                    deq[A[i*W+j]].append((A[i*W+j],i*W+j))
                    B[i*W+j]=False
    ans = H*W
    for i in range(1,Y+1):
        while deq[i]:
            #print(pq)
            a,pos = deq[i].pop()
            ans-=1
            for di,dj in DIR:
                ni = pos//W+di
                nj = pos%W+dj
                
                if not(0<=ni<=H-1 and 0<=nj<=W-1):
                    continue
                c = A[ni*W+nj]
                if c<i: c=i
                if B[ni*W+nj] and c<=Y:
                    B[ni*W+nj] = False
                    deq[c].append((c,ni*W+nj))
        print(ans)
if __name__ == "__main__":
    main()