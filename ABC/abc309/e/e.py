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
    N,M = myin_sp_i()
    P = myin_sp_i()
    ins = [0]*N
    for i in range(M):
        x,y = myin_sp_i()
        ins[x-1]=max(ins[x-1],y+1)
    E = [[] for i in range(N)]
    for i in range(1,N):
        E[P[i-1]-1].append(i)
    ans = 0
    def dfs(v,res_ins):
        nonlocal ans
        res_ins = max(res_ins,ins[v])
        if res_ins>0:
            ans+=1
        for vv in E[v]:
            dfs(vv,res_ins-1)
    dfs(0,0)
    print(ans)

if __name__ == "__main__":
    main()