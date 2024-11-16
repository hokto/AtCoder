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
    visited = [False]*N
    ans = []
    def dfs(v):
        nonlocal ans
        if visited[v]:
            ans.append(v+1)
            return v
        visited[v]=True
        res = dfs(A[v]-1)
        if res>=0 and res!=v:
            ans.append(v+1)
            return res
        return -1
    for i in range(N):
        if not visited[i]:
            dfs(i)
            if ans:
                break
    print(len(ans))
    print(*reversed(ans))

if __name__ == "__main__":
    main()