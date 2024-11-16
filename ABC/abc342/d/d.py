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

def prime_fact(x):
    primes = []
    y = 2
    while y*y<=x:
        cnt = 0
        while x%y==0:
            cnt+=1
            x//=y
        primes.append((y,cnt))
        y+=1
    if x!=1:
        primes.append((x,1))
    return primes
def main():
    from collections import defaultdict
    N = int(myin())
    A = myin_sp_i()
    num = defaultdict(int)
    for a in A:
        if a==0:
            num[a]+=1
            continue
        primes = prime_fact(a)
        d = 1
        for p,c in primes:
            if c%2==1:
                d*=p
        num[d]+=1
    
    ans = N*(N-1)//2-(N-num[0])*(N-num[0]-1)//2
    for n,c in num.items():
        if n==0:
            continue
        ans+=c*(c-1)//2
    print(ans)

if __name__ == "__main__":
    main()