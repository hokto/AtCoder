from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import math
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

def prime_div(x):
    ret = {}
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            ret[i]=0
        while x%i==0:
            ret[i]+=1
            x//=i
    if x!=1: ret[x]=1
    return ret
        
def main():
    N = int(myin())
    A = myin_sp_i()
    div_cnt = [0]*N
    ans = 0
    for i in range(N):
        a = A[i]
        p_div = prime_div(a)
        for sz in p_div.values():
            div_cnt[i]+=sz
        #div_cnt[i]-=1
        ans^=div_cnt[i]
    if ans!=0:
        print("Anna")
    else:
        print("Bruno")
if __name__ == "__main__":
    main()