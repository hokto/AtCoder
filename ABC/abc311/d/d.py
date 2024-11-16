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
    N,M = myin_sp_i()
    S = []
    for i in range(N):
        S.append(myin())
    done = [[[False]*4 for j in range(M)]for i in range(N)]
    visited = [[False]*M for i in range(N)]
    def bfs():
        from collections import deque
        DIR = [(-1,0),(1,0),(0,1),(0,-1)]
        deq = deque()
        deq.append((1,1,0))
        while deq:
            i,j,d = deq.popleft()
            if done[i][j][d]: continue
            visited[i][j] = True
            done[i][j][d]=True
            ni = i+DIR[d][0]
            nj = j+DIR[d][1]
            if S[ni][nj]=="#":
                for dd in range(4):
                    if d==dd: continue
                    deq.append((i,j,dd))
            else:
                deq.append((ni,nj,d))
    bfs()
    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]: ans+=1
    print(ans)

if __name__ == "__main__":
    main()