N = int(input())
A = list(map(int,input().split()))
ans=0
def dfs(groups_idx,d,kind):
    global ans
    groups = [[] for i in range(N)]
    if d == 3*N:
        for i,idx in enumerate(groups_idx):
            groups[idx].append(A[i])
        ac_flag = True
        for group in groups:
            if not(group[0]+group[1]>group[2] and group[1]+group[2]>group[0] and group[2]+group[0]>group[1]):
                ac_flag=False
                return
        ans+=1
        return
    for i in range(N):
        groups_idx[d] = i
        if kind[i]==3:
            continue
        kind[i] += 1
        dfs(groups_idx,d+1,kind)
        kind[i]-=1

dfs([0 for i in range(3*N)],0,{i:0 for i in range(N)})
for i in range(N):
    ans//=i+1
print(ans)