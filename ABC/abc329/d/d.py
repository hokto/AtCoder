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
    A = myin_sp_i()
    cnt = [0]*N
    now = 0
    for a in A:
        a-=1
        cnt[a]+=1
        if cnt[now]==cnt[a]:
            if now>a: now=a
        elif cnt[now]<cnt[a]:
            now = a
        print(now+1)

if __name__ == "__main__":
    main()