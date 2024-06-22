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

N = 5
A = []
class Crane:
    def __init__(self,id) -> None:
        self.id = id
        self.y = id
        self.x = 0
        self.op_log = ""
    def up(self) -> None:
        if(self.y-1 < 0):
            return
        self.y -= 1
        self.op_log+="U"
    def down(self) -> None:
        if(self.y+1>=N):
            return
        self.y+=1
        self.op_log+="D"
    def right(self) -> None:
        if(self.x+1>=N):
            return
        self.x+=1
        self.op_log+="R"
    def left(self) -> None:
        if(self.x-1<0):
            return
        self.x-=1
        self.op_log+="L"
    def put(self) -> None:
        self.op_log+="Q"
    
    def take(self) -> None:
        self.op_log+="P"
    def bomb(self) -> None:
        self.op_log += "B"
    
    def nop(self) -> None:
        self.op_log += "."
    
    def op(self) -> str:
        return self.op_log
    
# a1を置いたg1からa2を取ってそれをおく場所g2までの距離を計算
def calc_dist(a1,a2,pos_of_A) -> int:
    g1 = a1//N
    g2 = a2//N
    # 初期地点からの場合，(0,0)からg1までの距離計算のみ
    if a1==-1:
        g1 = 0    
    g1_pos = [g1,0]
    g2_pos = [g2,0]
    # 最終地点までの場合，すでにおいているため計算しない
    if a2 == N*N:
        #return abs(g1_pos[0]-pos_of_A[a1][0])+abs(g1_pos[1]-pos_of_A[a1][1])
        return 0
    a2_pos = pos_of_A[a2]
    return abs(g1_pos[0]-a2_pos[0])+abs(g1_pos[1]-a2_pos[1])+abs(a2_pos[0]-g2_pos[0])+abs(a2_pos[1]-g2_pos[1])

# リストBにおける転倒数を計算(要素数5なのでバブルソートして計算)
def calc_inversion(B) -> int:
    res = 0
    for i in reversed(range(N)):
        for j in reversed(range(i)):
            if B[j]> B[j+1]:
                res+=1
                B[j],B[j+1]=B[j+1],B[j]
    return res 

# Aの要素を//Nの値でグルーピング
def div_group_mod(A) -> list:
    group = [ [] for i in range(N)]
    for a in A:
        group[a//N].append(a)
    return group

# Aの要素//Nでグルーピングした後に，各転倒数の総和を計算する
def calc_all_inversion(A) -> int:
    ans = 0
    for group in div_group_mod(A):
        ans+=calc_inversion(group)
    return ans

def calc_all_dist(route,pos_of_A) -> int:
    dist = calc_dist(-1,route[0],pos_of_A)
    for i in range(N*N-1):
        dist+=calc_dist(route[i],route[i+1],pos_of_A)
    return dist
def main():
    N = int(myin())
    A = []
    pos_of_A = [(-1,-1) for _ in range(N*N)]
    ordering = [None for _ in range(N*N)]
    for _ in [0]*N:
        A.append(myin_sp_i())
    for i in range(N):
        for j in range(N-1):
            pos_of_A[A[i][j]] = [i,j+1]
    for i in range(N):
        pos_of_A[A[i][-1]] = [i,N-1]
    for i in range(N):
        ordering[A[i][-1]] = A[i][-2] # 最後の列に関しては直前の行を開けないと巡回できない
    crane_list = [Crane(id) for id in range(N)]
    
    # 20個のコンテナを出しておく
    for id in range(N):
        for goal in reversed(range(1,N-1)):
            crane_list[id].take()
            for to in range(goal):
                crane_list[id].right()
            crane_list[id].put()
            for back in range(goal):
                crane_list[id].left()
    for id in range(1,N):
        crane_list[id].bomb()
    for i in range(N-1):
        crane_list[0].right()
    # 制限付きtspを解く(制限は最後のコンテナを経由するときは，その直前のコンテナを経由していること)
    # もしかしたらハード制約でなくソフト制約にして，ペナルティをかなり重くしたほうがいい？
    # なるべく転倒数が発生しないようにペナルティを付与(問題と一緒)
    
    # 初期解生成(最近近傍法)
    import random
    random.seed(20240525)
    route = []
    a_of_order = [N*N for i in range(N*N)]
    visit = [False for i in range(N*N)]
    prev_container = -1
    best_score = 0
    # 制約を満たす解を生成するため
    while True:
        init_container = random.randint(0,N-1)
        if(not ordering[init_container]):
            route.append(init_container) 
            visit[init_container]=True
            prev_container = init_container
            a_of_order[init_container]=0
            break
    for i in range(1,N*N):
        next_container = -1
        best_dist = 10**2
        for container in range(N*N):
            if not visit[container]:
                if ordering[container] is None or visit[ordering[container]] or i>5:
                    dist = calc_dist(prev_container,container,pos_of_A)
                    if dist < best_dist:
                        best_dist = dist
                        next_container = container
        visit[next_container] = True
        route.append(next_container)
        a_of_order[next_container]=i
        prev_container = next_container
    M2 = 10**3
    best_score = calc_all_dist(route,pos_of_A)+M2 * calc_all_inversion(route) # ここで転倒数に関するペナルティをつける
    #print(best_score)
    #print(route) 
    SA_LIMIT_CNT = N*N*5*1000
    COOLING_CYCLE = N*N*20
    cooling_cnt = 0
    MAX_T =10000.0
    MIN_T = 0.1
    T = MAX_T
    C = (MIN_T/MAX_T)**(1/((SA_LIMIT_CNT/COOLING_CYCLE)-1))
    cooling = lambda x: x*C
    #f_tmp = open("./AHC/ahc033/temp.csv","w")
    #f_tmp.write("cnt,tmp\n")
    #f_pr = open("./AHC/ahc033/pr.csv","w") 
    #f_pr.write("cnt,pr\n")
    #f_eval = open("./AHC/ahc033/eval.csv","w") 
    #f_eval.write("cnt,eval\n")
    import math
    pr = lambda x: math.exp(x/T)
    is_move = lambda x: pr(x) >= random.random()
    import copy
    for sa_cnt in range(SA_LIMIT_CNT):
        container1 = random.randint(0,N*N-1)
        container2 = random.randint(0,N*N-1)
        if(container1==container2):
            continue
        new_route = copy.deepcopy(route)
        new_a_of_order = copy.deepcopy(a_of_order)
        new_route[a_of_order[container1]],new_route[a_of_order[container2]]=new_route[a_of_order[container2]],new_route[a_of_order[container1]]
        new_a_of_order[container1],new_a_of_order[container2]=new_a_of_order[container2],new_a_of_order[container1]
        is_violate = False
        #print(f"check:{new_a_of_order[10]<new_a_of_order[ordering[10]]}")
        # 制約違反のチェック
        for container in range(N*N):
            if ordering[container] is not None and new_a_of_order[container]<new_a_of_order[ordering[container]] and new_a_of_order[container]<=5:
                is_violate = True
                break
        if is_violate:
            continue
        prev_ct1 = a_of_order[container1]-1
        if prev_ct1>=0:
            prev_ct1 = route[prev_ct1]
        prev_ct2 = a_of_order[container2]-1
        if prev_ct2>=0:
            prev_ct2 = route[prev_ct2]
        next_ct1 = a_of_order[container1]+1
        if next_ct1<N*N:
            next_ct1 = route[next_ct1]
        next_ct2 = a_of_order[container2]+1
        if next_ct2<N*N:
            next_ct2= route[next_ct2]
        #new_score = best_score - calc_dist(prev_ct1,container1,pos_of_A)-calc_dist(container1,next_ct1,pos_of_A)-calc_dist(prev_ct2,container2,pos_of_A)-calc_dist(container2,next_ct2,pos_of_A)\
            #+ calc_dist(prev_ct1,container2,pos_of_A)+calc_dist(container2,next_ct1,pos_of_A)+calc_dist(prev_ct2,container1,pos_of_A)+calc_dist(container1,next_ct2,pos_of_A)
        new_score = calc_all_dist(new_route,pos_of_A)
        new_score += M2 * calc_all_inversion(new_route)
        eval = best_score - new_score
        if eval>0 or is_move(eval):
            best_score = new_score
            route = new_route
            a_of_order = new_a_of_order
        # 同じ温度でCOOLING_CYCLE回探索し，その後下げる
        cooling_cnt+=1
        if cooling_cnt==COOLING_CYCLE:
            cooling_cnt=0
            T = cooling(T)
        #f_tmp.write(f"{sa_cnt},{T}\n")
        #if(eval<0): f_pr.write(f"{sa_cnt},{pr(eval)}\n");f_eval.write(f"{sa_cnt},{-eval}\n")
    #print(best_score)
    #print(route)
    prev_pos = 0
    able_replace_ct = [False for i in range(N*N)]
    for a in route:
        # 先にordering[a]を出さないといけないのに，aが先にきている場合
        # 空いているところにordering[a]を退避させて，aを取り出す
        if ordering[a] and a_of_order[a] < a_of_order[ordering[a]]:
            shift_a = ordering[a]
            shift_pos = pos_of_A[shift_a]
            for _ in range(shift_pos[1]):
                crane_list[0].left()
            if shift_pos[0]>prev_pos:
                for _ in range(prev_pos,shift_pos[0]):
                    crane_list[0].down()
            else:
                for _ in range(shift_pos[0],prev_pos):
                    crane_list[0].up()
            crane_list[0].take()
            # 一旦，何も考えず空いているところが見つかったらそこに置いとく
            # ー＞後のこと考えて，出口側に置いとく
            best_replace_ct = -1
            best_replace_pos = (-1,-1)
            best_replace_dist = N*N
            for container in range(N*N):
                if not able_replace_ct[container]:
                    continue
                if a_of_order[container]<a_of_order[a] and pos_of_A[container][1]!=N-1:
                    replace_pos = pos_of_A[container]
                    replace_dist = abs(ordering[a]%N-replace_pos[0])+replace_pos[1]
                    if best_replace_dist > replace_dist:
                        best_replace_dist = replace_dist
                        best_replace_pos = replace_pos
                        best_replace_ct = container
            if best_replace_pos[0]>shift_pos[0]:
                for _ in range(shift_pos[0],best_replace_pos[0]):
                    crane_list[0].down()
            else:
                for _ in range(best_replace_pos[0],shift_pos[0]):
                    crane_list[0].up()
            for _ in range(N-1-best_replace_pos[1]):
                crane_list[0].right()
            crane_list[0].put()
            pos_of_A[ordering[a]] = best_replace_pos
            for _ in range(best_replace_pos[1]):
                crane_list[0].right()
            prev_pos = best_replace_pos[0]
            A[best_replace_pos[0]][best_replace_pos[1]-1] = ordering[a]
            able_replace_ct[best_replace_ct]=False
                    
                    
            
        pos = pos_of_A[a]
        for _ in range(pos[1]):
            crane_list[0].left()
        if pos[0]>prev_pos:
            for _ in range(prev_pos,pos[0]):
                crane_list[0].down()
        else:
            for _ in range(pos[0],prev_pos):
                crane_list[0].up()
        crane_list[0].take()
        next_pos = a//N
        if next_pos>pos[0]:
            for _ in range(pos[0],next_pos):
                crane_list[0].down()
        else:
            for _ in range(next_pos,pos[0]):
                crane_list[0].up()
        for _ in range(pos[1]):
            crane_list[0].right()
        crane_list[0].put()
        prev_pos = next_pos
        able_replace_ct[a]=True
        #print(A)
    for id in range(5):
        print(crane_list[id].op()) 

if __name__ == "__main__":
    main()