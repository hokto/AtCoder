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
    N,M = myin_sp_i()
    A = myin_sp_i()
    B = myin_sp_i()
    C = []
    for a in A:
        C.append((a,0))
    for b in B:
        C.append((b,1))
    C.sort() 
    for i in range(N+M-1):
        if C[i][1]==0 and C[i][1]==C[i+1][1]:
            print("Yes")
            exit()
    print("No")

if __name__ == "__main__":
    main()