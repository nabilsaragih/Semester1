# Checking if inputed number is leap year or not
# The first and second algorithm gives the same output

year = int(input("Enter year: "))

# First algorithm
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
    else:
        print(f"{year} is leap year")
else:           
    print(f"{year} is not leap year")

# Second Algorithm
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")