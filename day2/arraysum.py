def numsum(n:list):
    sum=0
    for i in n:
        sum=sum+i
    return sum
arr=list(map(int,input().split()))
result=numsum(arr)
print(result)

'''for i in range(1,size+1):
    sum=sum+numsum(sum,i)
    '''