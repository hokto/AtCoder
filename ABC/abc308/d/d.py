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
    H,W = myin_sp_i()
    S = []
    for i in range(H):
        S.append(myin())
    SNUKE = "snuke"
    INF = H*W+100
    def dfs():
        DIR = [(1,0),(-1,0),(0,1),(0,-1)]
        dist = [INF]*(H*W)
        if SNUKE[0]!=S[0][0]:
            return INF
        st = [(0,0)]
        while st:
            d,v = st.pop()
            j = v%W
            i = v//W
            if dist[v]!=INF: continue
            dist[v] = d
            for di,dj in DIR:
                ni = i+di
                nj = j+dj
                vv = ni*W+nj
                if not(0<=ni<H and 0<=nj<W and dist[vv]==INF): continue
                if SNUKE[(d+1)%5]!=S[ni][nj]: continue
                st.append((d+1,vv))
        return dist[-1]
    if dfs()<INF:
        print("Yes")
    else:
        print("No")
    #print(dfs())

if __name__ == "__main__":
    main()