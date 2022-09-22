# Operasi tambah
def tambah(nilaiPertama, nilaiKedua):
    return str(nilaiPertama + nilaiKedua)

# Operasi kurang
def kurang(nilaiPertama, nilaiKedua):
    return str(nilaiPertama - nilaiKedua)

# Operasi kali
def kali(nilaiPertama, nilaiKedua):
    return str(nilaiPertama * nilaiKedua)

# Operasi bagi
def bagi(nilaiPertama, nilaiKedua):
    return str(nilaiPertama / nilaiKedua)

# Operasi pangkat
def pangkat(nilaiPertama, nilaiKedua):
    return str(nilaiPertama ** nilaiKedua)

# Operasi modulo
def modulo(nilaiPertama, nilaiKedua):
    return str(nilaiPertama % nilaiKedua)




nilaiPertama = None
operasi = None
nilaiKedua = None

while True:
    # UI
    print("=" * 25)
    print("|" + "Operasi".center(23, " ") + "|")
    print("=" * 25)
    print("|" + "1. ".center(5, " ") + "Tambah".ljust(10) + "|" + "[+]".center(7) + "|")
    print("|" + "2. ".center(5, " ") + "Kurang".ljust(10) + "|" + "[-]".center(7) + "|")
    print("|" + "3. ".center(5, " ") + "Kali".ljust(10) + "|" + "[*]".center(7) + "|")
    print("|" + "4. ".center(5, " ") + "Bagi".ljust(10) + "|" + "[/]".center(7) + "|")
    print("|" + "5. ".center(5, " ") + "Pangkat".ljust(10) + "|" + "[^]".center(7) + "|")
    print("|" + "6. ".center(5, " ") + "Modulo".ljust(10) + "|" + "[%]".center(7) + "|")
    print("=" * 25 + "\n")
    # Inputan
    nilaiPertama = int(input("Masukkan nilai: "))
    operasi = str(input("Masukkan operasi (1, 2, 3, 4, 5, 6): "))
    nilaiKedua = int(input("Masukkan nilai: "))

    # Coba nilai
    try:
        int(nilaiPertama)
        int(nilaiKedua)
    except ValueError:
        print("Nilai yang anda masukkan bukan angka")
        operasi = None



    # Pemilihan operasi
    if operasi != None:
        if operasi == "1":
            print("Hasil adalah: " + tambah(nilaiPertama, nilaiKedua))
        elif operasi == "2":
            print("Hasil adalah: " + kurang(nilaiPertama, nilaiKedua))
        elif operasi == "3":
            print("Hasil adalah: " + kali(nilaiPertama, nilaiKedua))
        elif operasi == "4":
            print("Hasil adalah: " + bagi(nilaiPertama, nilaiKedua))
        elif operasi == "5":
            print("Hasil adalah: " + pangkat(nilaiPertama, nilaiKedua))
        elif operasi == "6":
            print("Hasil adalah: " + modulo(nilaiPertama, nilaiKedua))
        else:
            print("Operasi tidak valid")


    q = input("Keluar? [Ya/Tidak]: ")
    if q == "Ya" or q == "ya":
        break
