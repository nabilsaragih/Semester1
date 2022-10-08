# Import library yang diperlukan
import os
import time

# Fungsi menu
def menu():
    print("""
===================================
|         Pengubah Celcius        |
|=================================|
| [1] Ubah Celcius ke Reamur      |
| [2] Ubah Celcius ke Fahrenheit  |
| [3] Ubah Celcius ke Kelvin      |
| [4] Keluar dari program         |
===================================
    """)

# Fungsi untuk keluar dari program
def quit(q):
    if q == "Y" or q == "y":
        os.system("cls")
        return True
    else:
        os.system("cls")
        time.sleep(1)
        return False

# Fungsi pengubah celcius
def reamur(celcius):
    return (4 / 5) * celcius
def fahrenheit(celcius):
    return ((9 / 5) * celcius) + 32
def kelvin(celcius):
    return celcius + 273

# Looping program
while True:
    # Menampilkan menu
    menu()

    # Error handling pada nilai input
    try:
        jalur = int(input("Masukkan pilihan: "))
    except ValueError:
        print("Nilai input anda tidak valid.")

    # Jika input adalah 4 maka program langsung terhenti
    if jalur == 4:
        os.system("cls")
        break

    # Cek jika nilai input sesuai pada menu
    if jalur < 1 or jalur > 4:
        print("Pilihan anda tidak ada di menu.\n")
        time.sleep(1)
        continue

    try:
        celcius = float(input("Masukkan nilai dalam celcius: "))
    except ValueError:
        os.system("cls")
        print("Nilai input harus angka")


    # Pemilihan jalur
    try:
        if jalur == 1:
            print(f"Nilai Celcius dalam Reamur adalah {reamur(celcius)}")
            if quit(input("Keluar? [Y/N]: ")):
                break
        if jalur == 2:
            print(f"Nilai Celcius dalam Fahrenheit adalah {fahrenheit(celcius)}")
            if quit(input("Keluar? [Y/N]: ")):
                break
        if jalur == 3:
            print(f"Nilai Celcius dalam Kelvin adalah {kelvin(celcius)}")
            if quit(input("Keluar? [Y/N]: ")):
                break
    except NameError:
        print("Tidak bisa mengeluarkan output karena nilai input bukan angka.\n")
        time.sleep(1)

