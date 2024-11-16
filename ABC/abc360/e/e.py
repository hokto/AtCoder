from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    from atcoder.math import inv_mod
    import math
    # 左端か否かで考える
    # 左端以外は同様の操作になることから等確率で黒色があるはずなので，左端の確率pに対しそれぞれ(1-p)/(N-1)(\therefore (1-p)/(N-1)*(N-1)=1-p)
    # dp[k]:=k回の操作後に左端に黒色がある確率
    # 左端に黒色が来るためには，1. 直前にもあって左端同士を選ぶor左端以外同士を選ぶ 2.直前にはなくて左端以外のところから持ってくる の2つの可能性がある
    # 1.が起きる確率は(1+(N-1)^2)/N^2 2.が起きる確率は2/N^2
    # dp[k]=dp[k-1]*(1+(N-1)^2)/N^2+(1-dp[k-1])*2/N^2
    
    MOD = 998244353
    N,K = myin_sp_i()
    if N==1:
        print(1)
        exit()
    N_square_inv = inv_mod(N*N,MOD)
    pr = 1
    for k in range(K):
        pr=(pr*(1+(N-1)*(N-1))+(1-pr)*2)%MOD*N_square_inv%MOD
    ans=pr+(1-pr)*inv_mod(N-1,MOD)*(N*(N+1)*inv_mod(2,MOD)-1)
    print(ans%MOD)
if __name__ == "__main__":
    main()