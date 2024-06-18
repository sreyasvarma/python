score=input("Enter the scores followed by space").split()
score=[int(i) for i in score]
max=score[0]
for i in score:
    if i>=max:
        max=i

print(max)