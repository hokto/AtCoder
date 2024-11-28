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
    from collections import defaultdict
    R,C,K = myin_sp_i()
    item = [[0]*C for _ in range(R)]
    for k in range(K):
        r,c,v = myin_sp_i()
        r-=1
        c-=1
        item[r][c]=v
    dp2 = [[0]*4 for _ in range(C)]
    if item[0][0]>0:
        dp2[0][1] = item[0][0]
    dp1 = [0]*C
    for i in range(R):
        for j in range(C):
            v = item[i][j]
            if i-1>=0:
                dp2[j][0]=max(dp2[j][0],dp1[j])
                if v>0:
                    dp2[j][1]=max(dp2[j][1],dp1[j]+v)
            for k in range(4):
                if j-1>=0:
                    dp2[j][k] = max(dp2[j][k],dp2[j-1][k])
                    if v>0 and k!=3:
                        dp2[j][k+1]=max(dp2[j][k+1],dp2[j-1][k]+v)
            dp1[j] = max(dp2[j])
        dp2 = [[0]*4 for _ in range(C)]
    print(dp1[-1])

if __name__ == "__main__":
    main()