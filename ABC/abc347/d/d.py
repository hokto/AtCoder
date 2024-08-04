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
    a,b,C = myin_sp_i()
    c = C.bit_count()
    if a==b==c==0:
        print(0,0)
        exit()
    A = 0
    B = 0
    for i in range(60):
        if (C&(1<<i))>0:
            if a>b:
                A+=1<<i
                a-=1
            else:
                B+=1<<i
                b-=1
        if a<0 or b<0:
            break
    if a!=b:
        print(-1)
        exit()
    for i in range(60):
        if (C&(1<<i))==0:
            A+=1<<i
            B+=1<<i
            a-=1
        if a==0:
            break
    if a!=0:
        print(-1)
        exit()
    print(A,B)
if __name__ == "__main__":
    main()