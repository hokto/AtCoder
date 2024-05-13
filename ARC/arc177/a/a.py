coins = list(map(int,input().split()))
yen = [1,5,10,50,100,500]
coins.reverse()
yen.reverse()
N = int(input())
X = list(map(int,input().split()))
ans = True
for x in X:
    for i in range(6):
        while coins[i]>0 and x>=yen[i]:
            x-=yen[i]
            coins[i]-=1
    if x!=0:
        ans = False
        break
if ans:
    print("Yes") 
else:
    print("No")