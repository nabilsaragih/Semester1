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

'''
A. Algoritma Deskriptif
1. Masukkan Tahun
2. Jika Tahun modulo 4 sama dengan 0, maka kerjakan langkah ke-3. Jika tidak 
maka Tahun bukan tahun kabisat.
3. Jika Tahun modulo 100 sama dengan 0, maka kerjakan langkah ke-4. Jika tidak 
maka Tahun merupakan tahun kabisat.
4. Jika Tahun modulo 400 sama dengan 0, maka Tahun merupakan tahun kabisat. 
Jika tidak maka Tahun bukan tahun kabisat.

B. Pseudocode
Program menentukan apakah suatu tahun merupakan tahun kabisat atau bukan
Deklarasi var tahun: integer
Algoritma: 
INPUT tahun
IF (tahun % 4 == 0) THEN
IF (tahun % 100 == 0) THEN
IF (tahun % 400 == 0) THEN
PRINT tahun merupakan tahun kabisat
ELSE 
PRINT tahun bukan tahun kabisat
ENDIF
ELSE 
PRINT tahun merupakan tahun kabisat
ENDIF
ELSE 
PRINT tahun bukan tahun kabisat
ENDIF
'''