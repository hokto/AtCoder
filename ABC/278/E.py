N = int(input())
S = []
for i in range(N):
    S.append(input())
# dp[T][i]:=集合Tの中でiから始めたときに太郎くんが勝つならTrue,負けるならFalse
INIT = False if N%2==1 else True
dp = [[False for i in range(N)]for j in range(1<<N)]

for i in range(N):
    dp[1<<i][i] = not(INIT)

for T in range(1<<N):
    for i in range(N):
        if((T&(1<<i))==0):
            if(T.bit_count()%2!=N%2):
                dp[T|(1<<i)][i]=True
            for j in range(N):
                if(i!=j and ((T&(1<<j))>0) and S[i][-1]==S[j][0]):
                    # 太郎くんのターン 
                    if(T.bit_count()%2==N%2):
                        dp[T|(1<<i)][i]|=dp[T][j]
                    else:
                        dp[T|(1<<i)][i]&=dp[T][j]

#print(dp)                
ans = False
for i in range(N):
    ans|=dp[-1][i]
if ans:
    print("First")
else:
    print("Second")
