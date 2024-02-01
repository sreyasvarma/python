# compute interest

# prompt user to enter the principal amount
p = int(input("Enter principal amount: "

# prompt user to the interest rate
i = int(inputEnter the interest rate: "))
# prompt user enter the number of years
y = int(input("Enter number of years: "))

# initialize the number of years to 1
n = 1

# calculate the interest for each year
for n in range(0, y):
    # calculate the interest
    interest = (p * i / 100)

    # add the interest to the principal amount
    p = p + interest

    # increment the number of years
    n = n + 1

# print the total amount
print("Total amount: ", p)
