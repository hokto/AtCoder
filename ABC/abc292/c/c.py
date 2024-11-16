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
    ans = 0
    for ab in range(N+1):
        cd = N-ab
        ab_cnt = 0
        a = 1
        while a*a<=ab:
            if ab%a==0:
                ab_cnt+=(1 if ab//a==a else 2)
            a+=1
        c = 1
        cd_cnt=0
        while c*c<=cd:
            if cd%c==0:
                cd_cnt+=(1 if cd//c==c else 2)
            c+=1
        ans+=ab_cnt*cd_cnt
    print(ans)

if __name__ == "__main__":
    main()