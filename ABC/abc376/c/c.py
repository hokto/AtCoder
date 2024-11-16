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
    N = int(myin())
    A=  myin_sp_i()
    B= myin_sp_i()
    A.sort()
    B.sort()
    ng = -1
    ok = N
    def f(x):
        j = 0
        for i in range(N):
            if x==i:
                continue
            if A[i]>B[j]:
                return False
            j+=1
        return True
    while ok-ng>1:
        m = ng+(ok-ng)//2
        if f(m):
            ok = m
        else:
            ng = m
    if ok==N:
        print(-1)
    else:
        print(A[ok])

if __name__ == "__main__":
    main()