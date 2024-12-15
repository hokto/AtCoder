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
    from atcoder.segtree import SegTree
    N = int(myin())
    A = myin_sp_i()
    ODD = []
    EVEN = []
    for i in range(N):
        if A[i]&1:
            ODD.append(A[i])
        else:
            EVEN.append(A[i])
    ans = sum(ODD)*sum(EVEN)//2
    def solve(S):
        # 2の冪乗の大きさでソート
        M = len(S)
        B = []
        e_sum = 0
        q_sum = 0
        for i in range(M):
            e = 0
            while 2**(e+1)<=S[i]:
                e+=1
            e_sum+=2**e
            q = S[i]-(2**e)
            q_sum+=q
            B.append((e,q,S[i]))
        B.sort()
        res = 0
        for i in range(M):
            e,q,x = B[i]
            res+=e_sum//(2**e)+q_sum+(M-i)*q
            e_sum-=2**e
            q_sum-=q
        return res
    print(solve(ODD))
    print(solve(EVEN))
    ans+=solve(ODD)
    ans+=solve(EVEN)
    print(ans)

if __name__ == "__main__":
    main()