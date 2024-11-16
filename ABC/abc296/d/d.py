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
    INF = 10**14
    ng = M-1
    ans = INF
    for a in range(1,int(M**0.5)+10):
        b = (M+a-1)//a
        if a<=N and b<=N:
            ans = min(ans,a*b)
    if ans>=INF:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()