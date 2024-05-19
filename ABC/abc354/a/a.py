from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

def main():
    H = int(myin())
    x = 0
    ans = 0
    while x<=H:
        x += 2**ans
        ans+=1
    print(ans)

if __name__ == "__main__":
    main()