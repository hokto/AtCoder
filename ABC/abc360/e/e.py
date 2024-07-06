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
    MOD = 998244353
    #print(((65+32*2+32*3)*inv_mod(pow(3*3,2,MOD),MOD))%MOD)
    N,K = myin_sp_i()
    A = (1+(N-1)*(N-1))%MOD # 初期地点にある確率
    B = 2 # それ以外にあるそれぞれの確率(全て同じ)
    x = N*N%MOD
    for k in range(K-1):
        B = (B*B+(x-B)*(A+B*(N-2)))%MOD
        A = (A*A+(x-A)*(B*(N-1)))%MOD
        x = x*N*N%MOD
    ans = (A+(N*(N+1)*inv_mod(2,MOD)-1)*B)*inv_mod(x,MOD)%MOD
    print(ans)

if __name__ == "__main__":
    main()