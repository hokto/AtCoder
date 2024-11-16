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
    inv = []
    for i in range(N):
        a,b = myin_sp_i()
        a-=1
        b-=1
        if a>b: a,b = b,a
        inv.append((a,b))
    inv.sort()
    from atcoder.fenwicktree import FenwickTree
    bit = FenwickTree(2*N)
    ans = False
    for l,r in inv:
        if bit.sum(l+1,r)>0:
            ans = True
            break
        bit.add(r,1)
    print("Yes" if ans else "No")
if __name__ == "__main__":
    main()