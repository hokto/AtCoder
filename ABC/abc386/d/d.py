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
    from collections import defaultdict
    from atcoder.fenwicktree import FenwickTree
    N,M = myin_sp_i()
    X = defaultdict(list)
    Y = set()
    X_keys = set()
    for _ in range(M):
        x,y,c = myin_sp_s()
        x = int(x)
        y = int(y)
        X[x].append((y,c))
        X_keys.add(x)
        Y.add(y)
    X_keys = sorted(list(X_keys),reverse=True)
    Y = sorted(list(Y))
    change = {}
    for i,y in enumerate(Y):
        change[y] = i

    K = len(change)
    black_ft = FenwickTree(K)
    isok = True
    for x in X_keys:
        X_arr = sorted(X[x])
        exist_white = False
        for y,c in X_arr:
            y = change[y]
            if c=="B":
                if exist_white:
                    isok = False
                    break
                black_ft.add(y,1)
            else:
                if black_ft.sum(y,K)>0:
                    isok = False
                    break
                exist_white = True
    if isok:
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()