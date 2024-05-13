N = int(input())
S=input()
op = ["A","B"]
switch = 0
ans=""
for i in reversed(range(N)):
    if(switch!=int(S[i])):
        ans+=(i+1)*op[switch]
        switch^=1
print(len(ans)) 
print(ans)