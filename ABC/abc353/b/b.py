N,K = list(map(int,input().split()))
A=list(map(int,input().split()))

ans = 0
sum = 0
for i in range(N):
    if(sum+A[i]<=K):
        sum+=A[i]
    else:
        sum = A[i]
        ans+=1
if(sum!=0): ans+=1
print(ans)