import math
N,K = list(map(int,input().split()))
A = list(map(int,input().split()))
diff = [0 for i in range(K-1)]
for i in range(K-1):
    diff[i] = A[i+1]-A[i]

gcd = 0
for v in diff:
    gcd = math.gcd(gcd,v)
ans = []
for i in range(1,int(math.sqrt(gcd))+1):
    if gcd%i == 0:
        if (A[-1]-A[0])//i+1 <= N:
            ans.append(i)
        if gcd//i!=i:
            j = gcd//i
            if (A[-1]-A[0])//j+1 <= N:
                ans.append(j)

print(len(ans))
print(" ".join(map(str,sorted(ans))))