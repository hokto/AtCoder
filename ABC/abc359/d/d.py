from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
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
    MOD = 998244353
    N,K = myin_sp_i()
    S = myin()
    dp = [[0]*(1<<K) for i in range(N+1)] # dp[i][j]:=i番目までで直前の長さKの集合がjとなる文字列の個数(a=0,b=1とする)
    dp[0][0] = 1 # 一方からのみ遷移できるように片方だけ1
    for i in range(N):
        for j in range(1<<K):
            if i<K-1:
                if S[i]!="B":
                    dp[i+1][j]+=dp[i][j]
                    dp[i+1][j]%=MOD
                if S[i]!="A":
                    dp[i+1][j|(1<<i)]+=dp[i][j]
                    dp[i+1][j|(1<<i)]%=MOD
            elif i==K-1:
                if S[i]!="B":
                    bit = j
                    bit1 = format(bit,"b").zfill(K)[:K//2] # 上位K//2bitを取得
                    bit2 = "".join(reversed(format(bit,"b").zfill(K)[(K+1)//2:K])) # 下位K//2bitを取得
                    if bit1!=bit2:
                        dp[i+1][bit]+=dp[i][j]
                        dp[i+1][bit]%=MOD
                    
                if S[i]!="A":
                    bit = j|(1<<(K-1))
                    bit1 = format(bit,"b").zfill(K)[:K//2] # 上位K//2bitを取得
                    bit2 = "".join(reversed(format(bit,"b").zfill(K)[(K+1)//2:K])) # 下位K//2bitを取得
                    if bit1!=bit2:
                        dp[i+1][bit]+=dp[i][j]
                        dp[i+1][bit]%=MOD
            else:
                if S[i]!="B":
                    bit = j>>1
                    bit1 = format(bit,"b").zfill(K)[:K//2] # 上位K//2bitを取得
                    bit2 = "".join(reversed(format(bit,"b").zfill(K)[(K+1)//2:K])) # 下位K//2bitを取得
                    if bit1!=bit2:
                        dp[i+1][bit]+=dp[i][j]
                        dp[i+1][bit]%=MOD
                    
                if S[i]!="A":
                    bit = (j>>1)|(1<<(K-1))
                    bit1 = format(bit,"b").zfill(K)[:K//2] # 上位K//2bitを取得
                    bit2 = "".join(reversed(format(bit,"b").zfill(K)[(K+1)//2:K])) # 下位K//2bitを取得
                    if bit1!=bit2:
                        dp[i+1][bit]+=dp[i][j]
                        dp[i+1][bit]%=MOD
    #print(dp)
    print(sum(dp[-1])%MOD)
            
if __name__ == "__main__":
    main()