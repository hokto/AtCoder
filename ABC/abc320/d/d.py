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
    N,M = myin_sp_i()
    G = [[] for i in range(N)]
    for i in range(M):
        a,b,x,y = myin_sp_i()
        a-=1
        b-=1
        G[a].append((b,x,y))
        G[b].append((a,-x,-y))
    st = [(0,-1,0,0)]
    ans = [(-1,-1)]*N
    while st:
        v,p,x,y = st.pop()
        if ans[v]!=(-1,-1): continue
        ans[v] = (x,y)
        for vv,dx,dy in G[v]:
            if vv == p: continue
            if ans[vv]!=(-1,-1): continue
            st.append((vv,v,x+dx,y+dy))
    for i in range(N):
        if ans[i]==(-1,-1):
            print("undecidable")
        else:
            print(*ans[i])
if __name__ == "__main__":
    main()