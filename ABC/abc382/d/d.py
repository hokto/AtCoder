from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    ans = []
    N,M = myin_sp_i()
    def dfs(i,A):
        if i==N:
            if A[-1]>M: return False
            ans.append(" ".join(map(str,A[1:])))
            return True
        isok = False
        for k in range(10+1):
            A[i+1] = A[i]+k+10
            f = dfs(i+1,A)
            if not f: break
            isok = True
        return isok
    dfs(0,[-9]*(N+1))
    print(len(ans))
    print(*ans,sep="\n")

if __name__ == "__main__":
    main()