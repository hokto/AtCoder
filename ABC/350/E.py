N,A,X,Y = list(map(int,input().split()))
X = float(X)
Y = float(Y)
memo = {}
def dp(n):
    if n==0:
        return 0
    if n in memo:
        return memo[n]
    res1 = dp(n//A)+X
    res2 = Y*6/5
    for i in range(2,7):
        res2 += (dp(n//i))/5
    memo[n] = min(res1,res2)
    return memo[n]

print(dp(N))