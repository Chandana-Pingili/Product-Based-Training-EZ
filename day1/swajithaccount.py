p=int(input())
SI1=(p*(4/12)*12)/100
p=p-25000
SI2=(p*(4/12)*12)/100
p=p+10000
SI3=(p*(4/12)*12)/100
p=p+SI1+SI2+SI3
print("total balance=",p)

'''def withdraw(n1:int,n2:int):
    return n1-n2
def deposit(n1:int,n2:int):
    return n1+n2
def intrst(n1:int,n2:int):
    return (n1*(n2/12)*12)/100
p=int(input())
SI1=intrst(p,4)
p=withdraw(p,25000)
SI2=intrst(p,4)
p=deposit(p,10000)
SI3=intrst(p,4)
p=p+SI1+SI2+SI3
print(p)'''





    
