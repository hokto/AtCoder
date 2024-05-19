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
    AB = []
    N = int(myin())
    for i in range(N):
        a,b = myin_sp_i()
        AB.append((a,b))
    dp = [-1 for i in range(1<<N)]
    dp[0]=False
    for S in range(1<<N):
        b = False
        for i in range(N):
            for j in range(1,N):
                if ((1<<i)&S)!=0 and ((1<<j)&S)!=0 and (AB[i][0]==AB[j][0] or AB[i][1]==AB[j][1]):
                    if not dp[(S^(1<<i))^(1<<j)]:
                        b=True
        dp[S]=b
    if dp[-1]:
        print("Takahashi")
    else:
        print("Aoki")
    #print(memo)

if __name__ == "__main__":
    main()