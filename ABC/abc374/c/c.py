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
    N = int(myin())
    K = myin_sp_i()
    ans = sum(K)
    for bit in range(1<<N):
        A = 0
        B = 0
        for i in range(N):
            if (bit&(1<<i))>0:
                A+=K[i]
            else:
                B+=K[i]
        ans = min(ans,max(A,B))
    print(ans)

if __name__ == "__main__":
    main()