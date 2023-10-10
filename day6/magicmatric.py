n=int(input("Enter the size of matrix:"))
c,r=0,n//2
matrix = [[0] * n for _ in range(n)] 
for i in range(1,n**2+1):
    matrix[r][c]=i
    nr,nc=(r+1)%n,(c-1)%n
    if matrix[nr][nc]!=0:
        r=(r+1)%n
    else:
        r,c=nr,nc
print("The Magical matrix:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end="|")
    print("")