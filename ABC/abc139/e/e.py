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
    from collections import deque
    N = int(myin())
    A = []
    for i in range(N):
        A.append([a-1 for a in myin_sp_i()])
    idx = [0]*N
    arr = []
    used = [False]*N
    for i in range(N):
        a = A[i][idx[i]]
        if A[a][idx[a]]==i and not used[i] and not used[a]:
            arr.append((i,a))
            used[i]=used[a]=True
    ans = 0
    while arr:
        ans+=1
        tmp = []
        for u,v in arr:
            idx[u]+=1
            idx[v]+=1
            used[u]=used[v]=False
            if idx[u]<N-1:
                a = A[u][idx[u]]
                if idx[a]<N-1:
                    if A[a][idx[a]]==u and not used[u] and not used[a]:
                        tmp.append((u,a))
                        used[u]=used[a]=True
            if idx[v]<N-1:
                a = A[v][idx[v]]
                if idx[a]<N-1:
                    if A[a][idx[a]]==v and not used[v] and not used[a]:
                        tmp.append((v,a))
                        used[v]=used[a]=True
        arr = tmp
    #print(idx)
    if idx.count(N-1)!=N:
        print(-1)
    else:
        print(ans)
        

if __name__ == "__main__":
    main()