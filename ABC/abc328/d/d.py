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
    S = list(myin())
    stack = []
    for c in S:
        if c=="C":
            if len(stack)>=2 and stack[-1]=="B" and stack[-2]=="A":
                stack.pop()
                stack.pop()
                continue
        stack.append(c)
    print("".join(stack))

if __name__ == "__main__":
    main()