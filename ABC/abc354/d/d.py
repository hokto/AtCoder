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
    # 4x2の大きさで巡回していて，
    # [[2,1,0,1],[1,2,1,0]]の面積になっている
    A,B,C,D = myin_sp_i()
    # (0,0)から(x,y)の面積を求める(ただし，0<=x,y)
    def calc_area(x,y):
        accum_areas = [[0,0,0,0,0],
                       [0,2,3,3,4],
                       [0,3,6,7,8]]
        sx = x//4
        rx = x%4
        sy = y//2
        ry = y%2
        return sx*sy*accum_areas[-1][-1]+sx*accum_areas[ry][-1]+sy*accum_areas[-1][rx]+accum_areas[ry][rx]
    a = A%4
    b = B%4
    C-=A
    C+=a
    D-=B
    D+=b
    print(calc_area(C,D)-calc_area(a,D)-calc_area(C,b)+calc_area(a,b))
if __name__ == "__main__":
    main()