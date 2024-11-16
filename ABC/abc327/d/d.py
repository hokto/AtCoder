from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
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
    N,M = myin_sp_i()
    A= myin_sp_i()
    B = myin_sp_i()
    G = [[] for i in range(N)]
    for i in range(M):
        G[A[i]-1].append(B[i]-1)
        G[B[i]-1].append(A[i]-1)
    
    depth = [-1]*N
    def dfs(v,p,d):
        nonlocal depth
        if depth[v]>-1:
            if (depth[v]-d)%2==0:
                return True
            else:
                return False
        depth[v] = d
        res = True
        for vv in G[v]:
            if vv==p: continue
            res&=dfs(vv,v,d+1)
        return res
    for i in range(N):
        if depth[i]==-1:
            res = dfs(i,-1,0)
            if not res:
                print("No")
                return
    print("Yes")
if __name__ == "__main__":
    main()