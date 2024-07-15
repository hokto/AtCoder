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
    C1 = myin_sp_i()
    C2 = myin_sp_i()
    if C1[0]<=C2[0]<C1[3] or C2[0]<=C1[0]<C2[3]:
        if C1[1]<=C2[1]<C1[4] or C2[1]<=C1[1]<C2[4]:
            if C1[2]<=C2[2]<C1[5] or C2[2]<=C1[2]<C2[5]:
                print("Yes")
                exit()
    print("No")

if __name__ == "__main__":
    main()