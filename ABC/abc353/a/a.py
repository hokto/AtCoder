N = int(input())
H=list(map(int,input().split()))
ans = -1
for i in range(1,N):
    if H[0] < H[i]:
        ans = i+1
        break
print(ans)