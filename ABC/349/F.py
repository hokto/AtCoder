MOD = 998244353
N,M = list(map(int,input().split()))
A = list(map(int,input().split()))

def prime_factorize(n):
    i = 2
    x = n
    factorize = {}
    while i*i<=n:
        while x%i==0:
            if i in factorize:
                factorize[i]+=1
            else:
                factorize[i]=1
            x//=i
        i+=1
    if x!=1:
        factorize[x]=1
    return factorize

M_fact = prime_factorize(M)
K = len(M_fact)
cnt = [0]*(1<<K)
for a in A:
    if M%a!=0:
        continue
    x = 1
    c = 0
    for k,v in M_fact.items():
        if a%(k**v)==0:
            c+=x
        x*=2
    cnt[c]+=1
dp = [[0 for i in range(1<<K)]for j in range(1<<K)]
dp[0][0]=1
for j in range(1<<K):
    dp[0][j]+=dp[0][j]*(pow(2,cnt[0],MOD)-1)
    dp[0][j]%=MOD
for i in range(1,1<<K):
    c = pow(2,cnt[i],MOD)-1
    for j in range(1<<K):
        dp[i][i|j]+=dp[i-1][j]*c
        dp[i][i|j]%=MOD
        dp[i][j]+=dp[i-1][j]
        dp[i][j]%=MOD
if M==1:
    print((dp[-1][-1]-1)%MOD)
else:
    print(dp[-1][-1])