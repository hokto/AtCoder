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
    N,D,P = myin_sp_i()
    F = myin_sp_i()
    F.sort(reverse=True)
    ans = 0
    for i in range(N//D+1):
        s = 0
        for j in range(i*D,min((i+1)*D,N)):
            s+=F[j]
        ans += min(s,P) 
    print(ans)

if __name__ == "__main__":
    main()