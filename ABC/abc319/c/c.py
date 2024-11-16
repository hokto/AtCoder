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
    from itertools import permutations
    C = []
    for i in range(3):
        C.append(myin_sp_i())
    a = 1
    for i in range(9):
        a*=i+1
    b = a
    for perm in permutations(range(9)):
        find = [[False]*3 for i in range(3)]
        row = [0]*3
        col = [0]*3
        l = 0
        r = 0
        for v in perm:
            x = v%3
            y = v//3
            row[y]+=1
            col[x]+=1
            find[y][x]=True
            if x==y:
                l+=1
            if x==2-y:
                r+=1
            if row[y]==2:
                if (not find[y][0] and C[y][1]==C[y][2])or(not find[y][1] and C[y][0]==C[y][2])or(not find[y][2] and C[y][0]==C[y][1]):
                    b-=1
                    break
            if col[x]==2:
                if (not find[0][x] and C[1][x]==C[2][x])or(not find[1][x] and C[0][x]==C[2][x])or(not find[2][x] and C[0][x]==C[1][x]):
                    b-=1
                    break
            if l==2:
                if (not find[0][0] and C[1][1]==C[2][2])or(not find[1][1] and C[0][0]==C[2][2])or(not find[2][2] and C[0][0]==C[1][1]):
                    b-=1
                    break
            if r==2:
                if (not find[0][2] and C[1][1]==C[2][0])or(not find[1][1] and C[0][2]==C[2][0])or(not find[2][0] and C[0][2]==C[1][1]):
                    b-=1
                    break
    print(round(b/a,9))

if __name__ == "__main__":
    main()