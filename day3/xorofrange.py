#given a range l-r print xor/find xor for all numbers for the given range
def xor(n):
    if n%4==0:
        return n
    elif n%4==1:
        return 1
    elif n%4==2:
        return 0
    else:
        return n+1

n=int(input("strt bound : "))
m=int(input("end bound : "))
print(xor(n-1)^xor(m))

    