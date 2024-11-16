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
    def max_subprefix(s):
        length = 0
        for i in range(len(s)):
            if s[i]==T[length]:
                length+=1
            if length==M: break
        return length
    
    def max_subsuffix(s):
        length = 0
        for i in range(len(s))[::-1]:
            if s[i]==T[M-1-length]:
                length+=1
            if length==M: break
        return length
    N,T = myin_sp_s()
    N = int(N)
    M = len(T)
    S = []
    from atcoder.fenwicktree import FenwickTree
    ft  = FenwickTree(M+1)
    for i in range(N):
        s = myin()
        ft.add(max_subsuffix(s),1)
        S.append(max_subprefix(s))
    ans = 0
    for s_len in S:
        ans+=ft.sum(M-s_len,M+1)
    print(ans)

if __name__ == "__main__":
    main()