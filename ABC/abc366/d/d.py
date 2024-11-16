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
    N = int(myin())
    A = []
    for i in range(N):
        A.append([])
        for j in range(N):
            A[i].append(myin_sp_i())
    accum = [[[0 for i in range(N+1)]for j in range(N+1)] for k in range(N+1)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                accum[i+1][j+1][k+1]=A[i][j][k]+accum[i][j+1][k+1]+accum[i+1][j][k+1]+accum[i+1][j+1][k]-accum[i][j][k+1]-accum[i+1][j][k]-accum[i][j+1][k]+accum[i][j][k]
    #print(accum)
    Q = int(myin())
    for q in range(Q):
        x1,x2,y1,y2,z1,z2 = myin_sp_i()
        x1-=1
        y1-=1
        z1-=1
        print(accum[x2][y2][z2]-accum[x1][y2][z2]-accum[x2][y1][z2]-accum[x2][y2][z1]+accum[x1][y1][z2]+accum[x2][y1][z1]+accum[x1][y2][z1]-accum[x1][y1][z1])

if __name__ == "__main__":
    main()