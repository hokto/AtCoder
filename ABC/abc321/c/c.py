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
    K = int(myin())
    S = set()
    def dfs(now,d):
        S.add(now)
        for i in range(0,d):
            dfs(now*10+i,d=i)
    dfs(0,10)
    ans = list(sorted(S))
    #print(ans)
    print(ans[K])
    
            

if __name__ == "__main__":
    main()