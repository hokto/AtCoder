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
    T = myin()
    N = len(S)
    M = len(T)
    for i in range(min(N,M)):
        if S[i]!=T[i]:
            print(i+1)
            return
    if N==M:
        print(0)
    else:
        print(min(N,M)+1)

if __name__ == "__main__":
    main()