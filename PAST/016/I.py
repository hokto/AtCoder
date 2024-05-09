N,M,K = list(map(int,input().split()))
A=list(map(int,input().split()))

l = 0
r = A[0]+M*(K+1)
def f(X):
    res = 0
    for i in range(N):
        res+=max(0,(X-A[i]+K-1)//K)
    return res<=M
while r-l>1:
    m = l+(r-l)//2
    if f(m):
        l = m
    else:
        r = m

cnt = 0
ans = [A[i] for i in range(N)]
for i in range(N):
    now_cnt = max(0,(l-A[i]+K-1)//K)
    cnt+=now_cnt
    ans[i]+=now_cnt*K
ans2 = sorted([[ans[i],i] for i in range(N)])
for i in range(M-cnt):
    ans2[i][0]+=K
ans3 = [0 for i in range(N)]
for i in range(N):
    ans3[ans2[i][1]] = ans2[i][0]

print(" ".join(map(str,ans3)))
