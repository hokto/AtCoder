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
    H,W,N = myin_sp_i()
    RC = []
    for i in range(N):
        RC.append(myin_sp_i())
    RC.sort()
    prev = {}
    dp = []
    for i in range(N):
        r,c = RC[i]
        if len(dp)==0 or dp[-1][1]<=c:
            if len(dp)==0:
                prev[(r,c)]=(1,1)
            else:
                prev[(r,c)]=dp[-1]
            dp.append((r,c))
        else:
            ng = -1
            ok = len(dp)
            while ok-ng>1:
                m = ng+(ok-ng)//2
                if dp[m][1]>c:
                    ok = m
                else:
                    ng = m
            if ok==0:
                prev[(r,c)]=(1,1)
            else:
                prev[(r,c)]=dp[ok-1]
            dp[ok] = (r,c)
    print(len(dp))
    ans = []
    now = (H,W)
    pr = dp[-1]
    while now!=(1,1):
        ans+="D"*(now[0]-pr[0])
        ans+="R"*(now[1]-pr[1])
        now = pr
        if now in prev: pr = prev[now]
    print("".join(reversed(ans)))

if __name__ == "__main__":
    main()