jumlahBuku = int(input("Masukkan jumlah buku yang dibeli: "))
totalPembelian = int(input("Masukkan total pembelian: "))

if jumlahBuku >= 5 and totalPembelian > 100000:
    hargaDiskon = totalPembelian - (totalPembelian * 0.2)
    print(int(hargaDiskon))
else:
    print(f"Bayar {totalPembelian} anda tidak dapat diskon.")