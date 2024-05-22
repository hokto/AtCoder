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
    MOD = 998244353
    INV_2 = 499122177
    T=int(myin())
    for _ in [0]*T:
        A1,A2,A3 = myin_sp_i()
        if A1>A2:
            A1,A2 = A2,A1
        if A3==A2+1:
            if A1==A2:
                print((pow(10,A1,MOD))*(pow(10,A1,MOD)+1)*INV_2%MOD)
            else:
                print(print((pow(10,A1,MOD)-1-pow(10,A1-1,MOD)+1)*(pow(10,A1,MOD)-1-pow(10,A1-1,MOD)+1+1)*INV_2%MOD)) 
        elif A3==A2:
            print((pow(10,A1,MOD)-1-2*pow(10,A1-1,MOD)+1)*(pow(10,A1,MOD)-1-2*pow(10,A1-1,MOD)+1+1)*INV_2%MOD)
        else:
            print(0)

if __name__ == "__main__":
    main()