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
    from collections import defaultdict
    N,K = myin_sp_i()
    A = myin_sp_i()
    s = 0
    B = [0]*N
    for i in range(N):
        B[i] = A[i]-1
    S = defaultdict(int)
    k = 0
    while k<min(N,K-1):
        s = (s+B[k])%K
        S[s]+=1
        k+=1
    b = 0
    ans = 0
    for i in range(N):
        ans+=S[b]
        b=(b+B[i])%K
        S[b]-=1
        if k<N:
            s = (s+B[k])%K
            S[s]+=1
            k+=1
    print(ans)

if __name__ == "__main__":
    main()