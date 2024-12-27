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
    MOD = 10**9+7
    H,W,K = myin_sp_i()
    K-=1
    if W==1:
        print(1)
        return
    dp = [[0]*W for _ in range(H+1)] # dp[i][j]:=高さiで縦棒j番目にいるようなあみだの数
    dp[0][0] = 1
    for i in range(H):
        for bit in range(1<<(W-1)):
            isok = True
            for k in range(W-2):
                if bit&(1<<k) and bit&(1<<(k+1)):
                    # 2つが隣合う場合はあみだの制約を満たなさない
                    isok = False
            if not isok: continue
            for k in range(W-1):
                if bit&(1<<k):
                    # kとk+1が繋がる
                    dp[i+1][k]+=dp[i][k+1]
                    dp[i+1][k]%=MOD
                    dp[i+1][k+1]+=dp[i][k]
                    dp[i+1][k+1]%=MOD
                else:
                    if k==0:
                        dp[i+1][k]+=dp[i][k]
                        dp[i+1][k]%=MOD
                    elif k==W-2:
                        dp[i+1][k+1]+=dp[i][k+1]
                        dp[i+1][k+1]%=MOD
                    if k!=0 and (bit&(1<<(k-1)))==0:
                        dp[i+1][k]+=dp[i][k]
                        dp[i+1][k]%=MOD
                        
    print(dp[-1][K])
if __name__ == "__main__":
    main()