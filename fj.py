from itertools import combinations
n0d,n1d=input().split()
n1d=int(n1d)
l=[]
dd=combinations(n0d,len(n0d)-n1d)
for i in list(dd):
  l.append("".join(i))
print(min(l)
