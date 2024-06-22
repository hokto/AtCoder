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
    MOD = 998244353
    N = int(myin())
    B = N
    ans = 0
    x = N
    d = 1
    H = len(str(N))
    while B>0:
        if B&1>0:
            ans = (ans*pow(10,d*H,MOD))%MOD
            ans=(ans+x)%MOD
            #print(d)
            #print(ans)
        x = (x*pow(10,d*H,MOD)+x)%MOD
        d*=2
        #print(x)
        B>>=1
    print(ans)

if __name__ == "__main__":
    main()