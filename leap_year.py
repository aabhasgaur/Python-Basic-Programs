year=int(input("Enter the YEAR: "))
if year%4==0 and year%400==0:
    print("{} in a leap year!".format(year))
else:
    print("{} is NOT a leap year.".format(year))
