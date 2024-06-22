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
    N,L,R = myin_sp_i()
    ans = list(range(1,N+1))
    L-=1
    R-=1
    ans[L:R+1]=reversed(ans[L:R+1])
    print(*ans)

if __name__ == "__main__":
    main()