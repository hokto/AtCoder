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
    ans=0
    for q in range(Q):
        h,t = myin_sp_s()
        t=int(t)
        t-=1
        INF = N+10
        ans1 = INF
        ans2 = INF
        if h=="L":
            res1 = 0
            f = True
            l=L
            while l!=t:
                if (l+1)%N==R:
                    f = False
                    break
                l=(l+1)%N
                res1+=1
            if f: ans1=res1
            res2=0
            f=True
            l=L
            while l!=t:
                if (l-1)%N==R:
                    f=False
                    break
                l=(l-1)%N
                res2+=1
            if f: ans2=res2
            ans+=min(ans1,ans2)
            L=t
        else:   
            res1 = 0
            f = True
            r=R
            while r!=t:
                if (r+1)%N==L:
                    f = False
                    break
                r=(r+1)%N
                res1+=1
            if f: ans1=res1
            res2=0
            f=True
            r=R
            while r!=t:
                if (r-1)%N==L:
                    f=False
                    break
                r=(r-1)%N
                res2+=1
            if f: ans2=res2
            ans+=min(ans1,ans2)
            R=t
    print(ans)
if __name__ == "__main__":
    main()