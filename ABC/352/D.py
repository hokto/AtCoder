from atcoder.segtree import SegTree
N,K=list(map(int,input().split()))
P=list(map(int,input().split()))
idx = dict(zip(range(N),P))
diff = []
for i in range(1,N):
    diff.append(idx[i+1]-idx[i])

st = SegTree() 
    