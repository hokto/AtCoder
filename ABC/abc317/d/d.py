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
    MAX_Z = 10**5+10
    INF = 10**15
    dp = [INF]*(MAX_Z)
    dp[0] = 0
    sum_z = 0
    for i in range(N):
        x,y,z = myin_sp_i()
        for j in range(MAX_Z-z)[::-1]:
            dp[z+j]=min(dp[z+j],dp[j]+max(0,(x+y+1)//2-x))
        sum_z += z
    print(min(dp[(sum_z+1)//2:]))

if __name__ == "__main__":
    main()