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
    T = myin()
    N = len(T)
    isok = True
    if N%2:
        isok = False
    ab = {}
    for i in range(N//2):
        if T[2*i]==T[2*i+1] and T[2*i] not in ab:
            ab[T[2*i]]=1
        else:
            isok = False
    print("Yes" if isok else "No")

if __name__ == "__main__":
    main()