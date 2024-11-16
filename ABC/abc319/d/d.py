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
    N,M = myin_sp_i()
    L = myin_sp_i()
    ng = max(L)-1
    ok = max(L)*N*2
    def f(x):
        tail = 0
        s = 0
        m = 0
        while tail<N:
            while tail<N and s+L[tail]<=x:
                s+=L[tail]+1
                tail+=1
            m+=1
            s = 0
        return m<=M
    while ok-ng>1:
        m = ng+(ok-ng)//2
        if f(m):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == "__main__":
    main()