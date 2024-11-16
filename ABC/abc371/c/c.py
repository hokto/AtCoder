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
    from itertools import permutations
    N = int(myin())
    MG = int(myin())
    EG = []
    exist_EG = {}
    for i in range(MG):
        u,v = myin_sp_i()
        u-=1
        v-=1
        if u>v: u,v=v,u
        EG.append((u,v))
        exist_EG[(u,v)]=1
    MH = int(myin())
    EH = []
    exist_EH = {}
    for i in range(MH):
        u,v = myin_sp_i()
        u-=1
        v-=1
        if u>v: u,v=v,u
        EH.append((u,v))
        exist_EH[(u,v)]=1
    A = []
    for i in range(N-1):
        A.append(myin_sp_i())

    INF = 1<<30
    ans = INF
    base_list = list(range(N))
    for change_list in permutations(base_list):
        inv_change_list = [-1]*N
        for i in range(N):
            inv_change_list[change_list[i]]=i
        res = 0
        for (u,v) in EG:
            uu = change_list[u]
            vv = change_list[v]
            if uu>vv: uu,vv=vv,uu
            if (uu,vv) not in exist_EH:
                res+=A[uu][vv-uu-1]
        for (u,v) in EH:
            uu = inv_change_list[u]
            vv = inv_change_list[v]
            if uu>vv: uu,vv=vv,uu
            if (uu,vv) not in exist_EG:
                res+=A[u][v-u-1]
        if ans>res:
            ans = res
        #ans = min(ans,res) 
    print(ans)
if __name__ == "__main__":
    main()