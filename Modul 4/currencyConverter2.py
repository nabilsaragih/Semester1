# Nilai mata uang
usd = 0.000066
eur = 0.00006812646
yen = 0.0095

# Nilai inputan
nilai = int(input("Masukkan nilai dalam rupiah: "))
mataUang = str(input("Masukkan mata uang: "))

# Pemilihan rute dan output
if mataUang == "USD" or "usd":
    print(f"Nilai IDR dalam USD adalah {nilai * usd}")
elif mataUang == "EUR" or "eur":
    print(f"Nilai IDR dalam EUR adalah {nilai * eur}")
elif mataUang == "JPY" or "jpy":
    print(f"Nilai IDR dalam JPY adalah {nilai * yen}")

