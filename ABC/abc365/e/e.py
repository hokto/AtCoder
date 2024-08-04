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

def op(a,b):
    return a+b

def mapping(a,b):
    return a^b

def composition(f,g):
    return f^g
def main():
    N = int(myin())
    A = myin_sp_i()
    L = 30
    ans = 0
    for l in range(L):
        zero_cnt = 1
        one_cnt = 0
        accum_xor = [0 for i in range(N+1)]
        for i in range(N):
            accum_xor[i+1]=accum_xor[i]^((A[i]>>l)&1)
            if accum_xor[i+1]==0:
                zero_cnt+=1
            else:
                one_cnt+=1
        ans+=(1<<l)*zero_cnt*one_cnt
    ans-=sum(A)
    print(ans)
        
if __name__ == "__main__":
    main()