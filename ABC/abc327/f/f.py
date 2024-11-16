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
    from atcoder.lazysegtree import LazySegTree
    N,D,W = myin_sp_i()
    L = 2*10**5+10
    TX = []
    for i in range(N):
        TX.append(myin_sp_i())
    TX.sort()
    def lazy_op(x,y):
        return x+y
    lst = LazySegTree(max,0,lazy_op,lazy_op,0,L-W+1)
    head = 0
    tail = 0
    ans = 0
    while tail<N:
        while head<N and TX[head][0]-TX[tail][0]<D:
            x = TX[head][1]
            x-=1
            lst.apply(max(x-W+1,0),min(x+1,L-W+1),1)
            head+=1
        ans = max(ans,lst.all_prod())
        if head==N: break
        while tail<head and TX[head][0]-TX[tail][0]>=D:
            x = TX[tail][1]
            x-=1
            lst.apply(max(x-W+1,0),min(x+1,L-W+1),-1)
            tail+=1
    print(ans)

if __name__ == "__main__":
    main()