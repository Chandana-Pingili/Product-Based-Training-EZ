def merge_sort(l):
    if len(l)<=1:
        return l 
    else:
        mid=len(l)//2
        leftl=l[:mid]
        rlist=l[mid:]
        merge_sort(leftl)
        merge_sort(rlist)
        lst=merge(leftl,rlist)
        return lst 
def merge(leftlist,rightlist):
    mainlist=[]
    i=j=k=0
    n1=len(leftlist)
    n2=len(rightlist)
    while i<n1 and j<n2:
        if leftlist[i]<rightlist[j]:
            print(leftlist[i])
            mainlist[k]=leftlist[i]
            i+=1
            k+=1
        else:
            mainlist[k]=rightlist[j]
            print(rightlist[j])
            j+=1
            k+=1
    while i<n1:
        mainlist[k]=leftlist[i]
        i+=1
        k+=1
    while j<n2:
        mainlist[k]=rightlist[j]
        j+=1
        k+=1
    return mainlist
l=list(map(int,input("enter array elements").split()))
print(merge_sort(l))    