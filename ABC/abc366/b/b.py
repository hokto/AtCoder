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
    M = 0
    S=[]
    for i in range(N):
        T = myin()
        M=max(M,len(T))
        S.append(T)
    ans = [[""]*N for i in range(M)]
    m = 0
    for j in reversed(range(N)):
        T = S[N-1-j]
        m = max(m,len(T))
        for i in range(m):
            if len(T)<=i:
                ans[i][j]="*"
            else:
                ans[i][j]=T[i]
    for i in range(M):
        print("".join(map(str,ans[i])))

if __name__ == "__main__":
    main()