S = input()
S_rev= reversed(S)
ans = 1
x = 1
v = 0
MOD = 998244353
for c in S_rev:
    if c=="*":
        x = 1
        ans*=v
        ans%=MOD
        v=0
    else:
        v += x*int(c)
        v%=MOD
        x*=10
        x%=MOD
ans*=v
ans%=MOD
print(ans)