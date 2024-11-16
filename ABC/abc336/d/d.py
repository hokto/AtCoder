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
    A = myin_sp_i()
    L = [1]*N
    R = [1]*N
    head = 0
    tail = 0
    while tail<N:
        while tail<N and A[tail]>=tail-head+1:
            L[tail]=tail-head+1
            tail+=1
        if tail==N:
            break
        while head<tail and A[tail]<tail-head+1:
            head+=1
    head = N-1
    tail = N-1
    while head>=0:
        while head>=0 and A[head]>=tail-head+1:
            R[head]=tail-head+1
            head-=1
        if head<0:
            break
        while head<tail and A[head]<tail-head+1:
            tail-=1
    ans = 1
    for i in range(N):
        ans=max(ans,min(L[i],R[i]))
    print(ans)

if __name__ == "__main__":
    main()