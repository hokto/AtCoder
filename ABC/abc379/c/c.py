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
    N,M = myin_sp_i()
    X = myin_sp_i()
    A = myin_sp_i()
    XA = []
    for i in range(M):
        XA.append((X[i],A[i]))
    XA.sort(key=lambda x:x[0])
    XA.append((N,0))
    if XA[0][0]!=1:
        print(-1)
        return
    stones = XA[0][1]
    prev_x = 1
    ans = 0
    for i in range(M):
        next_x = XA[i+1][0]
        diff = next_x-prev_x
        if diff>stones:
            print(-1)
            return
        ans += stones*(stones-1)//2 - (stones-diff)*(stones-diff-1)//2
        stones -= diff
        stones += XA[i+1][1]
        prev_x = next_x
    if stones == 1:
        print(ans)
    else:
        print(-1)
if __name__ == "__main__":
    main()