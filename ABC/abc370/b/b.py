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
        A.append(myin_sp_i())
    now = 0
    for j in range(N):
        if now>=j:
            now = A[now][j]
        else:
            now = A[j][now]
        now-=1
    print(now+1)

if __name__ == "__main__":
    main()