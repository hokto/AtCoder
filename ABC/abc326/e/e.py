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
    N = int(myin())
    A = myin_sp_i()
    inv_N = pow(N,MOD-2,MOD)
    ans = 0
    p = inv_N
    for a in A:
        ans+=a*p
        p+=p*inv_N
        ans%=MOD
        p%=MOD
    print(ans)
if __name__ == "__main__":
    main()