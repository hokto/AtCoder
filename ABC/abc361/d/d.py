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

# .=0,W=1,B=2
def bfs(S_r,memo,N):
    from collections import deque
    memo[tuple(S_r)]=0
    deq = deque()
    deq.append((tuple(S_r),N,0))
    while deq:
        S,j,cost = deq.popleft()
        s = [0]*(N+2)
        for i in range(N+2):
            s[i]=S[i]
        for i in range(N+1):
            if i==j-1 or i==j or i==j+1:
                continue
            s[j]=s[i]
            s[j+1]=s[i+1]
            s[i]=s[i+1]=0
            if tuple(s) not in memo:
                memo[tuple(s)]=cost+1
                deq.append((tuple(s),i,cost+1))
            s[i]=s[j]
            s[i+1]=s[j+1]
            s[j]=s[j+1]=0
        
        
def main():
    N = int(myin())
    S = myin()
    SS = [0]*(N+2)
    for i in range(N):
        if S[i]=="W":
            SS[i]=1
        else:
            SS[i]=2
    T = myin()
    TT = [0]*(N+2)
    for i in range(N):
        if T[i]=="W":
            TT[i]=1
        else:
            TT[i]=2
    memo = {}
    bfs(SS,memo,N)
    #print(memo)
    if tuple(TT) not in memo:
        print(-1)
    else:
        print(memo[tuple(TT)])

if __name__ == "__main__":
    main()