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
    N,S = myin_sp_i()
    A = myin_sp_i()
    S%=sum(A)
    B = A+A
    tail = 0
    s = 0
    for head in range(2*N):
        while tail<2*N and s+B[tail]<=S:
            s+=B[tail]
            tail+=1
        if s==S:
            print("Yes")
            return
        if tail==2*N:
            break
        s-=B[head]
    print("No")

if __name__ == "__main__":
    main()