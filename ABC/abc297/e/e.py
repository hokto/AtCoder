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
    N,K = myin_sp_i()
    A = myin_sp_i()
    pq = [0]
    heapify(pq)
    k = 0
    prev = -1
    while k<K:
        while prev==pq[0]:
            heappop(pq)
        x = heappop(pq)
        prev = x
        for a in A:
            heappush(pq,x+a)
        k+=1
    while prev==pq[0]:
        heappop(pq)
    print(pq[0])
    

if __name__ == "__main__":
    main()