X = input()
if len(X) == 1 or sum(map(int,X))!=1 or sum(map(int,X[1:]))>0:
    if len(X)==1 and X[0] =="1":
        print(0)
    else:
        print(len(X))
else:
    print(len(X)-1)