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
    from heapq import heapify,heappop,heappush
    N,K = myin_sp_i()
    A = myin_sp_i()
    ok = 0
    ng = N*10**12+1
    def f(x):
        s = 0
        for a in A:
            s+=min(a,x)
        return s>=x*K
    while ng-ok>1:
        m = ok+(ng-ok)//2
        if f(m):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == "__main__":
    main()