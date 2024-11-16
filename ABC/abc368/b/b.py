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
    A = myin_sp_i()
    from heapq import heapify,heappop,heappush
    pq = [-a for a in A]
    heapify(pq)
    ans = 0
    while len(pq)>1:
        a = heappop(pq)
        b = heappop(pq)
        a*=-1
        b*=-1
        if a>1: heappush(pq,-(a-1))
        if b>1: heappush(pq,-(b-1))
        ans+=1
    print(ans)

if __name__ == "__main__":
    main()