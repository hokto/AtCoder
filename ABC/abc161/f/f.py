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
    def prime_division(n):
        x = n
        res = []
        k = 2
        while k*k<=n:
            cnt = 0
            while x%k==0:
                cnt+=1
                x//=k
            if cnt:
                res.append((k,cnt))
            k+=1
        if x!=1:
            res.append((x,1))
        return res
    N = int(myin())
    if N==2:
        print(1)
        return
    k = 2
    ans = 1 # Nで割った場合
    while k*k<=N:
        if N%k==0:
            s = N//k
            while s%k==0:
                s//=k
            if s%k==1:
                ans+=1
        k+=1
    # N=1(mod k)<->(N-1)=0(mod k)
    # N-1の約数を列挙すればkが求まる
    res = 1
    for k,v in prime_division(N-1):
        res*=v+1
    res-=1 # 1を除く
    ans+=res
    print(ans)

if __name__ == "__main__":
    main()