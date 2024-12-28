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
    from itertools import combinations
    N,K = myin_sp_i()
    A = myin_sp_i()
    if K<N//2:
        ans = 0
        for comb in combinations(A,K):
            res = 0
            for v in comb:
                res^=v
            ans = max(ans,res)
        print(ans)
    else:
        all_xor = 0
        for a in A:
            all_xor^=a
        K = N-K
        ans = 0
        for comb in combinations(A,K):
            res = 0
            for v in comb:
                res^=v
            ans = max(ans,all_xor^res)
        print(ans)

if __name__ == "__main__":
    main()