from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
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
    S = myin()
    dp = [[0]*2 for i in range(N+1)]
    dp[0][0] = dp[0][1]=1
    for i in range(N):
        is_parind = True
        if i<K:
            is_parind = False
        else:
            for k in range(i-K,i-K+K//2):
                pass
            
            
if __name__ == "__main__":
    main()