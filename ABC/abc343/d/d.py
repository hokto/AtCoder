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
    from collections import defaultdict
    N,T = myin_sp_i()
    num = defaultdict(int)
    ans = 1
    num[0] = N
    P = [0]*N
    for t in range(T):
        a,b = myin_sp_i()
        a-=1
        num[P[a]]-=1
        if num[P[a]]==0:
            ans-=1
        if num[P[a]+b]==0:
            ans+=1
        num[P[a]+b]+=1
        P[a]+=b
        print(ans)

if __name__ == "__main__":
    main()