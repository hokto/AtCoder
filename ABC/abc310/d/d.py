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
    N,T,M = myin_sp_i()
    E = [[] for i in range(N)]
    for i in range(M):
        a,b = myin_sp_i()
        a-=1
        b-=1
        E[a].append(b)
    vio_select = [[0]*N for i in range(N)]
    team_size = [0]*T
    ans = 0
    def dfs(v,i,team_cnt):
        nonlocal ans
        if T-team_cnt>N-v:
            return
        if v==N:
            ans+=1
            return
        if v!=0:
            for vv in E[v-1]:
                vio_select[vv][i] +=1
        for j in range(T):
            if vio_select[v][j]>0: continue
            team_size[j]+=1
            if team_size[j]==1:
                dfs(v+1,j,team_cnt+1)
            else:
                dfs(v+1,j,team_cnt)
            team_size[j]-=1
        if v!=0:
            for vv in E[v-1]:
                vio_select[vv][i] -=1
        
    dfs(0,0,0)
    print(ans//math.factorial(T))

if __name__ == "__main__":
    main()