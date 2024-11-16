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
    H = myin_sp_i()
    t = 0
    for h in H:
        if t%3!=0:
            if t%3==1:
                if h<=1:
                    h-=1
                    t+=1
                else:
                    h-=4
                    t+=2
            else:
                h-=3
                t+=1
        h = max(h,0)
        tt = h//5
        r = h%5
        t+=tt*3
        if r>=3:
            t+=3
        else:
            t+=r
        #print(t)
    print(t)

if __name__ == "__main__":
    main()