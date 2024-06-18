def add(m,n):
    return m+n
def sub(m,n):
    return m-n
def mul(m,n):
    return m*n
def div(m,n):
    return m/n
def cacl():
    m=int(input("Enter the first num"))
    op=input("Enter the operation you want to do here")
    n=int(input("Enter the second num"))
    if op=="+":
        print(add(m,n))
    elif op=="-":
        print(sub(m,n))
    elif op=="*":
        print(mul(m,n))
    elif op=="/":
        print(div(m,n))
    

while True:
    cacl()

