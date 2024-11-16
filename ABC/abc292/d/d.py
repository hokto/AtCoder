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
    G = [[] for _ in range(N)]
    for i in range(M):
        u,v = myin_sp_i()
        u-=1
        v-=1
        G[u].append(v)
        G[v].append(u)
    visited = [False]*N
    ok = True
    for r in range(N):
        if visited[r]: continue
        que = [r]
        sum_dig = 0
        sum_v = 0
        while que:
            v = que.pop()
            visited[v]=True
            sum_dig+=len(G[v])
            sum_v+=1
            for vv in G[v]:
                if visited[vv]: continue
                que.append(vv)
        if sum_dig//2 != sum_v:
            ok = False
            break
    if ok:
        print("Yes")
    else:
        print("No")
            

if __name__ == "__main__":
    main()