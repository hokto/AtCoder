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
    # 深さN-1の木．長さDを持つ最小の木の深さは(D+1)//2
    N,D = myin_sp_i()
    MOD = 998244353
    d_pow = [1]*(2*N+1)
    for i in range(1,2*N+1):
        d_pow[i]=(d_pow[i-1]*2)%MOD
    ans = 0
    for d in range(N-1):
        res = 0
        if d+D<=N-1:
            res+=d_pow[D+1]
        if not(2*(N-1-d)<D or D==1):
            if d+D<=N-1:
                res+=d_pow[D-1]*(D-1)
            else:
                res+=(2*(N-1-d)-D+1)*d_pow[D-1]
        ans=(ans+d_pow[d]*res)%MOD
    print(ans)

if __name__ == "__main__":
    main()