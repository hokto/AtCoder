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
    N,X,Y = myin_sp_i()
    busstops = []
    for i in range(N-1):
        busstops.append(myin_sp_i())
    K = 840
    times = [0]*K
    for ts in range(K):
        now = ts
        for i in range(N-1):
            p,t = busstops[i]
            now = ((now+p-1)//p)*p
            now+=t
        times[ts]=now-ts
    INF = 1<<32+10
    Q = int(myin())
    for _ in range(Q):
        q = int(myin())
        ans = q+X+times[(q+X)%K]+Y
        print(ans)

if __name__ == "__main__":
    main()