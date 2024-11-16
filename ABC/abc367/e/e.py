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
    import math
    N,K = myin_sp_i()
    X = myin_sp_i()
    A = myin_sp_i()
    if K==0:
        print(*A)
        exit()
    doubling = []
    KK = int(math.log2(K))
    for i in range(KK+1):
        l = [0]*N
        doubling.append(l)
    for i in range(N):
        doubling[0][i] = X[i]-1
    for k in range(1,KK+1):
        for i in range(N):
            doubling[k][i] = doubling[k-1][doubling[k-1][i]]
    ans = [A[i] for i in range(N)]
    tmp = [0]*N
    k=0
    while K>0:
        if K&1>0:
            for i in range(N):
                tmp[i] = ans[i]
            for i in range(N):
                ans[i] = tmp[doubling[k][i]]
        K//=2
        k+=1
    print(*ans)

if __name__ == "__main__":
    main()