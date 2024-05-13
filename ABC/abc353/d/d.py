N = int(input())
A = list(map(int,input().split()))
MOD = 998244353
digit = [0 for i in range(10)]
sum = [0 for i in range(N+1)]
for i in range(N):
    sum[i+1] = sum[i] + A[i]
for a in A:
    a_s = str(a)
    digit[len(a_s)-1]+=1
ans = 0
for i in range(N):
    ans=(ans+sum[N]-sum[i+1])%MOD
    digit[len(str(A[i]))-1]-=1
    for d in range(10):
        ans=(ans+digit[d]*A[i]*(10**(d+1)))%MOD
print(ans)