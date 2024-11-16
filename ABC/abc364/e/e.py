from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    N,X,Y = myin_sp_i()
    MAX = 10**4
    INF = Y+10
    dp = [(INF,-1) for i in range(X+1+MAX)] # dp[i]:=甘さがiの時に選んだ品数が最大となるしょっぱさの合計のペア(品数，しょっぱさ合計)
    dp[0] = (0,0)
    AB = []
    for i in range(N):
        AB.append(myin_sp_i())
    AB.sort(lambda x:x[1])
    for A,B in AB:
        for j in reversed(range(X+1)):
            if dp[j][0]<=Y:
                if dp[j+A][1]<dp[j][1]+1:
                    dp[j+A]=(dp[j][0]+B,dp[j][1]+1)
                elif dp[j+A][1]==dp[j][1]+1 and dp[j+A][0]>dp[j][0]+B:
                    dp[j+A]=(dp[j][0]+B,dp[j][1]+1)
    ans = 0
    for i in range(X+MAX+1):
        ans=max(ans,dp[i][1])
    print(ans)
if __name__ == "__main__":
    main()