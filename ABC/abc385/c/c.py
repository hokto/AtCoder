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
    H = myin_sp_i()
    ans = 1
    for l in range(N):
        for step in range(1,N):
            i = l+step
            res = 1
            while i<N:
                if H[i]!=H[l]:break
                res+=1
                i+=step
            ans = max(ans,res)
    print(ans)

if __name__ == "__main__":
    main()