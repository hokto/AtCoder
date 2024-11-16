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
    L,R = myin_sp_i()
    if L==1 and R==0:
        print("Yes")
    elif L==0 and R==1:
        print("No")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()