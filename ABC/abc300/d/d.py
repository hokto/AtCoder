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
    M = 10**6+20
    primes = []
    primes_cnt = [0]*(M+2)
    is_prime = [True]*(M+1)
    accum = 0
    for x in range(2,M):
        primes_cnt[x]=accum
        if not is_prime[x]: continue
        primes.append(x)
        accum+=1
        y = x+x
        while y<=M:
            is_prime[y]=False
            y+=x
    L = min(len(primes),1000)
    ans = 0
    for i in range(L):
        a = primes[i]
        for j in range(i+1,L):
            b = primes[j]
            c = int((N//(a**2*b))**0.5)
            ans+=max(primes_cnt[c+1]-primes_cnt[b+1],0)
    print(ans)

if __name__ == "__main__":
    main()