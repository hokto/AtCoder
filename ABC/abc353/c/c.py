N = int(input())
A = list(map(int,input().split()))
A = sorted(A)
sum = [0 for i in range(N+1)]
MOD = 10**8
for i in range(N):
    sum[i+1] = sum[i]+A[i]
    
ans = 0
for i in range(N):
    ans+=(N-i-1)*A[i]+(sum[N]-sum[i+1])
    head = i
    tail = N
    while tail-head>1:
        mid = head+(tail-head) //2
        if A[i]+A[mid]>=MOD:
            tail = mid
        else:
            head = mid
    ans-=(N-tail)*MOD
print(ans)
    
