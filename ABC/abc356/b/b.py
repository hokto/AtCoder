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
    N,M = myin_sp_i()
    A = myin_sp_i()
    B = [0 for i in range(M)]
    for i in range(N):
        X = myin_sp_i()
        for j in range(M):
            B[j]+=X[j]
    for i in range(M):
        if A[i]>B[i]:
            print("No")
            exit()
    print("Yes")

if __name__ == "__main__":
    main()