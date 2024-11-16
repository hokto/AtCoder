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
    L = []
    R = []
    for i in range(N):
        A,S = myin_sp_s()
        A = int(A)
        if S=="L":
            L.append(A)
        else:
            R.append(A)
    ans = 0
    for i in range(len(L)-1):
        ans+=abs(L[i]-L[i+1])
    for i in range(len(R)-1):
        ans+=abs(R[i]-R[i+1])
    print(ans)
if __name__ == "__main__":
    main()