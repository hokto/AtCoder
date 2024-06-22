from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    from collections import deque
    N,M = myin_sp_i()
    A = myin_sp_i()
    B = myin_sp_i()
    B_sorted = sorted(B)
    A_sorted = list(reversed(sorted(A)))
    dq = deque()
    ans = 0
    i = 0
    for b in reversed(B_sorted):
        while i<N and A_sorted[i]>=b:
            dq.append(A_sorted[i])
            i+=1
        if len(dq)<=0:
            print(-1)
            exit()
        ans+=dq.pop()
    print(ans)
        

if __name__ == "__main__":
    main()