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
    N,A,B = myin_sp_i()
    D = myin_sp_i()
    DD = [0]*N
    for i in range(N):
        DD[i] = D[i]%(A+B)
    DD.sort()
    ans = False
    if DD[-1]-DD[0]<A:
        ans = True
    for i in range(1,N):
        if A+B+DD[i-1]-DD[i]<A:
            ans = True
    if ans:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()