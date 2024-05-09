L,R=list(map(int,input().split()))
l=L
r=L
ans=[]
while r!=R:
    tmp = l
    if tmp==0:
        tmp=1
        while tmp<R:
            tmp*=2
    x=1
    while tmp%2==0:
        x*=2
        tmp//=2
    y=l//x
    while x*(y+1)>R:
        x//=2
        y=l//x
    r = x*(y+1)
    ans.append([l,r])
    l=r
print(len(ans))
for ll,rr in ans:
    print(f"{ll} {rr}")