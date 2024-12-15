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
    N,c1,c2 = myin_sp_s()
    N = int(N)
    S = myin()
    T = []
    for i in range(N):
        if S[i]!=c1:
            T.append(c2)
        else:
            T.append(c1)
    print(*T,sep="")

if __name__ == "__main__":
    main()