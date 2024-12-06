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
    MOD = 998244353
    S = myin()
    N = len(S)
    freq = [0]*26
    comb = [[0]*(N+1) for i in range(N+1)]
    comb[0][0] = 1
    for i in range(N):
        comb[i+1][0] = 1
        for j in range(N):
            comb[i+1][j+1]=(comb[i][j]+comb[i][j+1])%MOD
    for i in range(N):
        freq[ord(S[i])-ord("a")]+=1
    dp = [[0]*(N+1) for _ in range(26+1)] # dp[i][j]:=i種類目のアルファベットのみを使ってj文字の文字列を作れる組み合わせ
    dp[0][0] = 1 # 空文字は1種類
    for i in range(26):
        for k in range(freq[i]+1):
            for j in range(N-k+1)[::-1]:
                dp[i+1][j+k]+=dp[i][j]*comb[j+k][k]
                dp[i+1][j+k]%=MOD
    ans = 0
    for j in range(N):
        ans+=dp[-1][j+1]
        ans%=MOD
    print(ans)

if __name__ == "__main__":
    main()