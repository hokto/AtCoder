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

N=H=W=0
tills = []
def solve(board,unused,cur):
    while cur<H*W and board[cur]>0:
        cur+=1
    if cur==H*W:
        return True
    ny = cur//W
    nx = cur%W
    for i,(a,b) in enumerate(tills):
        if (unused&(1<<i))>0:
            if 0<=ny+a-1<H and 0<=nx+b-1<W:
                flag = True
                for dy in range(a):
                    for dx in range(b):
                        if board[(ny+dy)*W+nx+dx]>0:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    for dy in range(a):
                        for dx in range(b):
                            board[(ny+dy)*W+nx+dx]=1
                    f2 = solve(board,unused^(1<<i),cur)
                    if f2:
                        return True
                    for dy in range(a):
                        for dx in range(b):
                            board[(ny+dy)*W+nx+dx]=0
            if a!=b and 0<=ny+b-1<H and 0<=nx+a-1<W:
                flag = True
                for dy in range(b):
                    for dx in range(a):
                        if board[(ny+dy)*W+nx+dx]>0:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    for dy in range(b):
                        for dx in range(a):
                            board[(ny+dy)*W+nx+dx]=1
                    f3 = solve(board,unused^(1<<i),cur)
                    if f3:
                        return True
                    for dy in range(b):
                        for dx in range(a):
                            board[(ny+dy)*W+nx+dx]=0
    return False
                
            
def main():
    global N,H,W,tills
    N,H,W = myin_sp_i()
    tills = []
    for i in range(N):
        tills.append(myin_sp_i())
    if(solve([0 for _ in range(H*W)],(1<<N)-1,0)):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()