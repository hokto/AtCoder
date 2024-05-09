N,M = list(map(int,input().split()))
A=list(map(int,input().split()))

dp = [[[-1 for k in range(2)] for j in range(M+1)] for i in range(N+1)]
dp[0][0][0] = 0
dp[0][0][1] = 0
for i in range(N):
    for j in range(M+1):
        for k in range(2):
            # 宿題しないパターン
            if dp[i][j][k]!=-1:
                dp[i+1][j][0] = max(dp[i+1][j][0],dp[i][j][k]+A[i])
            # 宿題するパターン
            if k==0 and j!=M:
                if dp[i][j][0]!=-1:
                    dp[i+1][j+1][1] = max(dp[i+1][j+1][1],dp[i][j][0])
        if dp[i][M][0]!=-1:
            dp[i+1][M][0] = max(dp[i+1][M][0],dp[i][M][0]+A[i])
        dp[i+1][M][1] = max(dp[i+1][M][1],dp[i][M][1])
#for dpp in dp:
    #print(dpp)
print(max(dp[N][M]))