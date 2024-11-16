from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    M = 3
    P = [[] for _ in range(M)]
    N = 4
    for i in range(N):
        P[0].append(myin())
    for i in range(N):
        P[1].append(myin())
    for i in range(N):
        P[2].append(myin())
    def rotate(A):
        tmp = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                tmp[j][N-1-i] = A[i][j]
        return tmp
    def solve(i,s):
        #print(i)
        if i==M:
            for y in range(N):
                for x in range(N):
                    if s[y][x]!="#": return False
            return True
        res = False
        PP = P[i]
        for dy in range(-3,3+1):
            for dx in range(-3,3+1):
                for rotate_cnt in range(4):
                    #print((i,dy,dx,rotate_cnt))
                    isok = True
                    tmp = [[s[yy][xx] for xx in range(N)]for yy in range(N)]
                    for y in range(N):
                        for x in range(N):
                            ny = y+dy
                            nx = x+dx
                            if not(0<=ny<N and 0<=nx<N):
                                if PP[y][x]=="#": isok = False
                            else:
                                if PP[y][x]=="#":
                                    if s[ny][nx]=="#": isok = False
                                    else: tmp[ny][nx]="#"
                    if isok:
                        res |= solve(i+1,tmp)
                    PP = rotate(PP)
        return res
    ans = solve(0,[["." for _ in range(N)]for _ in range(N)])
    if ans:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()