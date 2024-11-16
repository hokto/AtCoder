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
    def prime_div(x):
        res = defaultdict(int)
        b = 2
        while b*b<=x:
            while x%b==0:
                res[b]+=1
                x//=b
            b+=1
        if x!=1:
            res[x]+=1
        return res
    K = int(myin())
    primes = prime_div(K)
    def f(x):
        for p,cnt in primes.items():
            res = 0
            q = p
            while q<=x:
                res+=x//q
                q*=p
            if cnt>res: return False
        return True
    ng = 1
    ok = 10**12+10
    while ok-ng>1:
        m = ng+(ok-ng)//2
        if f(m):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == "__main__":
    main()