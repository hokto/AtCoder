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
    from atcoder.fenwicktree import FenwickTree
    N = int(myin())
    C = [c-1 for c in myin_sp_i()]
    XX = myin_sp_i()
    Y = set()
    for xx in XX:
        Y.add(xx)
    Y = list(sorted(Y))
    change = {}
    X = []
    for i,y in enumerate(Y):
        change[y] = i
    for i in range(N):
        X.append(change[XX[i]])
    M = len(Y)
    overall_ft = FenwickTree(M)
    color = [set() for _ in range(N)]
    color_change_idx = [dict() for _ in range(N)]
    for i in range(N):
        color[C[i]].add(X[i])
    for i in range(N):
        if color[i]:
            color[i] = list(sorted(color[i]))
            for j in range(len(color[i])):
                color_change_idx[i][color[i][j]] = j
    color_ft = [FenwickTree(len(color[i])) for i in range(N)]
    ans = 0
    for i in range(N):
        c = C[i]
        color_size = len(color_change_idx[c])
        x = X[i]
        ans+=i-overall_ft.sum(0,x+1)
        ans-=color_ft[c].sum(color_change_idx[c][x]+1,color_size)
        color_ft[c].add(color_change_idx[c][x],1)
        overall_ft.add(x,1)
    print(ans)
        

if __name__ == "__main__":
    main()