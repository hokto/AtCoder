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
    S = myin()
    N = len(S)
    lower = 0
    upper = 0
    for i in range(N):
        c = S[i]
        if c.islower():
            lower+=1
        else:
            upper+=1
    if lower>upper:
        print(S.lower())
    else:
        print(S.upper())

if __name__ == "__main__":
    main()