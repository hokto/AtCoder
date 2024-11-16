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
    from atcoder.dsu import DSU
    N,M = myin_sp_i()
    ans = 0
    dsu = DSU(N)
    for i in range(M):
        A,_,C,_ = myin_sp_s()
        A = int(A)-1
        C = int(C)-1
        if dsu.same(A,C):
            ans+=1
        else:
            dsu.merge(A,C)
    print(f"{ans} {len(dsu.groups())-ans}")

if __name__ == "__main__":
    main()