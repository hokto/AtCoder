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
    from bisect import bisect_left,bisect_right
    N,Q = myin_sp_i()
    S = myin()
    slashs =[]
    for i in range(N):
        if S[i]=="/":
            slashs.append(i)
    one_cnt = [0]*(N+1)
    two_cnt = [0]*(N+1)
    for i in range(N):
        one_cnt[i+1]=one_cnt[i]
        if S[i]=="1":
            one_cnt[i+1]+=1
    for i in range(N)[::-1]:
        two_cnt[i] = two_cnt[i+1]
        if S[i]=="2":
            two_cnt[i]+=1
    for q in range(Q):
        l,r  = myin_sp_i()
        l-=1
        r-=1
        slash_l = bisect_left(slashs,l)
        slash_r = bisect_right(slashs,r)-1
        if slash_l>slash_r:
            print(0)
            continue
        ok = slash_l-1
        ng = slash_r+1
        ans = 0
        while ng-ok>1:
            m = ok+(ng-ok)//2
            c1 = one_cnt[slashs[m]+1]-one_cnt[l]
            c2 = two_cnt[slashs[m]]-two_cnt[r+1]
            ans = max(ans,min(c1,c2)*2+1)
            if c1<c2:
                ok = m
            else:
                ng = m
        print(ans)

if __name__ == "__main__":
    main()