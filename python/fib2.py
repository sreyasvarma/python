sum=0
p=1
n=int(input("Enter the value of n: "))
fib=[0,1]
for i in range(1,n):
    sum=fib[-1]+fib[-2]
    fib.append(sum)

num=int(input("Enter the number"))

if num in fib:
    print("It is Fibonacci number")
else:
    print("It is not Fibonacci number")