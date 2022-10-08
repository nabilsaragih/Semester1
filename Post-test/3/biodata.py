# Import library
import os
import time

# Data default
biodata = {
    "Nama": "",
    "NIM": "",
    "Prodi": "",
    "Umur": "",
    "Tinggi": ""
}

# Output data
def data():
    print(f"""
Biodata saat ini:
Nama\t: {biodata["Nama"]}
NIM\t: {biodata["NIM"]}
Prodi\t: {biodata["Prodi"]}
Umur\t: {biodata["Umur"]} Tahun
Tinggi\t: {biodata["Tinggi"]}m
""")

# Validasi tipe data nilai input
try:
    nama = str(input("Masukkan Nama: "))
    nim = str(input("Masukkan NIM: "))
    prodi = str(input("Masukkan Prodi: "))
    umur = int(input("Masukkan Umur: "))
    tinggi = float(input("Masukkan Tinggi (m): "))
except ValueError:
    print("Nilai input yang anda masukkan tidak benar.")

# Memasukkan nilai input ke dictionary
biodata["Nama"] = nama
biodata["NIM"] = nim
biodata["Prodi"] = prodi
biodata["Umur"] = umur
biodata["Tinggi"] = tinggi

while True:
    # Jalur
    try:
        jalur = str(input("Lihat, Ubah, atau Keluar? "))
    except ValueError:
        print("Jalur yang ada hanya Lihat, Ubah, atau Keluar.")

    if jalur == "Lihat" or jalur == "lihat":
        os.system("cls")
        data()
        time.sleep(1)

    if jalur == "Ubah" or jalur == "ubah":
        os.system("cls")
        key = input("Masukkan key: ")
        value = input("Masukkan value baru: ")
        biodata[key] = value
        time.sleep(1)

    if jalur == "Keluar" or jalur == "keluar":
        os.system("cls")
        break

