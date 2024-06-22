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
def greedy(H,dt,D=None,RD = None):
    import copy
    # 方針: 周りを回っていくように中心に向かって動く．その際に，土砂が多いなら掬って，少ないならある分の中で平らになるようにおく
    #       中心まで行ったら，今度は先ほどと逆の操作でもとに戻っていく．この時も同様に土砂を平らにもる操作を行う
    S = None
    if D is None:
        S = H
    else:
        S=D
    T = None
    if RD is None:
        T = H
    else:
        T = RD
    Lock_S = copy.deepcopy(S)
    for k in range(N//2):
        for x in range(N-1-2*k):
            d = S[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.right()
        for y in range(N-1-2*k):
            d = S[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.down()
        for x in range(N-1-2*k):
            d = S[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.left()
        for y in range(N-2-2*k):
            d = S[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.up()
        # 初期位置を左上に合わせるため
        d = S[dt.y][dt.x]
        if d!=0:
            if dt.loading(d):
                H[dt.y][dt.x]=0
        if k!=N//2-1:
            dt.right()
    Lock_T = copy.deepcopy(H)
    for k in range(N//2):
        # 初期位置を左上に合わせるため
        d = T[dt.y][dt.x]
        if d!=0:
            if dt.loading(d):
                H[dt.y][dt.x]=0
        if k!=N//2-1:
            dt.left()
        for y in range(2*k+1):
            d = T[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.down()
        for x in range(2*(k+1)):
            d = T[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.right()
        for y in range(2*(k+1)):
            d = T[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.up()
        for x in range(2*(k+1)):
            d = T[dt.y][dt.x]
            if d!=0:
                if dt.loading(d):
                    H[dt.y][dt.x]=0
            dt.left()
    
    return dt,sum(map(sum,H)),Lock_S,Lock_T

def sa(H,dt,D,RD,score):
    # 方針:行きがけでの増加量Rと帰りがえでの増加量RDをSAによって，最適化する
    #     行う操作はRもしくはRDのランダムな座標を+1もしくは-1することにより，スコアが更新するかを行なっていく
    
    import random
    import copy
    import math 
    random.seed(20020401)
    LOOP_LIMIT = 1000
    best_score = score
    best_D = D
    best_RD = RD
    TEMP = 10**10
    pr = lambda x: math.exp(x)
    is_selected = lambda x: pr(x/TEMP)>=random.random()
    cooling = lambda x: 0.95*x
    for ll in range(LOOP_LIMIT):
        dt.reset()
        t = random.randint(0,1) # RかRDのどちらか
        x = random.randint(0,N-1)
        y = random.randint(0,N-1)
        d = random.randint(0,1) # +か-か
        d = (-1)**d # ここで符号調整
        if t==0:
            D[y][x]+=d
        else:
            RD[y][x]+=d
        dt,new_score,_,_ = greedy(copy.deepcopy(H),dt,D,RD)
        eval = best_score - new_score
        if eval>=0 or is_selected(eval):
            best_score = new_score
        else:
            if t==0:
                D[y][x]-=d
            else:
                RD[y][x]-=d
        TEMP = cooling(TEMP)
    return dt,best_score,D,RD
def main():
    import copy
    _ = myin() # Nの入力飛ばし(N=20で固定)
    H = []
    dt = DumpTruck()
    for _ in range(N):
        H.append(myin_sp_i())
    dt,score,D,RD=greedy(copy.deepcopy(H),dt) 
    dt.reset()
    dt,_,_,_ = sa(copy.deepcopy(H),dt,D,RD,score)
    dt.reset()
    dt,_,_,_ = greedy(copy.deepcopy(H),dt)
    print("\n".join(dt.query_list))

if __name__ == "__main__":
    main()