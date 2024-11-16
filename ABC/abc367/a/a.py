from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
# 再帰用
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    A,B,C = myin_sp_i()
    if B<=C:
        if B<=A<=C:
            print("No")
        else:
            print("Yes")
    else:
        if B<=A+24<=C+24:
            print("No")
        else:
            print("Yes")

if __name__ == "__main__":
    main()