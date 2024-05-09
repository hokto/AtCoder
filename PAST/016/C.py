import collections
N = int(input())
A = collections.Counter(input().split())
if len(A)<8:
    print(0)
else:
    print(min(A.values()))