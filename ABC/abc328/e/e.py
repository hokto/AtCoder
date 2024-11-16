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
    from itertools import combinations
    from atcoder.dsu import DSU
    N,M,K = myin_sp_i()
    E = []
    for i in range(M):
        u,v,w = myin_sp_i()
        u-=1
        v-=1
        E.append((u,v,w))
    ans = K-1
    for edges in combinations(list(range(M)),N-1):
        dsu = DSU(N)
        res = 0
        for edge_idx in edges:
            u,v,w = E[edge_idx]
            res+=w
            if dsu.same(u,v):
                res=K-1
                break
            dsu.merge(u,v)
        res%=K
        ans = min(ans,res)
    print(ans)

if __name__ == "__main__":
    main()