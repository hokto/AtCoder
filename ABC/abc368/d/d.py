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

def dfs(v,p,G,find,use):
    flag = find[v]
    for vv in G[v]:
        if vv==p: continue
        flag|=dfs(vv,v,G,find,use)
    use[v]=flag
    return use[v]
def main():
    N,K = myin_sp_i()
    G = [[] for i in range(N)]
    for i in range(N-1):
        a,b = myin_sp_i()
        a-=1
        b-=1
        G[a].append(b)
        G[b].append(a)
    V = myin_sp_i()
    find = [False]*N
    for v in V:
        find[v-1]=True
    use = [False]*N
    dfs(V[0]-1,-1,G,find,use)
    print(use.count(True))
if __name__ == "__main__":
    main()