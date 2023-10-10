def generatelists(n:int):
    mainlist=[]
    for i in range(n):
        sublist=[]
        for j in range(n):
            sublist.append(j)
        mainlist.append(sublist)
    return mainlist

n=int(input())
print(generatelists(n))
