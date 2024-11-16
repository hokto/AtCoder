from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
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
    from atcoder.lazysegtree import LazySegTree
    H,W,M = myin_sp_i()
    e = 0
    row = [W]*H
    col = [H]*W
    row_bias = 0
    col_bias = 0
    query = []
    for m in range(M):
        t,a,x = myin_sp_i()
        a-=1
        query.append((t,a,x))
    X = [0]*(2*10**5+10)
    for t,a,x in reversed(query):
        if t==1:
            # row
            if row[a]>row_bias:
                X[x]+=row[a]-row_bias
                row[a]=0
                col_bias+=1
        else:
            # col
            if col[a]>col_bias:
                X[x]+=col[a]-col_bias
                col[a]=0
                row_bias+=1
    for i in range(H):
        if row[i]>row_bias:
            X[0]+=row[i]-row_bias
    ans = []
    for i,x in enumerate(X):
        if x>0:
            ans.append((i,x))
    print(len(ans))
    for i,x in ans:
        print(i,x)

if __name__ == "__main__":
    main()