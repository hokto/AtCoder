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
    H,W,N,h,w = myin_sp_i()
    A = []
    for i in range(H):
        A.append(myin_sp_i())
    accum = [[[0]*N for _ in range(W+1)]for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            for k in range(N):
                c = 0
                if k==A[i][j]-1:
                    c =1
                accum[i+1][j+1][k] = accum[i+1][j][k]+accum[i][j+1][k]-accum[i][j][k]+c
    ans = [[0]*(W-w+1) for _ in range(H-h+1)]
    for i in range(H-h+1):
        for j in range(W-w+1):
            cnt = 0
            for k in range(N):
                if accum[i+h][j+w][k]-accum[i+h][j][k]-accum[i][j+w][k]+accum[i][j][k]<accum[-1][-1][k]:
                    cnt+=1
            ans[i][j]=cnt
    for i in range(H-h+1):
        print(*ans[i])

if __name__ == "__main__":
    main()