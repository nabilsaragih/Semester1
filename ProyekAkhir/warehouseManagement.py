import csv, os, time, pwinput, datetime
from csv import DictWriter
from prettytable import PrettyTable, from_csv

def clear():
    os.system("cls")

def delay(seconds):
    time.sleep(seconds)

accountCsvLine = 0
accountIndex = 0
indexItem = 0
stockCsvLine = 0
lotsChoices = (1, 2, 3)
listOfStockDict = []

cwd = os.getcwd()
DBPath = cwd + "\\database"
accountDBPath = DBPath + "\\account.csv"
stockDBPath = DBPath + "\\stock.csv"
isDir = os.path.isdir(DBPath)
accIsFile = os.path.isfile(accountDBPath)
stockIsFile = os.path.isfile(stockDBPath)

if isDir == False:
    os.system("mkdir Database")

if accIsFile == False:
    with open('.\database\\account.csv', 'w', newline='\n') as csvfile:
        fieldnames = ['username', 'password', 'account_level']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        csvfile.close()

if stockIsFile == False:
    with open('.\database\\stock.csv', 'w', newline='\n') as stockcsv:
        list_header = ['Nama Barang', 'Jumlah Barang', 'Harga Barang', 'Tanggal Input']
        writer = csv.DictWriter(stockcsv, fieldnames=list_header)
        writer.writeheader()
        stockcsv.close()

while True:
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

                if accountCsvLine == 1:
                    print("Anda harus register terlebih dahulu.")
                    delay(1)
                    userReg = input("Masukkan username... ")
                    passReg = input("Masukkan password... ")
                    userLevel = input("Register sebagai? [Admin/User] ")

                    with open('.\Database\\account.csv', 'a', newline='\n') as csvfile:
                        fieldnames = ['username', 'password', 'account_level']
                        dictObject = DictWriter(csvfile, fieldnames=fieldnames)
                        dictObject.writerow({'username': userReg, 'password': passReg, 'account_level': userLevel.lower()})
                        csvfile.close()

                else:
                    print("Login to WAGE")
                    username = input("Masukkan username anda: ")
                    password = pwinput.pwinput("Masukkan password anda: ")

                    for akun in range(len(reader_list)):
                        if username == reader_list[akun][0]:
                            accountIndex += akun
                            if password == reader_list[accountIndex][1]:
                                if reader_list[accountIndex][2] == "admin":
                                    while True:
                                        clear()
                                        adminTable = PrettyTable(["Welcome to WAGE Admin Menu"])
                                        adminTable.add_row(["[1] Add new stock"])
                                        adminTable.add_row(["[2] View stock"])
                                        adminTable.add_row(["[3] Change stock"])
                                        adminTable.add_row(["[4] Delete stock"])
                                        adminTable.add_row(["[5] Logout"])
                                        adminTable.align["Welcome to WAGE Admin Menu"] = "l"
                                        print(adminTable)

                                        pilihan = int(input("Masukkan pilihan anda: "))
                                        match pilihan:
                                            case 1:
                                                clear()
                                                nama_barang = input("Masukkan nama barang: ")
                                                jumlah_barang = int(input("Masukkan jumlah barang: "))
                                                harga_barang = float(input("Masukkan harga barang: "))
                                                tanggal_input = datetime.datetime.now()

                                                with open('.\Database\\stock.csv', 'a', newline='\n') as stockinput:
                                                    list_header = ['Nama Barang', 'Jumlah Barang', 'Harga Barang', 'Tanggal Input']
                                                    dictObject = DictWriter(stockinput, fieldnames=list_header)
                                                    dictObject.writerow({'Nama Barang': nama_barang.title(), 'Jumlah Barang': jumlah_barang, 'Harga Barang': harga_barang, 'Tanggal Input': tanggal_input})
                                                    stockinput.close()

                                                print("Barang berhasil ditambahkan.")
                                                delay(1)
                                            case 2:
                                                clear()
                                                with open('.\Database\\stock.csv') as stockdata:
                                                    showData = from_csv(stockdata)
                                                    showData.align["Nama Barang"] = "l"
                                                    showData.align["Jumlah Barang"] = "r"
                                                    showData.align["Harga Barang"] = "r"
                                                    showData.align["Tanggal Input"] = "c"
                                                    print(showData)

                                                lanjut = input("Tekan ENTER untuk lanjut. ")
                                            case 3:
                                                clear()
                                                stock_dict = csv.DictReader(open('.\Database\\stock.csv'))
                                                stock_name = input("Masukkan nama barang yang ingin diubah: ")

                                                for row in stock_dict:
                                                    listOfStockDict.append(row)

                                                for stock in range(len(listOfStockDict)):
                                                    if stock_name.title() == listOfStockDict[stock]["Nama Barang"]:
                                                        indexItem += stock
                                                        print("Barang ditemukan!")
                                                
                                                pilih = input("Masukkan key dari item yang ingin diubah: ")
                                                ubah = input("Ubah menjadi: ")
                                                listOfStockDict[indexItem][pilih.title()] = ubah

                                                keys = listOfStockDict[0].keys()

                                                with open('.\Database\\stock.csv', 'w', newline='\n') as replace_csv:
                                                    dict_writer = csv.DictWriter(replace_csv, keys)
                                                    dict_writer.writeheader()
                                                    dict_writer.writerows(listOfStockDict)
                                                    replace_csv.close()
                                                
                                                indexItem = 0
                                                listOfStockDict = []
                                                lanjut = input("Barang berhasil diubah. Tekan ENTER untuk lanjut. ")
                                            case 4:
                                                clear()
                                                stock_dict = csv.DictReader(open('.\Database\\stock.csv'))
                                                hapus = input("Masukkan nama barang yang ingin dihapus: ")

                                                for row in stock_dict:
                                                    listOfStockDict.append(row)

                                                for stock in range(len(listOfStockDict)):
                                                    if hapus.title() == listOfStockDict[stock]["Nama Barang"]:
                                                        indexItem += stock

                                                for row in open(".\database\\stock.csv"):
                                                    stockCsvLine += 1

                                                if stockCsvLine == 2:
                                                    with open('.\Database\\stock.csv', 'r+') as deleteStock:
                                                        lines = deleteStock.readlines()
                                                        deleteStock.seek(0)
                                                        deleteStock.truncate()
                                                        deleteStock.writelines(lines[:-1])
                                                        deleteStock.close()
                                                else:
                                                    del listOfStockDict[indexItem]
                                                    print("Barang berhasil dihapus.")

                                                    keys = listOfStockDict[0].keys()

                                                    with open('.\Database\\stock.csv', 'w', newline='\n') as replace_csv:
                                                        dict_writer = csv.DictWriter(replace_csv, keys)
                                                        dict_writer.writeheader()
                                                        dict_writer.writerows(listOfStockDict)
                                                        replace_csv.close()

                                                    indexItem = 0
                                                    listOfStockDict = []
                                                    delay(1)
                                            case 5:
                                                clear()
                                                accountIndex = 0
                                                break

                                elif reader_list[accountIndex][2] == "user":
                                    while True:
                                        clear()
                                        userTable = PrettyTable(["Welcome to WAGE User Menu"])
                                        userTable.add_row(["[1] View available stock"])
                                        userTable.add_row(["[2] Search for stock"])
                                        userTable.add_row(["[3] Logout"])
                                        userTable.align["Welcome to WAGE User Menu"] = "l"
                                        print(userTable)

                                        pilihan = int(input("Masukkan pilihan anda: "))
                                        match pilihan:
                                            case 1:
                                                clear()
                                            case 2:
                                                clear()
                                            case 3:
                                                clear()
                                                accountIndex = 0
                                                break
                            else:
                                print("Password anda salah!")

            case 2:
                clear()
                userReg = input("Masukkan username... ")
                passReg = input("Masukkan password... ")
                userLevel = input("Register sebagai? [Admin/User] ")

                with open('.\Database\\account.csv', 'a', newline='\n') as csvfile:
                    fieldnames = ['username', 'password', 'account_level']
                    dictObject = DictWriter(csvfile, fieldnames=fieldnames)
                    dictObject.writerow({'username': userReg, 'password': passReg, 'account_level': userLevel.lower()})
                    csvfile.close()

            case 3:
                clear()
                break
    else:
        print("Invalid choice.")
        clear()