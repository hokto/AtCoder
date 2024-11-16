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
    from heapq import heapify,heappop,heappush
    pq = []
    heapify(pq)
    N = int(myin())
    cnt = {}
    for i in range(N):
        s,c = myin_sp_i()
        cnt[s]=c
        heappush(pq,s)
    ans = 0
    while pq:
        s = heappop(pq)
        ans+=cnt[s]%2
        if cnt[s]//2<=0: continue
        if s*2 not in cnt:
            cnt[s*2]=cnt[s]//2
            heappush(pq,s*2)
        else:
            cnt[s*2]+=cnt[s]//2
    print(ans)

if __name__ == "__main__":
    main()