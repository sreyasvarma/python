#leapyear func

def leapyear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year = int(input("Enter the year: "))
n=int(input("Enter the month:"))
month= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
lmonth= [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if leapyear(year):
    print(f"year {year} month has {lmonth[n-1]} days")
else:
    print(f"year {year} month has {month[n-1]} days")