import csv, os, time, pwinput, random, string
from csv import DictWriter
from prettytable import PrettyTable

def clear():
    os.system("cls")

def delay(seconds):
    time.sleep(seconds)

accountCsvLine = 0
lotsChoices = (1, 2, 3)

with open('.\database\\account.csv', 'w', newline='\n') as csvfile:
    fieldnames = ['username', 'password', 'unique_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

while True:
    cwd = os.getcwd()
    DBPath = cwd + "\\database"
    accountDBPath = DBPath + "\\account.csv"
    isDir = os.path.isdir(DBPath)
    isFile = os.path.isfile(accountDBPath)

    if isDir == False:
        os.system("mkdir Database")

    if isFile == False:
        open(".\database\\account.csv", "w")

    clear()
    myTable = PrettyTable(["Welcome to WAGE"])
    myTable.add_row(["[1] Login"])
    myTable.add_row(["[2] Register"])
    myTable.add_row(["[3] Exit"])
    myTable.align["Welcome to WAGE"] = "l"
    print(myTable)

    try:
        choices = int(input("Masukkan pilihan anda: "))
    except ValueError:
        print("Pilihan harus angka.")
        delay(1)
        continue

    if choices in lotsChoices:
        match choices:
            case 1:
                clear()

                data = open(".\database\\account.csv", "r")
                reader_file = csv.reader(data)
                reader_list = list(reader_file)

                for row in open(".\database\\account.csv"):
                    accountCsvLine += 1

                if accountCsvLine <= 2:
                    print("Anda harus register terlebih dahulu.")
                    delay(1)
                    userReg = input("Masukkan username... ")
                    passReg = input("Masukkan password... ")
                    uniqueReg = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))

                    with open('.\Database\\account.csv', 'a', newline='\n') as csvfile:
                        dictObject = DictWriter(csvfile, fieldnames=fieldnames)
                        dictObject.writerow({'username': userReg, 'password': passReg, 'unique_id': uniqueReg})
                        csvfile.close()

                else:
                    print("Login to WAGE")
                    username = input("Masukkan username anda: ")
                    password = input("Masukkan password anda: ")

                    print(reader_list)
                    # End here

            case 2:
                clear()
                userReg = input("Masukkan username... ")
                passReg = input("Masukkan password... ")
                uniqueReg = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))

                with open('.\Database\\account.csv', 'a', newline='\n') as csvfile:
                    dictObject = DictWriter(csvfile, fieldnames=fieldnames)
                    dictObject.writerow({'username': userReg, 'password': passReg, 'unique_id': uniqueReg})
                    csvfile.close()

            case 3:
                clear()
                break
    else:
        print("Invalid choice.")
        clear()