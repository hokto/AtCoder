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
    MOD = 10**9+7
    N,K = myin_sp_i()
    T = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = myin_sp_i()
        a-=1
        b-=1
        T[a].append(b)
        T[b].append(a)

    # すでにv,pには色が決定していて，子の塗り方の組み合わせを求める
    def dp(v,p):
        color_size = K-2
        if p==-1:
            color_size = K-1 # 親がない時はvを基準にこのペアが作れないためK-1
        res = 1
        if K<len(T[v]):
            return 0
        for vv in T[v]:
            if vv==p: continue
            res*=color_size
            color_size-=1
            res%=MOD
        for vv in T[v]:
            if vv==p: continue
            res*=dp(vv,v)
            res%=MOD
        return res
    
    ans = K*dp(0,-1)
    ans%=MOD
    print(ans)

if __name__ == "__main__":
    main()