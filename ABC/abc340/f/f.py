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

def ex_gcd(a,b) -> tuple:
    if(b==0):
        return (1,0)
    x,y = ex_gcd(b,a%b)
    return (y,x-a//b*y)
def main():
    import math
    X,Y = myin_sp_i()
    if math.gcd(X,Y)>2:
        print(-1)
        exit()
    A,B = ex_gcd(Y,-X)
    if math.gcd(X,Y)==1:
        A*=2
        B*=2
    print(A,B)

if __name__ == "__main__":
    main()