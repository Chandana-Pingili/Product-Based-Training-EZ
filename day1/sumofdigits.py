'''get one integer num as input and find sum of digits given number'''

n=int(input())
temp=n
sum=0
'''while n!=0:
    rem=n%10
    sum=sum+int(rem)
    n=n/10
print(sum)'''

for i in range(1,n,n//10):
    sum=sum+int(temp%10)
    temp=temp/10
print(sum)
    
