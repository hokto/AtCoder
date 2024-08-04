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
    H,W = myin_sp_i()
    A = []
    for i in range(H):
        A.append(myin())
    N = int(myin())
    E = [[0]*W for i in range(H)]
    for i in range(N):
        r,c,e = myin_sp_i()
        r-=1
        c-=1
        E[r][c]=e
    rs,cs = -1,-1
    rt,ct = -1,-1
    for i in range(H):
        for j in range(W):
            if A[i][j]=="S":
                rs,cs = i,j
            if A[i][j]=="T":
                rt,ct = i,j
    from heapq import heapify,heappop,heappush
    energy = [[-1]*W for i in range(H)]
    pq = [(-E[rs][cs],rs,cs)]
    heapify(pq)
    DIR = [[-1,0],[0,-1],[1,0],[0,1]]
    while pq:
        e,r,c = heappop(pq)
        e*=-1
        if energy[r][c]>=e: continue
        energy[r][c] = e
        for dr,dc in DIR:
            nr = r+dr
            nc = c+dc
            if not(0<=nr<H and 0<=nc<W and A[nr][nc]!="#"):
                continue
            if e>=1:
                e_ = max(e-1,E[nr][nc])
                heappush(pq,(-e_,nr,nc))
    #print(energy)
    if energy[rt][ct]>=0:
        print("Yes")
    else:
        print("No")
            
if __name__ == "__main__":
    main()