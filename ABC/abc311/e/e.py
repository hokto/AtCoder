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
    H,W,N = myin_sp_i()
    holes = [[0]*W for _ in range(H)]
    for i in range(N):
        a,b = myin_sp_i()
        a-=1
        b-=1
        holes[a][b]+=1
    accum = [[0]*(W+1) for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            accum[i+1][j+1]=accum[i+1][j]+accum[i][j+1]-accum[i][j]+holes[i][j]
    ans = 0
    for i in range(H):
        accum1 = accum[i+1]
        for j in range(W):
            if holes[i][j]>0: continue
            # (i,j)を右下にする穴を含まない最大の正方形を求める
            # (i-k,j-k)を左上，(i,j)を右下にした時に穴を含まない最大のkを求める
            ok = 1
            ng = min(i,j)+2
            while ng-ok>1:
                m = ok+(ng-ok)//2
                if accum1[j+1]-accum1[j+1-m]-accum[i+1-m][j+1]+accum[i+1-m][j+1-m]==0:
                    ok = m
                else:
                    ng = m
            ans+=ok
    print(ans)

if __name__ == "__main__":
    main()