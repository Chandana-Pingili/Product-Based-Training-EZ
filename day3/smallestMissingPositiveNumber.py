#after creating an array findout the smallest missing positive number
arr=list(map(int,input().split()))
if len(arr)==1:
    if arr[0]==0:
        print(1)
    elif ((arr[0]<0) or (arr[0]==1)):
        print(0)
    else:
        print(0)
for i in range(len(arr)):
    if i not in arr:
        break
print(i)
        
        
    
    