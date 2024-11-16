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
    N,M,L = myin_sp_i()
    A = myin_sp_i()
    B = myin_sp_i()
    BB = [(b,i) for i,b in enumerate(B)]
    BB.sort()
    cannot_a = [set() for i in range(N)]
    for i in range(L):
        c,d = myin_sp_i()
        c-=1
        d-=1
        cannot_a[c].add(d)
    ans = 0
    for i in range(N):
        for j in range(M)[::-1]:
            if BB[j][1] not in cannot_a[i]:
                ans = max(ans,A[i]+BB[j][0])
                break
    print(ans)

if __name__ == "__main__":
    main()