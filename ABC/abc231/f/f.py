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
    from atcoder.fenwicktree import FenwickTree
    from collections import defaultdict
    N = int(myin())
    A = myin_sp_i()
    B = myin_sp_i()
    C = sorted(set(B))
    change = {}
    for i,c in enumerate(C):
        change[c] = i
    M = len(change)
    for i in range(N):
        B[i] = change[B[i]]
    cnt = defaultdict(int)
    AB = set()
    for i in range(N):
        cnt[(A[i],B[i])]+=1
        AB.add((A[i],B[i]))
    AB = list(AB)
    AB.sort(key=lambda x:(x[0],-x[1]))
    #print(cnt)
    ft = FenwickTree(M)
    ans = 0
    for a,b in AB:
        ans+=ft.sum(b,M)*cnt[(a,b)]+cnt[(a,b)]*cnt[(a,b)]
        ft.add(b,cnt[(a,b)])
    print(ans)

if __name__ == "__main__":
    main()