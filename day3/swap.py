#swap 2 numbers using XoR
n=int(input("n:"))
m=int(input("m:"))
n=n^m
m=n^m
n=n^m
print("n:",n,"m:",m)