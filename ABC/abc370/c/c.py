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
    S = list(myin())
    T = list(myin())
    N = len(S)
    ans = []
    while True:
        check = True
        idx = -1
        for i in range(N):
            if S[i]!=T[i]:
                check = False
                idx = i
                if S[i]>T[i]:
                    break
        if check:
            break
        S[idx]=T[idx]
        ans.append("".join(S))
    print(len(ans))
    if len(ans)>0:
        print("\n".join(ans))


if __name__ == "__main__":
    main()