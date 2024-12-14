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
    N = int(myin())
    T = myin()
    B = 10**9+7
    M = (1<<61)-1
    B_inv = pow(B,M-2,M) # B^-1
    v1 = 0 # 先頭からの部分列
    v2 = 0 # 逆の部分列
    for i in range(N):
        v2=v2*B+(ord(T[N-1-i])-ord("a")+1)
        v2%=M
    for i in range(N):
        v1=v1*B+(ord(T[N+i])-ord("a")+1)
        v1%=M
    if v1==v2:
        print(T[N:])
        print(0)
        return
    for i in range(1,N+1):
        v1=v1-(ord(T[N-1+i])-ord("a")+1)*pow(B,N-i,M)+(ord(T[i-1])-ord("a")+1)*pow(B,N-i,M)
        v1%=M
        v2=(v2-(ord(T[i-1])-ord("a")+1))*B_inv+(ord(T[N-1+i])-ord("a")+1)*pow(B,N-1,M)
        v2%=M
        #print(v1,v2)
        if v1==v2:
            print(T[:i]+T[N+i:])
            print(i)
            return
    print(-1)
if __name__ == "__main__":
    main()