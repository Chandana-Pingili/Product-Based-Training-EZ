def search(n:list,k:int):
    flag=0
    for i in range(len(n)):
        if n[i]==k:
            flag=1
            break
    if flag==1:
        print(key," is found at location",i+1)
    else:
        print(key ,"not found")


arr=list(map(int,input().split()))
key=int(input())
position=search(arr,key)

