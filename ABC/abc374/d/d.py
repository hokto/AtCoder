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
    import math
    N,S,T = myin_sp_i()
    P = []
    for i in range(N):
        P.append(myin_sp_i())
    
    used = [False]*N
    INF = 10**15
    def dfs(x,y,n):
        if n==N:
            return 0.0
        ans = INF
        for i in range(N):
            if used[i]: continue
            used[i] = True
            d = math.sqrt((P[i][0]-P[i][2])**2+(P[i][1]-P[i][3])**2)/T
            res = math.sqrt((P[i][0]-x)**2+(P[i][1]-y)**2)/S+d+dfs(P[i][2],P[i][3],n+1)
            ans = min(res,ans)
            res = math.sqrt((P[i][2]-x)**2+(P[i][3]-y)**2)/S+d+dfs(P[i][0],P[i][1],n+1)
            ans = min(res,ans)
            used[i] = False
        return ans
    print(round(dfs(0,0,0),7))

if __name__ == "__main__":
    main()