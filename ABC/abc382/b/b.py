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
    N,D = myin_sp_i()
    S = list(myin())
    d = 0
    for i in range(N)[::-1]:
        if S[i]=="@" and d<D:
            S[i]="."
            d+=1
    print("".join(S))

if __name__ == "__main__":
    main()