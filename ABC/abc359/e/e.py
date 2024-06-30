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
    from collections import deque
    N = int(myin())
    H = myin_sp_i()
    stack = deque()
    ans = [0]
    for i in range(N):
        if len(stack)==0 or H[stack[-1]] >= H[i]:
            ans.append(ans[-1]+H[i])
            stack.append(i)
        else:
            while len(stack)>0 and H[stack[-1]]<H[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(H[i]*(i+1))
            else:
                ans.append(ans[stack[-1]+1]+H[i]*(i-stack[-1]))
            stack.append(i)
    for i in range(1,N+1):
        ans[i]+=1
    print(*ans[1:])

if __name__ == "__main__":
    main()