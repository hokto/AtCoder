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
    N = int(myin())
    dp = [0]*(1<<N)
    D = []
    for i in range(N-1):
        D.append(myin_sp_i())
    for bit in range(1<<N):
        for i in range(N):
            if (bit&(1<<i))>0: continue
            for j in range(i+1,N):
                if (bit&(1<<j))>0: continue
                dp[bit|(1<<i)|(1<<j)]=max(dp[bit|(1<<i)|(1<<j)],dp[bit]+D[i][j-1-i])
    print(dp[-1])
    

if __name__ == "__main__":
    main()