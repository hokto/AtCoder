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
    N,M = myin_sp_i()
    exist_A = defaultdict(int)
    for a in myin_sp_i():
        exist_A[a]=1
    if exist_A[N] or exist_A[1]:
        print("-1")
        exit()
    ans = [i for i in range(N+1)]
    idx = [i for i in range(N+1)]
    for a in list(range(1,N+1))[::-1]:
        if exist_A[a]:
            ans[idx[a]],ans[idx[a+1]]=ans[idx[a+1]],ans[idx[a]]
            idx[a],idx[a+1]=idx[a+1],idx[a]
    print(*ans[1:])
if __name__ == "__main__":
    main()