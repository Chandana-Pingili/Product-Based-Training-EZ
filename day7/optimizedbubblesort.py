def swap(n1,n2,f):
    return n2,n1,1

l=list(map(int,input().split()))
for i in range(len(l)-1):
    
    f=0
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1],f=swap(l[j],l[j+1],f)
    
    if f==0:
        break
    print(l)

        
