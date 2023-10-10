# for given n find xor of all n numbers
def xor(n):
    r=0
    for i in range(1,n+1):
        r=r^i
    return r
n=int(input())
print(xor(n))
