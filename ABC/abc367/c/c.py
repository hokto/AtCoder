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

ans = []
def solve(i,s,select,N,K,R):
    if i==N:
        if s%K==0:
            print(*select)
        return
    for k in range(R[i]):
        select[i] = k+1
        solve(i+1,s+k+1,select,N,K,R)
def main():
    N,K = myin_sp_i()
    R = myin_sp_i()
    solve(0,0,[-1]*N,N,K,R)
if __name__ == "__main__":
    main()