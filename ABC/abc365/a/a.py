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
    Y = int(myin())
    if Y%4!=0:
        print(365)
    elif Y%100!=0:
        print(366)
    elif Y%400!=0:
        print(365)
    else:
        print(366)

if __name__ == "__main__":
    main()