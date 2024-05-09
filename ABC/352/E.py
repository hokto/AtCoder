N,M = list(map(int,input().split()))
info = []
find = [0 for i in range(N)]
for m in range(M):
    K,C = list(map(int,input().split()))
    A= list(map(int,input().split()))
    for a in A:
        find[a-1]=1
    info.append((C,K,A))
edges = sorted(info)
for i in range(N):
    if find[i]==0:
        print(-1)
        exit()
from atcoder.dsu import DSU
dsu = DSU(N)
cnt = 0
ans = 0
for C,K,A in edges:
    for k1 in range(K):
        u = A[k1]
        u-=1
        for k2 in range(k1+1,K):
            v = A[k2]
            v-=1
            if not dsu.same(u,v):
                dsu.merge(u,v)
                ans+=C
                cnt+=1
                if cnt == N-1:
                    print(ans)
                    exit()
            
            