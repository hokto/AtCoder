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
    N = int(myin())
    ints = []
    MAX_T = 0
    for i in range(N):
        t,d = myin_sp_i()
        l = t
        r = t+d
        ints.append((l,r))
        MAX_T = max(MAX_T,r)
    ints.sort(key=lambda x:(x[0],x[1]))
    pq = []
    heapify(pq)
    t = 1
    ans=0
    i = 0
    while True:
        if not pq:
            if i==N: break
            t = ints[i][0]
        while i<N and ints[i][0]==t:
            heappush(pq,ints[i][1])
            i+=1
        while pq and pq[0]<t:
            heappop(pq)
        if pq:
            heappop(pq)
            ans+=1
        t+=1
    print(ans)

if __name__ == "__main__":
    main()