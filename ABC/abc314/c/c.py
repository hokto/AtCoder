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
    N,M = myin_sp_i()
    S = myin()
    C = myin_sp_i()
    colors = [[] for i in range(M)]
    for i,c in enumerate(C):
        c -=1
        colors[c].append(i)
    ans = [""]*N
    for color in colors:
        K = len(color)
        for i in range(K):
            ans[color[i]]=S[color[(i-1)%K]]
    print("".join(ans))

if __name__ == "__main__":
    main()