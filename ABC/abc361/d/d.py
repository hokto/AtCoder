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

def dp(S,memo,N,j,d):
    if S in memo:
        memo[S]=min(memo[S],d)
        return
    memo[S]=d
    S= list(S)
    for i in range(N+1):
        if i==j or i==j+1:
            continue
        s = ["" for k in range(N+2)]
        for k in range(N+2):
            s[k]=S[k]
        print(s)
        s[j]=s[i]
        s[j+1]=s[i+1]
        s[i]=s[i+1]="."
        s = "".join(s)
        dp(s,memo,N,i,d+1)
        
        
def main():
    N = int(myin())
    S = myin()
    T = myin()
    memo = {}
    dp(S+"..",memo,N,N,0)
    #print(memo)
    if (T+"..") not in memo:
        print(-1)
    else:
        print(memo[T+".."])

if __name__ == "__main__":
    main()