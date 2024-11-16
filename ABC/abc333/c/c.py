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
    R = []
    x = 1
    for i in range(20):
        R.append(x)
        x*=10
        x+=1
    ans = set()
    for r1 in R:
        for r2 in R:
            for r3 in R:
                ans.add(r1+r2+r3)
    
    ans = sorted(list(ans))
    print(ans[N-1])
if __name__ == "__main__":
    main()