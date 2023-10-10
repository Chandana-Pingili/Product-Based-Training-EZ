#in the given RRy every number occurs twice only one number occurs once find that number
def singleele(ar,n):
    r=ar[0]
    for i in range(1,n):
        r=r^ar[i]
    return r

n=list(map(int,input().split()))
print(singleele(n,len(n)))