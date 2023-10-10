
class A:
    def __init__(self):
        self.n1=int(input("enter num 1: "))
        self.n2=int(input("enter num 2: "))
        self.s=input("enter a string: ")
    
    def func1(self,s,n1):
        print("reverse of string is: ",self.s[::-1])
        print("square of num 1 is :",self.n1**2)
        
    def displayResults(self):
        print("len of string is : ",len(self.s))
        print("moduli of n2 and n1 is : ",self.n2%self.n2)
        
obj=A()
obj.func1("c",5)
obj.displayResults()

        
        
    