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
    from atcoder.dsu import DSU
    H,W = myin_sp_i()
    S = []
    for i in range(H):
        S.append(myin())
    dsu = DSU(H*W)
    non_senser = 0
    for i in range(H):
        for j in range(W):
            if S[i][j]==".":
                non_senser+=1
                continue
            for di in range(-1,1+1):
                for dj in range(-1,1+1):
                    if di==dj==0: continue
                    ni = i+di
                    nj = j+dj
                    if not(0<=ni<H and 0<=nj<W and S[ni][nj]=="#"): continue
                    dsu.merge(i*W+j,ni*W+nj)
                    
    print(len(dsu.groups())-non_senser)

if __name__ == "__main__":
    main()