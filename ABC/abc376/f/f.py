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
    L = 0
    R = 1
    ans = 0
    INF = 10**9
    for q in range(Q):
        h,t = myin_sp_s()
        t = int(t)-1
        if h=="L":
            RR = [INF]*N # RR[t]=INF
            mn = INF
            mn_r = -1
            for r in range(N):
                if r==t: continue
                res=[]
                res.append((r-R+N)%N+(t-L+N)%N)
                res.append((R-r+N)%N+(L-t+N)%N)
                if not((L<=t and (L<=R<=t or L<=r<=t)) or (t<=L and (t<=R<=L or t<=r<=L))):
                    res.append((r-R+N)%N+(t-L+N)%N)
                if not((L<=t and (L<=R<=t or L<=r<=t)) or (t<=L and (t<=R<=L or t<=r<=L))):
                    res.append((R-r+N)%N+(L-t+N)%N)
                RR[r]=min(res)
                if mn > RR[r]:
                    mn = RR[r]
                    mn_r = r
            ans+=mn
            R = mn_r
            L = t
        else:
            LL = [INF]*N # LL[t]=INF
            mn = INF
            mn_l = -1
            for l in range(N):
                if l==t: continue
                res=[]
                res.append((t-R+N)%N+(l-L+N)%N)
                res.append((R-t+N)%N+(L-l+N)%N)
                if not((R<=t and (R<=L<=t or R<=l<=t)) or (t<=R and (t<=L<=R or t<=l<=R))):
                    res.append((t-R+N)%N+(l-L+N)%N)
                if not((R<=t and (R<=L<=t or R<=l<=t)) or (t<=R and (t<=L<=R or t<=l<=R))):
                    res.append((R-t+N)%N+(L-l+N)%N)
                LL[l]=min(res)
                if mn > LL[l]:
                    mn = LL[l]
                    mn_l = l
            ans+=mn
            R = t
            L = mn_l
    print(ans)

if __name__ == "__main__":
    main()