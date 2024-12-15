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
    N,R = myin_sp_i()
    for i in range(N):
        D,A = myin_sp_i()
        if D==1:
            if 1600<=R<2800:
                R+=A
        else:
            if 1200<=R<2400:
                R+=A
    print(R)

if __name__ == "__main__":
    main()