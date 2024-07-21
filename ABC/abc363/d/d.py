from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    N = myin()
    B = 50
    dp = [[0 for i in range(10)] for j in range(B+1)]
    for j in range(10):
        dp[0][j]=j+1
    for j in range(1,10):
        dp[1][j]=10+j
    for i in range(2,B+1):
        for j in range(1,10):
            dp[i][j]=dp[i-1][-1]

if __name__ == "__main__":
    main()