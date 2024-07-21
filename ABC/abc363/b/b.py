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
    N,T,P = myin_sp_i()
    L = myin_sp_i()
    for l in range(T+1):
        cnt = 0
        for i in range(N):
            if L[i]+l>=T:
                cnt+=1
        if cnt>=P:
            print(l)
            exit()

if __name__ == "__main__":
    main()