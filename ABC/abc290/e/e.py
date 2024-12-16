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
    index = [[] for _ in range(N+1)]
    accum = [[] for _ in range(N+1)]
    for i,a in enumerate(A):
        index[a].append(i)
    for i in range(N+1):
        M = len(index[i])
        accum[i] = [0]*(M+1)
        for j in range(M)[::-1]:
            accum[i][j] = accum[i][j+1]+(N-index[i][j])
    ans = 0
    def f(x):
        xx = x//2
        if x%2==0:
            return xx*(xx+1)
        return xx*(xx+1)+(xx+1)
    for i in range(N-1):
        ans+=f(N-1-i)
    #print(accum[2])
    for i in range(N+1):
        inv = index[i]
        if not inv: continue
        M = len(inv)
        l = 0
        r = M-1
        while l<r:
            if inv[l]+1<N-inv[r]:
                ans-=(r-l)*(inv[l]+1)
                l+=1
            else:
                ans-=(r-l)*(N-inv[r])
                r-=1
        
    print(ans)

if __name__ == "__main__":
    main()