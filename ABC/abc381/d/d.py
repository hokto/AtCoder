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
    from collections import defaultdict
    N = int(myin())
    A = myin_sp_i()
    head = 0
    tail = 0
    ab = defaultdict(int)
    ans = 0
    while tail+1<N:
        while tail+1<N and A[tail]==A[tail+1] and ab[A[tail]]==0:
            ab[A[tail]]=1
            tail+=2
        ans = max(ans,tail-head)
        if tail+1>=N: break
        if ab[A[tail]]!=0:
            ab[A[head]]=0
            head += 2
            if head>=tail: tail=head
        else:
            ab.clear()
            if tail>0 and A[tail-1]==A[tail]:
                head = tail-1
                tail = tail+1
                ab[A[head]]=1
            else:
                head = tail+1
                tail = head
    print(ans)
        

if __name__ == "__main__":
    main()