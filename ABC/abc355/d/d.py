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
    from atcoder.fenwicktree import FenwickTree
    N = int(myin())
    LR = []
    inv = []
    for i in range(N):
        l,r = myin_sp_i()
        l-=1
        r-=1
        LR.append([l,r])
        inv.append(l)
        inv.append(r)
    inv.sort()
    inv = list(set(inv))
    M = len(inv)
    bit = FenwickTree(M)
    exc = {}
    for i,lr in enumerate(inv):
        exc[lr]=i
    ans = 0
    LR.sort(lambda x: x[1])
    for l,r in LR:
        ll = exc[l] 
        rr = exc[r]
        ans+=bit.sum(ll,M) 
        bit.add(rr,1)
    print(ans)

if __name__ == "__main__":
    main()