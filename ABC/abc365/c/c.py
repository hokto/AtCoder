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

def f(x,A,N,M):
    res = 0
    for i in range(N):
        res+=min(x,A[i])
    return M>=res
def main():
    N,M = myin_sp_i()
    A = myin_sp_i()
    if sum(A)<=M:
        print("infinite")
        exit()
    head = 0
    tail = max(A)
    while tail-head>1:
        m = head+(tail-head)//2
        if f(m,A,N,M):
            head = m
        else:
            tail = m
    print(head)

if __name__ == "__main__":
    main()