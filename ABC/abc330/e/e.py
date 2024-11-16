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
    N,Q = myin_sp_i()
    A = myin_sp_i()
    cnt = defaultdict(int)
    ft = FenwickTree(Q+1)
    for i in range(N):
        if Q>=A[i] and cnt[A[i]]==0:
            ft.add(A[i],1)
        cnt[A[i]]+=1
    for q in range(Q):
        i,x = myin_sp_i()
        i-=1
        cnt[A[i]]-=1
        if Q>=A[i] and cnt[A[i]]==0:
            ft.add(A[i],-1)
        A[i] = x
        if Q>=x and cnt[x]==0:
            ft.add(x,1)
        cnt[x]+=1
        
        ng = -1
        ok = Q+1
        while ok-ng>1:
            m = ng+(ok-ng)//2
            if ft.sum(0,m+1)<m+1:
                ok = m
            else:
                ng = m
        print(ok)

if __name__ == "__main__":
    main()