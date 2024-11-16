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
    S = []
    for i in range(N):
        S.append(myin())
    p1 = (-1,-1)
    p2 = (-1,-1)
    for i in range(N):
        for j in range(N):
            if S[i][j]=="P":
                if p1==(-1,-1):
                    p1 = (i,j)
                else:
                    p2 = (i,j)
    INF = N**5
    DIR = [(0,1),(0,-1),(1,0),(-1,0)]
    op_cnt = [[[[INF for i in range(N)] for j in range(N)]for k in range(N)]for l in range(N)]
    op_cnt[p1[0]][p1[1]][p2[0]][p2[1]]=0
    from collections import deque
    deq = deque()
    deq.append((p1[0],p1[1],p2[0],p2[1]))
    ans = INF
    while deq:
        p11,p12,p21,p22 = deq.popleft()
        for di,dj in DIR:
            q11 = p11+di
            q21 = p21+di
            q12 = p12+dj
            q22 = p22+dj
            if not(0<=q11<N and 0<=q12<N and S[q11][q12]!="#"):
                q11 = p11
                q12 = p12
            if not(0<=q21<N and 0<=q22<N and S[q21][q22]!="#"):
                q21 = p21
                q22 = p22
            if op_cnt[q11][q12][q21][q22]==INF:
                op_cnt[q11][q12][q21][q22]=op_cnt[p11][p12][p21][p22]+1
                deq.append((q11,q12,q21,q22))
                if q11==q21 and q12==q22:
                    ans = op_cnt[q11][q12][q21][q22]
                    print(ans)
                    exit()
    if ans==INF:
        print(-1)
    #else:
        #print(ans)
if __name__ == "__main__":
    main()