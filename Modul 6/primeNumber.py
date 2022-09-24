# Setup
bilanganPrima = []
panjangNilai = int(input("Masukkan panjang nilai: "))

# Looping dari 2 sampai panjang nilai
for nilai in range(2, panjangNilai + 1):
    # Looping untuk mencari faktor
    for faktor in range(2, nilai):
        # Jika nilai sama dengan faktor lanjut
        if nilai == faktor:
            continue
        # Jika nilai modulo faktor sama dengan 0 maka skip
        if nilai % faktor == 0:
            break
    # Jika kondisi tidak ada yang terpenuhi maka masukkan ke list
    else:
        bilanganPrima.append(nilai)
        # Panjang bilangan prima sama dengan panjang nilai maka program berhenti
        if len(bilanganPrima) == panjangNilai:
            break

# Output
print(f"Bilangan prima: {bilanganPrima}")
print(f"Jumlah bilangan prima dari 1 sampai {panjangNilai} adalah {len(bilanganPrima)}")

