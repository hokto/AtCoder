from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
from math import lcm
def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))


def f(A,N,M,K):
    return A//N+A//M-2*(A//lcm(N,M))>=K
def main():
    N,M,K = myin_sp_i()
    # N<Mと仮定
    # N*K<MならN*Kが答え
    # Aに対して，A//NがNで割り切れる中の番数,A//MがMで割り切れる中の番数,A//lcm(N,M)が共通して割り切れる中の番数なので
    # A//M+A//M-2*A//lcm(N,M)>=Kとなるものの中で最小のAを探索
    ng = 0
    ok = max(N,M)*K+10
    while ok-ng>1:
        m = ng+(ok-ng)//2
        if f(m,N,M,K):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == "__main__":
    main()