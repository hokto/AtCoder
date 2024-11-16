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
    N,M = myin_sp_i()
    G = [[] for i in range(N)]
    for i in range(M):
        a,b = myin_sp_i()
        a-=1
        b-=1
        G[a].append(b)
    visited = [False]*N
    def bfs():
        que = deque()
        que.append((0,0))
        while que:
            v,d = que.popleft()
            if visited[v]:
                if v==0:
                    return d
                else:
                    continue
            visited[v]=True
            for vv in G[v]:
                que.append((vv,d+1))
        return N+1
            
    ans = bfs()
    if ans>N:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()