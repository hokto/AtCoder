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
    S = myin()
    N = int(myin())
    L = len(S)
    res = 0
    for i in range(L):
        if S[i]=="1":
            res+=2**(L-1-i)
    if N<res:
        print(-1)
        return
    for i in range(L):
        if S[i]=="?" and res+2**(L-1-i)<=N:
            res+=2**(L-1-i)
    print(res)

if __name__ == "__main__":
    main()