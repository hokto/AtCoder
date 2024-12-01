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
    N,M = myin_sp_i()
    MAX = 2*10**5+1
    A = myin_sp_i()
    B = myin_sp_i()
    get = [-2]*(MAX)
    for i,a in enumerate(A):
        for j in range(a,MAX):
            if get[j]>=0: break
            get[j] = i
    for b in B:
        print(get[b]+1)
if __name__ == "__main__":
    main()