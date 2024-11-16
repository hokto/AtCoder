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
    from collections import defaultdict
    S= myin()
    L = len(S)
    l_accum = [[0]*26 for i in range(L+1)]
    r_accum = [[0]*26 for i in range(L+1)]
    for i in range(L):
        for j in range(26):
            c = 0
            if S[i]==chr(ord("A")+j):
                c=1
            l_accum[i+1][j]=l_accum[i][j]+c
    
    for i in range(L)[::-1]:
        for j in range(26):
            c = 0
            if S[i]==chr(ord("A")+j):
                c=1
            r_accum[i][j]=r_accum[i+1][j]+c
    ans = 0
    for i in range(L):
        for j in range(26):
            ans+=l_accum[i][j]*r_accum[i+1][j]
    print(ans)

if __name__ == "__main__":
    main()