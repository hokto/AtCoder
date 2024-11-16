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
    from collections import deque
    DIR = [(1,1),(1,-1),(-1,1),(-1,-1)]
    N = int(myin())
    A = myin_sp_i()
    B = myin_sp_i()
    S = []
    for _ in range(N):
        S.append(myin())
    INF = N*N+100
    dist = [[[INF]*4 for _ in range(N)] for _ in range(N)]
    for i in range(4):
        dist[A[0]-1][A[1]-1][i] = 0
    deq = deque()
    deq.append((0,A[0]-1,A[1]-1,-1))
    while deq:
        c,i,j,d = deq.popleft()
        for dd,(di,dj) in enumerate(DIR):
            ni = i+di
            nj = j+dj
            if not(0<=ni<N and 0<=nj<N and S[ni][nj]=="."): continue
            if d==dd:
                if dist[ni][nj][dd]<=c: continue
                dist[ni][nj][dd] = c
                deq.appendleft((c,ni,nj,dd))
            else:
                if dist[ni][nj][dd]<=c+1: continue
                dist[ni][nj][dd] = c+1
                deq.append((c+1,ni,nj,dd))
    ans = min(dist[B[0]-1][B[1]-1])
    if ans==INF:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()