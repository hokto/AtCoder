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
    num = [[] for i in range(N+1)]
    for i,a in enumerate(A):
        num[a].append(i)
    ans = 0
    for i in range(N+1):
        M = len(num[i])
        for j in range(M-1):
            ans+=(num[i][j+1]-num[i][j]-1)*(M-1-j)*(j+1)
    print(ans)

if __name__ == "__main__":
    main()