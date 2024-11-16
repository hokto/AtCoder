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
    from functools import cmp_to_key
    N = int(myin())
    def comp_func(x,y):
        if x[0]*(y[0]+y[1])==y[0]*(x[0]+x[1]):
            if x[2]<y[2]:
                return -1
            else:
                return 1
        else:
            if x[0]*(y[0]+y[1])>y[0]*(x[0]+x[1]):
                return -1
            else:
                return 1
    AB = []
    for i in range(N):
        a,b = myin_sp_i()
        AB.append((a,b,i+1))
    AB.sort(key=cmp_to_key(comp_func))
    print(*[AB[i][2] for i in range(N)])

if __name__ == "__main__":
    main()