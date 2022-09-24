panjangNilai = []

while True:
    inputInteger = int(input("Masukkan nilai integer: "))
    if inputInteger >= 0:
        panjangNilai.append(inputInteger)
    else:
        break

print(f"Nilai: {panjangNilai}")
print(f"Panjang nilai adalah {len(panjangNilai)}")
print(f"Jumlah nilai adalah {sum(panjangNilai)}")
