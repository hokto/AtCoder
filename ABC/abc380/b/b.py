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
    S = myin()
    L = len(S)
    ans = []
    cnt = 0
    for i in range(1,len(S)):
        if S[i]=="|":
            ans.append(cnt)
            cnt=0
        else:
            cnt+=1
    print(*ans)

if __name__ == "__main__":
    main()