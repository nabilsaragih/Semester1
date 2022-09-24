nilaiTerbesar = 0
nilaiPertama = int(input("Masukkan nilai pertama: "))
nilaiKedua = int(input("Masukkan nilai kedua: "))
nilaiKetiga = int(input("Masukkan nilai ketiga: "))

if nilaiPertama > nilaiTerbesar:
    nilaiTerbesar = nilaiPertama
if nilaiKedua > nilaiTerbesar:
    nilaiTerbesar = nilaiKedua
if nilaiKetiga > nilaiTerbesar:
    nilaiTerbesar = nilaiKetiga

print(f"Nilai terbesar adalah {nilaiTerbesar}")