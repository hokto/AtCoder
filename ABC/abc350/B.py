N,Q = list(map(int,input().split()))
T = list(map(int,input().split()))
ans = [1 for i in range(N)]
for t in T:
    t-=1
    ans[t]=(ans[t]+1)%2
print(sum(ans))
