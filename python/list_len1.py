l=[]
count=0
for i in range(0,100):
    i=input("Enter the element: ")
    if i=="":
        break
    else:
        l.append(i)
        count+=1

print(count)