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
    R,G,B = myin_sp_i()
    C = myin()
    if C[0]=="R":
        print(min(G,B))
    elif C[0]=="G":
        print(min(R,B))
    else:
        print(min(R,G))

if __name__ == "__main__":
    main()