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
    N,K = myin_sp_i()
    A = myin_sp_i()
    c = 0
    if K==1:
        print(0)
    elif K%2==0:
        ans = 0
        for i in range(0,K-c,2):
            ans+=A[i+1]-A[i]
        print(ans)
    else:
        l = 0
        r = 0
        for i in range(1,K,2):
            r+=A[i+1]-A[i]
        ans = r
        for i in range(1,K):
            # iが偶数ならちょうどiを基準に右・左で2つずつのペアを作る
            # iが奇数ならiのすぐ右とすぐ左でペアを作れば残りは隣同士でペアになる
            if i%2==1:
                r-=A[i+1]-A[i]
                l+=A[i+1]-A[i-1]
            else:
                l-=A[i]-A[i-2]
                l+=A[i-1]-A[i-2]
            ans = min(ans,l+r)
        print(ans)

if __name__ == "__main__":
    main()