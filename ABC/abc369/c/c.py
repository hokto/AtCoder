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
    ans = 0
    head = 0
    tail = 1
    prev = -1
    while tail<N:
        prev = A[tail]-A[head]
        while tail<N and A[tail]-A[tail-1]==prev:
            tail+=1
        ans+=(tail-head)*(tail-head+1)//2-1
        head = tail-1
        #print(ans)
    ans+=1
    print(ans)

if __name__ == "__main__":
    main()