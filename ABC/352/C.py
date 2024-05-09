N = int(input())
AB = []
for i in range(N):
    AB.append(list(map(int,input().split())))

sum = sum(map(lambda x:x[0],AB))
ans = 0
for i in range(N):
    ans = max(ans,sum-AB[i][0]+AB[i][1]) 
print(ans)