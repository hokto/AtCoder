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
    A = myin_sp_i()
    B = myin_sp_i()
    ng = 0
    ok = 10**9+10
    def f(x):
        seller = 0
        buyer = 0
        for a in A:
            if a<=x:
                seller += 1
        for b in B:
            if b>=x:
                buyer += 1
        return seller>=buyer
    while ok-ng>1:
        m = ng+(ok-ng)//2
        if f(m):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == "__main__":
    main()