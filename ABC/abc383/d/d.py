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
    M = 2*10**6
    prime_tb = [True]*(M+1)
    primes = []
    for i in range(2,M+1):
        if not prime_tb[i]: continue
        primes.append(i)
        j = i+i
        while j<=M:
            prime_tb[j]=False
            j+=i
    # p^2*q^2のパターンかp^8のパターンのみ
    ans = 0 
    i1 = 0
    while primes[i1]**8<=N:
        ans+=1
        i1+=1
    i2 = 0
    while (primes[0]**2)*(primes[i2]**2)<=N:
        ok = i2
        ng = len(primes)
        while ng-ok>1:
            m = ok+(ng-ok)//2
            if (primes[m]**2)*(primes[i2]**2)<=N:
                ok = m
            else:
                ng = m
        ans+=ok-i2
        i2+=1
    print(ans)

if __name__ == "__main__":
    main()