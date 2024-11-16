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
    N,M = myin_sp_i()
    S = set()
    DIR = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    for i in range(M):
        a,b = myin_sp_i()
        S.add((a,b))
        for di,dj in DIR:
            if 1<=a+di<=N and 1<=b+dj<=N:
                S.add((a+di,b+dj))
    print(N*N-len(S))

if __name__ == "__main__":
    main()