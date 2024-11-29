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
    from atcoder.segtree import SegTree
    N,M = myin_sp_i()
    S = myin()
    INF = N+M
    dp = SegTree(min,INF,N+1)
    dp.set(0,0)
    for i in range(1,N+1):
        if S[i]=="1": continue
        s = max(0,i-M)
        v = dp.prod(s,i)
        if v>=0:
            dp.set(i,v+1)
    #print(dp.get(N))
    if dp.get(N)>=INF:
        print(-1)
    else:
        ans = []
        i = N
        while i:
            k = i
            for j in range(max(i-M,0),i)[::-1]:
                if dp.get(j)==dp.get(i)-1:
                    k = j
            ans.append(i-k)
            i = k
        print(*reversed(ans),sep=" ")
if __name__ == "__main__":
    main()