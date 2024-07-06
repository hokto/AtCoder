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
    S,T = myin_sp_s()
    S = list(S)
    N = len(S)
    for w in range(1,N):
        for c in range(w):
            t = ""
            i = 0
            while i*w+c<N:
                t+=S[i*w+c]
                i+=1
            if t==T:
                print("Yes")
                exit()
    print("No")

if __name__ == "__main__":
    main()