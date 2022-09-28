# list kosong untuk menyimpan data
listUmur = []

# looping untuk memasukkan data berulang kali
while True:
    umur = int(input("Masukkan umur: "))
    listUmur.append(umur)

    lagi = str(input("Lagi: Ya / Tidak: "))
    if lagi == "Tidak" or lagi == "tidak":
        break

# list untuk menyimpan hasil inputan
muda = []
remaja = []
dewasa = []
lansia = []

# memasukkan nilai inputan ke list
for i in listUmur:
    if i >= 0 and i <= 12:
        muda.append(i)
    elif i >= 13 and i <= 16:
        remaja.append(i)
    elif i >= 17 and i <= 40:
        dewasa.append(i)
    else:
        lansia.append(i)

# mencetak nilai yang sudah disortir
print(f"Golongan muda: {muda}")
print(f"Golongan remaja: {remaja}")
print(f"Golongan dewasa: {dewasa}")
print(f"Golongan lansia: {lansia}")