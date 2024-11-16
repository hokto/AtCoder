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
    from collections import deque
    Q = int(myin())
    S = deque()
    S.append(1)
    MOD = 998244353
    ans = 1
    for q in range(Q):
        query = myin_sp_i()
        if query[0]==1:
            x = query[1]
            ans=ans*10+x
            ans%=MOD
            S.append(x)
        elif query[0]==2:
            ans-=S[0]*pow(10,len(S)-1,MOD)
            ans%=MOD
            S.popleft()
        else:
            print(ans)

if __name__ == "__main__":
    main()