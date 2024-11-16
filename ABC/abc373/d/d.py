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
        u,v,w = myin_sp_i()
        u-=1
        v-=1
        G[u].append((v,w))
        G[v].append((u,-w))
    ans = [None]*N
    def bfs(r):
        deq = deque()
        deq.append((r,-1,0))
        while deq:
            v,p,c = deq.popleft()
            ans[v] = c
            for vv,w in G[v]:
                if vv==p: continue
                if ans[vv] is not None: continue
                deq.append((vv,v,c+w))
    for i in range(N):
        if ans[i] is None:
            bfs(i)
    print(*ans)

if __name__ == "__main__":
    main()