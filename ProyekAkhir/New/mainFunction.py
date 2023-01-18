import csv
import os
import pwinput
import datetime
from csv import DictWriter
from prettytable import from_csv
import necessaryFunction as nf
import menu
import object as obj

lotChoice = (1, 2, 3, 4)
listOfStockName = []
listOfStockDict = []
listOfAccountDictionary = []

class csv_line:
    accountCsvLine = 0
    accountIndex = 0
    indexItem = 0
    stockCsvLine = 0
    
def register():
    with open('.\Database\\account.csv', 'r') as account:
        readacc = csv.DictReader(account) 
        for i in readacc:
            listOfAccountDictionary.append(i.get('username'))
        account.close()

    userReg = input("Masukkan username... ")
    passReg = input("Masukkan password... ")
    userLevel = input("Register sebagai? [Admin/User] ")

    if userReg or passReg or userLevel != "":
        if userReg in listOfAccountDictionary:
            print("Akun sudah terdaftar.")
            nf.delay(1)
        else:
            with open('.\Database\\account.csv', 'a', newline='\n') as csvfile:
                fieldnames = ['username', 'password', 'account_level']
                dictObject = DictWriter(csvfile, fieldnames=fieldnames)
                dictObject.writerow({'username': userReg, 'password': passReg, 'account_level': userLevel.lower()})
                csvfile.close()
            print("Akun berhasil ditambahkan")
            nf.delay(1)
    else:
        print("Nilai input anda harus sesuai")
        nf.delay(1)

def dir_setup():
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

def run():
    while True:
        menu.main_menu()
        try:
            choices = int(input("Masukkan pilihan anda: "))
        except ValueError:
            print("Pilihan harus angka.")
            nf.delay(1)
            continue

        if choices in lotChoice:
            match choices:
                case 1:
                    nf.clear()
                    # Melihat isi file account.csv, akan login jika akun sudah ada dan akan register jika akun belum ada
                    data = open(".\database\\account.csv", "r")
                    reader_file = csv.reader(data)
                    reader_list = list(reader_file)

                    for row in open(".\database\\account.csv"):
                        csv_line.accountCsvLine += 1
                    if csv_line.accountCsvLine == 1:
                        print("Anda harus register terlebih dahulu.")
                        nf.delay(1)
                        register()
                    else:
                        print("Login to WAGE")
                        username = input("Masukkan username anda: ")
                        password = pwinput.pwinput("Masukkan password anda: ")
                        for akun in range(len(reader_list)):
                            if username == reader_list[akun][0]:
                                csv_line.accountIndex += akun
                                if password == reader_list[csv_line.accountIndex][1]:
                                    if reader_list[csv_line.accountIndex][2] == "admin":
                                        while True:
                                            menu.admin_menu()

                                            pilihan = int(input("Masukkan pilihan anda: "))
                                            match pilihan:
                                                case 1:
                                                    nf.clear()
                                                    nama_barang = input("Masukkan nama barang: ")
                                                    jumlah_barang = int(input("Masukkan jumlah barang: "))
                                                    harga_barang = float(input("Masukkan harga barang: "))
                                                    tanggal_input = datetime.datetime.now()

                                                    # Membuka file dan mengappend nilai input ke dalam file
                                                    with open('.\Database\\stock.csv', 'a', newline='\n') as stockinput:
                                                        list_header = ['Nama Barang', 'Jumlah Barang', 'Harga Barang', 'Tanggal Input']
                                                        dictObject = DictWriter(stockinput, fieldnames=list_header)
                                                        dictObject.writerow({'Nama Barang': nama_barang.title(), 'Jumlah Barang': jumlah_barang, 'Harga Barang': harga_barang, 'Tanggal Input': tanggal_input})
                                                        stockinput.close()

                                                    print("Barang berhasil ditambahkan.")
                                                    nf.delay(1)
                                                case 2:
                                                    nf.clear()
                                                    # Mencetak isi file
                                                    with open('.\Database\\stock.csv') as stockdata:
                                                        showData = from_csv(stockdata)
                                                        showData.align["Nama Barang"] = "l"
                                                        showData.align["Jumlah Barang"] = "r"
                                                        showData.align["Harga Barang"] = "r"
                                                        showData.align["Tanggal Input"] = "c"
                                                        print(showData)

                                                    nf.lanjut()
                                                case 3:
                                                    nf.clear()
                                                    # Mengubah isi file
                                                    stock_dict = csv.DictReader(open('.\Database\\stock.csv'))
                                                    for row in stock_dict:
                                                        listOfStockDict.append(row)
                                                        listOfStockName.append(row.get("Nama Barang"))

                                                    if len(listOfStockDict) >= 1:
                                                        print(f"Barang yang tersedia: {', '.join(listOfStockName)}")
                                                        stock_name = input("Masukkan nama barang yang ingin diubah: ")
                                                        for stock in range(len(listOfStockDict)):
                                                            if stock_name.title() == listOfStockDict[stock]["Nama Barang"]:
                                                                csv_line.indexItem += stock
                                                            else: continue
                                                        if stock_name.title() in listOfStockName:
                                                            print("Barang ditemukan.")
                                                            print(f"Key: Value\nNama Barang: {listOfStockDict[csv_line.indexItem]['Nama Barang']}\nJumlah Barang: {listOfStockDict[csv_line.indexItem]['Jumlah Barang']}\nHarga Barang: {listOfStockDict[csv_line.indexItem]['Harga Barang']}")
                                                            pilih = input("Masukkan key dari item yang ingin diubah: ")
                                                            ubah = input("Ubah menjadi: ")
                                                            listOfStockDict[csv_line.indexItem][pilih.title()] = ubah.title()

                                                            keys = listOfStockDict[0].keys()

                                                            # Replace file awal menjadi file yang sudah diubah
                                                            with open('.\Database\\stock.csv', 'w', newline='\n') as replace_csv:
                                                                dict_writer = csv.DictWriter(replace_csv, keys)
                                                                dict_writer.writeheader()
                                                                dict_writer.writerows(listOfStockDict)
                                                                replace_csv.close()
                                                            print("Barang berhasil diubah.")
                                                        else:
                                                            print("Barang tidak ditemukan.")
                                                    else:
                                                        print("Barang tidak tersedia, input barang terlebih dahulu.")

                                                    csv_line.indexItem = 0
                                                    listOfStockDict = []
                                                    listOfStockName = []
                                                    nf.lanjut()
                                                case 4:
                                                    nf.clear()
                                                    # Menghapus stock
                                                    stock_dict = csv.DictReader(open('.\Database\\stock.csv'))
                                                    hapus = input("Masukkan nama barang yang ingin dihapus: ")

                                                    for row in stock_dict:
                                                        listOfStockDict.append(row)

                                                    for stock in range(len(listOfStockDict)):
                                                        if hapus.title() == listOfStockDict[stock]["Nama Barang"]:
                                                            csv_line.indexItem += stock

                                                    for row in open(".\database\\stock.csv"):
                                                        csv_line.stockCsvLine += 1

                                                    # Jika file stock hanya terdiri dari 2 baris
                                                    if csv_line.stockCsvLine == 2:
                                                        with open('.\Database\\stock.csv', 'r+') as deleteStock:
                                                            lines = deleteStock.readlines()
                                                            deleteStock.seek(0)
                                                            deleteStock.truncate()
                                                            deleteStock.writelines(lines[:-1])
                                                            deleteStock.close()
                                                    else:
                                                        # Jika file stock lebih dari 2 baris
                                                        del listOfStockDict[csv_line.indexItem]
                                                        print("Barang berhasil dihapus.")

                                                        keys = listOfStockDict[0].keys()

                                                        # Mereplace file yang sudah ada menjadi file yang sudah diubah
                                                        with open('.\Database\\stock.csv', 'w', newline='\n') as replace_csv:
                                                            dict_writer = csv.DictWriter(replace_csv, keys)
                                                            dict_writer.writeheader()
                                                            dict_writer.writerows(listOfStockDict)
                                                            replace_csv.close()

                                                        csv_line.indexItem = 0
                                                        csv_line.stockCsvLine = 0
                                                        listOfStockDict = []
                                                        nf.delay(1)
                                                case 5:
                                                    nf.clear()
                                                    csv_line.accountIndex = 0
                                                    listOfAccountDictionary = []
                                                    break

                                    elif reader_list[csv_line.accountIndex][2] == "user":
                                        while True:
                                            menu.user_menu()

                                            pilihan = int(input("Masukkan pilihan anda: "))
                                            match pilihan:
                                                case 1:
                                                    nf.clear()
                                                    stockdata = open('.\Database\\stock.csv', 'r')
                                                    for row in stockdata:
                                                        csv_line.stockCsvLine += 1

                                                    if csv_line.stockCsvLine == 1:
                                                        print("Barang masih kosong tunggu admin menambahkan barang.")
                                                    else:
                                                        with open('.\Database\\stock.csv', 'r') as stockdata:
                                                            showData = from_csv(stockdata)
                                                            showData.align["Nama Barang"] = "l"
                                                            showData.align["Jumlah Barang"] = "r"
                                                            showData.align["Harga Barang"] = "r"
                                                            showData.align["Tanggal Input"] = "c"
                                                            print(showData)

                                                    nf.lanjut()
                                                case 2:
                                                    nf.clear()
                                                    cariBarang = input("Masukkan nama barang: ")
                                                    with open('.\Database\\stock.csv') as stockdata:
                                                        searchData = csv.DictReader(stockdata)
                                                        for nama in searchData:
                                                            listOfStockName.append(nama.get("Nama Barang"))
                                                            listOfStockDict.append(nama)
                                                        for index in range(len(listOfStockName)):
                                                            if cariBarang.title() == listOfStockName[index]:
                                                                csv_line.indexItem += index
                                                        if cariBarang.title() in listOfStockName:
                                                            print("Barang ditemukan.\n")
                                                            print(f"Nama Barang: {listOfStockDict[csv_line.indexItem].get('Nama Barang')}\nJumlah Barang: {listOfStockDict[csv_line.indexItem].get('Jumlah Barang')}\nHarga Barang: {listOfStockDict[csv_line.indexItem].get('Harga Barang')}\n")
                                                            nf.lanjut()
                                                        else:
                                                            print("Barang tidak ditemukan.")
                                                            nf.delay(1)

                                                        csv_line.indexItem = 0
                                                case 3:
                                                    nf.clear()
                                                    csv_line.accountIndex = 0
                                                    listOfStockDict = []
                                                    break
                                else:
                                    print("Password anda salah!")
                            
                            else:
                                print("Akun tidak ditemukan.")
                
                case 2:
                    nf.clear()
                    register()

                case 3:
                    nf.clear()
                    obj.about()
                    nf.lanjut()

                case 4:
                    nf.clear()
                    break
        else:
            print("Invalid choice.")
            nf.clear()