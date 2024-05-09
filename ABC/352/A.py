N,X,Y,Z = list(map(int,input().split()))
if X<=Z<=Y or (Y<=Z<=X):
    print("Yes")
else:
    print("No")