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
    XA,YA = myin_sp_i()
    XB,YB = myin_sp_i()
    XC,YC = myin_sp_i()
    AB = (XA-XB)**2+(YA-YB)**2
    AC = (XA-XC)**2+(YA-YC)**2
    BC = (XB-XC)**2+(YB-YC)**2
    AB,AC,BC = sorted([AB,AC,BC])
    if BC == AB+AC:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()