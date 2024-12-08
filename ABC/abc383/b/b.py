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
    H,W,D = myin_sp_i()
    S = []
    floor_coor = []
    for i in range(H):
        S.append(myin())
    for i in range(H):
        for j in range(W):
            if S[i][j]==".": floor_coor.append((i,j))
    F = len(floor_coor)
    ans = 0
    for u in range(F):
        for v in range(u+1,F):
            i1,j1 = floor_coor[u]
            i2,j2 = floor_coor[v]
            res = 0
            for i in range(H):
                for j in range(W):
                    d1 = abs(i-i1)+abs(j-j1)
                    d2 = abs(i-i2)+abs(j-j2)
                    if S[i][j]=="." and (d1<=D or d2<=D):
                        res+=1
            ans = max(ans,res)
    print(ans)

if __name__ == "__main__":
    main()