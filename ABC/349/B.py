S=input()
N=len(S)
dict={}
for c in S:
    if c in dict:
        dict[c]+=1
    else:
        dict[c]=1
cnt = [0 for i in range(N+1)]
for k,v in dict.items():
    cnt[v]+=1
for i in range(1,N+1):
    if not(cnt[i]==0 or cnt[i]==2):
        print("No")
        exit()
print("Yes")
