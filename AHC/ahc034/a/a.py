from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
import random

def myin():
    return stdin.readline().rstrip()

def myin_sp():
    return stdin.readline().rstrip().split()

def myin_sp_i():
    return list(map(int,myin_sp()))

def myin_sp_s():
    return list(map(str,myin_sp()))

N = 20
QUERY_LIMIT = 1000000
class DumpTruck:
    def __init__(self) -> None:
        self.reset()
    def loading(self,d:int) -> bool:
        if self.weight+d>=0:
            self.query_list.append(f"{d:+}")
            self.query_size+=1
            self.weight+=d
            return True
        return False
    
    def up(self) -> bool:
        if self.is_up():
            self.query_list.append("U")
            self.query_size += 1
            self.y -= 1
            return True
        return False

    def down(self) -> bool:
        if self.is_down():
            self.query_list.append("D")
            self.query_size+=1
            self.y += 1
            return True
        return False
    
    def left(self) -> bool:
        if self.is_left():
            self.query_list.append("L")
            self.query_size+=1
            self.x -= 1
            return True
        return False
    
    def right(self) -> bool:
        if self.is_right():
            self.query_list.append("R")
            self.query_size+=1
            self.x +=1
            return True
        return False
    
    def is_up(self) -> bool:
        return self.y >0
    def is_down(self) -> bool:
        return self.y < N-1
    def is_left(self) -> bool:
        return self.x >0
    def is_right(self) -> bool:
        return self.x < N-1
    
    def queryable_cnt(self) -> int:
        return QUERY_LIMIT-self.query_size
    
    def reset(self) -> None:
        self.query_list = []
        self.query_size = 0
        self.x = 0
        self.y = 0
        self.weight = 0
def greedy(H,dt):
    # 方針: 周りを回っていくように中心に向かって動く．その際に，土砂が多いなら掬って，少ないならある分の中で平らになるようにおく
    for k in range(N//2):
        for x in range(N-1-2*k):
            d = H[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.right()
        for y in range(N-1-2*k):
            d = H[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.down()
        for x in range(N-1-2*k):
            d = H[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.left()
        for y in range(N-2-2*k):
            d = H[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.up()
        # 初期位置を左上に合わせるため
        d = H[dt.y][dt.x]
        if d!=0:
            if dt.loading(d):
                H[dt.y][dt.x]=0
        if k!=N//2-1:
            dt.right()
    return dt,H

def calc_dist(sigma,prev_x,prev_y):
    score = 0
    for x,y in sigma:
        score+=abs(x-prev_x)+abs(y-prev_y)
        prev_x = x
        prev_y = y
    return score
def kick(sigma):
    # 適用な位置を選択して，そこから連続4つを最後尾に移動させる(ただし，途中で先頭に戻る場合も含む)
    K = 5
    if len(sigma)<=K:
        return sigma
    base_idx = random.randint(0,len(sigma)-1)
    if base_idx+K<N:
        tmp = sigma[base_idx:base_idx+K]
        del sigma[base_idx:base_idx+K]
        sigma+=tmp
    else:
        tmp = sigma[base_idx:]+sigma[:K-len(sigma)-base_idx]
        del sigma[base_idx:],sigma[:K-len(sigma)-base_idx]
        sigma+=tmp
    return sigma

def sa(H,dt,D):
    # 方針: diffを0にすることはできているので，余分に移動しないことを目指す．つまり，すでにH[i][j]=0のところを訪れる必要性はないため，
    #       それを除いた地点で周回できる最短路をsaで求める
    import copy
    import math 
    random.seed(20020401)
    sigma = []
    for y in range(N):
        for x in range(N):
            if D[y][x]!=0:
                sigma.append((x,y))
    best_score = calc_dist(sigma,dt.x,dt.y)
    if len(sigma)<=2:
        return dt,best_score,sigma
    ITER_LIMIT = 30
    LOOP_LIMIT = 50000
    MAX_TEMP = -N*N/math.log(0.01)
    MIN_TEMP = -1/math.log(0.05)
    pr = lambda x: math.exp(x)
    is_selected = lambda x: pr(x/TEMP)>=random.random()
    cooling = lambda x: math.pow(MIN_TEMP/MAX_TEMP,1/LOOP_LIMIT)*x
    for il in range(ITER_LIMIT):
        TEMP = MAX_TEMP
        sigma = kick(sigma)
        best_score = calc_dist(sigma,dt.x,dt.y)
        for ll in range(LOOP_LIMIT):
            idx1 = random.randint(0,len(sigma)-1)
            idx2 = random.randint(0,len(sigma)-1)
            sigma[idx1],sigma[idx2] = sigma[idx2],sigma[idx1]
            score = calc_dist(sigma,dt.x,dt.y)
            eval = best_score - score
            if eval>=0 or is_selected(eval):
                best_score = score
            else:
                sigma[idx1],sigma[idx2]=sigma[idx2],sigma[idx1]
            TEMP = cooling(TEMP)
    return dt,best_score,sigma
def main():
    import copy
    _ = myin() # Nの入力飛ばし(N=20で固定)
    H = []
    dt = DumpTruck()
    for _ in range(N):
        H.append(myin_sp_i())
    dt,D=greedy(copy.deepcopy(H),dt) 
    dt,score,sigma = sa(copy.copy(H),dt,D)
    for x,y in sigma:
        nx = dt.x
        ny = dt.y
        dx = x-nx
        dy = y - ny
        if dx>0:
            for _ in range(dx):
                dt.right()
        else:
            for _ in range(-dx):
                dt.left()
        if dy>0:
            for _ in range(dy):
                dt.down()
        else:
            for _ in range(-dy):
                dt.up()
        dt.loading(H[y][x])
    print("\n".join(dt.query_list))

if __name__ == "__main__":
    main()