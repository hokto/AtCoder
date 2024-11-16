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
    N,K = myin_sp_i()
    P = myin_sp_i()
    for i in range(N):
        P[i]-=1
    logK = 1
    while(2**logK<=K): logK+=1
    doubling = [[-1 for _ in range(N)] for _ in range(logK)]
    for i in range(N):
        doubling[0][i] = i
        doubling[1][i] = P[i]
    for k in range(1,logK-1):
        for i in range(N):
            doubling[k+1][i]=doubling[k][doubling[k-1][doubling[k][i]]]
    print(doubling)
    ans = [P[i] for i in range(N)]
    k=0
    while K:
        if K&1:
            for i in range(N):
                ans[i] = doubling[k][ans[i]]
        k+=1
        K//=2
    for i in range(N):
        ans[i]+=1
    print(*ans)

if __name__ == "__main__":
    main()