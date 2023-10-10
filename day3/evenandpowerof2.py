import math
r=list(map(int,input("enter array range").split()))
print(r)
n=int(input("enter array size"))
l=[]
for i in range(n):
    k=int(input())
    if k in range(r[0],r[1]):
        l.append(k)

        
rel=[]
rpl=[]
for i in l:
    if i&1==0 and i in range(r[0],r[1]):
        rel.append(i)
        
    if  i&i-1==0 and i in range(r[0],r[1]):
        rpl.append(i)
 
print("even numbers"," ".join(map(str,rel)))
print("powers of 2:"," ".join(map(str,rpl)))
        
        