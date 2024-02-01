#factorial of any number

a=int(input("Enter number: "))

i=1
factorial=1
while i<=a:
    factorial=factorial*i
    i=i+1
print(factorial)
