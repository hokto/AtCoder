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
    N,C = myin_sp_i()
    T = myin_sp_i()
    prev = -(C+10)
    ans = 0
    for i in range(N):
        if T[i]-prev>=C:
            ans+=1
            prev=T[i]
    print(ans)

if __name__ == "__main__":
    main()