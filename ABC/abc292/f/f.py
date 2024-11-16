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
    import math
    A,B = myin_sp_i()
    if A>B:
        A,B = B,A
    ok = A
    ng = A**2+B**2
    err = 10**-9
    def f(x):
        if 3*(x**2)>4*(A**2):
            return False
        theta = math.acos(A/x)
        if math.cos(math.pi/6.0-theta)*x<=B:
            return True
        else:
            return False
    while ng-ok>err:
        m = ok+(ng-ok)/2
        if f(m):
            ok = m
        else:
            ng = m
    print(round(ok,10))
        

if __name__ == "__main__":
    main()