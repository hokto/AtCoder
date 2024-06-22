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
    from atcoder.dsu import DSU
    from collections import defaultdict
    N,M=myin_sp_i()
    dsu = DSU(N)
    for i in range(M):
        u,v=myin_sp_i()
        u-=1
        v-=1
        dsu.merge(u,v)
    check_comp=defaultdict(bool)
    K = int(myin())
    for k in range(K):
        x,y = myin_sp_i()
        x-=1
        y-=1
        lx=dsu.leader(x)
        ly = dsu.leader(y)
        if lx>ly: lx,ly = ly,lx
        check_comp[(lx,ly)]=True
    Q=int(myin())
    for q in range(Q):
        p,q = myin_sp_i()
        p-=1
        q-=1
        lp = dsu.leader(p)
        lq =dsu.leader(q)
        if lp>lq: lp,lq = lq,lp
        if check_comp[(lp,lq)]:
            print("No")
        else:
            print("Yes")

if __name__ == "__main__":
    main()