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
    N,Q = myin_sp_i()
    S = list(myin())
    ans=0
    for i in range(N-2):
        if "".join(S[i:i+3])=="ABC":
            ans+=1
    #print(ans)
    for q in range(Q):
        x,c = myin_sp_s()
        x = int(x)-1
        for i in range(x-2,x+1):
            if not(0<=i<N-2): continue
            s = ""
            t=""
            for j in range(3):
                s+=S[i+j]
                if i+j==x:
                    t+=c
                else:
                    t+=S[i+j]
            if s=="ABC" and t!="ABC":
                #print("Minus")
                ans-=1
            elif s!="ABC" and t=="ABC":
                #print("Plus")
                ans+=1
        S[x]=c
        print(ans)

if __name__ == "__main__":
    main()