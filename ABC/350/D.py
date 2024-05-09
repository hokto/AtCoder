from atcoder.dsu import DSU
N,M = list(map(int,input().split()))
if M==0:
    print(0)
    exit()
friend = [0 for i in range(N)]
dsu = DSU(N)
for i in range(M):
    a,b = list(map(int,input().split()))
    a-=1
    b-=1
    friend[a]+=1
    friend[b]+=1
    dsu.merge(a,b)

ans = 0
for i in range(N):
    ans+= dsu.size(i) - friend[i]-1
print(ans//2)