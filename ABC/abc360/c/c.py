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
    N = int(myin())
    A= myin_sp_i()
    W = myin_sp_i()
    box = [0 for i in range(N)]
    s = 0
    for i in range(N):
        a = A[i]-1
        box[a] = max(box[a],W[i])
        s+=W[i]
    print(s-sum(box))

if __name__ == "__main__":
    main()