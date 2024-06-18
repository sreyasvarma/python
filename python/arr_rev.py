arr=[]
n=int(input("Enter the number of elements"))
for i in range(0,n):
    i=int(input("Enter the value: "))
    arr.append(i)

l=arr[::-1]
print(l)