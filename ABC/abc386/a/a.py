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
    from collections import defaultdict
    A,B,C,D = myin_sp_i()
    kind = defaultdict(int)
    kind[A]+=1
    kind[B]+=1
    kind[C]+=1
    kind[D]+=1
    if len(kind)==2 and (kind[A]==2 or kind[A]==1 or kind[A]==3):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()