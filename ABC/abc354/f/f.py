from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def dfs(v,is_lis,d,D,G,ans):
    if is_lis[v]!=-1:
        return is_lis[v]
    if d==D:
        is_lis[v]=True
        ans.append(v+1)
        return True
    f = False
    for vv in G[v]:
        f|=dfs(vv,is_lis,d+1,D,G,ans)
    if f:
        ans.append(v+1)
    is_lis[v]=f
    return f
def main():
    import bisect
    T = int(myin())
    for _ in [0]*T:
        N = int(myin())
        A = myin_sp_i()
        dp = []
        v_sets = []
        G = [[]for _ in [0]*N]
        for i,a in enumerate(A):
            if len(dp)==0 or dp[-1]<a:
                dp.append(a)
                v_sets.append([i])
                if len(dp)>1:
                    v_sets2 = v_sets[-2]
                    l = -1
                    r = len(v_sets2)
                    while r-l>1:
                        m = l+(r-l)//2
                        if A[v_sets2[m]]<a:
                            r = m
                        else:
                            l = m
                    for k in range(r,len(v_sets2)):
                        G[v_sets2[k]].append(i)
            else:
                idx = bisect.bisect_left(dp,a)
                dp[idx]=a
                v_sets[idx].append(i)
                if idx>0:
                    v_sets2 = v_sets[idx-1]
                    l = -1
                    r = len(v_sets2)
                    while r-l>1:
                        m = l+(r-l)//2
                        if A[v_sets2[m]]<a:
                            r = m
                        else:
                            l = m
                    for k in range(r,len(v_sets2)):
                        G[v_sets2[k]].append(i)
        D = len(dp)
        is_lis= [-1 for _ in [0]*N]
        ans=[]
        for i in range(N):
            dfs(i,is_lis,1,D,G,ans)
            #print(ans)
        print(len(ans)) 
        print(*sorted(ans))
if __name__ == "__main__":
    main()