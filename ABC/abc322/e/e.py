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
    N,K,P = myin_sp_i()
    query = []
    INF = 10**9*100+10
    for i in range(N):
        query.append(myin_sp_i())
    dp = [INF]*((P+1)**K)
    dp[0] = 0
    for i in range(N):
        for j in range((P+1)**K)[::-1]:
            param = [0]*K
            idx = 0
            jj = j
            while jj>0:
                param[idx]=jj%(P+1)
                jj//=P+1
                idx+=1
            for k in range(K):
                param[k]=min(P,param[k]+query[i][k+1])
            x = 0
            for k in range(K):
                x+=param[k]*((P+1)**k)
            dp[x]=min(dp[x],dp[j]+query[i][0])
    if dp[-1]>=INF:
        print(-1)
    else:
        print(dp[-1])

if __name__ == "__main__":
    main()