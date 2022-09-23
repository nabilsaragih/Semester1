'''
Sebuah puskesmas meminta kalian untuk membuatkan program dimana mereka dapat
memasukan umur dari para warga dan program pun akan otomatis memasukan mereka
kedalam golongan muda, remaja, dewasa, dan lansia.
'''

listUmur = []
while True:
    umur = int(input("Masukkan umur: "))
    listUmur.append(umur)

    lagi = str(input("Lagi: Ya / Tidak: "))
    if lagi == "Tidak" or lagi == "tidak":
        break

muda = []
remaja = []
dewasa = []
lansia = []

for i in listUmur:
    if i >= 0 and i <= 12:
        muda.append(i)
    elif i >= 13 and i <= 16:
        remaja.append(i)
    elif i >= 17 and i <= 40:
        dewasa.append(i)
    else:
        lansia.append(i)

print(f"Golongan muda: {muda}")
print(f"Golongan remaja: {remaja}")
print(f"Golongan dewasa: {dewasa}")
print(f"Golongan lansia: {lansia}")