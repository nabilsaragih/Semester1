import math

jariJari = int(input("Masukkan nilai jari-jari: "))
tinggi = int(input("Masukkan nilai tinggi: "))
volume = 1 / 3 * (math.pi * ((jariJari ** 2) * tinggi))

print(volume)