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
    S = myin()
    if N%2==0:
        print("No")
        return
    for i in range(N//2):
        if S[i]!="1":
            print("No")
            return
    if S[N//2]!="/":
        print("No")
        return
    for i in range(N//2+1,N):
        if S[i]!="2":
            print("No")
            return
    print("Yes")

if __name__ == "__main__":
    main()