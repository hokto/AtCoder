N = int(input())
A = list(map(int,input().split()))
idx = dict(zip(A,range(N)))
#print(idx)
ans = []
for i in range(N):
    idx_i = idx[i+1]
    if idx_i != i:
        ans.append(f"{i+1} {idx_i+1}")
        A[i],A[idx_i]=A[idx_i],A[i]
        idx[i+1] = i
        idx[A[idx_i]] = idx_i
    #print(idx)
print(len(ans))
print("\n".join(ans))