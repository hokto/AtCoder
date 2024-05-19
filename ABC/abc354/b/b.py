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
    N = int(myin())
    SC = []
    sum = 0
    for i in range(N):
        SC.append(myin_sp_s())
        sum+=int(SC[-1][1])
    SC.sort() 
    print(SC[sum%N][0])
        

if __name__ == "__main__":
    main()