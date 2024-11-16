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

def f1(x,b,k,A,N,accum):
    # b-(A[x]-b)以上の最小の点yを求める
    # accum[x+1]-accum[y]がk以上ならTrue,それ以外False
    ng = -1
    ok = N
    while ok-ng>1:
        m = ng+(ok-ng)//2
        if b-(A[x]-b)<=A[m]:
            ok = m
        else:
            ng = m
    y = ok
    if y!=-1 and accum[x+1]-accum[y]>=k:
        return True
    return False

def f2(x,b,k,A,N,accum):
    # b+(b-A[x])以下の最大の点yを求める
    # accum[y+1]-accum[x]がk以上ならTrue,それ以外False
    ok = -1
    ng = N
    while ng-ok>1:
        m = ok+(ng-ok)//2
        if b+(b-A[x])>=A[m]:
            ok = m
        else:
            ng = m
    y = ok
    if y!=N and accum[y+1]-accum[x]>=k:
        return True
    return False
def main():
    N,Q = myin_sp_i()
    A = myin_sp_i()
    A.sort()
    accum = [i for i in range(N+1)]
    for q in range(Q):
        b,k = myin_sp_i()
        head1 = -1
        tail1 = N
        while tail1-head1>1:
            mid = head1+(tail1-head1)//2
            if f1(mid,b,k,A,N,accum):
                tail1 = mid
            else:
                head1 = mid
        
        head2 = -1
        tail2 = N
        while tail2-head2>1:
            mid = head2+(tail2-head2)//2
            if f2(mid,b,k,A,N,accum):
                head2 = mid
            else:
                tail2 = mid
        #print(tail1,head2)
        if tail1==N:
            print(b-A[head2])
        elif head2==-1:
            print(A[tail1]-b)
        else:
            print(min(b-A[head2],A[tail1]-b))

if __name__ == "__main__":
    main()