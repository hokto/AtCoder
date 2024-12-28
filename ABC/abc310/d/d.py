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
    N,T,M = myin_sp_i()
    hate = [0]*N
    for _ in range(M):
        a,b = myin_sp_i()
        a-=1
        b-=1
        hate[a]|=1<<b
        hate[b]|=1<<a
    
    teams = []
    ans = 0
    def dfs(now):
        nonlocal ans,teams
        if now==N:
            if len(teams)==T:
                ans+=1
            return
        for i in range(len(teams)):
            if (teams[i] & hate[now])==0:
                teams[i]^=1<<now
                dfs(now+1)
                teams[i]^=1<<now
        if len(teams)<T:
            teams.append(1<<now)
            dfs(now+1)
            teams.pop()
    dfs(0)
    print(ans)

if __name__ == "__main__":
    main()