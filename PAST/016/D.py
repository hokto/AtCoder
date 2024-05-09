N = int(input())
A = list(map(int,input().split()))

max_A = max(A)
ans = []
for a in A:
    v_10 = 10**10*a//max_A
    if v_10%10<5:
        v_10//=10
    else:
        v_10//=10
        v_10+=1
    ans.append(v_10)

print(" ".join(map(str,ans)))