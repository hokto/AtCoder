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
    S = [[0]*N for i in range(N)]
    for i in range(N):
        T = myin()
        for j in range(N):
            if T[j]=="o":
                S[i][j]=1
    row_sum = [0]*N
    col_sum = [0]*N
    for i in range(N):
        for j in range(N):
            row_sum[i]+=S[i][j]
            col_sum[j]+=S[i][j]
    ans = 0
    for i in range(N):
        for j in range(N):
            ans+=S[i][j]*(row_sum[i]-1)*(col_sum[j]-1)
    print(ans)

if __name__ == "__main__":
    main()