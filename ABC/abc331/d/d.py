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
    N,Q = myin_sp_i()
    P = [[0]*N for i in range(N)]
    for i in range(N):
        S = myin()
        for j in range(N):
            if S[j]=="B":
                P[i][j]=1
    accum = [[0]*(N+1) for i in range(N+1)]
    for i in range(N):
        for j in range(N):
            accum[i+1][j+1]=P[i][j]+accum[i+1][j]+accum[i][j+1]-accum[i][j]
    def calc_sum(i,j):
        si = i//N
        sj = j//N
        ri = i%N
        rj = j%N
        res = accum[-1][-1]*si*sj
        res+=accum[-1][rj+1]*si
        res+=accum[ri+1][-1]*sj
        res+=accum[ri+1][rj+1]
        return res
    for q in range(Q):
        A,B,C,D = myin_sp_i()
        A-=1
        B-=1
        C-=1
        D-=1
        #print(calc_sum(A+1,B+1))
        print(calc_sum(C+1,D+1)-calc_sum(C+1,B)-calc_sum(A,D+1)+calc_sum(A,B))
if __name__ == "__main__":
    main()