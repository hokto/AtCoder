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
    Sx,Sy = myin_sp_i()
    Tx,Ty = myin_sp_i()
    dx = Tx-Sx
    dy = Sy-Ty
    if dx < 0:
        if (Sx+Sy)%2==1:
            dx+=1
        dx+=abs(dy)
        if dx>0: dx=0
    if dx>0:
        if (Sx+Sy)%2==0:
            dx -=1
        dx-=abs(dy)
        if dx<0: dx=0
    print(abs(dy)+(abs(dx)+1)//2)

if __name__ == "__main__":
    main()