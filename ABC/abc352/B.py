S = input()
T = input()
ans = []
t_i =0
for s in S:
    while T[t_i]!=s:
        t_i+=1
    ans.append(t_i+1)
    t_i+=1
print(" ".join(map(str,ans)))