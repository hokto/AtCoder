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
    from collections import defaultdict
    N,K = myin_sp_i()
    A = myin_sp_i()
    dp = defaultdict(int)
    s = 1
    dp[0] = 1
    accum = 0
    MOD = 998244353
    for i,a in enumerate(A):
        accum+=a
        cur = (s-dp[accum-K])%MOD
        dp[accum]+=cur
        s+=cur
        if i==N-1:
            print(cur)

if __name__ == "__main__":
    main()