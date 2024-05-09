from atcoder.segtree import SegTree

N,Q = list(map(int,input().split()))
A= list(map(int,input().split()))
S = set()
seg = SegTree(max,0,N)
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0]==1:
        if query[1] in S:
            S.remove(query[1])
            seg.set(query[1],0)
        else:
            S.add(query[1])
            seg.set(query[1],A[query[1]])
    elif query[0]==2:
        print(f"{seg.all_prod()} 1")