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
    N,K = myin_sp_i()
    A = myin_sp_i()
    B = sorted(A)
    acc = 0
    if K<=0:
        f = True
        for b in B:
            acc+=b 
            if acc<K:
                f = False
                break
        if f:
            print("Yes")
            print(*B)
            exit()
        from collections import deque
        C = deque(B)
        ans = []
        acc2 = 0
        while len(C)>0:
            if acc2+C[0]>=K:
                ans.append(C.popleft())
            else:
                ans.append(C.pop())
            acc2 += ans[-1]
            if acc2<K:
                print("No")
                exit()
        print("Yes")
        print(*ans)
        exit()
    print("Yes")
    print(*B)

if __name__ == "__main__":
    main()