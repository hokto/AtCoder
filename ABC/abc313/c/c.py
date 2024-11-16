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
    s = sum(A)
    ave = s//N
    r = s%N
    B = [ave]*(N-r)+[ave+1]*r
    A.sort()
    ans = 0
    for i in range(N):
        if A[i]<B[i]:
            ans+=B[i]-A[i]
    print(ans)

if __name__ == "__main__":
    main()