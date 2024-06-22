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
    N,M = myin_sp_i()
    ans = 0
    MOD = 998244353
    x = 1
    while x<=M:
        if (M&x)>0:
            ans = (ans+N//(x*2)*x+min(N%(x*2),x))%MOD
            #print(N//(x*2))
            #print(ans)
        N-=x
        x*=2
    print(ans)
if __name__ == "__main__":
    main()