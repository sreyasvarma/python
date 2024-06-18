n=int(input("Enter numbr of elements in array"))
arr=[]
sum=0
for i in range(0,n):
    i=int(input("Enter the num"))
    arr.append(i)
    sum=sum+i

print(sum)