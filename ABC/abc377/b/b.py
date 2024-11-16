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
    S = []
    for i in range(8):
        S.append(myin())
    N = 8
    row = [True]*N
    col = [True]*N
    for i in range(N):
        for j in range(N):
            if S[i][j]=="#":
                row[i]=False
                col[j]=False
    ans = 0
    for i in range(N):
        for j in range(N):
            if row[i] and col[j]:
                ans+=1
    print(ans)

if __name__ == "__main__":
    main()