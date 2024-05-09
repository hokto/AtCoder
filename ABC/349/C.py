S=input().upper()
T=input()
if T[-1]=="X":
    idx0=0
    for c in S:
        if T[idx0]==c:
            idx0+=1
        if idx0==2:
            print("Yes")
            exit()
idx=0
ok=False
for c in S:
    if T[idx]==c:
        idx+=1
    if idx==len(T):
        print("Yes")
        exit()
print("No")