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
    N = int(myin())
    A = myin_sp_i()
    M = int(myin())
    B = myin_sp_i()
    L = int(myin())
    C = myin_sp_i()
    makable_num = {}
    for a in A:
        for b in B:
            for c in C:
                makable_num[a+b+c]=1
    Q = int(myin())
    X = myin_sp_i()
    for x in X:
        if x in makable_num:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()