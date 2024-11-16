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
    from itertools import accumulate
    from bisect import bisect_right
    N,Q = myin_sp_i()
    R = sorted(myin_sp_i())
    accum = list(accumulate(R))
    for q in range(Q):
        X = int(myin())
        print(bisect_right(accum,X))
if __name__ == "__main__":
    main()