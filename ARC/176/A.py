N,M=list(map(int,input().split()))
row = [M for i in range(N)]
col = [M for j in range(N)]
not_list = {}
A = [[0 for _ in range(N)]for i in range(N)]
ans=[]
for m in range(M):
    a,b = list(map(int,input().split()))
    ans.append(f"{a} {b}")
    a-=1
    b-=1
    row[a]-=1
    col[b]-=1
    not_list[f"{a} {b}"]=1
    A[a][b]+=1
row_with_index = [[row[i],i] for i in range(N)]
col_with_index = [[col[i],i] for i in range(N)]
row_with_index.sort(key=lambda x:-x[0])
col_with_index.sort(key=lambda x:-x[0])
print(row_with_index)
for _,i in row_with_index:
    for _,j in col_with_index:
        if row[i]==0:
            break
        if f"{i} {j}" in not_list:
            continue
        if col[j]>0:
            col[j]-=1
            row[i]-=1
            ans.append(f"{i+1} {j+1}")
            A[i][j]+=1
            
print(len(ans))
print("\n".join(map(str,ans)))
print("\n".join(map(str,A)))