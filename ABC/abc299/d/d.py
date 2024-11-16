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
    ok = 0
    ng = N+1
    while ng-ok>1:
        m = ok+(ng-ok)//2
        print(f"? {m}",flush=True)
        s = int(myin())
        if s==0:
            ok = m
        else:
            ng = m
    print(f"! {ok}")

if __name__ == "__main__":
    main()