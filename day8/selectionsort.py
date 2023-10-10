
def selectionsort(l):
    for i in range(len(l)):
        min=i
        for j in range(i+1,len(l)):
            print("key is compared with: ",l[j])
            
            if l[min]>l[j]:
                min=j
        l[min],l[i]=l[i],l[min]
        print(l)
       
l=list(map(int,input("enter list elements :").split()))
selectionsort(l)