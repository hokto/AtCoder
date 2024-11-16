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
    icecream = []
    for i in range(N):
        icecream.append(myin_sp_i())
    icecream.sort(key=lambda x:-x[1])
    mx = icecream[0]
    ans = 0
    for i in range(1,N):
        if mx[0]==icecream[i][0]:
            ans=max(ans,mx[1]+icecream[i][1]//2)
            break
    for i in range(1,N):
        if mx[0]!=icecream[i][0]:
            ans = max(ans,mx[1]+icecream[i][1])
    print(ans)

if __name__ == "__main__":
    main()