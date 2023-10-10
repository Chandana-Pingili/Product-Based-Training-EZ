l=[]
n=int(input("enter stack size:"))
for i in range(n):
    l.append(int(input("enter a element")))
print(l)
for i in range(n):
    print(l.pop())
print(l)

