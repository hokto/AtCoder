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
    import random
    MOD = 1<<61-1
    N,Q = myin_sp_i()
    A = myin_sp_i()
    B = myin_sp_i()
    hash_table = {}
    for a in A:
        hash_table[a] = random.randrange(MOD)
    for b in B:
        hash_table[b] = random.randrange(MOD)
    accum_xor_A = [0]*(N+1)
    accum_xor_B = [0]*(N+1)
    for i in range(N):
        accum_xor_A[i+1] = (accum_xor_A[i]+hash_table[A[i]])%MOD
        accum_xor_B[i+1] = (accum_xor_B[i]+hash_table[B[i]])%MOD
        
    for q in range(Q):
        l,r,L,R = myin_sp_i()
        l-=1
        r-=1
        L-=1
        R-=1
        if (accum_xor_A[r+1]-accum_xor_A[l])%MOD==(accum_xor_B[R+1]-accum_xor_B[L])%MOD:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()