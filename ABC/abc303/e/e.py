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
    N = int(myin())
    T = [[] for i in range(N)]
    dim = [0]*N
    r = -1
    for i in range(N-1):
        u,v = myin_sp_i()
        u-=1
        v-=1
        T[u].append(v)
        T[v].append(u)
        dim[u]+=1
        dim[v]+=1
    for i in range(N):
        if dim[i]==1:
            r = i
            break
    ans = []
    def dfs(v,p,l):
        res = 1
        for vv in T[v]:
            if vv==p: continue
            res+=dfs(vv,v,(l+1)%3)
        if l==0:
            ans.append(res-1)
            return 0
        else:
            return res
    dfs(r,-1,0)
    #print(len(ans))
    print(*sorted(ans))

if __name__ == "__main__":
    main()