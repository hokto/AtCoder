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
    intervals = []
    for i in range(N):
        l,r = myin_sp_i()
        intervals.append((l,r))
    intervals.sort(key=lambda x:x[1])
    ans = M*(M+1)//2
    tail = 1
    idx = 0
    for head in range(1,M+1):
        while idx<N and intervals[idx][0]<head:
            idx+=1
        if idx==N: break
        while tail<=M and tail<intervals[idx][1]:
            tail+=1
        ans-=M-tail+1
    print(ans)

if __name__ == "__main__":
    main()