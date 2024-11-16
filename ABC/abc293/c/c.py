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
    H,W = myin_sp_i()
    A = []
    for i in range(H):
        A.append(myin_sp_i())
    ans = 0
    def dfs(i,j,S):
        nonlocal ans
        if i==H-1 and j==W-1:
            ans+=1
            return
        if i+1<H and A[i+1][j] not in S:
            S.add(A[i+1][j])
            dfs(i+1,j,S)
            S.remove(A[i+1][j])
        if j+1<W and A[i][j+1] not in S:
            S.add(A[i][j+1])
            dfs(i,j+1,S)
            S.remove(A[i][j+1])
    S = set()
    S.add(A[0][0])
    dfs(0,0,S)
    print(ans)

if __name__ == "__main__":
    main()