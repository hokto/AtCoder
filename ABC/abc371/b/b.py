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
    used = [False]*N
    for i in range(M):
        a,b = myin_sp_s()
        a = int(a)-1
        if b=="M" and not used[a]:
            used[a]=True
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()