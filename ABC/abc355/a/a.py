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
    A,B=myin_sp_i()
    if A==B:
        print(-1)
    else:
        kouho = [False for i in range(3)]
        kouho[A-1]=True
        kouho[B-1]=True
        for i in range(3):
            if not kouho[i]:
                print(i+1)

if __name__ == "__main__":
    main()